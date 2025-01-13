Performance Metrics

# Question 1 - Transmission + Throughput
___
You are sending a file of 50KB from your phone to your friend’s computer. You are utilizing your phone while sending the file and thus slowing the processing delay down to 7ms. You are using a 5G network with 400Mbps bandwidth. Your friend’s  
computer requires 2ms for processing overhead. Assume the time of the flight to be 10ms.  
What’s the transmission time for the file? Throughput?

The transmission time is the $S + T_w + T_f + R$ where $T_f=10ms,\space R=2ms,\space S=7ms, \space T_w=?$ 
$T_w=\frac{50\times 8Kb}{400Mbps}=0.001 \space 1sec=1ms$
$\text{transmission time} = 10+2+7+1=20ms$

$\text{Throughput}=\frac{\text{400 Kbits}}{20ms}=20Mbit/s$ 

# Question 2 - Transmission Time 
___
Now assume that you are using TCP to transfer the file. The size of each TCP packet is 6KB and the size of the header is 1KB. The window size is 5 packets.  For simplicity, assume the processing delay and receiving delay are 0. Assume the size of the ACK to be 0 (i.e. no overhead). All other conditions remain the same: 

400Mbps bandwidth, time of the flight 10ms, 50KB file.  
What is the total time taken to complete this file transfer?  

Recall that in TCP we have to wait for ACKs on top of the original time of flight.

Size of file carried by the packet = 6KB-1KB=5KB (get rid of header)
Number of packets = 50KB file / 5KB TCP Packet = 10
Time of Flight (RTT): $2\times 10ms=20ms$

**Transmission Per Packet**
$T_w=\frac{\text{Network Size}}{\text{Network Bandwidth}}=\frac{6KB}{400 Mbps}=0.12ms$
Wire Delay 5 Packets (window size of 5): $0.12*5$= 0.6ms

**Total Time**
First Window: $0.6ms+20ms=20.6ms$
Second Window: $0.6ms+20ms=20.6ms$
Total: $20.6ms*2 =41.2ms$


# Question 3 Hops
![[Screenshot 2024-12-11 at 9.27.14 AM.png]]

# Question 4 - Link Layer Hops
Link Layer hops is constituted as a change in MAC or physical address
![[Screenshot 2024-12-11 at 9.27.55 AM.png]]

# Question 5 - Disk Performance Storage and Transfer Rate

Hard Drive Background:
**Platter**: Circular disk. Each platter has two sides (called surfaces)
**Surface**: Each platter has two surfaces (top and bottom) where data is stored on both sides
**Track**: Concentric Circles on each surface. Each track holds data and is divided into smaller units called *sectors*
**Sectors**: The smallest unit of storage. Each sector holds a fix number of bytes of data
$\text{Capacity} = \text{Platter}\times\text{Surfaces per Platter}\times \text{Tracks per Surface} \times \text{Sectors per Track} \times \text{Bytes per Sector}$
$\text{Transfer Rate (bytes/sec)}=\text{Bytes per Sector} * \text{Sectors per Track} * \text{Rotation per second}$
Question:
Double side recording  
8000 RPM  
2048 Bytes per sector  
198 sectors per track  
2^18 = 262144 tracks  
per surface  
8 Platters  
2 Surfaces per platter
What is the total Capacity of the Hard Drive? What is the transfer rate?
$Capacity = \text{8 Platters} * \text{2 Surface per Platter} * \text{198 Sectors per Track} * \text{2048 Bytes per sector}*\text{262144 Tracks}=1.7 TB$
$\text{Transfer Rate} = \text{2048 Bytes per Sector} * \text{198 Sectors per Track} * \text{8000 RPM}=54.08 MBps$
# Question 6 - Time for Random Access
Double side recording  
8000 RPM  
2048 Bytes per sector  
198 sectors per track  
2^18 = 262144 tracks  
per surface  
8 Platters  
2 Surfaces per platter

How long does it take to access a random block  
on disk? Assume average seek time is 6.5 ms
A random access is equal to the sum of seek time and average rotational latency. 

Time for one full rotation is $\frac{60 seconds}{RPM}=0.0075sec$
Average rotational latency: $0.0075/2=0.00375=3.75ms$
We need to divide by 2 because on average half a cycle for the head to move to target sector.
Thus the total access time is 6.5+3.75=10.25ms

# Question 7 - Random Reads
Double side recording  
8000 RPM  
2048 Bytes per sector  
198 sectors per track  
2^18 = 262144 tracks  
per surface  
8 Platters  
2 Surfaces per platter

How many random reads can we do per second?
Assume rotational latency time is 6ms. 

The HDD has 198 sectors per track. Reading on sector would require a fraction of the time it needs to read an entire track. If it takes 6 ms to read all 198, the time to read one sector is $6ms/198=0.0303ms$

Random Read = access sector + read sector = 10.25ms + 0.0303 ms = 10.2803 ms

The number of reads per millisecond is the reciprocal of the random seed time. $$\text{Reads per ms}=\frac{1}{10.2803}=0.09727 \text{ reads/ms}$$
$$\text{Reads per second}=1000 \times 0.09727 \text{ reads/ms} =97.2 \text{ reads/ms}$$

Follow up question: IF each read is 2 KB what is the transfer rate? 
$$\frac{97\text{ reads/sec}}{2048 \space Bytes}  = 198656 B/s=194KB/s$$