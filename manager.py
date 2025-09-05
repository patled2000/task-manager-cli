# manager.py

import json
from task import Task

DATA_FILE = "data.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, description="", due_date=None, priority="Low"):
        task_id = max([task.id for task in self.tasks], default=0) + 1
        task = Task(task_id, title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nID | Title | Due Date | Priority | Status")
        print("-" * 50)
        for task in self.tasks:
            print(f"{task.id} | {task.title} | {task.due_date or '-'} | {task.priority} | {task.status}")

    def update_task(self, task_id, **kwargs):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            print(f"No task with ID {task_id}")
            return
        for key, value in kwargs.items():
            if hasattr(task, key) and value is not None:
                setattr(task, key, value)
        self.save_tasks()
        print(f"Task ID {task_id} updated!")

    def delete_task(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            print(f"No task with ID {task_id}")
            return
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task ID {task_id} deleted!")
