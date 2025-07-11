
# Otocp

A MCP server written in python to add, list, complete and delete tasks in Obsidian.

### Tools available:

- add_task - Add tasks based on user input.
- read_tasks - Lists all the task.
- complete_task - Completes a specified task (doesn't have to be exact.)
- clear_tasks - Deletes everything

### Installation

Install using pip:

``` pip install otocp```

or use uv

Install uv first.

MacOS/Linux:

```curl -LsSf https://astral.sh/uv/install.sh | sh```

Windows:

```powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```

Now run:

```uvx otocp```

### MCP Config

```json 
{
  "mcpServers": {
    "otocp": {
      "command": "otocp",
      "args": [],
      "env": {
        "OTOCP_TODO_PATH": "path to your todo.md"
      }
    }
  }
}

```
OTOCP_TODO_PATH example:

```
"OTOCP_TODO_PATH": "/home/crystal/Desktop/example/todo.md"
```

If you get any errors (most likely because of path of otocp):

On Linux/MacOS run ``` which otocp``` on terminal and put the full path in command instead of just otocp like: 
``` 
      "command": "/home/crystal/.local/bin/otocp",

```

On Windows you can use ```where otocp``` and do the same thing.

### For Development:

Clone the repo: ``` https://github.com/lattisse/otocp.git ```

``` 
cd otocp
uv venv

```

To run mcp through use this MCP Config:

``` json
{
  "mcpServers": {
    "otocp": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/ABSOLUTE/PATH/TO//otocp/src/otocp/todo.py"
      ]
    }
  }
}
```