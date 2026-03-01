# Expense Tracker

This project is a simple command-line tool for tracking expenses and managing monthly budgets. This is part of the [Roadmap.sh Cackend Roadmap](https://roadmap.sh/backend) project challenges, specifically the [Expense Tracker Challenge](https://roadmap.sh/projects/expense-tracker).

## Features

- Add, update, delete expenses
- Categorize expenses (food, transportation, entertainment, utilities, other)
- List expenses, optionally filtered by category
- View monthly or overall expense summaries
- Set and view monthly budgets
- Export expenses to CSV

## Usage

Run the tracker from the command line:

```sh
python main.py <command> [options]
```

### Commands

- **add**  
  Add a new expense  
  Example:

  ```sh
  python main.py add "Lunch" 12.5 --category food
  ```

- **update**  
  Update an expense by ID  
  Example:

  ```sh
  python main.py update 1 --amount 15.0 --description "Lunch with friends"
  ```

- **delete**  
  Delete an expense by ID  
  Example:

  ```sh
  python main.py delete 1
  ```

- **list**  
  List all expenses, optionally by category  
  Example:

  ```sh
  python main.py list --category food
  ```

- **summary**  
  Show total expenses, optionally for a specific month  
  Example:

  ```sh
  python main.py summary --month 6
  ```

- **budget**  
  Set or view budgets  
  Example:

  ```sh
  python main.py budget --set 500 --month 6
  python main.py budget --month 6
  python main.py budget
  ```

- **export**  
  Export expenses to CSV. Default value for file is expenses.csv

  Example:

  ```sh
    python main.py export
  python main.py export --file expenses.csv
  ```

## Data Files

- `expenses.json`: Stores all expense records.
- `budget.json`: Stores monthly budget amounts.
- `expenses.csv`: Generated when exporting expenses.

## Requirements

- Python 3.x

See [main.py](main.py) for implementation details.
