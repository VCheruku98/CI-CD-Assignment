import requests

def check_for_new_commits(repo_url):
    response = requests.get(f"{repo_url}/commits")
    if response.status_code == 200:
        commits = response.json()
        return commits[0]["sha"] 
    else:
        return None

if __name__ == "__main__":
    repo_url = "https://api.github.com/repos/Vcheruku/CI-CD-Assignment"
    latest_commit = check_for_new_commits(repo_url)
    if latest_commit:
        print(f"New commit detected: {latest_commit}")
    else:
        print("No new commits found.")