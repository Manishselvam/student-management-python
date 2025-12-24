def show_menu():
    print("Todo App Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
tasks=[]
while(True):
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task description: ")
        tasks.append({"description": task, "completed": False})
        print("Task added successfully!\n")
    elif choice == "2":
        if not tasks:
            print("No tasks found.\n")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{i}. {t['description']} - {status}")
            print()
    elif choice == "3":
        task_num = int(input("Enter task number to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    elif choice == "4":
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    elif choice == "5":
        print("Exiting Todo App.")
        break
    else:
        print("Invalid choice. Please try again.\n")