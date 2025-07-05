# OpenTelemetry Instrumentation MCP

This is a minimal server that uses GitHub's GraphQL API and REST API to help you instrument your applications with OpenTelemetry.

## Usage

1. Add your GitHub token to the `.env` file.
2. Run the server using `./run.sh`.
3. Open your browser or make a request to the endpoints defined in main.py.

## Connect and test using MCPInspector:

```
npx @modelcontextprotocol/inspector \
  uv \
  --directory . \
  run \
  python \
  app/main.py
```

Note:

- Set Transport Type to Streamable HTTP
- Set URL to http://127.0.0.1:8000/mcp-server/mcp/
