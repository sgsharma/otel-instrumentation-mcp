import os
import requests

GITHUB_API_URL = os.getenv("GITHUB_GRAPHQL_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_repo_issues(repo: str, owner: str = "open-telemetry", count: int = 10):
    if owner != "open-telemetry":
      return {"nodes": []}  # Return empty result if not in open-telemetry org

    headers = {
        "Authorization": f"bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    query = f"""
    query {{
      repository(owner: "{owner}", name: "{repo}") {{
          issues(first: {count}, orderBy: {{field: CREATED_AT, direction: DESC}}) {{
            nodes {{
              title
              url
              state
              createdAt
              labels(first: 5) {{
                nodes {{
                  name
                }}
              }}
            }}
          }}
        }}
      }}
    """
    response = requests.post(GITHUB_API_URL, headers=headers, json={"query": query})
    response.raise_for_status()
    data = response.json()
    return data["data"]["repository"]["issues"]["nodes"]

def search_repo_issues(repo: str, keywords: str, owner: str = "open-telemetry", count: int = 10):
    if owner != "open-telemetry":
        return {"nodes": []}  # Return empty result if not in open-telemetry org
        
    headers = {
        "Authorization": f"bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    search_query = f'repo:{owner}/{repo} is:issue {keywords}'
    query = f"""
    query {{
      search(query: "{search_query}", type: ISSUE, first: {count}) {{
        nodes {{
          ... on Issue {{
            title
            url
            state
            createdAt
            labels(first: 5) {{
              nodes {{
                name
              }}
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(GITHUB_API_URL, headers=headers, json={"query": query})
    response.raise_for_status()
    data = response.json()
    return data["data"]["search"]["nodes"]
