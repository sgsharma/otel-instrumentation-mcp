from fastmcp import FastMCP
from fastapi import FastAPI
from starlette.routing import Mount
from app.opentelemetry_repos import get_opentelemetry_repos
from app.github_issues import get_repo_issues, search_repo_issues   
from app.opentelemetry_examples import get_demo_services_doc, get_demo_services_by_language    
from app.opentelemetry_docs import get_docs_by_language

mcp = FastMCP("Opentelemetry Instrumentation")

# Create the ASGI app
mcp_app = mcp.http_app(path='/mcp')

# Create a FastAPI app and mount the MCP server
app = FastAPI(lifespan=mcp_app.lifespan)

@mcp.tool
@app.get("/repos")
async def list_opentelemetry_repos():
    """List OpenTelemetry repositories
    
    Returns a list of OpenTelemetry repositories
    """
    return {"repositories": get_opentelemetry_repos()}

@mcp.tool
@app.get("/issues")
async def list_opentelemetry_issues(repo: str = "opentelemetry-python"):
    """Get OpenTelemetry repository issues
    
    Returns issues from a specific OpenTelemetry repository
    
    Args:
        repo: Repository name (e.g. opentelemetry-python)
    """
    return {"issues": get_repo_issues(repo)}

@mcp.tool
@app.get("/issues/search")
async def search_opentelemetry_issues(repo: str = "opentelemetry-python", keywords: str = "metrics"):
    """Search OpenTelemetry repository issues
    
    Search for issues in a specific OpenTelemetry repository using keywords
    
    Args:
        repo: Repository name (e.g. opentelemetry-python)
        keywords: Keywords to search for in issues
    """
    return {"issues": search_repo_issues(repo, keywords)}

@mcp.tool
@app.get("/examples")
async def get_opentelemetry_examples():
    """Get OpenTelemetry examples
    
    Returns a list of OpenTelemetry demo services and examples
    """
    return {"examples": get_demo_services_doc()}

@mcp.tool
@app.get("/demo")
async def get_opentelemetry_examples_by_language(language: str = "python"):
    """Get OpenTelemetry examples by language
    
    Returns OpenTelemetry examples for a specific programming language
    
    Args:
        language: Programming language (e.g. python, java, go)
    """
    return {"examples": get_demo_services_by_language(language)}

@mcp.tool
@app.get("/otel-docs")
async def get_opentelemetry_docs_by_language(language: str = "python"):
    """Get OpenTelemetry documentation by language
    
    Returns OpenTelemetry documentation for a specific programming language
    
    Args:
        language: Programming language (e.g. python, java, go)
    """
    return {"docs": get_docs_by_language(language)}

app.mount("/mcp-server", mcp_app)
