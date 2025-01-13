![[Screenshot 2024-12-11 at 1.14.34 AM.png | 600]]
**TCP Features:**
- Involves setting up a connection between two endpoints of communication. The data flow between two endpoints is a *stream of bytes*
- TCP connection is a full duplex connection: both sides can simultaneously send and receive data once the connection is set up. 
- **Connection Set up**: 
	- Client sends the server a connection request message with info regarding initial sequence number it plans to use for its data packets
	- Server acknowledges the message to connection with information mention above
	- Client allocates resources (packet buffer for windowing, timers for retransmission, etc) and sends an acknowledgement. The server allocates resources as well
- **Reliable data transport**: Protocol guarantees the data handed to it from the upper layers will faithfully delivered in order to the receiving end without loss or corruption
- **Congestion Control**: sender  self-regulates its flow by observing congestion and dynamically adjusts window size to avoid the buildup of the queue in routers. TCP flows could experience unbounded delays in the presence of network congestion. 
- **Connection Teardown**: Two endpoint agree as follows:
	- Client sends a connection teardown request (field to distinguish from normal data) to the server. The server send an ACK
	- The server sends it own teardown request to the client. The client send the ACK. The client de-allocates client-side resources associated. Upon receiving an ACK, server does the same time and the connection is closed.
**UDP Features**
- Messages can be out of order, lost, and there is no self-control so UDP flow may be the source of increased congestion.
- Connection-less, unregulated, message as datagram, no ACKs or windowing
- Simplicity and suited for environment with low chance of packet loss and application tolerant to packet loss
![[Screenshot 2024-12-11 at 2.22.18 AM.png]]

## TCP
___
- TCP stream are always bidirectional. Either side can send data to the other side. \
- Uses a sequence number in each direction to maintain packet order
- We refer to the 3 packets at the beginning of a TCP connection as the SYN, SYN-ACK, and ACK packets, hence the term 3-way handshake. SYN and ACK are flag bits in the TCP header
- 