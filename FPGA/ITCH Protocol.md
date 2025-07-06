**System Event Message** is used to signal a market or data feed handler event. These message don't relate to specific orders, but inform of system wide events: start or ending of trading; market open or close; and halts.

At the start of each trading day, NASDAQ sends out **Stock Directory Messages** for every active symbol. This provides metadata regarding each stock.
- Round Lot Size: Tells you how many shares make a round lot for this stock
- Round Lots Only: If yes, it only accepts round lots for this security. If no, NASDAQ accepts any order size including odd lots (1,3,5,... shares).

**Stock Trading Action Message** indicates the current trading status of a stock to the market. It's sent **before** the markets open as a part of a "spin" to declare which securities are ready to trade. It's also sent during market hours to **update** status when a stock is **halted, paused,** or **resumed.**

**Reg SHO Short Sale Price Test Restricted** is a message indicating whether a stock is subject to short sale restriction. If a stock drops 10% or more from the previous day's close, short selling is restricted for the rest of the day and the next trading day. 
- `'0'`: No short sale price test in place.
- `'1'`: Test restriction **triggered today** due to 10% price drop.  
- `'2'`: Restriction is **continuing** from a previous day.


**Market Participant Position** message tells you the status of the market participant (MPID) for a specific stock at a given moment. At the start of each trading day for all market participants or intraday, if there's a status change (e.g. someone is no longer a MM for a stock). Provides real time transparency on who is quoting and making markets in a stock. 

**Market-Wide Circuit Breaker Message** tells market participants the percentage threshold that, if breached, will trigger a market halt. They give time to slow down panic selling and give the market time to stabilize.  

**Market-Wide Circuit Breaker** Status message is sent when a market-wide circuit breaker is actually triggered and tells you the level at which it is breached.

**IPO Quoting Period** is a message that communicates the anticipated quotation release time for an IPO security. 

**LULD Action Collar Message** is used during Limit Up - Limit Down Trading Pauses. After a trading halt due to excessive volatility, this message: 
- Specifies the price range which the auction can take place
- Provides a reference prices for lower and upper bound
- Communicates how many extensions have occurred for the reopening auction 

**Operational Halt** notifies market participants that a specific Nasdaq market center has a interruption for a stock, without halting trading on other exchanges. This is different from a **regulatory halt** because it's technical. 

The **Add Order Message** tells the market that a new order has been added to the Nasdaq order book. There are two version - **includes an MPID** and **doesn't include an MPID**. This message is sent by NASDAQ. A market participant sends a new order to NASDAQ where it receives the order. If NASDAQ accepts the order and adds it to the order book, it would then send out this message.

The **Order Executed Message** indicates that a previously added order has been executed either fully or partially. You receive multiple 'E' messages for a single order if it's filled in pieces. After receiving a "A" or "F" message, it will send an "E" message with the quantity of shares executed. 

The "E" message is used when the execution price differs from the price in the original add order message. Since the execution price is different than the display price of the original Add order, Nasdaq includes the price filed. Non-printable field means that the shares will be included into a later bulk print. 

**Order Cancel** "X" message is sent by Nasdaq when a participant **cancels part of an order** that is already in the book. **Order Delete** "D" message is an order that is completely removed from the book. **Order Replace** "U" message is sent by Nasdaq when an order on the book has been canceled and replaced. That means the old order is replace with a new size or price added in its place. 

The **Trade Message** "P" reports execution involving non-displayable orders
Example: A hidden buy order is matched at $12.34 for 300 shares. Nasdaq sends a "P" message. This trade doesn't affect the order book, but it does affect volume, VWAP, and time & sales fee

A **cross** is a special type of trade where the Nasdaq matches a large batch of buy and sell orders at a single price. Cross trades happen during the opening, closing, ipo, or halt resume sessions. Nasdaq gather all order and executes one big match at a single price. 

A **Broken Trade** Message tells a market participant that a previously reported trade was canceled.

**Net Order Imbalance Indicator Message** is sent during opening cross, closing cross, IPO, halts, and extending trading closes. This message gives a snapshot of what the expected match and imbalance looks like before a cross happens. 

**Retail Price Improvement Indicator** identifies a retail interest indication of the bid, ask, or both the bid and ask for a Nasdaq security.

This message is sent **only for Direct Listings with Capital Raise (DLCR)** and it provides critical price information **before the listing becomes eligible to trade**. This is a special type of IPO. A company lists directly on Nasdaq without traditional underwritten IPO. It raises captial by selling new shares during the opening auction. 