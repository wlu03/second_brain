# What is MCP
The standard way for LLM-based client and servers to exchange: **resources** and **tools**. *Resources* are read only data retrieval endpoints (i.e. no side effects). *Tools* are actions with side effects such as writing to a database or making an external API call. MCP runs over a transport layer (e.g STDIN/STDOUT, HTTP) and exposes resources and tools over HTTP verbs: `get`, `post`, `patch`, and `delete`. 

## Resource
*Use Case*: Read only operations (from a database)
*Signature*
``` typescript
server.resource<YourResponseShape>(
  name: string,
  uri: string,
  handler: (uri: URL) => Promise<{ contents: { uri: string, text: string }[] }>
)
```
## Tool
*Use Case*: Any operation with side effects (INSERT, POST)
*Signature*:
``` typescript
server.tool<InputSchema, OutputShape>(
  name: string,
  inputSchema: ZodSchema, // validated at runtime
  handler: (data: InputType) => Promise<OutputShape>
)
```

## Schema Validation with ZOD
``` typescript
import { z } from "zod";

const MatchInput = z.object({
  horse1: z.string().describe("First Horse ID"),
  horse2: z.string().describe("Second Horse ID"),
  meetingDate: z.string().describe("ISO 8601 date of meeting"),
});
```

## Example: MCP Server

Fireship Video Example
``` typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/transport/stdio.js";
import sql from "your-sql-client"; // e.g. postgres client

// 1. Create MCP server
const server = new McpServer({
  name:    "Horse Tinder AI",
  version: "4.2.0",
});

// 2. Resource: fetch all 'single' horses
server.resource(
  "list-single-horses",
  "postgres://database/horses",
  async (uri) => {
    const horses = await sql`
      SELECT * FROM horses
      WHERE status = 'single';
    `;
    return {
      contents: [{
        uri:  uri.href,
        text: JSON.stringify(horses, null, 2),
      }],
    };
  }
);

// 3. Tool: match two horses on a given date
server.tool(
  "horse-matching-service",
  z.object({
    horse1:      z.string().describe("First Horse ID"),
    horse2:      z.string().describe("Second Horse ID"),
    meetingDate: z.string().describe("Meeting time (ISO)"),
  }),
  async (data) => {
    const response = await fetch(
      "https://api.horsetinder.com/v1/match",
      {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify(data),
      }
    );
    return await response.json();
  }
);

// 4. Start listening on STDIO
const transport = new StdioServerTransport();
await server.connect(transport);
```
____
## Current MCP Clients
**Claude Desktop App**: Resources + Prompts + Tools
**Claude Code**: Prompts + Tools
**5ire**: Tools only
**BeeAI Framework**: Tools only
	Note: Claude Desktop App just doesn't support Sampling and Roots. 
	

## Developing Own Client
1. Choose transport method (e.g. WebSocket, STDIO, HTTP)
2. Implement client stub that
	- Discovers resources and tools
	- Feed LLM prompt with "tool spec" metadata

## Adding MCP Server to Claude Desktop
Edit your Claude Config (config.json)
![[Screenshot 2025-04-17 at 5.24.21 PM.png | 300]]
Edit Config File to add MCP
```
{
	"mcpServers": {
		"horse": {
			"command": "deno",
			"args" : [
				"run",
				"-A",
				"D:/apps/mcp-app/main.ts"
			]
		}
	}
}
```
*Essentially this is just a command to start your MCP server*

## What is Sampling and Roots
Sampling is a client-provided feature that lets an MCP server request intermediate LLM completions via the client enabling the server to act more "agentic" (to plan, reason, or break its logic into multiple LLM calls) rather than just return static data or side effects.

This way server can decompose complex tasks into steps each driven by a fresh LLM completion. Clients can surface sampling requests for user approval, improving safety.

### How Sampling Works
1. During the JSON-RPC handshake, the client advertises a "sampling" method under capabilities
``` typescript
const outline = await client.sample({
	prompt: "Plan the steps to compare two horses' genetics",
	model: "claude-3.7",
	max_tokens: 150
});
```
- The client may stream tokens back to the server or deliver them all at once
- Clients can enforce rate limits, ask for user confirmation or reject sampling calls.

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "Planner Server", version: "1.0.0" });

server.tool(
  "strategic-planner",
  /* input schema… */,
  async (input, client) => {
    // 1. Ask the client’s LLM to outline a plan
    const plan = await client.sample({
      prompt:     `Create a 3‑step plan to match horse ${input.horse1} with ${input.horse2}`,
      model:      "claude-v1",
      max_tokens: 200
    });

    // 2. Use that plan to drive your business logic…
    return { plan };
  }
);
// …then connect transport as usual
```

### Roots in MCP
Roots are named entry-points (URIs) that the client provides to its server at connection time which define scopes where the server may read or write resources. Servers can list or traverse files under those roots. Servers tailor their resources/tools to the client’s project or environment.

#### How Roots Work
1. **Handshake Advertisement**
    - Client sends a `roots/list` capability with an array of `{ name, uri }`.
2. **Server Usage**
    - When defining a resource, the server can reference a root URI to fetch or watch files.
3. **Dynamic Updates**
    - Some clients allow roots to be updated on‑the‑fly (e.g. the user opens a new folder in their IDE).
``` typescript
// Client → Server (during initialization)
{
  "method": "roots/list",
  "params": {
    "roots": [
      { "name": "project", "uri": "file:///Users/alice/my-app" },
      { "name": "config",  "uri": "file:///Users/alice/.config" }
    ]
  }
}

// Server side: define a resource under the 'project' root
server.resource(
  "list-project-files",
  "file://${roots.project}",           // URI template refers to the root
  async (uri) => {
    const dir = uri.pathname;          // e.g. /Users/alice/my-app
    const files = await fs.readdir(dir);
    return {
      contents: files.map(name => ({
        uri:  `file://${path.join(dir, name)}`,
        text: await fs.readFile(path.join(dir, name), "utf8")
      }))
    };
  }
);
```

**Client‑Declared, User‑Controlled**
- When you configure your MCP client (e.g. Claude Desktop), you choose exactly which directories (or other URIs) to expose as roots.
``` json
{
  "roots": [
    { "name": "project", "uri": "file:///Users/alice/my-app" },
    { "name": "notes",   "uri": "file:///Users/alice/Private/Notes" }
  ]
}
```
- The server never “auto‑discovers” your home folder—only the paths you list.
**Server Can Only Use What You Give It**
- Roots are just metadata. Your server’s resource handlers have to explicitly read from those URIs.
- If you list `file:///Users/alice/my-app`, a handler might do:
    `const files = await fs.readdir("/Users/alice/my-app")`
- But if you don’t list `file:///Users/alice/Secrets`, the server has no URI pointing there and won’t touch it.

TLDR: 
- **Sampling** lets MCP servers nest LLM calls via the client, unlocking richer, multi‑step logic while keeping model usage centralized.
- **Roots** define the filesystem or API “home bases” servers may safely access, improving security and context relevance.