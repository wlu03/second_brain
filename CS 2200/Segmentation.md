Segmentation is a system that allows a process's memory space to e subdivided into chunks of memory each associated with some aspect of the overall program. This is another way to do virtual memory. **Segmentation is visible to the ISA (but not transparent like paging)**, so it doesn't work as a retrofit to ISA with contiguous memory model. We have paging that could be transparently slipped under existing memory management.  Segments can be different sizes. 

Process address space divided up into n distinct segmented based on program organization. Each segment has: a **number** and a **size**. Each segment starts at its own address 0 and goes up to its size-1. 
![[Screenshot 2024-10-29 at 5.10.29 PM.png]]
*there is external fragmentation problem*
![[Screenshot 2024-10-29 at 5.11.02 PM.png]]

## Paged Segmentation
___
- Page Tables can be big (64-Bit Virtual Address) and we need one for each process in memory. 
	- ex. a 64 bit virtual address with 4KB pages means that the VPN is 64-12 = 52 bits long 
	- How much space? 
		- Space needed is the number of entries times the size of each entry
		- $2^{52} \text{ entries}$ 
		- Each page table entry is 64-Bits, which is 8 bytes or $2^3$ bytes
		- $2^{52} * 2^{3} = 2^{55} \text{ bytes}$ 
		- Segmentation will help this because it's huge
![[Screenshot 2024-10-29 at 5.16.41 PM.png | 400]]
**Translation with Paged Segmentation**
When accessing a virtual address, it's split to three parts. Segment Number (S), Page Number (P), and the Offset (W) within the page. 
- **Segment Lookup**: The segment number is used to look up the **segment descriptor** in the **Segment Descriptor Table**
- The **Limit** is checked to ensure the requested page number doesn't exceed the segment size. 
- **Page Table Lookup**: The page number within the segment is used to look up the PTE in the page table where the PTE provides the PPN (Physical Page Number) combined with the **offset** to make the final physical address.
- **Advantages**: We get a page table for each segment, but the PT is only as big as we need.

