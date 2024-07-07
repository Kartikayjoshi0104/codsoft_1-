import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # List to store tasks
        self.tasks = []

        # Frame for the entry and add button
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Entry widget to enter a task
        self.task_entry = tk.Entry(frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Button to add a task
        self.add_button = tk.Button(frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=60, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Frame for the action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Button to delete a selected task
        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Button to update a selected task
        self.update_button = tk.Button(button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        # Button to clear all tasks
        self.clear_button = tk.Button(button_frame, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task to update.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def clear_all_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
