import tkinter as tk
from tkinter import messagebox


class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.tasks = self.load_tasks()
        self.todolist_widgets()

    def todolist_widgets(self):
        welcome_label = tk.Label(
            self.root,
            text="Welcome to your To-Do List",
            font=(14)
        )
        input_frame = tk.Frame(
            self.root
        )
        input_label = tk.Label(
            input_frame,
            text="Enter your To-Do List"
        )
        self.input_entry = tk.Entry(
            input_frame,
            width=50
        )

        self.listbox_tasks = tk.Listbox(
            self.root,
            highlightcolor="blue",
            width=50,
        )

        button_frame = tk.Frame(
            self.root
        )
        add_task_button = tk.Button(
            button_frame,
            text="Add Task",
            width=12,
            command=self.add_task
        )
        remove_task_button = tk.Button(
            button_frame,
            text="Remove Task",
            width=12,
            command=self.remove_task
        )
        close_button = tk.Button(
            button_frame,
            text="Close Program",
            width=12,
            command=self.root.quit
        )

        welcome_label.pack(pady=10)
        input_frame.pack(pady=10)
        input_label.pack()
        self.input_entry.pack()
        self.reset_listbox('')
        self.listbox_tasks.pack(pady=10)
        button_frame.pack(pady=10)
        add_task_button.grid(row=0, column=0)
        remove_task_button.grid(row=0, column=1, padx=5)
        close_button.grid(row=0, column=2, padx=5)
        # Show select taks on entry
        self.listbox_tasks.bind("<<ListboxSelect>>",
                                self.onclick_list_to_entry)

        # Check entry box vs listbox
        self.input_entry.bind("<KeyRelease>", self.check_match_entry_listbox)

    def load_tasks(self):
        self.tasks = []
        try:
            # Check file
            with open("tasks.txt", "r") as file:
                for task in file:
                    self.tasks.append(task.strip())
            return self.tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task+"\n")

    def reset_listbox(self, match):
        # Clear the listbox
        self.listbox_tasks.delete(0, tk.END)
        # Add tasks to listbox
        if match != '':
            for task in match:
                self.listbox_tasks.insert(tk.END, task)
        else:
            for task in self.tasks:
                self.listbox_tasks.insert(tk.END, task)

    def onclick_list_to_entry(self, event):
        self.input_entry.delete(0, tk.END)
        # Add clicked list item to entry box
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            self.input_entry.insert(0, self.listbox_tasks.get(selected_index))

        # self.input_entry.insert(0, self.listbox_tasks.get(tk.ACTIVE))

    def check_match_entry_listbox(self, event):
        # grab what was typed
        typed = self.input_entry.get()
        if typed != '':
            match = []
            for task in self.tasks:
                if typed.lower() in task.lower():
                    match.append(task)
        else:
            match = self.tasks
        # Update listbox wiht selected items
        self.reset_listbox(match)

    def add_task(self):
        new_task = self.input_entry.get()
        if not new_task.strip() or new_task.strip() in self.tasks:
            messagebox.showwarning(
                "Invalid Task",
                "Task cannot be empty or already exists."
            )
            return
        self.tasks.append(new_task.strip())
        messagebox.showinfo(
            "Task Added",
            f"{new_task} has been added to your List."
        )
        self.reset_listbox('')
        self.save_tasks()

    def remove_task(self):
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            selected_task = self.listbox_tasks.get(selected_task_index)
            confirm = messagebox.askyesno(
                "Confirm Delete",
                f"Are you sure you want to delete '{selected_task}' ?"
            )
            if confirm:
                self.tasks.pop(selected_task_index)
                self.reset_listbox('')
                self.save_tasks()
        except IndexError:
            messagebox.showwarning(
                "No Selection",
                "Please select a task to remove."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
