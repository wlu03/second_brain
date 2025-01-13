Multithreading is a technique for a program to do multiple tasks, perhaps concurrently.
A *thread* is a similar to a process in that it represents an active unit of processing.
![[Screenshot 2024-11-14 at 2.45.18 PM.png | 450]]
Multithreading is attractive from the point of view of program modularity, opportunity for overlapping computation with I/O, and the potential for increased performance due to parallel processing.

## Creation/Termination of Thread 
___
In a C program, when you create a thread, you specify a function (referred to as the "top-level procedure") that will run as the main function of the new thread. This is essentially the "entry point" of the thread, meaning that the thread will start executing from this function. **Top-level procedure** is the name of the function that the thread will run when it starts. 
The syntax for creating a thread looks like this:`
`thread_create(top-level procedure, args);`

For example, suppose you want to create a thread to execute a function called `print_nums`. This function takes one argument, an int `n`. 
```
void print_nums(int n) {
	for (int i = 0; i < n; i++) {
		printf("%d\n", i);
	}
}
```
To create a thread to execute this function, call
`thread_create(print_nums, 10);`
The main program and this new thread will now run concurrently. 
![[Screenshot 2024-11-14 at 3.00.59 PM.png]]
When a program begins execution, the operating system creates a separate, isolated environment for it, known as the _address space_. This address space is unique to each process and provides a structured layout for the program's code and data. It serves as a “sandbox” — an isolated environment that separates the process’s memory space from those of other processes, preventing unintended access and ensuring stability across running programs.

The address space typically includes several key sections:
1. **Code (or Text) Section**: This part of the address space holds the executable instructions of the program. It is often marked as read-only to prevent accidental or malicious modification, ensuring that the instructions executed remain as intended.
2. **Global Data Section**: Here, global variables and static data are stored. These values are accessible throughout the lifetime of the program and are initialized once, retaining their state between function calls.
3. **Heap Section**: The heap is a dynamic memory area where memory can be allocated and freed during the program’s execution, supporting data structures like linked lists, trees, and other dynamic structures that require flexible memory management. Allocating and freeing memory in the heap is managed by calls like `malloc` and `free` in C, or `new` and `delete` in C++.
4. **Stack Section**: The stack supports function calls and local variable storage. Each time a function is called, a new _stack frame_ is created, containing the function’s local variables, parameters, and return address. Once the function completes, its stack frame is popped, and memory is reclaimed. The stack grows and shrinks as functions are called and returned, making it suitable for temporary, short-lived data.
For each process, this address space is unique and managed by the operating system, which also isolates it from other processes. This separation is crucial for security and stability: one process cannot directly access or modify another process's memory. This “sandbox” model allows processes to run independently, preventing one process from crashing or corrupting another.

When a process creates _child processes/thread_, each thread inherits an identical copy of the parent’s address space initially. This includes the same code, data, and stack layout, as if the child were a clone of the parent process. 

**Termination**: A thread is automatically terminated when it exits the top-level procedure that it started in. Using the exam, when it finishes `print_nums` with `n=10` then the thread will stop. Additionally, an explicit call can also terminate a thread for sure: `thread_terminate(tid)`. The `tid` is the system supplied identifier of the thread we wish to terminate. 

#### Example of Creating Thread
```
digitizer()
{
	// code
}
tracker()
{
	// code
}
main() 
{
	/* thread ids */
	thread_type digitizer_tid, tracker_tid;
	/* create digitizer and tracker thread */
	digitizer_tid = thread_create(digitizer, NULL);
	tracker_tid = thread_create(tracker, NULL);
	
}
```
### Memory Protection and Communication (amongst threads)
___
Memory Protection is a fundamental difference between thread and process. The operating system turns each program into a process, each with its own address space. However, threads execute within a single address space. Each thread is not protected from each other. 

Data structure that are visible to multiple threads within the scoping rules of the original program become shared data structures for the threads. Concretely, in a programming language such as C, the global data structures become shared data structures for the threads. 

**Read-Write Conflicts**
This condition is which multiple concurrent threads are simultaneously trying to access a shared variable with at least one of the threads trying to write to the shared variable. This can lead to inconsistent results if not managed properly

*Example*
Imagine a bank account system where multiple threads represent different ATM machines or online transactions accessing the same account balance. If two threads try to withdraw $50 from a $100 balance account at the same time both passing the condition. But the final balance ends up not accurate
```
balance = 100

def withdraw(amount):
    global balance

	## both thread pass condition at the same time
    if balance >= amount:
	    ## only one update is made thus the balance is equal to 50,
	    ## when its suppose to be 0.
        balance -= amount
        print(f"Withdrew {amount}, new balance is {balance}")
    else:
        print("Insufficient funds")

```

**Race Conditions**
Race condition is defined as the situation where a read-write conflict exists in a program without an intervening synchronization operation separating the conflict. These conditions could be intended/unintended. For example, if a shared variable is used for synchronization among threads, then there will be a race condition. However, such a race condition is an intended one.

*Example*
If both thread execute `increment()` simultaneously, the counter will end up being 2000 after both threads complete.
```
counter = 0

def increment():
    global counter
    for _ in range(1000):
        counter += 1

```

**Non-determinism**
This condition means that the program's execution can yield different results across runs, even with the same inputs.
```
def thread1():
    for _ in range(5):
        print("Thread 1")

def thread2():
    for _ in range(5):
        print("Thread 2")

## Printed
Thread 1
Thread 1
Thread 2
Thread 1
```
Depending on how the OS schedules the threads, the orders can be not how the programmer wants it. The order of execution of these threads is simply a function of the available number of processors in the computer, any dependency among the threads, and the scheduling algorithm used by the operating system. If there is 4 thread in a process on a uniprocessor, there will be 4! combinations of possible execution in a non-preemptive scheduler.

**Example**
Given the following threads and their execution history, what is the final value in memory location x? Assume that the execution of each instruction is atomic. Assume that $MEM[x] = 0$ initially.

```
Thread 1
Time 0: R1 <- MEM[x]
Time 2: R1 <- R1+2
Time 4: MEM[x] <- R1

Thread 2:
Time 1: R2 <- MEM[x]
Time 3: R2 <- R2+1
Time 5: MEM[x] <- R2

Answer:
0: R1 = 0
1: R2 = 0
2: R1 = 2
3: R2 = 1
4: MEM[x] = 2
5: MEM[X] = 1
The final mem value is 1.

```


## Execution Model
___
**Sequential Program:**
The program execution is deterministic, i.e., instructions execute in program order. The hardware implementation of the processor may reorder instructions for efficiency of pipelined execution so long as the appearance of program order is preserved despite such reordering.
**Parallel Program:**
The program execution is non-deterministic, i.e., instructions of each individual thread execute in program order. However, the instructions of the different threads of the same program may be arbitrarily interleaved.


## Mutual Exclusion Lock and Critical Selection
____
A program can declare any number of locks just as it declared variables. Only one thread can hold a particular lock at a time. Once a thread acquires a lock, other threads cannot get the same lock until the first thread *releases* the lock.
`mutex_lock_type mylock;`
The following call allows a thread to acquire and releases a particular lock:
`thread_mutex_lock (mylock);`
`thread_mutex_unlock (mylock);`

*Example*
```
item_type buffer;
mutex_lock_type buflock;

int producer()
{
	item type item;
	thread_mutex_lock(buflock);
		buffer = item;
	thread_mutex_unlock(buflock);
}
int consumer()
{
	item type item;
	thread_mutex_lock(buflock);
		item = buffer;
	thread_mutex_unlock(buflock);
}
main() 

Note: Buffer and Buflock are shared data structures. Item is a local variable within each thread.
```

A **critical section** is a portion of code that accesses shared resources and must be excuted excluseively by only one thread at a time controlled by locks.
![[Screenshot 2024-11-16 at 8.03.44 PM.png]]
- T1 is an **active** thread and **executing** inside its critical section 1 
- T2 is a **blocked** thread and **waiting** to get inside critical section 2
- T3 is an **active** thread and **executing** outside critical section 1
- T4 is an **active** thread and **executing** inside critical section 2

## Rendezvous
____
This is where threads synchronize their operations by waiting for one another at specific point of execution. The **main thread** spawns a **child thread** to perform a read operation asynchronously allowing the main thread to continue with other tasks concurrently. 

When the main thread completes it concurrent task, it needs to wait for the child thread to finish its file read. This is a good example where main may wait for its child to terminate which would be an indication that the file read is complete. The **rendezvous** can be called using: `thread_join (peer_thread_id)`. Upon the peer thread's termination, the calling thread resumes execution. This is a good way for thread in parallel program to coordinate their activities with respect to one another in the presence of the non-deterministic execution model.  
*Example*
```
int foo (int n) 
{
	return 0;
}

int main ()
{
	int f;
	thread_type child_tid;
	child_tid = thread_create(foo, &f);
	thread_join(child_tid);
}
```

Here is how a thread is internally represented:
- **T1**: Acquires `thread_mutex_lock(L1)`.
- **T2**: Attempts to acquire `thread_mutex_lock(L1)` (same lock as T1).
- **T3**: Acquires `thread_mutex_lock(L2)`.
- **T4**: Attempts to acquire `thread_mutex_lock(L2)` (same lock as T3).
- **T5**: Attempts to acquire `thread_mutex_lock(L1)` (same lock as T1 and T2).
![[Screenshot 2024-11-16 at 8.36.46 PM.png]]
*Although thread_type and mutex_lock_type are opaque data types, the threads library has accounting information regarding the variable. It will know if a process is holding onto a thread, and the queue of waiting requestors for the lock. For the example above, the lock variable L is holding onto thread 1 while waiting on thread 2 & 3*. 

## Deadlocks
___
Deadlock is when a thread is waiting for an event that will never happen. Thus both threads are stuck. Livestock is the situation wherein a thread is actively checking for an event that will never happen.


## Conditional Variables
___
A condition variable is a synchronization primitive that allows threads to wait until a certain condition is true. It enables one thread to signal other threads that a specific condition has been met. 

**Declaration**: `cond_var_type buf_not_empty;`
- Declares a condition variable `buf_not_empty` which will be used to synchronize other methods

There are calls that allows threads to wait and signal to one another using the condition variables
- `thread_cond_wait(conditional_varaible, lock_variable);`
	- Makes thread wait until the condition is satisfied. 
	- Unlocks the mutual exclusion lock to allow other threads to work
	- Deschedules itself
	- When another thread signals the condition (`thread_cond_signal()`), the waiting thread reacquires t he lock and resumes where it left off
- `thread_cond_signal(conditional_varaible);`
	- Send signal to any thread that is waiting on the condition variable
	- If no thread are waiting, this signal is ignored. 
	- If there are multiple threads waiting, one is chosen in FSFC
![[Screenshot 2024-11-16 at 9.27.18 PM.png]]

*Example*
Write a function wait_for_buddy() to be used by EXACTLY 2 threads to rendezvous with each other as shown in the figure below. The order of arrival of the two thread should be immaterial. Note that this is a general example of accomplishing a rendezvous among independent threads of the same process.
![[Screenshot 2024-11-16 at 9.29.34 PM.png | 400]]
*Solution*
```
boolean buddy_waiting = FALSE;
mutex_lock_type mtx;
cond_var_type cond;

wait_for_buddy()
{
	/* both executes the lock state */
	thread_mutex_lock(mtx);

	if (buddy_waiting == FALSE) {
		// First arrives executes this block
		buddy_waiting = TRUE;
		thread_cond_wait (cond, mtx);


		// First thread wakes up from signal of second thread 
		thread_cond_signal(cond);
	} else {
		buddy_waiting = FALSE;
		thread_cond_signal (cond);
		thread_cond_wait (cond, mtx);
	
	}
	thread_mutex_unlock (mtx);
}
```
- if `buddy_waiting = FALSE;` (first thread), it sets `buddy_waiting = TRUE;` to signal that it is waiting for the second thread.
- It **waits** on the condition variable. This releases the lock and puts the thread to sleep until second thread signals it. 
- When second thread arrives, it sees that it's true so go to ELSE block. It sets `buddy_waiting = FALSE;` to signal that the condition is met. It signals to the first thread to wake up. Then it waits itself allowing the first thread to signal back.
- After both threads are awake unlock mutex. 

### Internal Representation of Condition Variable
A variable of `cond_var_type` has:
- a queue of threads waiting for the signal on the variable
- for each thread there is an associated mutex lock

A thread that calls `thread_cond_wait` names a mutex lock. 

**Thread Behavior**:
   - **`T3`**: Calls `thread_cond_wait(C, L1)`:
     - This means `T3` will wait on condition variable `C` and release lock `L1` while waiting.
   - **`T4`**: Calls `thread_cond_wait(C, L2)`:
     - Similarly, `T4` waits on the same condition variable `C` and releases lock `L2`.

2. **Internal Representation**:
   - After both threads execute their respective `thread_cond_wait` calls, the internal state of `C` will reflect both `T3` and `T4` as waiting threads.
   - The condition variable `C` keeps track of all threads currently waiting on it.
![[Screenshot 2024-11-16 at 9.40.14 PM.png]]


*Example*
Assume that the following events happen in the order shown (T1-T7 are threads of the same process):
```
T1 executes thread_mutex_lock(L1);  
T2 executes thread_cond_wait(C1, L1); 
T3 executes thread_mutex_lock(L2);  
T4 executes thread_cond_wait(C2, L2); 
T5 executes thread_cond_wait(C1, L2);
```
(a) Assuming there has been no other calls to the threads library prior to this, show the state of the internal queues in the threads library after the above five calls.
```
T6 executes thread_cond_signal(C1);
T7 executes thread_cond_signal(C2);
```
![[Screenshot 2024-11-16 at 9.46.03 PM.png | 400]] 
Subsequently the following event happens:
(b) Show the state of the internal queues in the threads library after these two calls.
![[Screenshot 2024-11-16 at 9.46.46 PM.png | 400]]
*The library moves T2 from the waiting queue of L1 and T4 on the waiting queue on L2.*


## While vs If Statements
The change from an **`if` statement** to a **`while` statement** in the program fixes potential synchronization issues by ensuring that the thread rechecks the **predicate condition** (in this case, `res_state == NOT_BUSY`) after being signaled. This is necessary because:

### **Why Use a `while` Instead of `if`?**
**Spurious Wake-Ups**:
   - In multithreaded programming, **spurious wake-ups** can occur. This means a thread waiting on a condition variable may be awakened without a corresponding signal or broadcast from another thread.
   - If an `if` statement is used, the thread would incorrectly assume the condition is satisfied and proceed, potentially leading to inconsistent behavior.
   - Using a `while` loop ensures that the thread goes back to waiting on the condition variable if the predicate is still not true.
   **Race Conditions**:
   - After a thread is signaled and resumes, other threads might have already acquired the resource before the current thread gets a chance to execute. This creates a **race condition** where the predicate (e.g., `res_state == NOT_BUSY`) might no longer be true.
   - With a `while` loop, the thread rechecks the predicate, ensuring that it does not proceed unless the condition is actually met.

**Predicate Rechecking**:
   - A condition variable only provides a signal that the state of the system **might have changed**. It does not guarantee that the predicate (e.g., `res_state == NOT_BUSY`) is true when the thread resumes.
   - The `while` loop forces the thread to re-evaluate the predicate and block again if necessary.

#### Original Code with `if`:
```c
if (res_state == BUSY) {
    thread_cond_wait(res_not_busy, cs_mutex);
}
res_state = BUSY;
```

#### Fixed Code with `while`:
```c
while (res_state == BUSY) {
    thread_cond_wait(res_not_busy, cs_mutex);
}
res_state = BUSY;
```

### **How Does the `while` Fix the Problem?**

1. **Thread Safety**:
   - The `while` loop ensures that even if a thread is spuriously awakened or loses the race to acquire the resource after being signaled, it will block again until the resource is genuinely available.

2. **Proper Synchronization**:
   - The shared state (`res_state`) is protected from incorrect assumptions. The thread only proceeds if the condition (`res_state == NOT_BUSY`) is actually satisfied.

3. **Robustness**:
   - This change makes the program **robust** against unexpected behaviors like spurious wake-ups or other threads modifying the state while a thread is waiting.

## How is Multithreading Used?
____
File servers, mail servers, and web servers execute on multiprocessors. A dispatcher model is used such that a dispatcher thread dispatches requests as they come in to one of a pool of worker threads. Upon completion of the request, the worker thread returns to the free pool. The request queue serves to smooth traffic when a burst of request exceeds server capacity. 

## pthread
___
It's short for POSIX threads, a threading library defined by Portable Operating System Interface. It provides an API for creating/managing threads as well as synchronization primitives. 


