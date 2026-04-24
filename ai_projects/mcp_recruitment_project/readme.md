# Job Search MCP Server

An MCP (Model Context Protocol) server that enables Claude Desktop to search for jobs on Indeed and LinkedIn Netherlands using the Serper API.

## Features

- Search for jobs by title and location
- Filter by salary and currency
- Add custom keywords to narrow results
- Supports Indeed and LinkedIn Netherlands

## Prerequisites

- Python 3.11+
- A [Serper API key](https://serper.dev)
- Claude Desktop

## Installation

1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd mcp_recruitment_project
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install mcp httpx beautifulsoup4 python-dotenv
```

4. Create a `.env` file in the project root:

SERPER_API_KEY=your_serper_api_key_here


## Claude Desktop Configuration

Add the following to your `claude_desktop_config.json`:

- **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "job-search": {
      "command": "/path/to/your/venv/bin/python",
      "args": ["/path/to/your/app.py"],
      "env": {
        "SERPER_API_KEY": "your_serper_api_key_here"
      }
    }
  }
}
```

Restart Claude Desktop after saving.

## Usage

Open Claude Desktop and ask naturally, for example:

- *"Find data engineering jobs in Amsterdam paying over 100k EUR"*
- *"Search for senior Python developer roles in the Netherlands"*
- *"Look for remote machine learning jobs in Amsterdam on LinkedIn"*

## Tool Reference

### `search_jobs`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `job_title` | string | required | Job title to search for |
| `location` | string | `"Netherlands"` | Location to search in |
| `site` | string | `"indeed"` | `"indeed"` or `"linkedin"` |
| `keywords` | string | `""` | Extra filters e.g. `"remote, senior"` |
| `min_salary` | int | `None` | Minimum annual salary |
| `currency` | string | `"EUR"` | Currency for salary |

## Limitations

- LinkedIn aggressively blocks scrapers, so Indeed tends to return better results
- Salary filtering is best-effort, as not all job listings advertise salary figures
- Results are limited to the snippets and page text returned by Serper