import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} | Priority: {task['priority']} | Due: {task['due_date']}")

def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")  # validate date
        tasks.append({
            "name": name,
            "priority": priority,
            "due_date": due_date
        })
        save_tasks(tasks)
        print("Task added.")
    except ValueError:
        print("Invalid date format. Task not added.")

def remove_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–4.")

if __name__ == "__main__":
    main()
