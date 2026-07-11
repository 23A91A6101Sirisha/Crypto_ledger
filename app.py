from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Tells Flask to use a local SQLite file named ledger.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ledger.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'emergency_placement_secret_key'

db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# This is what a database table looks like in Python code (ORM)
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_name = db.Column(db.String(10), nullable=False)   # e.g., BTC, ETH
    amount = db.Column(db.Float, nullable=False)            # e.g., 0.025
    price_usd = db.Column(db.Float, nullable=False)         # e.g., 60000.00
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Automatically create the database file and table when app starts
with app.app_context():
    db.create_all()

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Grab data incoming from the frontend HTML form
        token = request.form.get('token_name').upper()
        amount_str = request.form.get('amount')
        price_str = request.form.get('price_usd')

        # 2. Defensive Backend Validation (Interviewers love this!)
        if not token or not amount_str or not price_str:
            return "Error: Missing form inputs", 400
        
        try:
            # 3. Save the new row safely into the SQLite Database
            new_tx = Transaction(
                token_name=token,
                amount=float(amount_str),
                price_usd=float(price_str)
            )
            db.session.add(new_tx)
            db.session.commit()
            return redirect('/')
        except ValueError:
            return "Error: Invalid numeric input data", 400

    # If it's a GET request, fetch all records and calculate totals
    all_transactions = Transaction.query.order_by(Transaction.timestamp.desc()).all()
    
    total_value = sum(tx.amount * tx.price_usd for tx in all_transactions)

    # Send data arrays over to the Jinja2 HTML engine
    return render_template('index.html', transactions=all_transactions, total_value=total_value)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
