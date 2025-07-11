from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("OTOCP")

DEFAULT_TODO_PATH = os.path.join(
    os.path.expanduser("~"), 
    "Documents", 
    "Obsidian Vault", 
    "todo.md"
)
TODO_FILE = os.getenv("OTOCP_TODO_PATH", DEFAULT_TODO_PATH)

def ensure_file():
    os.makedirs(os.path.dirname(TODO_FILE), exist_ok=True)
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            f.write("# Todo List\n\n")


@mcp.tool()
def add_task(task: str) -> str:
    """
    Append a new task to the todo file.

    Args:
        task (str): The task to be added.

    Returns:
        str: Confirmation message indicating that task was added.
    """
    ensure_file()
    with open(TODO_FILE, "a") as f:
        f.write(f"- [ ] {task}\n")
    return "Task Saved!"


@mcp.tool()
def read_tasks() -> str:
    """
    Read and return all the tasks from the todo file.

    Returns:
        str: All tasks as a single string seperated by line breaks. If no tasks exist, a default message is returned.
    """

    ensure_file()
    with open(TODO_FILE, "r") as f:
        content = f.read().strip()
    return content or "No tasks yet."


@mcp.tool()
def complete_task(task_line: str) -> str:
    """
    Mark the task line as completed in the todo file.

    Args:
        task_line (str): The task to be completed. If user input is not exact task, try finding a similar one and complete it.

    Returns:
        str: Confirmation message.
    """
    ensure_file()
    with open(TODO_FILE, "r") as f:
        lines = f.readlines()

    updated = False
    for i, line in enumerate(lines):
        # Check if the task is incomplete and contains the given task_line
        if line.strip().startswith("- [ ]") and task_line.strip() in line:
            lines[i] = line.replace("- [ ]", "- [x]", 1)
            updated = True
            break

    if updated:
        with open(TODO_FILE, "w") as f:
            f.writelines(lines)
        return f"Marked '{task_line}' as completed!"
    else:
        return f"Task '{task_line}' not found or already completed."

@mcp.tool()
def clear_tasks() -> str:
    """
    Clear all tasks from the todo file.

    Returns:
        str: Confirmation message indicating all tasks were cleared.
    """

    ensure_file()
    with open(TODO_FILE, "w") as f:
        f.write("")
    return "All tasks cleared."


@mcp.resource("task://latest")
def get_latest_task() -> str:
    """
    Get the most recently added task from the todo file.

    Returns:
        str: The last task entry. If no tasks exist, a default message is returned.
    """

    ensure_file()
    with open(TODO_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No tasks yet."


if __name__ == "__main__":
    mcp.run()
