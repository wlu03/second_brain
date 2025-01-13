The network is a collection of hosts and routers each with their distinct identity. The identity is a unique IP address. If the network is fully connected then one could route a packet from any source to any destination in one hop assuming the cost of sending a packet is the same. However, the **network is not fully connected** and **the cost is the composite of the latency** for moving a packet between any two points and the network traffic between the two points. 
## Dijkstra's Link State Routing Algorithm
___
![[Screenshot 2024-11-24 at 5.08.01 AM.png]]
The edges represent the cost to move from packet to packet. The Link State Routing Algorithm (Dijkstra) is a local algorithm that uses global information. That is all node in the network have complete information about the state of the network (cost associated with links and connections). Given this information, each node can determine an optimal route to send a packet to any destination in the network by running thus algorithm itself. This is just a simple Djikstra's algorithm from DSA.
![[Screenshot 2024-11-24 at 5.09.46 AM.png]]
## Distance Vector Algorithm
____
Distance Vector Algorithm is asynchronous and works with partial knowledge of the link-state of the network. Due to the evolutionary nature of the Internet (growing/expanding, potential deletion of nodes, varying time in cost, etc.), these properties make the it viable. 

**Intuition**: Regardless of the destination, any node has to decide to send a packet to one of its neighbors to which it has a physical link. The choice of which neighbor is the least cost route to the desired destination. This is a **greedy** algorithm that chooses the lowest cost of each neighbor to the given destination. This is updated in the table.  
![[Screenshot 2024-11-24 at 5.14.05 AM.png]]

## Hierarchical Routing
___
Given the scale of the internet, a better way to route is organizing them by hierarchy. *Autonomous Systems (ASs)* are regions organized by the routers. Routers within an AS may run a LS or DV protocols for routing among the hosts that are within the AS. *Gateway routers* of different ASs communicate using *Border Gateway Protocol or BDP*.
![[Screenshot 2024-11-24 at 5.29.37 AM.png]]
### Internet Addressing
___
Host is an end device at the edge of the network and typically has a single connection to the network through the NIC. Router allows several hosts to be connected to it. It serves as an intermediary to route an incoming message on one connection to an appropriate output connection towards the intended destination. A router has number f NIC for each connection it supports. Host contains 5 layers while router contains bottom 3 layers. 

**IP Addresses**: in IPv4, IP addresses are 32-bit. It has 4-part expressed in *dotted decimal notation*: p.q.r.s where each is a 8-bit quantity. For example, the IP address **128.61.23.216** each part of the decimal is a 8-bit pattern. `(10000000 00111101 00010111 11011000)_2` or `(128 61 23 216)_10`.

The bottom 8-bits can be used to uniquely identify the specific device connected to the network using the notation `x.y.z.0/n` where $n$ is the number of bits reserved for the network part of the IP address.
- **128.61.23.0/24**:
    - Network range: `128.61.23.0` to `128.61.23.255` (254 usable host addresses, excluding the network ID `128.61.23.0` and broadcast address `128.61.23.255`).
    - The `/24` tells us this is a single Class C network.
- **192.168.1.0/16**:
    - Network range: `192.168.0.0` to `192.168.255.255`.
    - Here, `/16` reserves the first 16 bits for the network, allowing for a much larger network with many subnets.
- **10.0.0.0/8**:
    - Network range: `10.0.0.0` to `10.255.255.255`.
    - With `/8`, the first 8 bits are reserved for the network, allowing for a vast number of hosts.
- Not all networks are 24-bit. If a company had to hook up 1000 computers to the internet. You would get ISP of IP address that range need to have the top 22 bits fixed. The bottom 10 bits allows you to connect 1024 $(2^{10})$ machine to the internet. A network will have the dotted decimal form of `x.y.z.0/22`
![[Screenshot 2024-11-24 at 5.49.47 AM.png]]
**Answer**:
- 128.61.21.0/n
- 128.61.22.0/n
- 128.61.23.0/n
There is three IP networks in this figure. 