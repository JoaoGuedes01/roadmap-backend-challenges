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
            print(task["id"])
            if task["id"] == task_id:
                task["description"] = new_name
                SaveToFile(tasks, save_file_path)
                return f"Successfully updated task name for id: {task_id}"
        return f"Failed to locate task with id: {task_id}"
    except Exception as e:
        return f"Error during task creation: {e}"


def handle_delete(task_id):
    try:
        for task in tasks:
            print(task["id"])
            if task["id"] == task_id:
                tasks.remove(task)
                SaveToFile(tasks, save_file_path)
                return f"Successfully deleted task: {task_id}"
        return f"Failed to locate task with id: {task_id}"
    except Exception as e:
        return f"Error during task creation: {e}"


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
        case "list":
            return tasks
        case _:
            return f"No command {command} is available"


if __name__ == "__main__":
    res = main()
    print(res)
