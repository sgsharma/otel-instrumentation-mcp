import os
import requests

GITHUB_API_URL = os.getenv("GITHUB_GRAPHQL_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_opentelemetry_repos():
    headers = {
        "Authorization": f"bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    query = """
    query {
      organization(login: "open-telemetry") {
        repositories(first: 100, orderBy: {field: NAME, direction: ASC}) {
          nodes {
            name
            description
            url
            isArchived
            stargazerCount
            updatedAt
          }
          pageInfo {
            hasNextPage
            endCursor
          }
        }
      }
    }
    """

    response = requests.post(GITHUB_API_URL, headers=headers, json={"query": query})
    response.raise_for_status()
    data = response.json()
    repos = data["data"]["organization"]["repositories"]["nodes"]

    # Filter client-side for names starting with "opentelemetry-"
    filtered_repos = [
        {
            "name": repo["name"],
            "description": repo["description"],
            "url": repo["url"],
            "stars": repo["stargazerCount"],
            "archived": repo["isArchived"],
            "updatedAt": repo["updatedAt"]
        }
        for repo in repos if repo["name"].startswith("opentelemetry-")
    ]

    return filtered_repos
