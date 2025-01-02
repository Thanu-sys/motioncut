import datetime
import csv
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_expense(expenses):
    clear_screen()
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter a brief description: ")
        date_str = input("Enter date (YYYY-MM-DD, or leave blank for today): ")
        if date_str:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = datetime.date.today()
        expenses.append([date, amount, category, description])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount and a valid date format.")
    input("Press Enter to continue...")

def view_expenses(expenses):
    clear_screen()
    if not expenses:
        print("No expenses recorded yet.")
        input("Press Enter to continue...")
        return

    print("Expenses:")
    print("-" * 50)
    print("{:<12} {:<10} {:<15} {:<15}".format("Date", "Amount", "Category", "Description"))
    print("-" * 50)
    for expense in expenses:
        print("{:<12} {:<10.2f} {:<15} {:<15}".format(str(expense[0]), expense[1], expense[2], expense[3]))
    print("-" * 50)
    input("Press Enter to continue...")


def save_expenses(expenses, filename="expenses.csv"):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Amount", "Category", "Description"])  # Header row
            writer.writerows(expenses)
        print(f"Expenses saved to {filename}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses(filename="expenses.csv"):
    expenses = []
    try:
        if os.path.exists(filename):
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None) #skip header row
                for row in reader:
                    date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
                    amount = float(row[1])
                    expenses.append([date, amount, row[2], row[3]])
    except FileNotFoundError:
        print("No existing expense file found. Starting fresh.")
    except ValueError:
        print("Error reading the expense file. It might be corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")
    return expenses

def main():
    expenses = load_expenses()

    while True:
        clear_screen()
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()