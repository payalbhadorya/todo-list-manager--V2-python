import json
#load tasks from file if it exists
try:
    with open("tasks.json","r") as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []

#using loop
while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

# 1.(ADD TASK)
    if choice == "1":
        title = input("Enter task title: ")
        priority = input("Enter priority (High / Medium / Low): ")
        due_date = input("Enter due date (DD-MM-YYYY): ")

        task = {
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "status": "Pending"
        }

        tasks.append(task)
        print("Task added successfully!")

# 2.(VIEW TASK)
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"\nTask {i+1}")
                print("Title:", tasks[i]["title"])
                print("Priority:", tasks[i]["priority"])
                print("Due Date:", tasks[i]["due_date"])
                print("Status:", tasks[i]["status"])

# 3.(MARK TASK)
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to Complete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['title']} - {tasks[i]['status']}")
            
            task_no = int(input("Enter task number to mark as Complted:"))

            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["status"] = "Completed"
                print("Task marked as completed!")
            else:
                print("Invalid task number.")    

# 4.(DELETE TASK)
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['title']}")

            task_no = int(input("Enter task number to delete:"))   

            if 1 <= task_no <= len(tasks):
                deleted_task = tasks.pop(task_no -1)
                print(f"Task '{deleted_task['title']}' deleted.")
            else:
                print("Invalid task number.")    

#choice 5.(EXIT TASK)
    elif choice == "5":
        with open("tasks.json","w") as file:
            json.dump(tasks,file)
        print("Tasks saved, Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

