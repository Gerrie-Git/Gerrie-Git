# 1. Task Management CLI with Status Enum

# Import Enum base class to define fixed status values
from enum import Enum
# Import rich components for styled terminal output
from rich.console import Console
from rich.table import Table
from rich import print as rprint

# Create a console instance used to render rich output
console = Console()

# Define the possible statuses a task can have using an Enum
# Each status has a numeric value representing its order
class TaskStatus(Enum):
    to_do = 0
    in_progress = 1
    completed = 2

# Define the Task class to hold a task's title and current status
class Task():

    def __init__(self, title, status=TaskStatus.to_do):
        # Store the task title and default status to 'to_do'
        self.title = title
        self.status = status

    def __str__(self):
        # Return a readable string representation of the task
        return f"{self.title} [{self.status.name}]"

# Global list to store all tasks
tasks = []

# Map each TaskStatus to a rich color for styled terminal output
STATUS_STYLES = {
    TaskStatus.to_do: "yellow",
    TaskStatus.in_progress: "blue",
    TaskStatus.completed: "green",
}

def add_task(title):
    # Create a new Task with the given title and add it to the list
    tasks.append(Task(title))
    rprint(f"[green]✓[/green] Task '[bold]{title}[/bold]' added")

def update_status(index, status):
    try:
        # Look up the task by index and update its status using the Enum key
        tasks[index].status = TaskStatus[status]
        rprint(f"[blue]↻[/blue] Task '[bold]{tasks[index].title}[/bold]' updated to [bold]{status}[/bold]")
    except (IndexError, KeyError):
        # Handle invalid index or status name
        rprint("[red]✗ Invalid task index or status[/red]")

def list_tasks():
    # Create a rich table with a title and visible row lines
    table = Table(title="Task Manager", show_lines=True)
    table.add_column("ID", style="cyan", justify="center", width=4)
    table.add_column("Title", style="white")
    table.add_column("Status", justify="center")

    # Add a row for each task, coloring the status based on STATUS_STYLES
    for i, task in enumerate(tasks):
        style = STATUS_STYLES[task.status]
        table.add_row(str(i), task.title, f"[{style}]{task.status.name}[/{style}]")

    # Print the completed table to the terminal
    console.print(table)


if __name__ == "__main__":
    # Example usage
    add_task("Write report")
    add_task("Review PR")
    update_status(0, "in_progress")
    list_tasks()
