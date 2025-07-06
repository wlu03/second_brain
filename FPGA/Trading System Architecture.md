This document outlines the components and process flow for our trading system. The system continuously monitors market data and news events to execute both market making and directional trades based on evolving market conditions.

## Overview

Our system is composed of several key modules:

1. **Data Ingestion & Monitoring:**  
   - **News Scraper & Parser:** Uses Selenium-based scrapers (e.g., `nytimes_listenser.py`) to monitor news sites and social media for relevant market events.  
   - **LLM Parser:** Uses an LLM (as implemented in `llm_parser.py`) to analyze news articles and extract sentiment or trading signals.

2. **Market Analysis & Trading Logic:**  
   - **Arbitrage & Directional Trading:** Implemented in `trading_logic.py` and integrated within the main trading loop (see `main.py`), this module analyzes current market conditions, orderbook data, and news signals to determine directional bets.
   - **Risk Management:** Enforces exposure limits and order sizing based on the current balance and market conditions.

3. **Market Making Module:**  
   - **Quote Generation:** A new module (`market_maker.py`) implements market making strategies by dynamically generating bid and ask orders.  
     - **Skew Calculation:** Adjusts the bid and ask quotes based on current inventory imbalances.
     - **Spread Adjustment:** Modifies the base spread according to market volatility.
     - **Price & Size Determination:** Generates multiple levels of orders using both linear and geometric spacing functions.
   - **Integration:** The market making module runs concurrently with the directional trading logic. When no significant news event is detected, it continuously places liquidity-providing limit orders. Upon a valid news signal, the system cancels the market making orders and transitions to directional trading.

4. **Exchange Interface:**  
   - **Order Placement & Cancellation:** Communicates with Kalshi’s API via an exchange client (as instantiated in `main.py`). This component is responsible for placing limit orders (market making) and market orders (directional trades).

## Process Flow

1. **Data Ingestion:**  
   - News sources are polled continuously.
   - Market data (order book, volatility, and balance) is fetched from the exchange.

2. **News Analysis:**  
   - The LLM parser analyzes incoming news articles to determine if there is a significant market event.
   - If a relevant news event is detected (with a clear directional signal), the system transitions to the post-news mode.

3. **Market Making Mode:**  
   - The market making module generates bid and ask quotes based on:
     - Current inventory and skew adjustments.
     - Volatility-adjusted spread.
     - Order size calculations.
   - Orders are placed as limit orders on both sides of the market.
   - The system runs market making concurrently with news monitoring.

4. **Directional Trading Mode:**  
   - Upon detecting valid news, the system cancels all market making orders.
   - Based on the news analysis (YES/NO signal), the system executes directional trades (typically market orders) to take advantage of the perceived opportunity.

## Files & Modules

- **`scraper.py`:** Monitors news sites and social media channels.
- **`llm_parser.py`:** Interfaces with an LLM to analyze news content and extract trading signals.
- **`trading_logic.py`:** Contains the core arbitrage strategy and directional trade decision logic.
- **`market_maker.py`:** Implements the market making strategy, including skew, spread adjustment, and quote generation.
- **`main.py`:** The central entry point that orchestrates market making, news monitoring, risk management, and trade execution.

## Integration Points

- **Shared State:**  
  The `SharedState` class (or equivalent) aggregates live market data (tick size, volatility, best bid/ask, inventory, etc.) which is used by both the market making module and the directional trading logic.

- **Asynchronous Execution:**  
  The main trading loop (in `main.py`) uses asynchronous tasks to run the market making engine in parallel with news monitoring. This ensures that the system continuously provides liquidity while remaining responsive to news events.

- **Risk & Order Management:**  
  The system computes dynamic order sizes and ensures that total exposure stays within predefined limits before placing any orders. On news-triggered events, it cancels outstanding market making orders to minimize unintended risk.

---

This updated architecture ensures that your trading system remains robust by combining continuous liquidity provision through market making with opportunistic directional trading based on real-time news analysis.
