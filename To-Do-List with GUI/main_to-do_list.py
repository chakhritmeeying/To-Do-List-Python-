import tkinter as tk
from tkinter import messagebox


class ToDoListMainForm:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")

        self.tasks = self.load_tasks()
        self.todolist_widgets()

    def todolist_widgets(self):
        tk.Label(
            self.root,
            text="Welcome to your To-Do List!",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        buttons_frame = tk.Frame(
            self.root
        )
        buttons_frame.pack(pady=10)
        button_add_task = tk.Button(
            buttons_frame,
            text="Add a task",
            width=20,
            command=self.add_task_widgets
        )
        button_view_tasks = tk.Button(
            buttons_frame,
            text="View tasks",
            width=20,
            command=self.view_tasks_widgets
        )
        button_del_task = tk.Button(
            buttons_frame,
            text="Delete a task",
            width=20
        )
        button_search = tk.Button(
            buttons_frame,
            text="Search task",
            width=20
        )
        button_add_task.pack(pady=10)
        button_view_tasks.pack(pady=10)
        button_del_task.pack(pady=10)
        button_search.pack(pady=10)

    def add_task_widgets(self):
        add_form = tk.Toplevel(self.root)
        add_form.title("Add Task")
        add_form.geometry("400x300")

        tk.Label(
            add_form,
            text="Add your task"
        ).pack(pady=10)
        entry_add_task = tk.Entry(
            add_form,
            width=30
        )
        sumit_button = tk.Button(
            add_form,
            text="Submit",
            command=lambda: self.add_task(
                entry_add_task.get(),
                add_form
            )
        )
        button_close = tk.Button(
            add_form,
            text="Close",
            command=lambda: add_form.destroy()
        )
        entry_add_task.pack(pady=10)
        sumit_button.pack(pady=10)
        button_close.pack(pady=10)

    def add_task(self, task, window):
        self.tasks.append(task)
        messagebox.showinfo(
            "Task Added",
            f"{task} has been added to your List."
        )
        self.save_tasks()
        window.destroy()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        self.tasks = []
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.tasks.append(line.strip())
            return self.tasks
        except FileNotFoundError:
            return []

    def view_tasks_widgets(self):
        view_form = tk.Toplevel(self.root)
        view_form.title("View To-Do List")
        view_form.geometry("400x300")

        tk.Label(
            view_form,
            text="Your To-Do List"
        ).pack(pady=10)

        self.create_listbox_tasks(view_form)
        button_close = tk.Button(
            view_form,
            text="Close",
            command=lambda: view_form.destroy()
        )
        button_close.pack(pady=10)

    def create_listbox_tasks(self, form):
        form = form
        self.listbox_tasks = tk.Listbox(
            form,
            selectmode="single",
            highlightcolor="blue",
            width=40,
        )
        self.listbox_tasks.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.listbox_tasks.insert(tk.END, f"{idx}. {task}")
        self.listbox_tasks.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListMainForm(root)
    root.mainloop()
