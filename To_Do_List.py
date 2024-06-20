# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to delete a task
def delete_task():
    if not tasks:
        print("No tasks available to delete.")
        return
    try:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
