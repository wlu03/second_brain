Searchable MCP Registry
- Discover Existing Servers: mcp-get.com and smithery.com
- Create a `registries` table to store tags `id`, `name`, `description`, `openapi_url`, `auth_type`, `tags[]`, `tool_count`, `model_count`, `last_healthcheck`, `owner_id`
- Semantic Search: embed each server's tool description with a embedding model
	- Expose `/registry/search?q=` that does hybrid (SQL + vector) ranking so the “Add New MCP” search bar feels instant.

```
/apps
  web     (Next.js – your current UI)
/services
  gateway (tRPC / FastAPI – auth, sessions, rate limit)
  mcp-core
    ├─ registry.controller.ts
    ├─ planner.service.ts      # picks tools
    ├─ executor.service.ts     # calls tools
    └─ memory.service.ts       # chat + RAG
/postgres  (pgvector enabled)
/redis     (short‑term cache, rate limits)
/object‑store (S3-compatible – file outputs)

```

**Chatbot & Planning Agent**
- conversation memory
- planner (chain of thought) using langgraph 
	- **LangGraph** or `ChatOpenAI` + ReAct. Prompt = “Here are the MCP tools the user authorised… design a minimal sequence.”
- Tool execution: Simple async queue (BullMQ / Celery). Stream partial JSON back to the UI via WebSocket or SSE so your arrow diagram can animate.
- LLM provider: Start with GPT‑4o function‑calling; support Claude Opus soon since Anthropic authored MCP.
- **Short‑term**: store entire dialogue + tool invocations in Postgres (`conversations`, `messages`, `tool_runs`).
- **Long‑term knowledge**: keep only the final “result objects” (summaries, files). Raw chat can be pruned or vector‑compressed to save $.
```
POST /chat                                 # {conversation_id?, user_msg}
GET  /chat/{id}/stream                     # SSE for incremental tokens
GET  /registry                             # list + filters
POST /registry                             # add custom MCP
POST /registry/{id}/healthcheck
POST /chain/execute                        # run a saved multi‑step plan
```


## UI wiring

- **Search bar** in “Add New MCP” → `debounce(300ms)` → `GET /registry?q=…` → show suggestions.
- **Test connection** button calls `/registry/{id}/healthcheck`.
- **Execute Chain** calls `/chain/execute`, then listens to `/chat/{runId}/stream` to update the nice three‑step timeline while the back‑end fires actual API calls.
- Save chains as _templates_ (`user_templates` table) so the “Saved templates” sidebar works.