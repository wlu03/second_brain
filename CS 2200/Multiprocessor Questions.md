Question 1
___
**Given the following details about an SMP (symmetric multiprocessor):**

- **Cache coherence protocol:** `write-invalidate`
- **Cache to memory policy:** `write-back`

**Initially:**
- The caches are empty  
- Memory locations:  
  - A contains 10  
  - B contains 5  
**Consider the following timeline of memory accesses from processors P1, P2, and P3.**
![[Screenshot 2024-11-20 at 12.56.32 AM.png]]![[Screenshot 2024-11-20 at 12.58.23 AM.png]]
- **Write-invalidate protocol**:
    - When a processor writes to a memory location, any cached copies of that memory location in other processors are invalidated.
- **Write-back policy**:
    - Changes are written to the cache first, and only updated to memory when necessary.

**T1: Processor P1 loads A**
- P1 loads memory location A into its cache
- The cache of P1 contains A=10
- P2 and P3 don't have A in their cache 
**T2: Processor P2 loads A**
- P2 loads memory location A into its cache
- The cache of P1 & P2 contains A=10
- P3 don't have A in their cache 
**T3: Processor P3 loads A**
- P3 loads memory location A into its cache
- The cache of P1, P2, & P3 contains A=10
**T4: Processor P2 stores into A**
- P2 writes the value of 40 to A
- write invalidate protocol ensures all other cache copies are invalidated. 
- P2 cache has 40, P1 & P3 have their copies invalid (I)
- Memory still contains 10 as P2 follows the write-back policy (changes are not immediately written to memory)
**T5: Processor P1 stores 30 into B**
- P1 writes the value of 30 into B.
- Since no other processor has B, no invalidation needed.
