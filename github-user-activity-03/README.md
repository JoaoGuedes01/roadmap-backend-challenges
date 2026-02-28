# GitHub User Activity Fetcher

This project is a simple Python script that fetches and displays recent public activity events for a specified GitHub user using the GitHub API.

## Features

- Retrieves recent events (pushes, pull requests, issues, comments, stars, forks, releases, etc.) for any GitHub username.
- Summarizes each event in a human-readable format.
- Handles API errors and missing data gracefully.

## Requirements

- Python 3.10 or newer (because of `match` statement)
- Internet connection
- A GitHub personal access token (for authenticated requests, because anonymous requests have very low api rating allowance)

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd github-user-activity-03
   ```
2. **Install dependencies:**
   This script uses only Python's standard library (no extra packages required).
3. **Set your GitHub token:**
   Export your GitHub personal access token as an environment variable named `GH_TOKEN`:
   - On Windows (PowerShell):
     ```powershell
     $env:GH_TOKEN = "your_token_here"
     ```
   - On Linux/macOS:
     ```sh
     export GH_TOKEN="your_token_here"
     ```

## Usage

Run the script from the command line, passing the GitHub username as an argument:

```sh
python main.py <github_username>
```

**Example:**

```sh
python main.py octocat
```

The script will print a list of recent actions performed by the user.

## Output Example

```
Fetching GitHub events for user: octocat
User pushed to octocat/Hello-World at 2026-02-27T12:34:56Z
User opened a pull request in octocat/Hello-World at 2026-02-26T11:22:33Z
...
```

## Notes

- The script only fetches public events.
- If no events are found or an error occurs, a message will be displayed.
- Make sure your GitHub token has appropriate permissions for public API access.
