# High Level Breakdown
**Client (Claude Desktop App)** 
- Host the LLM UI and orchestrates conservations
- Exposes "tools" which are actions the LLM can invoke and "resources" which is the data LLM can fetch
**MCP Server**
- **Tool Registry**
	- Market Data
	- SEC Filing Retrieval
	- Earning Call Transcription
	- Financial Metrics and Statement
	- Web-scraping
	- Deep-research
- **Resource Registry** 
	- Databases of historical prices, filings, transcripts
	- Vector stores for semantic retrieval
- **LLM Orchestration**
	- Routes LLM request to tools and resources
	- Validates inputs/outputs using Zod schemas
**Execution**
- Trades are then places on Alpaca 
- Tools of Alpaca include: placing trades
- Resources of Alpaca include: Position management, tracking, inventory management 

![[Pasted image 20250418021110.png]]