## Example
____
What is the response time for P1, P2, and P3?
![[Screenshot 2024-10-17 at 7.00.13 PM.png | 600]] 
What is the wait time for P1, P2, P3?
![[Screenshot 2024-10-17 at 7.00.57 PM.png]]
![[Screenshot 2024-10-17 at 7.01.10 PM.png]]![[Screenshot 2024-10-17 at 7.01.36 PM.png]]
![[Screenshot 2024-10-17 at 7.02.02 PM.png | 400]]
What is the total throughput of these processes?
3 Processes done in 23 seconds -> $3/23=0.13 \space pcs/sec$

What is the processor utilization during the processes?
22 out of 23 seconds had a process running in the CPU -> 95.7% utilization rate

Intervals 6 to 7 and 9 to 10 indicate a preemptive algorithm (processes are kicked off the CPU) which are SRTF, RR or priority. Because there is uneven time slices, no context about priority it has to be SRTF.
