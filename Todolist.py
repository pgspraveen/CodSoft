import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20, fill=tk.BOTH, expand=True)

        self.add_task_entry = tk.Entry(self.root, width=40)
        self.add_task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.load_tasks_into_listbox()

    def load_tasks(self):
        if os.path.exists('todolist.json'):
            with open('todolist.json', 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open('todolist.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks_into_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def add_task(self):
        task_text = self.add_task_entry.get()
        if task_text:
            self.tasks.append({'task': task_text, 'completed': False})
            self.save_tasks()
            self.load_tasks_into_listbox()
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task_text = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task_text:
                self.tasks[selected_task_index[0]]['task'] = new_task_text
                self.save_tasks()
                self.load_tasks_into_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = True
            self.save_tasks()
            self.load_tasks_into_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.save_tasks()
            self.load_tasks_into_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
