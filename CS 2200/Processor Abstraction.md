We need to know where processes are in memory. We introduce a **broker** which is a management for CPU accessing memory. 
![[Screenshot 2024-10-23 at 11.24.50 AM.png | 400]]
- Lower Bound and Upper Bound registers are used to store the bounds of a process. 
![[Screenshot 2024-10-23 at 11.25.30 AM.png |400]]
- every PCB has a lower and upper bound. 
- The limits of "bound registers" mechanism cannot relocate.
- The program cannot swap processes within these bounds

**Static Relocation**
- At assembly time, we lock-in memory addresses
- This gives poor memory utilization (ex. P1 can only be in memory between 1000 & 2000)
- The program must be loaded into the address range into which it was linked. There's no way we could move it later

**Dynamic Relocation**
- Dont hard code addresses in executable. Set memory bounds at load time rather than link time.
- This implies making all addresses relative to some base register or the PC
- LC-2200 code is not dynamically relocated able because LC2200 code cannot move once it's started to run
- To fix this, change the hardware and use an ADDER instead of a comparator

![[Screenshot 2024-10-23 at 11.37.57 AM.png]]
- If the CPU is in user state, add Base to address. If the address is less than limit, execute the operation. Therefore, the CPU will use the values from this "UB" and "LB"
- All P1 and P2 addresses appear to start at zero.
- This is the first instance of a virtual memory where process sees memory addresses different from physical addresses

*new PBC*
```
enum state_type {new, ready, running, waiting, halted};
typedef struct control_block_type {
	enum state_type state;
	address PC; // where to resume
	int reg_file[NUMREGS]; // register contents that's visible
	struct control_block *next_pcb;
	int priority; // extrinistic attribute 
	address BASE; // NEW
	address LIMIT; // NEW 
	
} control_block;
```

**Fixed Size Partition**
![[Screenshot 2024-10-23 at 11.54.16 AM.png | 400]]
- At boot, the size is determined. An allocation table is initialized as well.
![[Screenshot 2024-10-23 at 11.55.32 AM.png | 400]]
- Internal fragmentation = size of partition - actual used. In this example, it is 8k-6k.
- Lets say there is a process that takes 7K. However, there is no place to load it so it needs to wait
- Doesn't use memory efficiently - internal + external fragmentation.

![[Screenshot 2024-10-23 at 11.59.41 AM.png | 400]]

**External vs. Internal**
- Size of Partition - Actual Memory Used = Internal
- All non-contiguous free partitions. If there is only one free partition, we say that external fragmentation is zero 

**Variable Size Partitions**
![[Screenshot 2024-10-23 at 12.05.48 PM.png | 400]]
- Split the variable size. The partitions get created and released.
![[Screenshot 2024-10-23 at 1.03.50 PM.png | 400]]
- You cannot run P4 as it not continuous.

## Algorithms
- Reducing external fragmentation