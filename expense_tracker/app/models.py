from __future__ import annotations
from datetime import datetime
from typing import List, Dict
from . import db


class Trip(db.Model):
    __tablename__ = "trips"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    currency = db.Column(db.String(8), default="USD", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    participants = db.relationship("Participant", backref="trip", cascade="all, delete-orphan")
    expenses = db.relationship("Expense", backref="trip", cascade="all, delete-orphan")


class Participant(db.Model):
    __tablename__ = "participants"
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    # one-to-many splits and payments
    splits = db.relationship("ExpenseSplit", backref="participant", cascade="all, delete-orphan")


class Expense(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid_by_id = db.Column(db.Integer, db.ForeignKey("participants.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    paid_by = db.relationship("Participant", foreign_keys=[paid_by_id])
    splits = db.relationship("ExpenseSplit", backref="expense", cascade="all, delete-orphan")


class ExpenseSplit(db.Model):
    __tablename__ = "expense_splits"
    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey("expenses.id"), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey("participants.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)


class Settlement(db.Model):
    __tablename__ = "settlements"
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    payer_id = db.Column(db.Integer, db.ForeignKey("participants.id"), nullable=False)
    payee_id = db.Column(db.Integer, db.ForeignKey("participants.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    payer = db.relationship("Participant", foreign_keys=[payer_id])
    payee = db.relationship("Participant", foreign_keys=[payee_id])


# ---------- Balance utilities ----------

def compute_balances(trip: Trip) -> Dict[int, float]:
    """Return mapping participant_id -> net balance (positive means others owe them)."""
    balances: Dict[int, float] = {p.id: 0.0 for p in trip.participants}

    for expense in trip.expenses:
        balances[expense.paid_by_id] += expense.amount
        for split in expense.splits:
            balances[split.participant_id] -= split.amount

    # Apply settlements as transfers
    settlements = Settlement.query.filter_by(trip_id=trip.id).all()
    for s in settlements:
        balances[s.payer_id] -= s.amount
        balances[s.payee_id] += s.amount

    return balances


def suggest_settlements(trip: Trip) -> List[Dict[str, int | float]]:
    """Greedy settlement suggestions from debtors to creditors."""
    balances = compute_balances(trip)
    debtors = [(pid, -amt) for pid, amt in balances.items() if amt < 0]
    creditors = [(pid, amt) for pid, amt in balances.items() if amt > 0]

    debtors.sort(key=lambda x: x[1], reverse=True)
    creditors.sort(key=lambda x: x[1], reverse=True)

    i, j = 0, 0
    suggestions: List[Dict[str, int | float]] = []
    while i < len(debtors) and j < len(creditors):
        debtor_id, debt_amt = debtors[i]
        creditor_id, cred_amt = creditors[j]
        pay = min(debt_amt, cred_amt)
        suggestions.append({"payer_id": debtor_id, "payee_id": creditor_id, "amount": round(pay, 2)})
        debtors[i] = (debtor_id, round(debt_amt - pay, 2))
        creditors[j] = (creditor_id, round(cred_amt - pay, 2))
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1
    return suggestions
