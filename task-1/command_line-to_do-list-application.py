import json
import os
from datetime import datetime

# Define the file to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['description']} - Priority: {task['priority']} - Due Date: {task['due_date']}")

def add_task(tasks, description, priority, due_date):
    new_task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task['description']}")
        save_tasks(tasks)
    else:
        print("Invalid task index")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Marked task as completed: {tasks[task_index - 1]['description']}")
        save_tasks(tasks)
    else:
        print("Invalid task index")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n** To-Do List App **")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, description, priority, due_date)
        elif choice == "3":
            task_index = int(input("Enter task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()