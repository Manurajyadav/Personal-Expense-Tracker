from expense import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker!")
    expensive_file_path = "expenses.csv"
    budget = 100000

    # Get user input for Expense.
    expense = get_user_expense()
    
    # Write their expense to a file.
    save_expense_to_file(expense, expensive_file_path)

    # Read file and summarize expense.
    summarize_expense(expensive_file_path, budget)

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    expense_categories = ["Food","Home","Work","Fun","Mislaneous"]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}.{category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again")

def save_expense_to_file(expense: Expense, expensive_file_path):
    print(f"Saving User Expense: {expense} to {expensive_file_path}")
    with open(expensive_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")



def summarize_expense(expensive_file_path, budget):
    print(f"Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expensive_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense  = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
        
        amount_by_category = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        print("Expenses by category")
        for key, amount in amount_by_category.items():
            print(f" {key}: ₹{amount:.2f}")

        total_spent = sum([x.amount for x in expenses])
        print(f"You've spent ₹{total_spent:.2f} this month")

        remaining_budget = budget - total_spent
        print(f"Budget remining ₹{remaining_budget:.2f}")

        current_date = datetime.date.today()
        last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]
        remaining_days = last_day_of_month - current_date.day

        daily_budget = remaining_budget / remaining_days
        print(green(f"Budget per day: ₹{daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"




if __name__ == "__main__":
    main()