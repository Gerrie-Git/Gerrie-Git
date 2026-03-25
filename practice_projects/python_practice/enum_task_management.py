# 1. Task Management CLI with Status Enum

from enum import Enum

class TaskStatus(Enum):
    to_do = 0
    in_progress = 1
    completed = 2

class Task():

    def __init__(self, title, status=TaskStatus.to_do):
        self.title = title
        self.status = status

    def __str__(self):
        return f"{self.title} [{self.status.name}]"
    
tasks = []

def add_task(title):
    tasks.append(Task(title))
    print(f"Task {title} added")

def update_status(index, status):
    try:
        tasks[index].status = TaskStatus[status]
        print(f"Task {tasks[index].title} status updated to {status}")
    except (IndexError, ValueError):
        print("Invalid task index or status")


def list_tasks():
    for key, value in enumerate(tasks):
        print(f"Task: {key} Status: {value}")


if __name__ == "__main__":
    # Example usage
    add_task("Write report")
    add_task("Review PR")
    update_status(0, "in_progress")
    list_tasks()

