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
            width=20,
            command=self.delete_task_widgets
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
        if hasattr(self, "add_form") and self.add_form.winfo_exists():
            self.add_form.focus()
            return
        self.add_form = tk.Toplevel(self.root)
        self.add_form.title("Add Task")
        self.add_form.geometry("400x300")

        tk.Label(
            self.add_form,
            text="Add your task"
        ).pack(pady=10)
        entry_add_task = tk.Entry(
            self.add_form,
            width=30
        )
        sumit_button = tk.Button(
            self.add_form,
            text="Submit",
            command=lambda: self.add_task(
                entry_add_task.get(),
                self.add_form
            )
        )
        button_close = tk.Button(
            self.add_form,
            text="Close",
            command=lambda: self.add_form.destroy()
        )
        entry_add_task.pack(pady=10)
        sumit_button.pack(pady=10)
        button_close.pack(pady=10)

    def add_task(self, task, window):
        if not task.strip():
            messagebox.showwarning(
                "Invalid Task",
                "Task cannot be empty."
            )
            return
        self.tasks.append(task)
        messagebox.showinfo(
            "Task Added",
            f"{task} has been added to your List."
        )
        self.reset_listbox_tasks()
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

    def delete_task_widgets(self):
        if hasattr(self, "delete_form") and self.delete_form.winfo_exists():
            self.delete_form.focus()
            return

        self.delete_form = tk.Toplevel(self.root)
        self.delete_form.title("Delete task")
        self.delete_form.geometry("400x300")

        self.create_listbox_tasks(self.delete_form)
        button_delete = tk.Button(
            self.delete_form,
            text="Delete",
            width=10,
            command=lambda: self.delete_tasks(
                self.listbox_tasks.curselection()
            )
        )
        button_close = tk.Button(
            self.delete_form,
            text="Close",
            width=10,
            command=lambda: self.delete_form.destroy()
        )
        button_delete.pack(pady=10)
        button_close.pack(pady=10)

    def delete_tasks(self, tasks):
        selected_tasks = tasks
        check_confirm = messagebox.askyesno(
            "Confirm Deletion", f"Your select is {self.listbox_tasks.get(selected_tasks)}"
        )
        if not check_confirm:
            self.delete_form.focus()
            return
        self.tasks.pop(selected_tasks[0])
        messagebox.showinfo(
            "Deleted",
            f"{self.listbox_tasks.get(selected_tasks[0])} has been deleted."
        )
        self.reset_listbox_tasks()
        self.save_tasks()
        self.delete_form.focus()

    def view_tasks_widgets(self):
        if hasattr(self, "view_form") and self.view_form.winfo_exists():
            self.view_form.focus()
            return
        self.view_form = tk.Toplevel(self.root)
        self.view_form.title("View To-Do List")
        self.view_form.geometry("400x300")

        tk.Label(
            self.view_form,
            text="Your To-Do List"
        ).pack(pady=10)

        self.create_listbox_tasks(self.view_form)
        button_close = tk.Button(
            self.view_form,
            text="Close",
            command=lambda: self.view_form.destroy()
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
        self.reset_listbox_tasks()
        self.listbox_tasks.pack(pady=10)

    def reset_listbox_tasks(self):
        self.listbox_tasks.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.listbox_tasks.insert(tk.END, f"{idx}. {task}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListMainForm(root)
    root.mainloop()
