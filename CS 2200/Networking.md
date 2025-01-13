The network, a high-speed device, uses DMA for interfacing with the system. The **socket** library provides an API for developing network applications. The computer connects to the network via a Network Interface Card (*NIC*). 

How does a network work? A computer is plugged into a cable modem where it connects to the *Internet Service Provider (ISP)*. This is the access point into the internet, so it represents an *access network*. This access network can be cable, phone line, satellite, etc. The *core* of the network handles larger traffic. On the receiving end, the ISP of the recipient transfers the data to their device/computer. The internet adopted a unviersal addressing system for every device connected. This is called the *Internet Protocol Address* or *IP address*. These connects of access networks, ISP, and core of network creates the internet. The internet is a network of networks.

Packets traverses through a series of *queues* that reside at the input of the routers en route from source to destination. When there is *network congestion* a packet experience queuing delays as it makes it way through the routers towards the destination. *Packet loss* is associated with the queue being full then packets would be dropped. 

## Networking Software
____
This is referred to as the *protocol stack*. 

Ethernet is a protocol used on LANs. It uses the maximum packet size of 1518 bytes refereed to as frame that contains data, destination address, and other information to ensure data transmission. 

For example, if you want to send an image over a network. The image may be several megabytes in size. This image doesn't fit in one network packet. The message has to be broken down into several smaller sized packets to compensate for the physical limitation of the network medium.
- Another issues that arises with this is the *queuing delays* that it might experience. 
- Additionally, the packets of the message will need to arrive *in order* at the destination. Since there are multiple paths between the sender and receiver the network is free to route the packets along different paths. 
- The third issue is that a packet may get *lost* on the network. For example, this could be due to insufficient resources (buffer capacity in an intermediate router) 
- The fourth problem involves transient failure along the way that may mangle the contents of a packet. This could mean bit errors in the transmission through traversing the network. 
To sum the problems: 
1. Arbitrary message size and physical limitations of network packets
2. Out of order delivery of packets
3. Packet loss
4. Bit errors
5. Queuing delays
![[Screenshot 2024-11-22 at 6.54.12 PM.png]]

The **protocol stack** addresses these problems. The stack takes an arbitrary sized application message, transports it and reconstructs it at the destination. The protocol layers using abstraction to separate the different issues. The outgoing messages *pushed* down the layers of the stack form the application down to the physical medium and incoming messages are popped up the layers of the stack from the wire to the application.
![[Screenshot 2024-11-22 at 7.20.54 PM.png]]
**Application**
- Responsible for supporting network-based applications (i.e. instant messenger, P2P sharing, web browser, file transfer)
- A variety of protocols may be employed in this layer such as **HTTP** for web apps. **SMTP** for e-mail, **FTP** for file transfer
- Role of the protocol is to serve a common language between the application level entities (clients, servers, and peers) 
**Transport** 
- This layer takes an application layer message and ferries it between the ends of communication (breaking a message into packets and out of order delivery of packets).
- **TCP** and **UDP** are dominant transport protocols.
- **TCP** stands for transmission control protocol and provides *reliable and in-order delivery* of application data in the form of *byte-stream* between two endpoints. 
	- The connection established between two endpoints before the actual data transmission takes place.
	- When the connection is over, there is usually a *connection teardown*. 
- **UDP** stands for User Datagram Protocol. It deals with messages that have strict boundaries. 
	- UDP does not involve any connection establishment or any teardown. 
	- Messages may arrive out of order since the protocol makes no guaranteed regarding order delivery. 
**Network Layer**
- Transport layer doesn't know how to *route* a packet from the source to destination.
- Routing is responsibility of the network layer. 
- Sending side: given a packet from the transport layer, the network finds a way to get the packet to the intended destination address.
- Receiving end: the network layer passes the packet up the transport layer which is responsible for collating this packet into the message to be delivered to the application layer.  
- Analogy: The network layer is like postal service. 
- The network packet needs a format of the layer such as: address, data, etc. For example, the protocol for this layer has the generic name *Internet Protocol (IP)* and subsumes both the formatting of the packet as well as the route it will take. 
**Link** 
- Link layer ferries the IP packets between nodes on the Internet through which a packet has to be routed from the source to destination. 
- Ethernet, Token Ring, and IEEE 802.11 are example of link protocols. 
- The **network layer** hand the IP packets of the appropriate link layer depending on the next hop to be taken by a packet. 
- This layer delivers the fragments to the next step which is up to the network layer.
**Physical**
- This layer is responsible for moving the bits of the packet from one node to the next.

![[Screenshot 2024-11-23 at 6.33.57 PM.png]]
## OSI Model
There is no hard set number of layers per stack. Therefore, it depends on the functionality that need to be delivered by the protocol stack. Thus, the OSI model came up with a 7-layer model. 
![[Screenshot 2024-11-23 at 6.35.32 PM.png | 200]]

It has two more laying including: presentation and session. The **session layer** is the manager of the specific communication session between two ends. ex: if you're using IM session with friends, the session layer maintains process level information specific to each such pairs of communication. The transport layer then worries about getting them messages reliably across *any* pair of endpoints. The **presentation** layer subsumes some functionality that may be common across several applications. ex. it formates the textual outputs on the display window for clients (AOL for IM). This can include text characters, formatting, and character conversions.

### Issues with Layering
1. **OSI Model as a Reference**: The OSI model provides a checklist for protocol stack functionality but isn't strictly followed in implementations.
2. **TCP/IP as De Facto Standards**: The TCP/IP protocol stack has largely shaped how layers interact, often collapsing or subsuming the OSI layers. For example:
    - Application protocols like HTTP, FTP, and SMTP integrate layers 7-5.
    - TCP and UDP align with layer 4.
    - IP corresponds to layer 3.
    - Network interfaces (e.g., Ethernet cards) serve layer 2 functionality.
Issues: 
1. **Deviation from Strict Layering**:
    - Real implementations often do not adhere strictly to the OSI model's layering discipline due to practical considerations and efficiency needs.
    - Layers are frequently "collapsed" or combined to simplify functionality or improve performance.
2. **Simultaneous Evolution of Standards**:
    - The OSI model and the Internet evolved concurrently in the 1980s. This led to the dominance of the TCP/IP protocol stack, which diverged from the strict OSI layering model.
3. **Layer Collapsing**:
    - Protocols like HTTP, FTP, and SMTP combine or subsume multiple layers (OSI layers 5-7).
    - TCP and UDP implement functionalities of layer 4, while IP handles layer 3 tasks.
    - Hardware, such as Ethernet cards, takes on layer 2 roles directly.

## Application Layer
___
Two Part in a network (generally speaking...):
- **Client**: This is the part that sits on end devices such as handhelds, cellphones, laptops, and desktops.
- **Server**: This is the part that provides the expected functionality of some network service (e.g., a search engine).

**Example**
Network Applications include: World Wide Web (WWW), electronic mail, network file system.  A network application is more than an application layer protocol. A web browser needs to maintain a history of URLs accessed, a cache of web pages downloaded, etc. 

Application-layer protocols are designed to support various network applications, such as HTTP for web interactions and SMTP for email communication. These protocols are platform-independent, enabling access to services like email or websites across diverse devices and operating systems, such as cellphones, public terminals, and Internet cafés.

Operating systems also provide unique network services, such as accessing files from a Unix file system or printing to a network printer. To facilitate such functionalities, operating systems include network communication libraries that offer APIs for client-server interaction, similar to how thread libraries support interactions within an address space.

For example, Unix provides the socket library for network programming, while other platforms like Microsoft Vista and MacOS have equivalent APIs. Although the implementation details of socket libraries are outside this textbook's scope, they are fundamental for building network applications. Basics of network programming using the socket API are covered later in the textbook.

## Transport Layer
___
The transport layer provides a set of calls, *Application Program Interface (API)* so that the application layer can send and receive data on the network. 
- **send (destination-address, data)**
- **receive (source-address, data)**

Expected functionalities of transport layer:
1. Support arbitrary data size at the application level
2. Support in-order delivery of data
3. Shield the application from loss of data
4. Shield the application from bit errors in transmission.

**Protocols**: This layer could view the data form the application layer either as *byte stream* or as a *message*. The transport may be either *stream* or *connection oriented (e.g. TCP)* in which case the application data is considered a continuous stream of bytes. The transport layer chunks the data into predefined units called *segments* and sends segments to its peer at the destination. Alternatively, the transrt layer may be message or datagram oriented (e.g., UDP – User Datagram Protocol) in which case the application data is treated similar to a postcard sent through the postal mail system.

**Scatter/Gather:** Transport layer at the source has to break up the data into *packets* with the limitations of the network. The peer transport layer at the destination has to assemble the packets back into the original message to the recipient of them message. This functionality is called **scatter/gather**. The transport layer deals with out of order at destination by giving a *sequence number* for each packet of a message. 

**Packet Loss and Corruption:** Bit errors do not always make the packet completely unusable. To do error correction on packets, we use *Forward Error Correction (FEC)* when such bit-errors occur. If the FEC algorithm doesn't work, consider the packet lost. *Positive acknowledgement* is used to ensure that the packet has arrived. To track how long it took, *round trip time (RTT)* is how long it took for the data to arrive.
![[Screenshot 2024-11-24 at 3.06.32 AM.png]]

### Transport (Session) Protocols
___
**Stop and Wait**
1. Send a packet and wait for positive acknowledgement, **ACK**
2. As the packet is received, the recipient generates and sends an ACK for that packet. The ACK should contain the information for the sender to discern ambiguously the packet being acknowledged. Sequence number is unique signature of each packet. 
3. The sender waits for a period of time called *timeout*. If within the period, it does not hear an ACK. It *re-transmits* the packet. 
This is called **stop-and-wait** since the sender *stops* transmission after sending one packet and *waits* for an ACK before proceeding with the next.

*Sequence Number*: To ensure that the current packet is received and no duplicates. The sequence number is used to track monotonically increasing sequence numbers. It is sufficient if we represent the sequence number by a single bit. If protocol sends a packet with a sequence number of 0 and waits for an ACK with number 0. When receiving the ACK, it will send the next packet with number 1 and wait for ACK with the sequence number 1. This is called the *alternating bit protocol*. It makes everything simpler because it takes up less data.
![[Screenshot 2024-11-24 at 3.25.20 AM.png]]

**Pipelined Transmission**
Stop and wait protocol is simple. However, there is *dead time* on the network while the sender is waiting for the ACK to arrive. Dead time is defined as the time when there is no activity on the network. If the network is reliable (aka no packet loss) we can *pipeline* the packet transmission without waiting for ACks.
![[Screenshot 2024-11-24 at 3.27.52 AM.png]]
**Bandwidth** is the amount of time it would take the host to place packet on the wire. **Propagation time** refers to the end-to-end delay for a packet to reach the destination. 

*Example*: A message has 10 packets, and the time to send a packet from source to destination is 1 msec. Assuming the receive/send time is neglible compared to propagation time, no packet loss. The amount of time to completely transmit with pipelining is 1 msec. 

**Reliable Pipelined Transmission**
This is the intermediate approach between *stop-and-wait* and *pipelining with no-acks*. 
- The source sends a set of packets (called a *window*) before expecting an acknowledgment. 
- The destination acknowledges each packet **individually** as before. The sender does not have to wait for acknowledgements for all the outstanding data packets before starting to send again.
![[Screenshot 2024-11-24 at 3.32.45 AM.png]]
- The size of the window is agreed upon as a *parameter* of the protocol or dynamically adjusted based on observed *network congestion*

### Network Congestion
*Motivated Example*: If there are four 1 GBPS network flows into the pipe that can support 10 GBPS. Even if all the four networks flows are coming in the 10 GPBS pipe can sustain their requirements. If there is 20 flows coming in, the network cannot sustain the rate. 

The buildup of the *packet queues* in the routers cause this congestion. This results in unpredictable *queuing delays* and *packet losses* due to the router dropping the packets due to lack of buffer space. Some area with limited network flow will experiment more congestion. This is because not all network can support high usage GBPS. 

#### Sliding Window
The window size serves as the mechanism for self-regulation in a transport protocol that incorporates congestion control. The window size restricts the sender's rate and in turn prevents the buildup of queues in the routers thus mitigating the network congestion.

A given window size we can define an *active window* of sequence numbers that corresponds to the set of packets that the source can send without waiting for ACKs. The width represents the time it takes at the sender to push a packet out of the computer on to the network. It could be a ratio of packet size to the bandwidth of the network interface. 

*Example*: 
The width of each packet, or the time it takes to transmit a single packet, can be calculated using the formula:
$\text{Transmission Time (Packet Width)} = \frac{\text{Packet Size (bits)}}{\text{Bandwidth (bits per second)}}$
Given:
- Network bandwidth = 1 Gbps (1,000,000,000 bits per second)
- Packet size = 1000 bytes = 1000 × 8 bits = 8000 bits

Now, calculate the transmission time (width):
$$\text{Transmission Time}=\frac{1,000,000,000 \text{ bits}}{8000 \text{ bits/sec}}​=8\text{ microseconds}$$
The width of the packet give an upper bound for the maximum window size that is reasonable to use for a given RTT. Lets say an RTT is 2 ms, then the maximum window size can be 250 packets (each packet is 1000 bytes). $$\frac{2000 \text{ microseconds}}{8 \text{ microseconds per packet}}=250 \text{ packets}$$
The actual window size may be chosen to be smaller than this upper bound for reasons such as: network congestion, buffer space for packets at the sender and receiver, and the size of field used to denote the packet sequence number in the header.
![[Screenshot 2024-11-24 at 4.11.01 AM.png]]
As soon as the ACK for the first red packet in the active window is received, the active window moves one step to the right. This is called the *sliding window protocol*.

*Example Calculation*:
A message has 10 packets, and the RTT is 2 msec. Assuming that the time to send/receive the packet and the ACK are negligible compared to the propagation time on the medium, and no packet loss, how much time is required to complete the transmission with the sliding window protocol with a window size of 5?
*Answer*: 
Since the RTT is 2 msec, the source sends a window of 5 packets and then waits for the ACK. The first ACK is recieved 2 msec after the first packet is sent. Therefore, in one cycle of 2msec, the source has completed sending out 5 packets. Following the end of the first packet, the next one is sent. Thus, when the 5th packet is finishing sending, it starts on the 10th packet. Therefore, it will finish in 4 msec.
![[Screenshot 2024-11-24 at 4.18.14 AM.png]]

**Initiation on Sliding Window**: So why does this protocol optimized for the ACKs? Instead of sending an ACK for each of the n packets, a single ACK for the $n^{th}$ packet is sent. Since the $n^{th}$ packet implies the successful reception of the n-1 packets preceding the $n^{th}$ packet. TCP uses cumulative ACKs to reduce overhead. The source and destination use timeout mechanism to discover packet losses. Each side will set a timer upon sending a packet. If the source doesn't receive an ACK for the packet within the timeout period, it will retransmit the packet. The source has to *buffer* the packets for the ACKs it didn't receive. 

*Example*:
Assume that the network loses 1 in 5 packets on an average. For a message that consists of 125 packets, determine the total number of packets sent by the sender to successfully complete the message transmission.
*Answer*: 
Since there is a 20% loss, we need a number $x$ that would send a total of 125. $$x(0.8)=125,x=156$$
### [[TCP vs UDP]]
___
![[Screenshot 2024-12-11 at 1.14.34 AM.png]]

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
## Network Layer
To get from the source to destination, the data needs to be go through several intermediate hops. The path taken by packets from source to destination is called a **route**. The network layer is responsible for routing a packet given a destination address. It maintains a table (called *routing table* that contains a route or a path from the source to any desired destination host). 

Functionalities needed in the network layer. 
- **[[Routing Algorithms]]**: Determines a route for packets to take. 
- **Service Model**: This layer should forward an incoming packet as an incoming link to the appropriate outgoing link based on the routing information. This is referred to as the switching function of the network. 

The device that performs functionalities on the network layer is called a *router*. 

**IP Addressing and Subnets**
- 32 Bits, 4 Octets
	- An IPv4 address is represented as four decimal number separated by dots (e.g. 130.207.7.31) where each decimal number represents an 8-bit octet
	- It can be converted to hexadecimal or binary (e.g. 0x82CF071F for 130.207.7.31)
- Subnet Masks: Use to divide the IP address into:
	- **Network Part**: identify the network
	- **Host Part**: identify the specific device on the network
	- **Broadcast address** is the IP address used to send data to all devices within a subnet. 
	- ![[Screenshot 2024-12-11 at 3.18.57 AM.png]]
	- /16 Subnet Example:
		- **IP Address:** `172.16.0.0`
		- **Subnet Mask**: `255.255.0.0`
		- **Network Portion**: First two octets (`172.16`)
		- **Host Portion:** `0.0` to `255.255`
		- **Useable Host Range:** `172.16.0.1` to `172.16.255.254`
		- **Broadcast Network:** `172.16.255.255`
### Rules for IP Routing
1. **Same Network**:
    - If two devices are on the same network (i.e., their network parts match), they can communicate directly by **passing the packet to layer 2 for delivery**
    - The communication is handled at the **Data Link Layer** (e.g., Ethernet).
2. **Different Networks**:
    - If two devices are on different networks, the communication is forwarded through a router.
    - The router uses its **routing table** to determine the next hop for the packet.
    - Send the packet to the next-hop router by choosing the longest match in the IP routing table.
![[Screenshot 2024-12-11 at 3.40.11 AM.png | 400]]
*From 223.1.1.2 to 223.1.3.2 is 2 hops.*

## TCP Connection
___
TCP allows data to flow in both direction. Each side uses a random sequence to track and ensure order of packets. The three-way handshake is a TCP connection setup involving SYN, SYN-ACK, and ACK. The handshake ensures that both the client and server agree on initial sequence numbers and are ready for communication. SYN (synchronize) and ACK (acknowledge) flags in the TCP header are used to establish the connection. 
![[Screenshot 2024-12-11 at 4.26.49 AM.png]]
1. Client sends SYN. Indicates the client is trying to start a connection. Random Sequence Number, x, is the starting point for tracking the data stream. 
2. Server responds with SYN-ACK. The server acknowledges the client's request and indicates readiness. Acknowledges client's sequence number by adding `x+1`. It creates it's own sequence number. 
3. Client sends ACK to acknowledge the server's sequence number by sending `y+1`

## TCP and UDP Ports
___
Ports are numerical identifiers that help direct data to the correct application or process on a device. Both TCP and UDP use ports to enable multiple network connections to and from a single device. **Source Port** is dynamically assigned by the sender's system to identify the sending application. **Destination Port** specifies the service or application that data is intended for on the receiver's side.
![[Screenshot 2024-12-11 at 7.20.01 AM.png | 450]]

**Example**
- When the browser opens a connection, it doesn't specify a source port. The **TCP stack** dynamically assigns a source port that isn't already in use on the client device. 
- Each TCP connection is uniquely identified by a **quadruple**: `(Source IP, Soruce Port, Destination IP, Desination Port)`
- Using ports `31339` and `31337` as examples, the identifiers look like:
	- `(193.12.1.5, 31339, 130.207.7.13, 80)`
	- `(193.12.1.5, 31337, 130.207.7.13, 80)`
	- **Reverse** quads are also used to identify packets going in the opposite direction (from server to client).
**Firewalls**
- A **stateful firewall** is a type of firewall that monitors the state of active connections and make decisions based on: 
	- The state of the connection
	- a predefined policy 
		- Example:
			  Allows no inbound packets or allows inbound packets
	- Maintains a **local state table/connection table** to track active connections using a **quadruple.**
	- When an outbound packet is allowed, the firewall records its details in the connection table.
	- Example:
        - If `(193.12.1.5, 31337, 130.207.7.13, 80)` is added to the table, the firewall will automatically allow return traffic:
            `(130.207.7.13, 80, 193.12.1.5, 31337)`  
	    - This ensures responses from the server are allowed without requiring an explicit rule.
**Drop Unauthorized Traffic**:
    - Any incoming traffic not matching an entry in the connection table is **dropped** unless explicitly allowed by a policy.
    - For example:
        - Inbound traffic to a port not listed in the connection table (e.g., `192.13.1.5, 51284`) will be denied.

## Network Address Translation
Network Address Translation (NAT), is a method used to modify network address information in packet headers while in transit. NAT is used to improve security and manage the scarcity of IPv4 addresses. NAT allows multiple devices on a private network to share a single public IP Address for accessing external networks. NAT rewrites the source or destination IP address and may adjust ports in IP Packets as they pass through NAT enabled routers. 

**Types**: 
1. Static One-One NAT
	- **Description**:
	    - A specific private IP address is permanently mapped to a public IP address.
	    - Each private IP address has a corresponding unique public IP address.
	    - **Checksums** are recalculated to reflect the changes in the IP address.
	- **Use Case**:
	    - Suitable for devices that need a fixed external IP address (e.g., servers hosting websites).
2. Dynamic One-One NAT
	- **Description**:
	    - Similar to static NAT but uses a pool of public IP addresses.
	    - A private IP address is mapped to a public IP address dynamically, and the mapping lasts only for the duration of the connection.
	    - When the connection ends, the public IP is returned to the pool.
	- **Use Case**:
	    - Useful when you have more private devices than public IPs and need temporary external access.
3. Port Address Translation (PAT) / Network and Port Address Translation (NPAT)
	- **Description**:
	    - Extends dynamic NAT by mapping multiple private IP addresses and ports to a single public IP address.
	    - Both the **source address** and **source port** are translated.
	    - Return traffic is identified by the combination of **destination address** and **destination port**.
	- **Use Case**:
	    - Common in home or small office networks to enable multiple devices to share a single public IP.
	    - Helps conserve IPv4 addresses by allowing many devices to use one public IP.

### **Big Difference Between Dynamic NAT and PAT/NPAT**
The **key difference** between **Dynamic NAT** and **PAT/NPAT** lies in how multiple devices on a private network share public IP addresses:
1. **Dynamic NAT**:
    - Maps **one private IP** to **one public IP** dynamically.
    - Requires a pool of public IP addresses.
    - Only as many devices can access the internet as there are public IPs in the pool.
    - **No port translation** is involved.
2. **PAT/NPAT**:
    - Maps **multiple private IPs** to a **single public IP** using **port numbers** for differentiation.
    - Allows **many devices** to share a **single public IP address**.
    - Uses source and destination port numbers to track and manage connections.

### **Examples**
#### **Dynamic NAT Example**

1. **Setup**:
    - **Private Network**: `192.168.1.0/24` (e.g., devices `192.168.1.10`, `192.168.1.11`, `192.168.1.12`).
    - **Public IP Pool**: `203.0.113.1` to `203.0.113.5` (5 public IPs).
2. **Scenario**:
    - Device `192.168.1.10` starts a connection to the internet. The NAT router assigns `203.0.113.1` from the pool.
    - Device `192.168.1.11` starts another connection and gets `203.0.113.2`.
    - If a sixth device (`192.168.1.15`) tries to connect, it will be **blocked** because all public IPs are in use.
3. **Limitation**:
    - The number of simultaneous connections is limited by the size of the public IP pool.
    - Dynamic NAT **does not support port sharing**, so each public IP is assigned to only one private IP at a time.
#### **PAT/NPAT Example**
1. **Setup**:
    - **Private Network**: `192.168.1.0/24` (e.g., devices `192.168.1.10`, `192.168.1.11`, `192.168.1.12`).
    - **Single Public IP**: `203.0.113.1`.
2. **Scenario**:
    - Device `192.168.1.10` initiates a connection to a web server:
        - Source IP: `192.168.1.10`, Source Port: `1025`.
        - NAT translates it to: `203.0.113.1:40000` (new source port assigned by the NAT router).
    - Device `192.168.1.11` initiates another connection:
        - Source IP: `192.168.1.11`, Source Port: `1026`.
        - NAT translates it to: `203.0.113.1:40001`.
    - When responses arrive, the NAT router uses the port numbers (`40000` and `40001`) to forward traffic to the correct private IP.
3. **Advantage**:
    - PAT allows **thousands of devices** to share a single public IP address by differentiating them using **port numbers**.

## Remote Procedure Call (RPC)
___
RPC provides a higher-level abstraction for distributed computing, enabling a client to invoke procedures on a remote server without knowing the details of network communication. To the caller, the procedure appears as a local function, but it is executed on a remote system.![[Screenshot 2024-12-11 at 7.40.14 AM.png]]


#### **1. Shim Function on the Caller Side (Host 1)**
When a client invokes a remote procedure:
- **Packing Arguments**:
    - The arguments for the function are serialized (packed) into a network-friendly format.
- **Sending Packet**:
    - The packed arguments are sent as a network packet to the remote server.
- **Waiting for Return Value**:
    - The client waits for the remote server to process the function and return the result.
- **Unpacking and Returning**:
    - The result is deserialized (unpacked) and returned to the caller.

#### **2. Listener on the Remote Side (Host 2)**
On the server:
- **Receiving and Unpacking**:
    - A listener process continuously waits for incoming requests.
    - When a request arrives, it unpacks the arguments from the network packet.
- **Executing the Function**:
    - The server calls the requested function with the unpacked arguments.
- **Packing Results**:
    - The result of the function is serialized into a network packet.
- **Returning Results**:
    - The result packet is sent back to the client.

### **Key Differences Between IPv4 and IPv6**
____
#### **1. Header Format**
- **IPv4**:
    - Variable-length header, typically **20 bytes**.
    - Includes fields for fragmentation, checksums, and options within the header.
- **IPv6**:
    - Fixed-length **40-byte header** for simplicity and efficiency.
    - Options (if needed) are handled after the main header using **extension headers**.
#### **2. Address Size**

- **IPv4**:
    - Uses **32-bit addresses**, allowing approximately **4.3 billion addresses**.
    - Addresses are written in dot-decimal notation (e.g., `192.168.1.1`).
- **IPv6**:
    - Uses **128-bit addresses**, allowing for **3.4×10³⁸ unique addresses**.
    - Written in hexadecimal format, separated by colons (e.g., `2001:0db8::1`).
    - The first **64 bits** are always for the **network part**.
#### **3. Broadcasting vs Multicasting**

- **IPv4**:
    - Supports **broadcasting**, where data is sent to all devices on a network.
- **IPv6**:
    - Does not support broadcasting to avoid unnecessary network traffic.
    - Supports **multicasting**, allowing data to be sent to multiple specific devices simultaneously.
#### **4. Fragmentation**
- **IPv4**:
    - Allows **fragmentation** at intermediate routers, which can lead to additional overhead.
- **IPv6**:
    - Fragmentation is **not allowed** at routers. Only the originating host can fragment packets, making routing more efficient.
#### **5. Addressing and Subnets**
- **IPv4**:
    - Subnetting is commonly used to divide the address space.
    - ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses.
- **IPv6**:
    - Supports **1.8×10¹⁹ subnets**, each with **1.8×10¹⁹ hosts**.
    - Replaces ARP with **Neighbor Discovery Protocol (NDP)**, which uses ICMPv6 for address resolution and network discovery.

#### **6. NAT (Network Address Translation)**
- **IPv4**:
    - Widely uses NAT to allow multiple devices to share a single public IP address due to address scarcity.
- **IPv6**:
    - **Discourages NAT**, as the large address space makes it unnecessary.
    - Still allows **local addressing** for private networks (e.g., `fc00::/7`).
#### **7. Link-Local Addresses**
- **IPv4**:
    - Link-local addressing is optional and not commonly required for basic operation.
- **IPv6**:
    - Every interface **must have** a **link-local address** (e.g., `fe80::/10`), which is used for communication within the local link (e.g., neighboring devices).
#### **8. Scanning Subnets**
- **IPv4**:
    - Small address space makes it feasible to scan a subnet for hosts.
- **IPv6**:
    - The massive address space makes scanning a subnet **impractical** for discovering devices, enhancing security.


# Data Link Layer
___
This layer in the OSI model is responsible for facilitating communication between directly connected devices in a network by organizing raw data into frames and ensuring reliable data transfer. Ethernet is a very common data link network.
![[Screenshot 2024-12-11 at 7.48.56 AM.png]]
To send a frame
- Wait until no one is using the cable (carrier sense)
- Assert carrier signal on the cable
- Broadcast the frame to all stations on the cable
- If a collision is detected while transmitting, so and re-queue the frame for retransmission

Within the payload contains the IP addresses in the ethernet frame.
![[Screenshot 2024-12-11 at 7.52.52 AM.png]]
**Address Resolution Protocol (ARP)** is used in networks to map an **IP address** to a **MAC address**. A device (e.g., a computer) wants to send data to another device with a specific **IP address (`a`)** but doesn’t know the corresponding MAC address. The device broadcasts an **ARP request** to the entire local network (LAN). The request is sent as a broadcast frame to **all devices** on the local network because the MAC address of the destination is unknown. The device with IP address `a` responds with a **unicast ARP reply**. The sender stores the resolved MAC address in its **ARP table** (a temporary cache) for future use. The ARP table entries are periodically refreshed or removed if they become stale. The device uses the MAC address obtained from the ARP reply to send the data frame directly to the destination.

**Ethernet Bridging Algorithm**
- A **bridge** (or switch) is a device that connects multiple network segments and directs traffic between them based on MAC addresses.
- Bridges use a **bridge table** (also called a MAC address table) to learn and store information about connected devices.
Steps in Bridging Algorithm:
- **Frame Arrival**:
    - When a frame enters a bridge, the switch inspects its **destination MAC address** and processes it according to the rules below.
- **Destination MAC in Bridge Table**:
    - If the destination MAC address is found in the **bridge table**:
        - The frame is forwarded to the port listed in the bridge table for that MAC address.
    - This minimizes network traffic by sending the frame directly to the intended recipient.
- **Destination MAC Not in Bridge Table**:
    - If the destination MAC address is **not found** in the bridge table:
        - The switch assumes the device is on an unknown segment.
        - The frame is **flooded** to all ports except the port it arrived on.
        - Flooding ensures the frame reaches the intended device, which can then respond, allowing the switch to learn its location.
- **Update Bridge Table with Source MAC**:
    - The **source MAC address** of the frame is added to the bridge table if it's not already present.
    - The switch records:
        - The **source MAC address**.
        - The port where the frame was received (**ingress port**).
        - The time the frame was received (to mark the entry as "recently used").
- **Removing Stale Entries**:
    - Entries in the bridge table that have not been used for a specific time are removed.
    - This ensures the table remains up-to-date and does not become cluttered with outdated or unused MAC addresses.

# Network Socket Programming
___
![[Screenshot 2024-12-11 at 7.56.53 AM.png]]

## Performance Metrics
____
$\text{Transmission Time (end-to-end latency)}=S+T_W+T_f+R$ 
$\text{Message Throughput} = \frac{\text{Message - Size}}{\text{end-to-end latency}}$
$S$ is Processing overhead of sender
$T_W$ is wire delay
$T_f$ is flight time
$R$ is the processing overhead at receiver
![[Screenshot 2024-12-11 at 7.59.35 AM.png]]![[Screenshot 2024-12-11 at 8.00.01 AM.png]]

**Example**
![[Screenshot 2024-12-11 at 8.00.29 AM.png]]