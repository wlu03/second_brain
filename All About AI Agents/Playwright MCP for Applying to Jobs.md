**Playwright MCP**: https://github.com/microsoft/playwright-mcp

1. Download Docker
```
docker run --rm -p 31337:31337 \
  mcr.microsoft.com/playwright:v1.44.0-jammy \
  bash -lc "npx -y @playwright/mcp@latest --headless --port 31337"

use this command to open a headlesss playwright using port 31337
```

2. Call Playwright
```
import playwright_mcp_client as mcp

mcp_client = mcp.Client(url="http://localhost:31337/sse")
```