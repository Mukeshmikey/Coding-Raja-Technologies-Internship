import json
import os
from datetime import datetime

# Define the file to store transactions
TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
        return transactions
    else:
        return {"income": [], "expenses": []}

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=2)

def display_transactions(transactions, category):
    print(f"\n** {category.capitalize()} Transactions **")
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['category']}: ${transaction['amount']}")

def add_transaction(transactions, category, amount):
    new_transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "amount": float(amount)
    }
    transactions[category].append(new_transaction)
    save_transactions(transactions)

def calculate_budget(transactions):
    income = sum(transaction['amount'] for transaction in transactions['income'])
    expenses = sum(transaction['amount'] for transaction in transactions['expenses'])
    remaining_budget = income - expenses
    return remaining_budget

def analyze_expenses(transactions):
    expense_categories = set(transaction['category'] for transaction in transactions['expenses'])
    print("\n** Expense Analysis **")
    for category in expense_categories:
        total_spent = sum(transaction['amount'] for transaction in transactions['expenses'] if transaction['category'] == category)
        print(f"{category.capitalize()}: ${total_spent}")

# Main program loop
def main():
    transactions = load_transactions()

    while True:
        print("\n** Budget Tracker **")
        print("1. Enter Income")
        print("2. Enter Expense")
        print("3. View Expenses")
        print("4. Calculate Budget")
        print("5. Expense Analysis")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            category = "income"
            amount = input("Enter income amount: $")
            add_transaction(transactions, category, amount)
        elif choice == "2":
            category = "expenses"
            amount = input("Enter expense amount: $")
            add_transaction(transactions, category, amount)
        elif choice == "3":
            display_transactions(transactions['expenses'], "expenses")
        elif choice == "4":
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == "5":
            analyze_expenses(transactions)
        elif choice == "6":
            print("Exiting the Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()