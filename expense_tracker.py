"""
Expense Tracker 

This  allows users to track their expenses by adding, viewing,
saving, and loading expense data from a CSV file.

Functions:
    clear_screen(): Clears the console screen.
    add_expense(expenses): Adds a new expense to the expense list.
    view_expenses(expenses): Displays the recorded expenses.
    save_expenses(expenses, filename="expenses.csv"): Saves expenses to a CSV file.
    load_expenses(filename="expenses.csv"): Loads expenses from a CSV file.
    main(): The main function that controls the program flow.
"""
import datetime
import csv
import os

def clear_screen():
   '''
    This function clears the console screen. It uses a conditional expression:
    os.name == 'nt': Checks if the operating system is Windows ('nt'). If so, it uses the cls command.
  '''
   os.system('cls' if os.name == 'nt' else 'clear')

def add_expense(expenses):
    '''
    This function adds a new expense to the expenses list.
    It takes the expense amount, category, description, and date as input.
    It handles potential ValueError exceptions.
    It uses datetime.datetime.strptime() to parse the date string entered by the user. If the user leaves the date blank, it uses the current date.
    It appends the new expense as a list [date, amount, category, description] to the expenses list.
    
    '''
    clear_screen()
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        date_str = input("Enter date (YYYY-MM-DD, or leave blank for today): ")
        if date_str:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = datetime.date.today()
        expenses.append([date, amount, category])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount and a valid date format.")
    input("Press Enter to continue...")

def view_expenses(expenses):
    '''
    This function displays the recorded expenses.
    It checks if there are any expenses recorded. If not, it prints a message.
    It prints a formatted table of expenses, including the date, amount, category, and description.
    '''
    clear_screen()
    if not expenses:
        print("No expenses recorded yet.")
        input("Press Enter to continue...")
        return

    print("Expenses:")
    print("-" * 50)
    print("{:<12} {:<10} {:<15} ".format("Date", "Amount", "Category"))
    print("-" * 50)
    for expense in expenses:
        print("{:<12} {:<10.2f} {:<15} ".format(str(expense[0]), expense[1], expense[2]))
    print("-" * 50)
    input("Press Enter to continue...")


def save_expenses(expenses, filename="expenses.csv"):
    '''
    This function saves the expenses to a CSV file named expenses.csv.
    It opens the file in write mode ('w').
    It uses csv.writer to write the expenses to the CSV file.
    It includes a header row in the CSV file.
    It includes error handling in case there is a problem writing to the file.

    '''
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Amount", "Category"])  # Header row
            writer.writerows(expenses)
        print(f"Expenses saved to {filename}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses(filename="expenses.csv"):
    '''
    This function loads expenses from the expenses.csv file.
    It opens the file in read mode ('r').
    It uses csv.reader to read the expenses from the CSV file.
    It converts the date string back to a datetime.date object and the amount to a float.
    It handles FileNotFoundError if the file doesn't exist and other potential errors during file reading.
   '''
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
    '''
    This is the main function that controls the program flow.
    It loads expenses from the CSV file at the start.
    It presents a menu to the user: Add Expense, View Expenses, Save Expenses, Exit.
    It takes the user's choice and calls the appropriate function.
    It saves the expenses to the CSV file before exiting.
    
    '''
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