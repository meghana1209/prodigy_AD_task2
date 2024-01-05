import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(master, width=40, font=('Arial', 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, font=('Arial', 12))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(master, width=40, height=10, font=('Arial', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Mark as completed button
        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.complete_task, font=('Arial', 12))
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Remove task button
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, font=('Arial', 12))
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.destroy, font=('Arial', 12))
        self.quit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index] = f"[Completed] {self.tasks[task_index]}"
            self.refresh_task_list()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()