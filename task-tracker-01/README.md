## How to Use

Below are example commands for using the CLI:

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```
# Task Tracker CLI Challenge

This project is a command-line interface (CLI) application for managing tasks, implemented in Python. It is designed to help users add, list, update, and delete tasks efficiently from the terminal, without using any external libraries.

## Features

- Add new tasks
- List all tasks
- Update existing tasks
- Delete tasks
- Mark tasks as todo/in-progress/done

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Usage

Run the CLI with:

```bash
python app.py [command] [options]
```

#### Commands

- `add <task>`: Add a new task
- `list`: List all tasks
- `update <id> <new-task>`: Update a task
- `delete <id>`: Delete a task
- `complete <id>`: Mark a task as complete
- `incomplete <id>`: Mark a task as incomplete


## Example

```bash
python app.py add "Finish documentation"
python app.py list
python app.py complete 1
```
## Challenge Link

Add the link to the original challenge here:

[Roadmap.sh Task Tracker CLI Challenge](<your-challenge-link-here>)

## License

MIT
