from fastapi import FastAPI
from app.opentelemetry_repos import get_opentelemetry_repos
from app.github_issues import get_repo_issues, search_repo_issues   
from app.opentelemetry_examples import get_demo_services_doc, get_demo_services_by_language    

app = FastAPI()

@app.get("/repos")
async def list_opentelemetry_repos():
    return {"repositories": get_opentelemetry_repos()}

@app.get("/issues")
async def list_opentelemetry_issues(repo: str = "opentelemetry-python"):
    return {"issues": get_repo_issues(repo)}

@app.get("/issues/search")
async def search_opentelemetry_issues(repo: str = "opentelemetry-python", keywords: str = "metrics"):
    return {"issues": search_repo_issues(repo, keywords)}

@app.get("/examples")
async def get_opentelemetry_examples():
    return {"examples": get_demo_services_doc()}

@app.get("/demo")
async def get_opentelemetry_examples_by_language(language: str = "python"):
    return {"examples": get_demo_services_by_language(language)}
