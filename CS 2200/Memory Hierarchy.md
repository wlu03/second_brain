In a page memory system, it takes **two memory assess** for every instruction (access PTE and access instr). 
- **Page Table Access**: The CPU first accesses the page table to translate the virtual address to physical address
- **Memory Assess**: The CPU assesses memory to retrieve the instruction or data

**TLB** saves this for only one memory access (PC -> TLB -> Memory). TLB cache recent virtual to physical translations. If the TLB has required address translation (TLB hit), the CPU doesn't need to access the page table eliminating one memory access. 

The CPU clock cycle speed is ~1ns while memory assess time is ~100ns. This means our pipeline is getting a 100:1 ratio (99 bubbles).

The TLB operates on the principle of **spatial** and **temporal locality** which speeds up the translation of virtual addresses to physical addresses. Instruction are sequential within the program. Recent translation are stashed away from in-memory page tables into high-speed hardware. Subsequent translations become fast (no ned to go to memory for PTE). 
- **Spatial**: Refers to the high probability of a program accessing **adjacent** memory locations
- **Temporal**: Refers to the high probability of a program accessing in the near future, the **same memory** location that it is accessing currently. 

## SRAM and DRAM
___
**SRAM (Static RAM)** 
- SRAM stores data using a flip-flop circuit. It's static. It's fast compared to the DRAM. 
- TLB + Register (Reg File) -> SRAM
- 6 Transistor per cell, Faster, Bulkier

**DRAM (Dynamic RAM)** 
- Stores data using a single transistor. It keeps DRAM needs to be refreshed.
- DRAM is slower than SRAM due to the need for periodic refreshing and slower access times of its simpler structure
- 1 Transistor per cell, Slower, Denser
## Terminologies

| Terms                               | Description              | more. |
| ----------------------------------- | ------------------------ | ----- |
| Hit                                 | Hit ratio $h$            | h+m=1 |
| Miss                                | Miss ratio $m$           |       |
| Cycle Time                          | $T_c$ cache access time  |       |
|                                     | $T_m$ memory access time |       |
| Memory Access Time                  | Same for SRAM            |       |
| Memory Cycle Time                   | Different for DRAM       |       |
| Miss Penality                       | $T_m$                    |       |
| Effective memory access time (EMAT) | $EMAT=T_c+T_m*m$         |       |

![[Screenshot 2024-11-05 at 12.42.06 AM.png | 500]]
- L1 Cache is closest to CPU, it provides fast assess to data and instructions
- L2 Cache is the second layer to store data not found in L1 cache. Slower and larger than L1.![[Screenshot 2024-11-05 at 12.45.14 AM.png | 450]]
## Cache Organizations
____
### Direct Mapped
![[Screenshot 2024-11-05 at 12.55.44 AM.png | 400]] 
- 3-bit cache index means that there is $2^3$ cache values.
- Since its a 4-bit memory address, there can be a possible $2^4=16$ unique addresses ranging from 0 to 15.
- Since we have 1 tag bit, there are $2^1=2$ possible values for the tag, 0 or 1. 
- For example, the address `0000` will map to 0 in the main memory and `1000` will map to 8.
**Misses** 
- **Compulsory**: First Time a block is brought into the cache or data is accessed. Since the cache has never seen this data before, it must load the data from main memory. Can be reduced through prefetching
- **Capacity**: The cache is completely full. There is not enough space to store additional data. Old entries must be evicted to make room for new data. Minimized using set-associative caches
- **Conflict**: Multiple memory addresses map to the same cache index, leading to eviction even though the cache is not full. Addressed by increasing cache size or better memory management
- Compulsory > Capacity > Conflict
	- Checked in this order for what miss it is.
- Conflict misses would not occur if the cache were fully associate with LRU replacement.
- Fully associated cache can't have conflict misses by definition.

**Example Question**
You have a 64 entry direct-mapped cache for a memory with 16-bit addresses and 16-bit words. 
- There will always be a **1 bit valid flag**
- $\log_2(64)=6$ bits index to represent 64 entries
- Each word is 16 bits therefore we assume that one word is stored in each cache entry (**16 bit data**)
- We used 6 bits for the index, so the remaining bits will be used for the tag (**Tag Bits = 16 (total address bits) - 6 (index bits) = 10 bits**)

![[Screenshot 2024-11-05 at 1.09.27 AM.png | 400]]
*compulsory example*
![[Screenshot 2024-11-05 at 1.09.52 AM.png  | 400]]
*another compulsory example*
![[Screenshot 2024-11-05 at 1.10.13 AM.png | 400]]
*conflict example*
![[Screenshot 2024-11-05 at 1.40.21 AM.png | 450]]
*how to replace using index*
![[Screenshot 2024-11-05 at 1.54.39 AM.png | 400]]
*using the tag*
![[Screenshot 2024-11-05 at 1.56.10 AM.png  | 400 ]] 
*valid tag to know if it's trash that can be replaced*

## Example
Let us consider the design of a direct mapped cache for a realistic memory system. Assume that the CPU generates a 32-bit byte addressable memory address. Each memory word contains 4 bytes. A memory access brings a full word into the cache. The direct-mapped cache is 64K bytes in size (this is the amount of data that can be stored in the cache) with each cache entry containing one word of data. Compute additional storage space needed for the valid bits and the tag fields of the cache. 

To calculate the additional storage space needed for the valid bits and tag fields in a direct-mapped cache, we break down the details as follows:

1. **Cache Size and Structure**:
   - The cache size is 64 KB (64,000 bytes).
   - Each memory word contains 4 bytes.
   - This means each cache entry holds one word (4 bytes) of data.

2. **Number of Cache Entries**:
   - Since each entry contains 4 bytes, the number of entries in the cache is calculated by dividing the cache size by the size of each entry:
	    $$\text{Number of entries} = \frac{64,000 \text{ bytes}}{4 \text{ bytes per entry}} = 16,384 \text{ entries} = 2^{14} \text{ entries}$$

3. **Index and Tag Fields**:
   - The memory address is 32 bits (since it’s a 32-bit addressable memory).
   - The cache is direct-mapped, so each memory location can only map to one specific cache line, determined by the index.
   - Since there are $2^{14}$ entries, the index field requires 14 bits.

4. **Tag Field**:
   - The remaining bits in the address are used for the tag. 
   - Since we have a 32-bit address and we use 14 bits for the index and 2 bits for the byte offset (to address each byte in a 4-byte word), the remaining bits for the tag are:
     $$\text{Tag bit} = 32 - 14 - 2 = 16 \text{ bits}$$

5. **Valid Bit**:
   - Each cache entry also requires a 1-bit valid bit to indicate if the data in the entry is valid.

6. **Additional Storage Calculation**:
   - For each cache entry, we need 1 valid bit and 16 tag bits.
   - So, the additional storage per entry is \(1 + 16 = 17\) bits.
   - For $2^{14}$ entries, the total additional storage needed is:
     $$17 \text{ bits} \times 2^{14} = 278,528 \text{ bits}$$
   - Converting to bytes:
     $$ \frac{278,528 \text{ bits}}{8} = 34,816 \text{ bytes}$$
Therefore, the additional storage required for the valid bits and tag fields is 34,816 bytes.

## How Does Cache work w/ CPU
![[Screenshot 2024-11-05 at 2.46.57 PM.png]]
- Dirty Bit:
	- **Purpose**: Indicates whether the data in the cache line has been modified (written to) and is different from the corresponding data in main memory.
	- **Explanation**: In write-back caches, data is only written back to main memory when it is evicted. If the dirty bit is set (1), it means the cache contains modified data that needs to be written back to memory before eviction. If the dirty bit is not set (0), the data in the cache matches the data in memory, so no write-back is needed. This optimizes performance by reducing unnecessary writes to main memory.

# Metrics w/ Cache

$CPI_{eff}=CPI_{avg} + \text{memory-stalls}_{avg}$
$\text{cycles per instruction or CPI}_{avg} = \text{miss rate} * \text{miss penalty}$
$\text{Execution Time} = N * CPI_{eff} * \text{cycle time}$
$\text{Execution Time} = N * (CPI_{avg}+ \text{memory-stalls}_{avg}) * \text{cycle time}$
$\text{memory-stalls}_{avg} = \text{misses per instruction}_{avg} * \text{miss-penalty}_{avg}$
$\text{Total Memory Stalls}= N*\text{memory-stalls}_{avg}$

**Example**
Find the effective CPI of the processor accounting for memory stalls.
- **Initial CPI (without stalls)** = 1.8
- **Instruction Cache (I-Cache)**:
    - Hit rate = 95%
    - Miss rate = 5% (since miss rate = 1 - hit rate)
- **Data Cache (D-Cache)**:
    - Hit rate = 98%
    - Miss rate = 2% (since miss rate = 1 - hit rate)
- **Memory reference instructions**:
    - 30% of all instructions
    - 80% are loads, 20% are stores
- **Miss Penalties**:
    - Read-miss penalty = 20 cycles
    - Write-miss penalty = 5 cycles

*Solution*
1. I-Cache Miss Penalty
	- 5% miss rate
	- miss penalty for instruction cache = 20 cycles
	- 1 cycle per instruction
2. D-Cache Miss Penalty (for Loads)
	- Load miss rate = 2%
	- Load miss penalty = 20 cycles
	- 30% of instructions were 80% are loads, load frequency is 24%
	- Load miss cycle per instruction = load frequency * miss rate * miss penalty = 0.
	- 0.24 x 0.02 x 20 = 0.096 cycles per instruction
3. D-Cache Miss Penalty (for Stores) 
	- Store miss rate = 2%
	- Store miss penalty = 5 cycles
	- of the 30% of instruction, 20% are stores, store frequency is 6%
	- stores miss stall cycles per instruction = store frequency * miss rate * miss penalty 
	- 0.06 x 0.02 x 5 = 0.006 cycles per instruction
4. Total Stall Cycles per instruction
	- 1 + 0.096 + 0.006 = 1.102 cycles per instruction
5. Effective CPI = Average CPI + memory stalls
	2.902 = 1.8+1.102

## Interpreting Memory Address
S = size of cache, B = block size, L = lines in cache

| cache tag | cache index | block offset |
| --------- | ----------- | ------------ |
| t         | n           | b            |
- $b = log_2(B)$
- $L = S/B$
- $n = log_2(L)$
- $t=a-(b+n)$

## Multi-word Cache Organization Example
Direct-mapped cache
- 32-bit byte addressable memory address
- Each memory word contains 4 bytes
- Block size = 4 words (16 bytes)
- A memory access brings a block
- 64k Bytes cache
- Write back cache with dirty bit per word
*Solution*
- block offset = $log_2(16)=4$ block offset
- Number of cache lines = 64k Byte / 16 Block Size = 4,000 lines/blocks
- The number of bits needed to represent 4000 lines/blocks is $log_2(4000)=12$ bits. Therefore the index is 12 bits
- The tag is just the remainder so $32-12-4=16$ bits of tag

![[Screenshot 2024-11-05 at 3.35.59 PM.png | 400]]
![[Screenshot 2024-11-05 at 3.48.26 PM.png | 400]]

## Fully Associated Mapping
Allow any memory block to be brought into any cache block. This is similar to be able to bring in a virtual page into any available physical page frame. 

For address interpretation, we don't need to split memory address index and tag. It just all becomes a tag 

**Before**: $[\text{ Cache Tag } | \text{ Index }]$
**After**: $[\text{ Cache Tag }]$ 
![[Screenshot 2024-11-05 at 3.51.15 PM.png]]
*make a comparator per tag whichever hits is the one where we get the data. this is typically how you build TLB. every expensive, but fast*

## Set-Associated Cache
Turns out direct-mapped and fully-associative caches are degenerate cases of a set-associative cache! There is only one cache organization.

Certainly! Here’s an explanation of **set-associative**, **fully associative**, and **direct-mapped** cache mapping techniques, along with their key differences.

#### Direct-Mapped Cache
- **Mapping:** Each block of memory maps to **exactly one line in the cache**.
- **Mechanism:** A memory block is placed in a specific cache line determined by the formula:
  $\text{cache line} = (\text{memory block address}) \mod (\text{number of lines in the cache})$
- **Advantages:** Simple, fast to access, and uses less complex hardware.
- **Disadvantages:** High chance of **cache conflicts** if multiple memory blocks map to the same line, which can lead to higher miss rates.

**Example:** If the cache has 8 lines, a memory block with address 16 will always map to line 0, address 17 to line 1, and so on.

#### Fully Associative Cache
- **Mapping:** A memory block can be placed **in any line of the cache**.
- **Mechanism:** When the CPU requests data, the cache is searched to see if any line contains the requested data. This search is typically done with a Content Addressable Memory (CAM) or a fully associative search mechanism.
- **Advantages:** **No mapping conflicts** since any block can go anywhere, leading to fewer cache misses due to conflicts.
- **Disadvantages:** Requires complex and expensive hardware to check every line in the cache, which can slow down access time for larger caches.

**Example:** In an 8-line fully associative cache, a memory block with address 16 could be placed in any of the 8 lines.

#### Set-Associative Cache
- **Comparator**: For $n$ sets, there is always $n$ t-bit tag comparators
- **Mapping:** A hybrid approach that provides a compromise between direct-mapped and fully associative caches. Here, the cache is divided into a number of **sets**. Each memory block maps to a specific set, but within that set, it can occupy **any of the lines** (or "ways").
- **Mechanism:** A memory block’s address determines which set it maps to. Once mapped to a set, it can be placed in any line within that set. For example, in a **4-way set-associative cache** with 16 lines, there would be 4 sets (each set containing 4 lines).
- **Advantages:** Reduces cache conflicts compared to direct-mapped caches while being more efficient in terms of hardware complexity than fully associative caches.
- **Disadvantages:** Although it reduces conflicts, it is still not as flexible as a fully associative cache. The complexity also increases with the number of ways per set.

**Example:** In an 8-line cache that is 2-way set-associative, there are 4 sets, each with 2 lines (ways). A memory block might map to set 1, where it can go into either of the 2 lines within that set.

### Comparison Summary

| Mapping Type           | Placement Flexibility                   | Hardware Complexity                  | Cache Conflicts |
|------------------------|-----------------------------------------|--------------------------------------|------------------|
| **Direct-Mapped**      | Each block maps to a single cache line  | Low – easy to locate specific line   | High            |
| **Fully Associative**  | Any block can go into any line          | High – searches entire cache         | Minimal         |
| **Set-Associative**    | Each block maps to a specific set,      | Medium – searches only within set    | Moderate        |
|                        | and can go into any line within the set |                                      |                  |

### Choosing Among the Three
- **Direct-Mapped** is chosen for simplicity and low-cost applications but has higher chances of conflicts.
- **Fully Associative** is ideal when avoiding cache conflicts is critical, but it requires more complex hardware, which is usually more practical for small caches (like L1).
- **Set-Associative** provides a balanced approach, offering flexibility with lower complexity than fully associative and fewer conflicts than direct-mapped. It is commonly used in L2 and L3 caches.

A cache set is a row in the cache. The number of blocks per set is determined by the type of cache
- Direct Mapped: $n$ sets, 1 element
- P-way set associative: $n/p$ sets, $p$ elements
- Fully associative: 1 set, $n$ elements
![[Screenshot 2024-11-05 at 4.18.56 PM.png]]
*four way set associated cache setup*
### Four way Set Associated Cache Example
You're given the following
- 4 way set associative cache
- 32-bit memory, byte-addressable
- Cache size of 64k Bytes
- Each memory word contains 4 bytes
- Cache block size is 16 bytes
- Write through policy
- One valid bit per block
Compute the total amount of storage for implementing the cache (actual data and meta data)

*Solution*
- Number of total cache lines $64k/16 = 4096 lines$. Because there is 4 set caches, you need to divide by 4. Therefore, there is $4096/4=1024$ cache lines per set.
- To represent $1k$ lines, you need $log_2(1024)=10$ bits. This is the index. 
- The offset is 4 because $log_2(16)=4$ bits. Since the block size is 16 bytes, you need unique identify each byte within the block.
- Since it's 32bit byte addressable, then you take the rest which is $32-10-4=18$ bits for the tag.

- Meta-Data
	- Tag is 18 bits
	- Data = 128 (16 * 8) -> 16 bytes * (8 bits per byte) = 128 bits. 16 bytes comes from $2^{\text{number of offset bits}}$
	- Valid bit is 1 bit

- Total Amount of Storage
	- (1 (valid bit) + 18 (tag bits) + 128 (data bits) * 1K (cache line) * 4 (4 sets)) / 8 (to get bytes) = 75,264 bytes

**Cache Setup**
- **Cache Size**: 64 KB (65,536 bytes).
- **Cache Block (Line) Size**: 16 bytes.
- **Associativity**: 4-way set associative.
  
Based on this setup:
- **Total Cache Lines**: $\frac{65,536 \text{ bytes}}{16 \text{ bytes per line}} = 4096$ lines.
- **Number of Sets**: $\frac{4096 \text{ lines}}{4} = 1024$ sets.
  
**Address Breakdown**
Assume a **32-bit memory address**. We’ll divide it into **tag**, **index**, and **offset** bits.

1. **Offset**: 4 bits are needed to address each byte in a 16-byte block $2^4 = 16$.
2. **Index**: 10 bits are needed to address the 1024 sets $2^{10} = 1024$.
3. **Tag**: The remaining 18 bits will serve as the tag.

**Example Memory Address**
Suppose we want to access data at the memory address:
```
0xAF26D15C
```
In binary, this address is:
```
10101111001001101101000101011100
```

Using the breakdown:
- **Tag**: First 18 bits → `101011110010011011`
- **Index**: Next 10 bits → `0100010101`
- **Offset**: Last 4 bits → `1100`

 **Step-by-Step Cache Access Process**

1. **Index Lookup**:
   - The **index** (`0100010101` in binary) corresponds to set **277** in decimal. So, we’ll look at **set 277** in the cache.

2. **Tag Comparison**:
   - In set 277, there are 4 cache lines (because it’s a 4-way set associative cache).
   - Each cache line in set 277 will store a tag along with the data.
   - The **tag** we’re looking for is `101011110010011011`.
   - The cache controller will compare this tag with the tags stored in each of the 4 lines in set 277.

   **Possible Outcomes**:
   - **Cache Hit**: If one of the lines in set 277 has a matching tag (`101011110010011011`), we have a cache hit, meaning the requested data is in the cache.
   - **Cache Miss**: If none of the lines in set 277 have this tag, it’s a cache miss, and the requested data must be fetched from main memory and loaded into one of the lines in set 277.

3. **Offset Usage**:
   - If there is a cache hit, the **offset** (`1100` in binary, or 12 in decimal) tells us to go to the 12th byte within the matched 16-byte block.
   - This offset allows us to retrieve exactly the data byte (or word) we need within that block.


## Cache Replacement Policy
____
If we had 2-way set associative cache, how many LRU bits would we need? You would just need one because you can set LRU bit to 0/1 if we read from cache 0 or cache 1. 

**Context Switch**
- *TLB*: You must flush user entries
- *Cache*: Nothing. This is because we are using physical addresses. 
	- If the OS brings a page from disk directly to a physical page frame and bypasses the cache, it must flush any cache locations for the previous contents. 
	- If the cache holds virtual addresses, then flushing cache entries form the page is required. This is because each process has its own virtual addresses.

### Putting Cache and VM
___
**Before**: 
![[Screenshot 2024-11-05 at 7.30.20 PM.png | 500]]
**After**: 
- The page offset is the same in both VA and PA. We if we arrange the index + block offset the same as the page offset. 
- We can give the Cache to access without waiting for the TLB
- This was TLB and Cache access in **parallel**
![[Screenshot 2024-11-05 at 7.38.45 PM.png]]

## Page Coloring
![[Screenshot 2024-11-05 at 7.47.31 PM.png | 400]]
- the 4 bits have the be the same from VPN and PFN. The page frame must be divided into 16 different color. The page replacement can only choose the same color, but we can have a bigger cache. 
- The low bits of the VPN and PFN to be identical. This allows the use of these bits are part of either VA or PA
- A virtual page can only occupy a subset of page frames in which the low bits of the VPN match the low bits of the PFN. 
- Page coloring which means the page replacement algorithms keep track of the "color" of the VPNs and PFNs to ensure virtual pages are only loaded into like-color page frames
- This makes processes tend to use contingous pages so the VPNs of the ages are spread evenly among the colors

**Example (from HW8)**
Page coloring is used to make sure that a few least significant bits of the virtual page number (VPN) and physical frame number (PFN) remain unchanged during address translation.

Imagine the following memory hierarchy:
- 64-bit virtual address
- 32-bit physical address
- Virtually-indexed, physically-tagged, 8-way set associative cache
- Page size of 4 KB
- Memory is byte-addressable
- Total Cache Size of 2 MB
- Cache block size of 128 bytes
Assume K = 1024 and M = 1024 * 1024.

*Solution*
- Page Size = 4KB, $log_2(4096)=12 \text{ bits}$ page offset
- $64-12=52 \text{ VPN Bits}$ 
- $32-12=20 \text{ PFN Bits}$ 
- 8 block x 128 bytes block size = 1024 bytes per set
- 2MB / 1024 = 2024 byte, $log_2(2024)=11$ cache index 
- 128 byte block size, $2^7$, 7 bit cache offset.
- cache index + cache offset = 11 + 7 = 18 
- 18 - 12 = 6 bits