import argparse
import time
import json
import csv


def setup_config():
    config = {
        "data_file": "expenses.json",
        "budget_file": "budget.json",
    }
    return config


def read_from_file(file_name):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def write_to_file(file_name, expenses):
    try:
        with open(file_name, "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")


def setup_add_command(subparsers):
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("description", type=str, help="Expense description")
    add_parser.add_argument("amount", type=float, help="Expense amount")
    add_parser.add_argument(
        "--category",
        type=str,
        help="Expense category",
        choices=["food", "transportation", "entertainment", "utilities", "other"],
    )
    return add_parser


def setup_update_command(subparsers):
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("id", type=int, help="Expense ID to update")
    update_parser.add_argument(
        "--description",
        type=str,
        help="New expense description",
    )
    update_parser.add_argument(
        "--amount",
        type=float,
        help="New expense amount",
    )
    update_parser.add_argument(
        "--category",
        type=str,
        help="New expense category",
        choices=["food", "transportation", "entertainment", "utilities", "other"],
    )
    return update_parser


def setup_delete_command(subparsers):
    delete_parser = subparsers.add_parser("delete", help="Delete an existing expense")
    delete_parser.add_argument("id", type=int, help="Expense ID to delete")
    return delete_parser


def setup_list_command(subparsers):
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument(
        "--category",
        type=str,
        help="Filter by category",
        choices=["food", "transportation", "entertainment", "utilities", "other"],
    )
    return list_parser


def setup_summary_command(subparsers):
    summary_parser = subparsers.add_parser("summary", help="Show summary of expenses")
    summary_parser.add_argument(
        "--month", type=int, choices=range(1, 13), help="Filter by month (1-12)"
    )
    return summary_parser


def setup_budget_command(subparsers):
    budget_parser = subparsers.add_parser("budget", help="Set or view budgets")
    budget_parser.add_argument(
        "--set", type=float, help="Set a new budget amount for a specified month"
    )
    budget_parser.add_argument(
        "--month",
        type=int,
        choices=range(1, 13),
        help="Specify the month for the budget (1-12)",
    )
    return budget_parser


def setup_export_command(subparsers):
    export_parser = subparsers.add_parser("export", help="Export expenses to CSV")
    export_parser.add_argument(
        "--file", type=str, default="expenses.csv", help="Output CSV file name"
    )
    return export_parser


def setup_argparse():
    # Setup the main argument parser
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Setup the subparsers
    setup_add_command(subparsers)
    setup_update_command(subparsers)
    setup_delete_command(subparsers)
    setup_list_command(subparsers)
    setup_summary_command(subparsers)
    setup_budget_command(subparsers)
    setup_export_command(subparsers)
    return parser


def extract_month_from_timestamp(timestamp):
    return time.localtime(timestamp).tm_mon


def add_expense(description, amount, category=None):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Auto Increment highest ID in dataset by 1
    highest_id = max((expense["id"] for expense in expenses), default=0)
    new_expense = {
        "id": highest_id + 1,
        "description": description,
        "amount": amount,
        "created_at": time.time(),
        "updated_at": time.time(),
        "category": category,
    }
    new_expense["month"] = extract_month_from_timestamp(new_expense["created_at"])

    # Budget Check
    budget_for_month = budget.get(str(new_expense["month"]), 0)
    month_sum = sum(
        expense["amount"]
        for expense in expenses
        if expense["month"] == new_expense["month"]
    )
    if month_sum + amount > budget_for_month:
        print(
            f"Warning: This expense exceeds the budget for month {new_expense['month']} (Budget: {budget_for_month:.2f}) (Current Total: {month_sum:.2f}, New Total: {month_sum + amount:.2f})"
        )
    expenses.append(new_expense)
    write_to_file(config["data_file"], expenses)
    return f'Expense added successfully (ID: {new_expense["id"]})'


def update_expense(expense_id, description=None, amount=None, category=None):
    if amount is not None and amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    for expense in expenses:
        if expense["id"] == expense_id:
            if description is not None:
                expense["description"] = description
            if amount is not None:
                expense["amount"] = amount
            if category is not None:
                expense["category"] = category
            expense["updated_at"] = time.time()
            write_to_file(config["data_file"], expenses)
            return f"Expense with ID {expense_id} updated successfully."

    raise ValueError(f"Expense with ID {expense_id} not found.")


def delete_expense(expense_id):
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            del expenses[i]
            write_to_file(config["data_file"], expenses)
            return f"Expense with ID {expense_id} deleted successfully."

    raise ValueError(f"Expense with ID {expense_id} not found.")


# list first should filter then print
def list_expenses(category=None):
    if not expenses:
        return "No expenses found."

    if category:
        filtered_expenses = [
            expense for expense in expenses if expense["category"] == category
        ]
    else:
        filtered_expenses = expenses

    if not filtered_expenses:
        return f"No expenses found for category '{category}'."

    result = "Expenses:\n"
    for expense in filtered_expenses:
        result += f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']:.2f}, Category: {expense.get('category', 'N/A')}, Created At: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expense['created_at']))}, Updated At: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expense['updated_at']))}\n"
    return result.strip()


def summarize_expenses(month=None):
    if not expenses:
        return 0

    if month:
        filtered_expenses = [
            expense for expense in expenses if expense["month"] == month
        ]
    else:
        filtered_expenses = expenses

    total_amount = sum(expense["amount"] for expense in filtered_expenses)
    return f"Total Expenses: {total_amount:.2f}"


def handle_budget_command(set_amount=None, month=None):
    if set_amount is not None and set_amount <= 0:
        raise ValueError("Budget amount must be greater than zero.")

    if month and set_amount is not None:
        budget[str(month)] = set_amount
        write_to_file(config["budget_file"], budget)
        return f"Budget for month {month} set to {set_amount:.2f}."

    if month and set_amount is None:
        current_budget = budget.get(str(month), 0)
        return f"Current budget for month {month}: {current_budget:.2f}"

    if not month:
        result = "Current Budgets:\n"
        for m in range(1, 13):
            current_budget = budget.get(str(m), 0)
            result += f"Month {m}: {current_budget:.2f}\n"
        return result.strip()


def export_expenses_to_csv(file_name):
    if not expenses:
        return "Nothing to export. No expenses found."
    try:
        with open(file_name, "w", newline="") as csvfile:
            fieldnames = [
                "id",
                "description",
                "amount",
                "category",
                "created_at",
                "updated_at",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(
                    {
                        "id": expense["id"],
                        "description": expense["description"],
                        "amount": f"{expense['amount']:.2f}",
                        "category": expense.get("category", ""),
                        "created_at": time.strftime(
                            "%Y-%m-%d %H:%M:%S", time.localtime(expense["created_at"])
                        ),
                        "updated_at": time.strftime(
                            "%Y-%m-%d %H:%M:%S", time.localtime(expense["updated_at"])
                        ),
                    }
                )
        return f"Expenses exported successfully to {file_name}."
    except Exception as e:
        raise ValueError(f"Error exporting to CSV: {e}")


def main():
    global expenses
    global config
    global budget

    config = setup_config()
    expenses = read_from_file(config["data_file"])
    budget = read_from_file(config["budget_file"])
    if not isinstance(budget, dict):
        budget = {}
    parser = setup_argparse()

    try:
        args = parser.parse_args()

        handler_res = None
        match args.command:
            case "add":
                handler_res = add_expense(args.description, args.amount, args.category)
            case "update":
                handler_res = update_expense(
                    args.id, args.description, args.amount, args.category
                )
            case "delete":
                handler_res = delete_expense(args.id)
            case "list":
                handler_res = list_expenses(args.category)
            case "summary":
                handler_res = summarize_expenses(args.month)
            case "budget":
                handler_res = handle_budget_command(args.set, args.month)
            case "export":
                handler_res = export_expenses_to_csv(args.file)
        print(handler_res)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
