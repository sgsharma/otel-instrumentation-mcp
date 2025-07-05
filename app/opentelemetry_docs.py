import requests
import re
from markdown import markdown
from bs4 import BeautifulSoup

def get_docs_by_language(language: str):
    RAW_BASE_URL = "https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/languages"
    language = language.strip().lower()
    raw_url = f"{RAW_BASE_URL}/{language}/getting-started.md"
    print(f"Fetching raw content from: {raw_url}")
    
    response = requests.get(raw_url)
    
    if response.status_code == 404:
        return {
            "language": language,
            "message": f"No docs found for language: {language}"
        }

    # Step 1: Convert Markdown to HTML
    html = markdown(response.text)

    # Step 2: Strip HTML tags to get plain text
    soup = BeautifulSoup(html, "html.parser")
    plain_text = soup.get_text()

    # Step 3: Remove punctuation and normalize whitespace
    cleaned_text = re.sub(r'[^\w\s]', '', plain_text)  # Remove all punctuation
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Collapse whitespace

    return {
        "language": language,
        "content": [
            {
                "url": raw_url,
                "cleaned_text": cleaned_text
            }
        ]
    }
