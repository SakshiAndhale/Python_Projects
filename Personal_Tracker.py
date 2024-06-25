import pandas as pd
from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])
    
    def add_transaction(self, description, category, amount):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_transaction = {'Date': date, 'Description': description, 'Category': category, 'Amount': amount}
        self.transactions = self.transactions.append(new_transaction, ignore_index=True)
        print("Transaction added successfully.")
    
    def edit_transaction(self, index, description=None, category=None, amount=None):
        if 0 <= index < len(self.transactions):
            if description:
                self.transactions.at[index, 'Description'] = description
            if category:
                self.transactions.at[index, 'Category'] = category
            if amount is not None:
                self.transactions.at[index, 'Amount'] = amount
            print("Transaction updated successfully.")
        else:
            print("Invalid transaction index.")
    
    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            self.transactions = self.transactions.drop(index).reset_index(drop=True)
            print("Transaction deleted successfully.")
        else:
            print("Invalid transaction index.")
    
    def view_transactions(self):
        if self.transactions.empty:
            print("No transactions to show.")
        else:
            print(self.transactions)
    
    def generate_summary(self):
        if self.transactions.empty:
            print("No transactions to summarize.")
        else:
            income = self.transactions[self.transactions['Category'] == 'Income']['Amount'].sum()
            expenses = self.transactions[self.transactions['Category'] == 'Expense']['Amount'].sum()
            balance = income - expenses
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Balance: ${balance:.2f}")

def main():
    tracker = BudgetTracker()
    
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. Edit Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions")
        print("5. Generate Summary")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter description: ")
            category = input("Enter category (Income/Expense): ")
            amount = float(input("Enter amount: "))
            tracker.add_transaction(description, category, amount)
        
        elif choice == '2':
            index = int(input("Enter transaction index to edit: "))
            description = input("Enter new description (or press Enter to skip): ")
            category = input("Enter new category (Income/Expense) (or press Enter to skip): ")
            amount = input("Enter new amount (or press Enter to skip): ")
            amount = float(amount) if amount else None
            tracker.edit_transaction(index, description, category, amount)
        
        elif choice == '3':
            index = int(input("Enter transaction index to delete: "))
            tracker.delete_transaction(index)
        
        elif choice == '4':
            tracker.view_transactions()
        
        elif choice == '5':
            tracker.generate_summary()
        
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
