import sys
import json
import time
import os

save_file_name = "tasks_data.json"
save_file_path = f"./{save_file_name}"

def ReadFromFile(file_name):
    if not os.path.exists(file_name):
        SaveToFile([], file_name)
        return []

    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def SaveToFile(data, file_name):
    with open(file_name, "w") as f:
        json.dump(data, f)


def GetTime():
    return time.time()


def generateNewId():
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def CreateTask(task_name):
    print(f"Creating new task: {task_name}")
    new_task = {
        "id": generateNewId(),
        "description": task_name,
        "status": "todo",
        "created_at": GetTime(),
        "updated_at": None,
    }
    return new_task


def handle_add(task_title):
    try:
        new_task = CreateTask(task_title)
        tasks.append(new_task)
        SaveToFile(tasks, save_file_path)
        return f"Task added successfully (ID: {new_task['id']})"
    except Exception as e:
        return f"Error during task creation: {e}"


def handle_update(task_id, new_name):
    try:
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_name
                task["updated_at"] = GetTime()
                SaveToFile(tasks, save_file_path)
                return f"Successfully updated task name for id: {task_id}"
        return f"Failed to locate task with id: {task_id}"
    except Exception as e:
        return f"Error during task creation: {e}"
    
def handle_update_status(task_id, new_status):
    try:
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updated_at"] = GetTime()
                SaveToFile(tasks, save_file_path)
                return f"Successfully updated task status for id: {task_id}"
        return f"Failed to locate task with id: {task_id}"
    except Exception as e:
        return f"Error during task creation: {e}"


def handle_delete(task_id):
    try:
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                SaveToFile(tasks, save_file_path)
                return f"Successfully deleted task: {task_id}"
        return f"Failed to locate task with id: {task_id}"
    except Exception as e:
        return f"Error during task creation: {e}"

def FilterTasksByStatus(status):
    return [task for task in tasks if task["status"] == status]

def PrintTasks(tasks):
    if not tasks:
        return "No tasks found"
    result = "Tasks:\n"
    for task in tasks:
        result += f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}\n"
    return result

def main():
    global tasks
    tasks = ReadFromFile(save_file_path)
    args = sys.argv

    if len(args) < 2:
        return "You need to input a command"

    command = args[1]

    match command:
        case "add":
            if len(args) < 3:
                return "You need to specify a task name"
            task_title = args[2]
            return handle_add(task_title)
        case "update":
            if len(args) < 4:
                return "You need to specify id and new task name"
            task_id = int(args[2])
            new_name = args[3]
            return handle_update(task_id, new_name)
        case "delete":
            if len(args) < 3:
                return "You need to specify task id to delete"
            task_id = int(args[2])
            return handle_delete(task_id)
        case "mark-done":
            if len(args) < 3:
                return "You need to specify task id to mark as done"
            task_id = int(args[2])
            return handle_update_status(task_id, "done")
        case "mark-in-progress":
            if len(args) < 3:
                return "You need to specify task id to mark as in-progress"
            task_id = int(args[2])
            return handle_update_status(task_id, "in-progress")
        case "mark-todo":
            if len(args) < 3:
                return "You need to specify task id to mark as todo"
            task_id = int(args[2])
            return handle_update_status(task_id, "todo")
        case "list":
            if len(args) < 3:
                return PrintTasks(tasks)
            filter = args[2]
            if filter == "todo":
                return PrintTasks(FilterTasksByStatus("todo"))
            elif filter == "done":
                return PrintTasks(FilterTasksByStatus("done"))
            elif filter == "in-progress":
                return PrintTasks(FilterTasksByStatus("in-progress"))
            else:
                return f"Unknown filter: {filter}"
        case _:
            return f"No command {command} is available"


if __name__ == "__main__":
    res = main()
    print(res)
