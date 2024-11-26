# Simple Budget Tracker

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def show_balance(self):
        print(f"\nTotal Income: ${self.income}")
        print(f"Total Expenses: ${self.expenses}")
        print(f"Balance: ${self.income - self.expenses}\n")

    def add_income(self):
        amount = float(input("Enter income amount: "))
        self.income += amount
        print(f"Income of ${amount} added.")

    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        self.expenses += amount
        print(f"Expense of ${amount} added.")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Show Balance")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            budget_tracker.show_balance()
        elif choice == '2':
            budget_tracker.add_income()
        elif choice == '3':
            budget_tracker.add_expense()
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
