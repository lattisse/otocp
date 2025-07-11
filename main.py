from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("OTOCP")

home_dir = os.path.expanduser("~")
TODO_FILE = os.path.join(home_dir, "Documents", "Obsidian Vault", "todo.md")

def ensure_file():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            f.write("")

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

if __name__ == "__main__":
    mcp.run()