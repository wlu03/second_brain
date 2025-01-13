Virtual Address is mapped using a broker to physical address. The OS sets it up. The hardware on every assess looks at it. How big is this page table. A bigger page gets more internal fragmentation. Smaller pages gets us a bigger page table and take more CPU time to manage. Demand Paging also has internal fragmentation.

# Page Size
___
If the page size $2^n$ the lower n bits are the offset and bit $n$ and up the are the virtual page number.

Example. We have a 4KB page size and a 32-bit virtual address space. 4KB is $2^{12}$ so the bottom 12 bits are the offset and the remaining 20 bits are the VPN (32-12=20). ![[Screenshot 2024-10-23 at 2.06.52 PM.png | 400]]
ex. For the virtual address 0x00004FFF, the VPN is 4 and the offset is 4095 (FFF = 4095)

**Address Translation**
![[Screenshot 2024-10-23 at 2.11.39 PM.png | 400]]
![[Screenshot 2024-10-23 at 2.15.32 PM.png | 500]]

**Example 1.**
Consider a memory system with 32-bit virtual addresses and 24-bit physical memory addresses. Assume that the pagesize is 4K Bytes. 
How many page frames can be in memory?
	PFN bits = $24 - 12 = 12, 2^{12} \space \text{hoFrames}$
How big is the page table?
	VPN bits = $32-12=20,2^{20} \space \text{Entries}$

**Example 2.**
You have a memory system with 16-bit virtual and physical addresses and a 1K page size. The entries in the current page table are 0->0x14, 1->0x18, 2->0x08, 3->0x01. 
What is the physical address that virtual address 0x4ED?
	VPN Bit = $16-10=6 \space \text{bits}, 10 \space \text{offset bits}$
	Virtual Address = 0x4ED, VPN = 0x01, Offset = 0x0ED
	(0000 01 | 00 1110 1101), the VPN bit is split at 6, thus VPN is 0x01.
	PFN=0x18, offset= 0x0ED
	(011000 | 0011101101)
	(0110 0000 1110 1101) 
	The physical address is 0x60ED
![[Screenshot 2024-10-23 at 3.06.47 PM.png]]

- The page table is in the broker and it's in physical memory.
- [[PTBR]] holds the base physical address of the page table for the currently running process. 
- We need broker hardware to lookup the PFN from the page table for each memory reference. PTBR is base the VPN is the index.

![[Screenshot 2024-10-23 at 3.16.24 PM.png]]
- Each entry is called a PTE (Page Table Entry)
- If the page is not in memory, the hardware raises a page fault exceptions which traps to the page fault handler in the OS. 
- The page fault hits us at MEM as it tries to access data. 

**Page Fault**
- Find a free page frame
- Load the faulting virtual page from seondary storage into the page frame (slow)
- Give up the CPU while waiting for the paging I/O to complete
- Update the page table entry for the faulting page 
- Link the PCB of the process back in the ready_q of the scheduler
- Call the scheduler

![[Screenshot 2024-10-23 at 3.22.58 PM.png]]
*array for each page frame*
- The number of entries in the frame table is the same as the number of physical memory page frames
- Use a linked list for the frame table.
- Finding pages on secondary storage on the disk map

![[Screenshot 2024-10-23 at 3.38.08 PM.png | 300]]
![[Screenshot 2024-10-23 at 3.39.33 PM.png | 400]]

| Per         | Data Structure         | Description                                                                                                                   |
| ----------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Per Process | PCB                    | Holds saved PTBR register (hardware defined)                                                                                  |
| Per Process | Page Table             | VPN->PFN mapping (hardware defined).  Memory manager uses it for setup. Hardware uses on each memory access. Stored in memory |
| Per System  | Free List / Linked Lis | Free page frames in physical memory (software defined)                                                                        |
| Per System  | Frame Table            | PFN to <PID, VPN> mapping needed for evicting pages from physical memory (software defined)                                   |
| Per Process | Disk Map               | VPN to disk block mapping needed for bringing missing pages from disk to physical memory (software defined)                   |
```
enum state_type {new, ready, running, waiting, halted};
typedef struct control_block_type {
	enum state_type state;
	address PC; // where to resume
	int reg_file[NUMREGS]; // register contents that's visible
	struct control_block *next_pcb;
	int priority; // extrinistic attribute 
	address PTBR;
	disk_address *disk_map;
	
} control_block;
```

**Example**
- Process P1 page fault at VPN = 20
- Free List is empty
- Select page frame PFN = 52 as victim
- Frame currently houses VPN = 33 of process P4
![[Screenshot 2024-10-23 at 3.47.39 PM.png | 400]]

![[Screenshot 2024-10-23 at 3.49.07 PM.png | 400]]


# Page Replacement Algorithms
___
## FIFO 
___
![[Screenshot 2024-10-23 at 3.57.43 PM.png | 400]]
- Replace the oldest page that you have
![[Screenshot 2024-10-23 at 3.59.39 PM.png | 400]]
ex. 
![[Screenshot 2024-10-23 at 4.02.23 PM.png]]
- Once reference number 7 comes, 0 comes back again. This is not optimal 

## LRU
___
- Least recently used is a good predictor of future behavior
![[Screenshot 2024-10-23 at 4.12.54 PM.png]]
- Problems: Memory references are known to the hardware, but the memory management (victim selection) is in the software. One possibility is to make the stack shared by the HW and SW. Implement stack in hardware and let hardware update stack on each reference. Let software (OS) use this stack as data structure
- However, this is doesn't work because the size of the stack is the number of page frames and a memory write is required for each memory reference. 
![[Screenshot 2024-10-23 at 4.17.29 PM.png | 700 ]]
- Look at the page with the counter that has the lowest value

## Second Chance w/ Reference
____
1. Initially clear all the referenced bits
2. As the process runs, set reference bits on each page referenced 
3. If a page has to be evicted, the memory manager selects a page in a FIFO manner
4. If the chosen victim's referenced bit is set the manager clears the referenced bit and moves on to the next page
5. The victim is the first page that doesn't have the referenced bit set


## Page Table Entry Example 
___
![[Screenshot 2024-10-23 at 4.31.16 PM.png]]
- Dirty Bit is a flag that indicates whether a page in memory has been **written to** since it was loaded from the disk. If the dirty bit is unset, the page data is the same as what is stored on disk. If the page is written to while in memory, the OS sets the dirty bit to 1. It tells the system that if the page needs to be replace from memory, it must be written back to disk to save the changes. 

## Translation Lookaside Buffer (TLB) 
____
- Used to improve the performance of the virtual memory by speeding up the translation of virtual to physical addresses. Without a TLB, every virtual memory access would require a page table look up which involves assessing memory and slows down the system. If the translation is found, the physical address can be obtained quickly. It reduced NOP within a pipeline. It's very expensive and associated. It's not addressed by physical location, its addressed by contents of its row. ![[Screenshot 2024-10-23 at 4.58.11 PM.png]]
Kernel can only access the TLB flush instruction.

## Thrashing
___
![[Screenshot 2024-10-23 at 5.01.53 PM.png]]

## Memory Pressure
____
![[Screenshot 2024-10-23 at 5.04.11 PM.png]]
**Ex**. 
During the time interval t1 - t2, the following virtual page accesses are recorded for  
the three processes P1, P2, and P3, respectively.  

P1: 0, 10, 1, 0, 1, 2, 10, 2, 1, 1, 0  
P2: 0, 100, 101, 102, 103, 0, 101, 102, 104  
P3: 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5  

What is the working set for each of the processes
	P1 = {0, 1, 2, 10}, |P1| = 4
	P2 = {0, 100, 101, 102, 103, 104}, |P2| = 6
	P3 = {0, 1, 2, 3, 4, 5}, |P3| = 6
What is the cumulative memory pressure on the system.
	4+6+6=16 page frames