# main.py

from manager import TaskManager
from utils import parse_date

def print_help():
    print("""
Commands:
    add        - Add a new task
    view       - View all tasks
    update     - Update a task
    delete     - Delete a task
    help       - Show this help
    exit       - Exit program
""")

def main():
    manager = TaskManager()
    print("Welcome to CLI Task Manager!")
    print_help()

    while True:
        cmd = input("\nEnter command: ").strip().lower()
        if cmd == "add":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD, optional): ")
            due_date = due_date if parse_date(due_date) else None
            priority = input("Priority (Low/Medium/High): ") or "Low"
            manager.add_task(title, description, due_date, priority)

        elif cmd == "view":
            manager.view_tasks()

        elif cmd == "update":
            task_id = int(input("Task ID: "))
            status = input("Status (Pending/Completed, leave blank to skip): ") or None
            title = input("New Title (leave blank to skip): ") or None
            manager.update_task(task_id, status=status, title=title)

        elif cmd == "delete":
            task_id = int(input("Task ID to delete: "))
            manager.delete_task(task_id)

        elif cmd == "help":
            print_help()

        elif cmd == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' to see commands.")

if __name__ == "__main__":
    main()
