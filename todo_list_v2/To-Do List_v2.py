def load_tasks():  # Load tasks from a file
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):  # Save tasks to a file
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


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


def search_tasks(tasks, search_keyword):
    matching_tasks = []
    for idx, task in enumerate(tasks, start=1):
        if search_keyword.lower() in task.lower():
            matching_tasks.append((idx, task))
    return matching_tasks


tasks = load_tasks()
print("Welcome to your To-Do List!")
while True:  # Main Loop

    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Search task")
    print("5. Exit")

    choice = input("Please enter your choice (1-5): ")
    if choice == "1":  # Add a task
        new_task = input("Enter the task you want to add: ")
        add_task(tasks, new_task)
        print(f"{new_task} has been added to your List.\n")
        save_tasks(tasks)

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
            try:
                remove_index = int(remove_choice)
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue
            if 1 <= remove_index <= len(tasks):
                task = remove_task(tasks, remove_index)
                print(f"{task} has been removed from your List.\n")
                save_tasks(tasks)
            else:
                print("Invalid task number.\n")

    elif choice == "4":  # Search a task
        print("Search Tasks.")
        search_keyword = input("Enter the keyword you want to search : ")
        matching_tasks = search_tasks(tasks, search_keyword)
        if not matching_tasks:
            print("No matching tasks found.")
        else:
            print("Matching tasks: ")
            for idx, task in matching_tasks:
                print(f"{idx} : {task}")
            print("\n")

    elif choice == "5":  # Exit and save tasks
        save_tasks(tasks)
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please try again.\n")
