A process is a program and all of the states that represent its executions (registers, memory, pc, stack). There are multi task running within your CPU, but how do you know which ones to run first? A **scheduler** gets a chance to look at whichever process to run given some properties. **Thread**: Unit of scheduling and/or execution which is contained within a process. **Task** is a unit of work.

**Program Properties**
CPU to I/O Ratio
- This is important as the ratio helps identify performance bottlenecks and optimize system resources. 

**CPU Burst**: Continuous CPU activity by a process before requiring an I/O operation
**I/O Burst***: Activity initiated by the CPU on an I/O device

**Ready Queue**: Queue of PCBs that represent the set of memory resident processes that are ready to run on the CPU 
**I/O Queue**: Queue of PCBs that represent the set of memory resident processes that are waiting for some I/O operations either to be initiated or completed. 

**PCB - Process Control Block**
- Represents a process' state
```
enum state_type {new, ready, running, waiting, halted};
typedef struct control_block_type {
	enum state_type state;
	address PC; // where to resume
	int reg_file[NUMREGS]; // register contents that's visible
	struct control_block *next_pcb;
	int priority; // extrinistic attribute 
	address memory_footprint; // memory occupancy
	
} control_block;
```

**Preemptive vs. Non-Preemptive**
Preemptive: External Interrupt, Algorithm that **forcibly** takes the processor away from currently scheduled process to external event
Non-Preemptive: System call (Trap), I/O request, process exit, Algorithm that allows the currently scheduled process on the CPU to **voluntarily** relinquish the processor.

**Metric**
![[Screenshot 2024-10-22 at 6.20.24 PM.png]]
# Multitasking
____
## First Come First Serve
___
- Intrinsic Property
![[Screenshot 2024-10-22 at 6.50.39 PM.png]]
- High average waiting times 
- High average turnaround times
- Convoy Effect
## Shortest Job First
___
- Intrinsic Property
![[Screenshot 2024-10-22 at 7.06.11 PM.png]]
- Potential for unfairness. As long as there is a bundle of small processes, P1 will never run. This is called starvation
- Low average waiting and turnaround time.
- Slightly underutilized the CPU

## Priority Scheduler
____
 ![[Screenshot 2024-10-22 at 7.11.47 PM.png]]
 - Within each priority the levels can choose between different algorithm such as FCFS or SJF

# Preemptive Schedulers
___

## FCFS w/ preemptive
___
![[Screenshot 2024-10-22 at 7.14.30 PM.png]]
## SFJ w/ preemptive
____
- Estimate remaining time to make preemptive decisions.
![[Screenshot 2024-10-22 at 7.19.00 PM.png]]
- P1 will run next on CPU
## Priority w/ preemption
____
![[Screenshot 2024-10-22 at 7.25.16 PM.png]]

## Round Robin
___
- RR is preemptive and requires a timer interrupt.
- When a process starts, it is given a time (time slice) which limits the continuous CPU time it may use
- When process is dispatched the timer is set to interrupt at the end of the remaining time quantum. 
- If a processes uses up its remaining time quantum
	- the process is interrupted
	- scheduler is called to put the process at the end of the ready list
	- process' remaining time is reset
- if interrupt (other than timer) occurs, the process' remaining time quantum is reduced by the amount it has used prior to the interrupt

![[Screenshot 2024-10-22 at 8.00.00 PM.png | 450]]
![[Screenshot 2024-10-22 at 8.02.11 PM.png]]
- Choosing a small time slice increase the overhead, but too large doesn't divide time evenly
- Potential for unfairness, no starvation, no convey effect
- Average waiting and turnaround time