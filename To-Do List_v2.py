

def add_task(tasks, new_task):  # Add a task to the list
    tasks.append(new_task)


def view_tasks(tasks):  # Show all tasks in the list
    print("-------------------------------------")
    print("Your To-Do List:")
    for idx, t in enumerate(tasks, start=1):
        print(f"{idx}. {t}")
    print("-------------------------------------\n")


def remove_task(tasks, task_index):  # Remove a task from the list
    return tasks.pop(task_index - 1)


tasks = []
print("Welcome to your To-Do List!")
while True:  # Main Loop

    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Please enter your choice (1-4): ")
    if choice == "1":  # Add a task
        new_task = input("Enter the task you want to add: ")
        add_task(tasks, new_task)
        print(f"{new_task} has been added to your List.\n")

    elif choice == "2":  # View tasks
        if not tasks:
            print("You do not have List.\n")
        else:
            view_tasks(tasks)

    elif choice == "3":  # Remove a task
        if not tasks:
            print("You do not have List to remove.\n")
        else:
            view_tasks(tasks)
            remove_choice = input(
                "Enter the number of the task you want to remove: ")
            remove_index = int(remove_choice)
            if 1 <= remove_index <= len(tasks):
                remove_task = remove_task(tasks, remove_index)
                print(f"{remove_task} has been removed from your List.\n")
            else:
                print("Invalid task number.\n")

    elif choice == "4":  # Exit
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please try again.\n")
