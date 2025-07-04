import os
import requests

GITHUB_API_URL = os.getenv("GITHUB_REST_URL")
OPENTELEMETRY_DOCS_REPO = os.getenv("OPENTELEMETRY_DOCS_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_demo_services_doc():
    headers = {
        "Authorization": f"bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    path = "content/en/docs/demo/services/_index.md"
    content_url = f"{GITHUB_API_URL}/repos/{OPENTELEMETRY_DOCS_REPO}/contents/{path}"

    response = requests.get(content_url, headers=headers)
    if response.status_code == 404:
        return {"error": f"Could not find file at path: {path}"}
    response.raise_for_status()

    file_meta = response.json()
    if file_meta.get("type") == "file" and file_meta.get("download_url"):
        raw_response = requests.get(file_meta["download_url"])
        raw_response.raise_for_status()

        return {
            "url": file_meta["html_url"],
            "content": raw_response.text
        }
    else:
        return {"error": f"Invalid file or missing download URL for path: {path}"}


def get_demo_services_by_language(language: str):
    services_by_language = {
        ".NET": ["accounting", "cart"],
        "Java": ["ad"],
        "Go": ["checkout", "product-catalog"],
        "C++": ["currency"],
        "Ruby": ["email"],
        "Kotlin": ["fraud-detection"],
        "TypeScript": ["frontend", "react-native-app"],
        "Python/Locust": ["load-generator"],
        "JavaScript": ["payment"],
        "Python": ["recommendation"],
        "PHP": ["quote"],
        "Rust": ["shipping"]
    }
    BASE_URL = "https://github.com/open-telemetry/opentelemetry-demo/tree/main/src"
    language = language.strip().lower()
    matched = [(lang, services) for lang, services in services_by_language.items() if lang.lower() == language]

    if not matched:
        return {
            "language": language,
            "services": [],
            "message": f"No services found for language: {language}"
        }

    lang, services = matched[0]
    return {
        "language": lang,
        "services": [
            {
                "name": service,
                "url": f"{BASE_URL}/{service}"
            }
            for service in services
        ]
    }
