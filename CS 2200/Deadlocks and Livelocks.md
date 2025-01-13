Deadlocks occur when a thread waits for an event that will never happen, often due to limited resources in a concurrent system. For instance, in a uniprocessor system with a non-preemptive scheduler, if one application enters an infinite loop, other processes are stuck waiting for the processor. This scenario is an example of a **resource deadlock**, where processes are blocked due to unavailable physical resources. The condition that led to the deadlock: mutual exclusion for **accessing a shared resource**, and **lack of preemption**. 

In a computer system, four conditions must occur simultaneously for a resource deadlock:
1. **Mutual Exclusion**: Resources can only be used by one process at a time.
2. **No Preemption**: A process holding a resource cannot be forced to release it; it must do so voluntarily.
3. **Hold and Wait**: A process can hold a resource while waiting for additional resources.
4. **Circular Wait**: Processes are in a cyclic dependency, each waiting for a resource held by another (e.g., A waits for B, B waits for C, ..., X waits for A).

## Strategies for Deadlocks
___
**Avoidance**
- Assumes that the request pattern for resources are known a **priori**. 
- Algorithm will make resource allocation decision that are guaranteed to never result in a deadlock
- Poor resource utilization due to conservatism. Not practical as it need prior knowledge of future resources requests.
**Prevention**
Break one of the necessary conditions and prevent the system from deadlocking

| **Condition**        | **Technical Prevention Strategy**                                                          |
| -------------------- | ------------------------------------------------------------------------------------------ |
| **Mutual Exclusion** | Use spooling, buffering, or read-write locks to eliminate exclusive access where possible. |
| **No Preemption**    | Implement preemptive resource allocation (e.g., preempt CPU, memory pages).                |
| **Hold and Wait**    | Use atomic resource allocation or require all resources to be requested simultaneously.    |
| **Circular Wait**    | Impose a global resource ordering and enforce requests to be made in increasing order.     |
- **Mutex**: Implement **spooling or buffering** for resources like printers. Instead of requiring exclusive access to the printer, processes write their print jobs to a spool (buffer). The printer processes these jobs sequentially.
- **Prevention Strategy**:
	- Allow the system to preempt resources forcibly from a process when needed by another.
	    - **Technical Example**: If a process holding a resource is waiting for another resource, preempt the currently held resource and return it to the pool for other processes.
	        - **CPU Scheduling**: Preemptive scheduling algorithms like **Round Robin** ensure that a process does not hold the CPU indefinitely.
	        - **Memory Management**: Swap out pages held by one process and allocate them to another using techniques like **virtual memory**.
**Detection**
**Deadlock detection** is a strategy used in operating systems and concurrent systems to handle deadlocks by allowing them to occur and then identifying and resolving them. Unlike **prevention** or **avoidance**, this approach is more flexible, permitting processes to request and hold resources without strict constraints, thereby improving resource utilization.
