from enum import Enum
from rich.console import Console
from rich.table import Table
from rich import print as rprint

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Status(Enum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2

class Task():
    
    def __init__(self, id, title, created_at , priority=Priority.LOW, status=Status.TO_DO):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status
        self.created_at = created_at

    def __str__(self):
        return f""" Title: {self.title} 
                    Status: {self.status}
                    Priority: {self.priority}
                    Created: {self.created_at}"""""

tasks = []

class Taskmanager():

    def __init__(self, title, status=Status.TO_DO) :
        self.title = title
        self.status = status


    def add_task(task):
        tasks.append(Task(task))


    def update_status(index, status):
        try:
            tasks[index].status = status
            print(f"Status for task.title has been updated to {status}")
        except (IndexError, KeyError):
            print(f"Index is out of bounds")


    def list_tasks():
        return tasks
    

    def filter_by_priority():
        return tasks.sort

# dd_task, update_status, list_tasks, filter_by_priority

if __name__== "__main":
    task1 = Task(1, "Call with Pete", "2026-04-20")
    task2 = Taskmanager(task1)
    task2.add_task(task1)
    task2.list_tasks()