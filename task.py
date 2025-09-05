
# task.py

import datetime

class Task:
    def __init__(self, id, title, description="", due_date=None, priority="Low", status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date  # string format YYYY-MM-DD
        self.priority = priority  # Low, Medium, High
        self.status = status      # Pending or Completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            priority=data.get("priority", "Low"),
            status=data.get("status", "Pending")
        )
