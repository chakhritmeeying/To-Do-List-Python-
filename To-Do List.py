task = []
print("Welcome to your To-Do List!")
while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = int(input("Please enter your choice (1-4): "))
    # Main Loop
    if choice == 1:  # Add a task
        new_task = input("Enter the task you want to add: ")
        task.append(new_task)
        print(f"{new_task} has been added to your List.\n")
    elif choice == 2:  # View tasks
        if not task:
            print("You do not have List.\n")
        else:
            print("-------------------------------------")
            print("Your To-Do List:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
            print("-------------------------------------\n")
    elif choice == 3:  # Remove a task
        if not task:
            print("You do not have List to remove.\n")
        else:
            print("-------------------------------------")
            print("Your To-Do List:")
            for idx, t in enumerate(task, start=1):
                print(f"{idx}. {t}")
            remove_task = int(
                input("Enter the number of the task you want to remove: "))
            if 1 <= remove_task <= len(task):
                task.remove(task[remove_task - 1])
                print("List has been removed.\n")
            else:
                print("Invalid task number.\n")
    elif choice == 4:  # Exit
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please try again.\n")
