## User Level Threads
___
![[Screenshot 2024-11-19 at 6.14.17 PM.png]]
- At the OS level, it maintains a ready queue of set of schedulable processes. 
- The thread library maintain a list of ready to run threads **in each process** with information about their **thread control blocks (TCBs)** 
	- Contains minimal information about each threads: PC value, SP value, and GPR values.
- Processes at user level may be single threaded or multithreaded.

**Concurrency**
- **User**: The user level in a given process cannot execute concurrently. True parallelism is not possible because the kernel treats the entire process as a single thread. Even on multi-core processors, only one user-level thread can execute at a time per process.

**Switching**:
- **User**: Cheap to switch threads at the user level as it doesn't involve the operating system. The cost of context switch approximates making a procedure call in a program.  

**Blocking System Call** 
A blocking system call is a type of system call that causes the executing process or thread to be put into a waiting state until the requested operation completes. During this time, the process cannot execute any further instructions.

- **User-level threads are invisible to the operating system:** The OS only recognizes and schedules processes, not the individual threads within them.
- If one thread in a multithreaded process makes a **blocking system call** (e.g., reading from a file or waiting for network data), the **entire process is blocked** because the OS has no knowledge of the other threads in the same process that might be ready to execute.
- This means that even if other threads are available to perform useful work, they will be unable to run because the entire process is paused by the OS.

**Potential Solutions**: 
**Wrapping System Calls (Envelope Wrapping)**
- How it works:
    - The thread library wraps all system calls (e.g., `fopen`, `read`) into custom thread-aware versions (e.g., `thread_fopen`, `thread_read`).
    - When a thread makes a blocking system call, the thread library intercepts the call and examines the state of other threads in the process.
    - Instead of issuing the blocking system call immediately, the library defers it until all threads in the process are unable to make progress.
    - Once no other threads are runnable, the library issues the blocking system call on behalf of the thread.
- **Benefit:** This avoids blocking the entire process until absolutely necessary.
- **Limitation:** Adds complexity to the thread library and can increase overhead for handling system calls.
**Upcall Method**
- How it works:
	- The operating system is extended to include an **upcall mechanism** that interacts with the thread library in user space.
	    - Before a thread in a process makes a blocking system call, the OS sends a signal or "upcall" to the thread library, warning it that the system call would block.
	    - The thread library can respond to the upcall by:
	        - **Switching to another thread:** The library may schedule a different user-level thread to execute while the blocking call is deferred.
	        - **Deferring the blocking call:** The thread library may decide to postpone the blocking call until a later time when no other threads in the process can make progress.
- **Benefit:** The process is not entirely blocked, and other threads can continue execution.
- **Limitation:** Requires changes to the operating system, which may not always be feasible.
![[Screenshot 2024-11-19 at 6.31.29 PM.png]]

### **Key Features of Kernel-Level Threads**

1. **Shared Address Space**:
   - All threads within a process share the same **address space** because they belong to the same process.
   - The operating system must ensure that all threads in the process share the same **page table**, which maps the virtual memory used by the process to physical memory.

2. **Separate Stack**:
   - Each thread requires its own **stack** to maintain its execution state (local variables, function call frames, etc.).
   - The rest of the memory, including the code, global data, and heap, is shared among all threads in the process.

3. **Thread Synchronization**:
   - The operating system must provide **thread-level synchronization constructs** (e.g., mutexes, condition variables) to allow threads to coordinate access to shared resources safely.

####  Two-Level Scheduling in Kernel-Level Threads

The operating system uses a **two-level scheduler** to manage threads and processes efficiently, as described in the text:
1. **Process-Level Scheduler**:
   - **Manages Process Control Blocks (PCBs):**
     - Each process has a PCB that stores information shared by all its threads, such as the **page table** and accounting details.
   - **Allocates CPU Time to Processes:**
     - The process-level scheduler is responsible for preemptive scheduling among **processes** (e.g., using Round Robin or Priority Scheduling).
     - Each process is assigned a time quantum.
2. **Thread-Level Scheduler**:
   - **Manages Thread Control Blocks (TCBs):**
     - Each thread has a TCB that tracks its execution state (e.g., program counter, stack pointer, CPU registers).
   - **Schedules Threads Within a Process:**
     - Within the time quantum assigned to a process, the thread-level scheduler schedules the threads of that process.
     - Scheduling strategies could include:
       - **Round Robin:** Threads take turns executing in a fixed order.
       - **Co-Routine Mode:** Threads voluntarily yield the processor to allow another thread to run.
#### Advantages of Kernel-Level Threads
1. **Independent Thread Execution**:
   - Since the OS is aware of each thread, it can schedule them independently, allowing threads to run on different CPU cores for **true parallelism**.
2. **Blocking Calls Do Not Block the Process**:
   - If a thread makes a blocking system call (e.g., waiting for I/O), the OS can switch to another thread in the same process.
   - This eliminates the issue faced by user-level threads, where the entire process would block in such cases.
3. **Thread-Level Synchronization**:
   - The OS natively supports thread synchronization primitives, simplifying thread management and resource sharing for the application.
#### Disadvantages of Kernel-Level Threads
1. **Higher Overhead**:
   - Context switching between threads involves kernel-level operations, which are slower than user-level thread switches.
   - Managing TCBs in the kernel adds complexity and consumes additional system resources.

2. **Less Flexibility**:
   - Applications have less control over thread scheduling and synchronization since these are managed by the OS.
   
**Example: Two-Level Scheduling in Action**
Imagine a process `P1` with three threads: `T1`, `T2`, and `T3`. Here's how the two-level scheduler works:

1. **Process-Level Scheduling**:
   - The process scheduler assigns `P1` a time quantum (e.g., 10ms).
   - If there are other processes (`P2`, `P3`), the scheduler switches between them after their respective time quanta.

2. **Thread-Level Scheduling**:
   - During `P1`'s time quantum, the thread-level scheduler selects one thread (`T1`, `T2`, or `T3`) to execute.
   - For example:
     - `T1` runs for 3ms and then yields.
     - `T2` runs for 4ms, and so on, until the time quantum for `P1` expires.

3. **Blocking Call Handling**:
   - If `T1` makes a blocking I/O call, the kernel immediately switches to another thread (e.g., `T2`) within the same process.
   - This prevents the process as a whole from being blocked.

![[Screenshot 2024-11-19 at 6.41.02 PM.png]]

