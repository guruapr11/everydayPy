from __future__ import annotations
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import Trip, Participant, Expense, ExpenseSplit, Settlement, compute_balances, suggest_settlements

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    trips = Trip.query.order_by(Trip.created_at.desc()).all()
    return render_template("index.html", trips=trips)


@main_bp.route("/trip/create", methods=["POST"]) 
def create_trip():
    name = request.form.get("name", "").strip()
    currency = request.form.get("currency", "USD").strip() or "USD"
    if not name:
        flash("Trip name is required", "danger")
        return redirect(url_for("main.index"))
    trip = Trip(name=name, currency=currency)
    db.session.add(trip)
    db.session.commit()
    flash("Trip created", "success")
    return redirect(url_for("main.view_trip", trip_id=trip.id))


@main_bp.route("/trip/<int:trip_id>")
def view_trip(trip_id: int):
    trip = Trip.query.get_or_404(trip_id)
    balances = compute_balances(trip)
    suggestions = suggest_settlements(trip)
    return render_template("trip.html", trip=trip, balances=balances, suggestions=suggestions)


@main_bp.route("/trip/<int:trip_id>/participant", methods=["POST"]) 
def add_participant(trip_id: int):
    trip = Trip.query.get_or_404(trip_id)
    name = request.form.get("name", "").strip()
    if not name:
        flash("Name is required", "danger")
        return redirect(url_for("main.view_trip", trip_id=trip.id))
    p = Participant(trip_id=trip.id, name=name)
    db.session.add(p)
    db.session.commit()
    flash("Participant added", "success")
    return redirect(url_for("main.view_trip", trip_id=trip.id))


@main_bp.route("/trip/<int:trip_id>/expense", methods=["POST"]) 
def add_expense(trip_id: int):
    trip = Trip.query.get_or_404(trip_id)
    description = request.form.get("description", "").strip()
    amount = float(request.form.get("amount", 0) or 0)
    paid_by_id = int(request.form.get("paid_by_id"))
    split_mode = request.form.get("split_mode", "equal")

    if not description or amount <= 0:
        flash("Valid description and amount required", "danger")
        return redirect(url_for("main.view_trip", trip_id=trip.id))

    expense = Expense(trip_id=trip.id, description=description, amount=amount, paid_by_id=paid_by_id)
    db.session.add(expense)
    db.session.flush()  # get expense.id

    splits: list[ExpenseSplit] = []
    participant_ids = [p.id for p in trip.participants]

    if split_mode == "equal":
        share = round(amount / max(len(participant_ids), 1), 2)
        remainder = round(amount - share * len(participant_ids), 2)
        for idx, pid in enumerate(participant_ids):
            adj = remainder if idx == 0 else 0.0
            splits.append(ExpenseSplit(expense_id=expense.id, participant_id=pid, amount=share + adj))
    else:
        # custom splits from form: split_<participant_id>
        total = 0.0
        for pid in participant_ids:
            val = float(request.form.get(f"split_{pid}") or 0)
            total += val
            splits.append(ExpenseSplit(expense_id=expense.id, participant_id=pid, amount=val))
        if round(total, 2) != round(amount, 2):
            db.session.rollback()
            flash("Custom splits must sum to the total amount", "danger")
            return redirect(url_for("main.view_trip", trip_id=trip.id))

    db.session.add_all(splits)
    db.session.commit()
    flash("Expense added", "success")
    return redirect(url_for("main.view_trip", trip_id=trip.id))


@main_bp.route("/trip/<int:trip_id>/settlement", methods=["POST"]) 
def add_settlement(trip_id: int):
    trip = Trip.query.get_or_404(trip_id)
    payer_id = int(request.form.get("payer_id"))
    payee_id = int(request.form.get("payee_id"))
    amount = float(request.form.get("amount", 0) or 0)
    if payer_id == payee_id or amount <= 0:
        flash("Invalid settlement", "danger")
        return redirect(url_for("main.view_trip", trip_id=trip.id))
    s = Settlement(trip_id=trip.id, payer_id=payer_id, payee_id=payee_id, amount=amount)
    db.session.add(s)
    db.session.commit()
    flash("Settlement recorded", "success")
    return redirect(url_for("main.view_trip", trip_id=trip.id))
