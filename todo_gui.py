import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ----------------
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Select a task to remove.")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = load_tasks()

# Input box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)

btn_remove = tk.Button(root, text="Remove Selected Task", command=remove_task)
btn_remove.pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Load existing tasks
for task in tasks:
    listbox.insert(tk.END, task)

# Run the app
root.mainloop()
