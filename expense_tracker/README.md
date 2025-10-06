# Travel Expense Tracker

A simple Flask app to track shared travel expenses. Create trips, add participants, record expenses with equal or custom splits, see balances, and record settlements.

## Quickstart

1. Create virtualenv and install deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
python run.py
```

3. Open http://localhost:5000

## Notes
- Default DB is SQLite file `expense_tracker.db` placed next to the app.
- Use `DATABASE_URL` env var to point to Postgres or another DB.
- Migrations are set up via Flask-Migrate; you can run `flask db init/migrate/upgrade`.
