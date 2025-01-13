Multiprocessors consists of multiple processors in a single computer sharing the resources such as memory, bus, input/output devices. 
![[Screenshot 2024-11-19 at 7.10.12 PM.png]]
An SMP increases system performance at a nominal increase in total cost. 

**Multiprocessor Cache Coherence**
___
![[Screenshot 2024-11-20 at 12.25.36 AM.png | 500]]
- Hardware is responsible for maintaining a consistent view of shared memory that may be encached in the per-processor cache.  
![[Screenshot 2024-11-20 at 12.25.48 AM.png | 500]]
T1, T2, T3 executes on P1, P2, and P3. All of them currently have location X cached in their respective caches. T1 writes to X. At this point, the hardware can do:

**Write-Invalidation**
- Invalidate copies of X in the peer caches. This requires enhancement to the shared bus of a **invalidation line**. 
- The cache monitor the bus by **snooping** in it to watch for invalidation request from peer caches.
- Every cache checks if the this location is cached locally. If it is then it invalidates that location. 
- When an invalidation request for X is detected, each cache checks if it holds a copy of X. If a cache has a copy, it marks it as invalid as it can no longer be used. 
- After invalidation, if any processor needs X, it results in a cache miss (because its copy was invalidated.)
**Write-Update**
- Ensures all caches maintain consistency when processors share and modify data.
- When a processor (e.g. P1) modifies a memory location X that might also be present in other caches, it broadcasts the updated value of X on the shared bus. 
- Other caches that hold a copy of **X** listen to this broadcast and **update their local copies** with the new value.
- Similar to the write-invalidate protocol, caches continuously **snoop** on the shared bus.
 - When they detect a broadcast update for **X**, they check if they have **X** in their cache.
    - If they do, they update their local copy to reflect the new value.
- Compared to write invalidate protocol, cache doesn't discard their copies.

## Snoopy Cache
___
This is referred to bus-based cache coherence protocols. Snoopy cache do not work if the processors do not have a shared bus to snoop in.