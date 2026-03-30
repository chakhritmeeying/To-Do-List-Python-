import json


class TodoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        self.tasks = []
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = json.load(file)

        except FileNotFoundError:
            self.tasks = []

    def add_task(self, new_task):
        self.tasks.append({
            "text": new_task,
            "done": False
        })

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else "❌"
            print(f"{idx} : {task['text']} : status {status} ")

    def update_task(self, index_task):
        self.tasks[index_task -
                   1]["done"] = not self.tasks[index_task - 1]["done"]
        return self.tasks[index_task - 1]

    def delete_task(self, index_task):
        return self.tasks.pop(index_task - 1)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            json.dump(self.tasks, file)


def main():
    todo_list = TodoList()
    todo_list.load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Taks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choice you command (1 - 5): ")

        if choice == '1':
            new_task = input("Enter task : ")
            todo_list.add_task(new_task)
            print(f"{new_task} has been add to list.")
            todo_list.save_tasks()

        elif choice == '2':
            if not todo_list.tasks:
                print("List is empty.")
                continue
            else:
                total_list = len(todo_list.tasks)
                print("\nYour To-Do List")
                todo_list.view_tasks()
                print(f"Total list : {total_list} list.")

        elif choice == '3':
            cancel = len(todo_list.tasks)+1
            print("\nYour To-Do List")
            todo_list.view_tasks()
            print(f"{cancel} : back to main mane")

            try:
                index = int(input("\nEnter index to update status : "))
            except ValueError:
                print("Please enter a number.")
                continue

            if 1 <= index <= len(todo_list.tasks):
                update_task = todo_list.update_task(index)
                print(f"{update_task['text']} has been updated.\n")
                todo_list.save_tasks()
            elif index == cancel:
                print("back to main mane")
                continue
            else:
                print("Invalid index.")
                continue

        elif choice == '4':
            cancel = len(todo_list.tasks)+1
            print("\nYour To-Do List")
            todo_list.view_tasks()
            print(f"{cancel} : back to main mane")

            try:
                index = int(input("\nEnter index to delete : "))
            except ValueError:
                print("Please enter a number.")
                continue

            if 1 <= index <= len(todo_list.tasks):
                delete_task = todo_list.delete_task(index)
                print(
                    f"{delete_task['text']} has been removed from your List.\n")
                todo_list.save_tasks()
            elif index == cancel:
                print("back to main mane")
                continue
            else:
                print("Invalid index.")
                continue

        elif choice == '5':
            todo_list.save_tasks()
            if not todo_list.tasks:
                print("List is empty")
                break
            print("\nYour all To-Do List.")
            todo_list.view_tasks()
            break
        else:
            print("Please choice 1 - 5 !")
            continue


if __name__ == "__main__":
    main()
