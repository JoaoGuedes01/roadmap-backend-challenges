import sys
import urllib.request
import urllib.error
import json
import os

github_endpoint = "https://api.github.com"
gh_token = os.environ.get("GH_TOKEN")


def prepare_data(data):
    if len(data) == 0:
        return []

    actions = []
    for event in data:
        match event["type"]:
            case "PushEvent":
                actions.append(
                    f"User pushed to {event['repo']['name']} at {event['created_at']}"
                )
            case "PullRequestEvent":
                actions.append(
                    f"User {event['payload']['action']} a pull request in {event['repo']['name']} at {event['created_at']}"
                )
            case "IssuesEvent":
                actions.append(
                    f"User {event['payload']['action']} an issue in {event['repo']['name']} at {event['created_at']}"
                )
            case "IssueCommentEvent":
                actions.append(
                    f"User commented on an issue in {event['repo']['name']} at {event['created_at']}"
                )
            case "PullRequestReviewCommentEvent":
                actions.append(
                    f"User commented on a pull request in {event['repo']['name']} at {event['created_at']}"
                )
            case "CreateEvent":
                actions.append(
                    f"User created {event['payload']['ref_type']} in {event['repo']['name']} at {event['created_at']}"
                )
            case "DeleteEvent":
                actions.append(
                    f"User deleted {event['payload']['ref_type']} in {event['repo']['name']} at {event['created_at']}"
                )
            case "ForkEvent":
                actions.append(
                    f"User forked {event['repo']['name']} at {event['created_at']}"
                )
            case "WatchEvent":
                actions.append(
                    f"User starred {event['repo']['name']} at {event['created_at']}"
                )
            case "ReleaseEvent":
                actions.append(
                    f"User released {event['repo']['name']} at {event['created_at']}"
                )
            case _:
                actions.append(
                    f"User performed {event['type']} in {event['repo']['name']} at {event['created_at']}"
                )
    return actions


def get_request(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {gh_token}",
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            try:
                json_data = json.loads(data)
                return json_data
            except json.JSONDecodeError:
                print("Error decoding JSON response.")
                return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def fetch_gh_user_events(username):
    print(f"Fetching GitHub events for user: {username}")
    url = f"{github_endpoint}/users/{username}/events"
    return get_request(url)


def print_actions(actions):
    if not actions:
        print("No actions to display.")
    else:
        for action in actions:
            print(action)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        return "No arguments provided."

    username = args[0]
    user_data = fetch_gh_user_events(username)
    if user_data is None:
        return f"Error fetching data for user: {username}"

    actions = prepare_data(user_data)

    if actions == []:
        print(f"No events found for user: {username}")
    else:
        print_actions(actions)


if __name__ == "__main__":
    main()
