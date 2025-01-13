## Components in File System
___
The part of the OS system that manages the file system is called the *File System Manager (FS)*. There are layers in the FS manager:
- **Media Independent Layer:** This is the user interface provided to the user. This application program interface model gives the file system commands for the user to open/close, read/write file. The *name resolver* model translate user-supplied name to an internal representation in the FS. 
- **Device Driver**: Communicates with the command to the device and effects data transferring. 
- **Media Specific Storage Space Allocation Layer**: This layer embodies the space (on file creation), space reclamation (on file deletion), free-list maintenance, and other functions associated with managing the space on the physical device. 
- **Media specific requests scheduling layer**: Scheduling the requests from the OS with physical properties of the device. i.e. Disk Scheduling Algorithms

### OS File Check
In UNIX, the OS automatically runs file system check (FSCK) on boot up. If the system passes the consistency check the boot process continues. When an OS crashes either to power failure or user error, the OS dumps the contents of memory onto mass storage devices before terminating. It takes time to boot up as it tries to consistently check that the has the correct memory data.

### Journaling File System
___
File size too small then there is both space and time overhead writing into small files to the disk. Small files not only waste space on the disk (Due to internal fragmentation). but also result in time overhead (seek time, metadata management). System crashes in the middle of writing to a file leads to a inconsistent state. 

Modern FS uses a journaling approach where it keeps a "journal". This journal/record logs the information corresponding to file writes. The *journal* is a time-ordered record of all changes to the file system. This data structure is composed of *log segments*. Each log segment is of finite size. As it fills up, the FS write this out to a contiguous portion of the disk and starts a new segment for the writes to the FS. Once the change has been committed hte log segment is discarded. 

On system crashes, the journal helps with storing the information. The OS stores everything in memory to the disk at the time of the crash. Upon restart, the OS will recover the in-memory log segments. The file system will recognize that the changes in the log segments (both the ones on the disk as well as the in-memory log segments that were recovered from the crash) were not committed successfully. It will simply reapply the log records to the file system to make the file system consistent.
## Layout of the File System on the physical media
___
Operating system takes control of resources in the system during boot-up. The layout of information on the mass storage device becomes a contract between the BIOS and the operating system. Assuming the mass storage device is a disk. At the very beginning of the storage space on the disk {platter 0, tracker 0, sector 0} is a special record called the *Master Boot Record* (MBR). BIOS serving as the loader to load this program into memory and it will transfer control to MBR. The MBR program knows the layout of the rest of the disk and knows the exact location of the OS on the disk. 

The physical disk is made up of different partitions. 
![[Screenshot 2024-11-14 at 1.38.04 PM.png | 450]]
The key data structure of the MBR program is the partition table. The table gives the start and end device address in the form: $\text{\{platter, track, sector\}}$. MBR uses this table to decide which partition has to be activated depending on the choice exercised by the user at boot time. 

![[Screenshot 2024-11-14 at 1.44.02 PM.png | 400]]
The layout of each partition: 
- **Boot Block**: The very first time in every partition. MBR reads the boot block of the partition. Its a program that is loads in the OS associated with the partition. Every partition starts with boot block even if there is no OS associated with a partition. 
- **Superblock**: Contains all the information pertinent to the file system contained in this partition. Boot block reads the superblock into memory. It contains a code referred to as the magic number that identifies the type of FS housed in this partition, the # of disk blocks, and other admin info. 
- **Storage Management Data Structures:** The data structure will hold the specific allocation strategy being employed by the FS. ex. it may contain a bit map to represent all the available data blocks (free list). another ex. it can hold the FAT data structure. 
- **Per-File Information**: Data structure is unique to the specifics of the FS. In UNIX, every file has a unique number associated called the i-node number.
- **Root Directory**: Points tot he root directory of the file system
- **Data and Directory Files**: The data structures in the storage management entry of the partition are responsible for allocating and de-allocating these disk blocks. These disk blocks may be used to hold data (e.g., a JPEG image) or a directory containing other files (i.e., data files and/or other directories).
## Attributes
Attributes associated with a file is referred to as **metadata**. **Metadata** represents space overhead and therefore requires careful analysis as to its utility. 
- **Name**: identify contents of file. Modern OS implements a multi part hierarchal name. Each part of the name is unique only with respect to the previous parts of the name. 
	- DEC TOPS-10 OS can generate text files with the .TXT suffix to the user supplied name. In UNIX and Windows OS, such file name extensions are optional. 
	- Some OS allows [[Alias in OS|aliases]] to a file. 
- **Access Rights**: *who* has access to a particular file and *what* privileges each user has such as: *read, write, execute, change ownership, change privileges*. 
	- User: is an authorized user of the system
	- Group: is a set of authorized users
	- All: refers to all authorized user
- **Last Write Time**: Time when the file was written to last.
- **Owner**: creator of the file
- **Size**: occupancy within the file system


| Unix Commands                 | Semantics                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\text{touch <name>}$         | creates a file with the name                                                                                                                                                                                                       |
| $\text{mkdir <sub-dir>}$      | creates a sub directory. User must have write privilege to the current working directory to be successful.                                                                                                                         |
| $\text{rm <name>}$            | removes (or deletes) the file name. Only the owner can delete a file                                                                                                                                                               |
| $\text{rmdir <name>}$         | removes (or deletes) the sub directory. Only the onwer can remove it                                                                                                                                                               |
| $\text{ln -s <orig> <new>}$   | creates a name and make it symbolically equivalent to the file. This is name equivalence only. If the original is deleted, the storage associated is reclaim and the new file will be a dangling reference to a non-existent file. |
| $\text{ln <orig> <new>}$      | creates a name that is physically equivalent to the file. Even if the orig file is deleted, the physical file remains accessible via the new name.                                                                                 |
| $\text{chown <user> <name>}$  | changes the owner of the file to be this user                                                                                                                                                                                      |
| $\text{chgrp <group> <name>}$ | changes the group associated with the file to be apart of the group                                                                                                                                                                |
| $\text{cp <orig> <new>}$      | creates a new file that is a copy of the file                                                                                                                                                                                      |
| $\text{mv <orig> <new>}$      | renames a file with a new name                                                                                                                                                                                                     |
## Design Choices in Implementing a File System on Disk Subsystem
___

| Allocation Strategy      | File Representation               | Free List Maintenance | Sequential Access               | Random Access                   | File Growth | Allocation Overhead | Space Efficiency                    |
| ------------------------ | --------------------------------- | --------------------- | ------------------------------- | ------------------------------- | ----------- | ------------------- | ----------------------------------- |
| Contiguous               | Contiguous blocks                 | complex               | Very good                       | Very good                       | messy       | Medium to high      | Internal and external fragmentation |
| Contiguous With Overflow | Contiguous blocks for small files | complex               | Very good for small files       | Very good for small files       | OK          | Medium              | Internal and external fragmentation |
| Linked List              | Non-contiguous blocks             | Bit vector            | Good but dependent on seek time | Not good                        | Very good   | Small to medium     | Excellent                           |
| FAT                      | Non-contiguous blocks             | FAT                   | Good but dependent on seek time | Good but dependent on seek time | Very good   | Small               | Excellent                           |
| Indexed                  | Non-contiguous blocks             | Bit vector            | Good but dependent on seek time | Good but dependent on seek time | limited     | Small               | Excellent                           |
| Multilevel Indexed       | Non-contiguous blocks             | Bit vector            | Good but dependent on seek time | Good but dependent on seek time | Good        | Small               | Excellent                           |
| Hybrid                   | Non-contiguous blocks             | Bit vector            | Good but dependent on seek time | Good                            | Good        | Small               | Excellent                           |


An *address* on the disk is a triple $\{ cylinder\#, surface\#, sector\#\}$. The file system views the disk as *disks blocks* a design parameter of the file system. Each disk block is a physically contiguous region of the disk. The disk block address, as a short hand for the disk address (the 4-tuple, {cylinder#, surface#, sector#, size of disk block}) corresponding to a particular disk block, and designate it by a unique integer. 

The file system maintains a *free list* of available disk blocks. The enables the file system to keep track of the currently unallocated disk block. The file system uses the free list of disk blocks to make disk block allocation for the creation of new files.
![[Screenshot 2024-11-13 at 8.30.17 PM.png | 400]]
Each node in the free list gives the starting disk block address and the number of available blocks. Allocation to a new file could follow best fit or first fit policy. Upon **deletion**, the released disk blocks return to the free list. 

Similar to memory management, some disk allocation strategies also suffer from *external fragmentation*. Since files system commits a fixed size chunk of disk blocks (allowing for maximum expect growth size) at file creation time, this could suffer from *internal fragmentation*. This is a similar issue to **fixed size partition memory**. 

## Contiguous Allocation with Overflow Area
___
Add an overflow region which is an extra storage space that allows files larger than the fixed partition size to spill over additional space. This overflow region is also contiguous meaning its data blocks are stored in physically adjacent locations. On a negative note, random access suffers slightly for large files due to the spill into overflow region. 

## Linked Allocation
___
In this scheme, the file system deals with allocation at the level of individual disk blocks. The file system maintains a free list of all available disk blocks. A file occupies as many disk blocks as it takes to store it on the disk. The file system allocates the disk blocks from the free list as the file grows. The free list may actually be a linked list of the disk blocks with each block pointing to the next free block on the disk. The file system has the head of this list cached in memory so that it can quickly allocate a disk block to satisfy a new allocation request. Upon deletion of a file, the file system adds its disk blocks to the free list. In general having such a linked list implemented via disk blocks leads to expensive traversal times for free-list maintenance. An alternative is to implement the free list as a bit vector, one bit for each disk block. The block is free if the corresponding bit is 0 and busy if it is 1.

The free list changes over time as files grow and shrink. There is no guarantee that a file will occupy contiguous disk blocks. The allocation is quick since its one disk block at a time. No external fragmentation due to on-demand allocation. Accessing file performs poorly compared to contiguous allocation. 

## File Allocation Table (FAT)
___
**Variation of linked allocation.** A table on the disk known as the FAT contains the linked list of files currently populating the disk. The scheme divides the disk logically into partitions. Each partition has a FAT in which each entry corresponds to particular disk block. *Free/busy* field indicates the availability of that disk block (0-free, 1-busy). **Next** field gives the nect disk block of the linked list that represents a file. (-1) value indicates this entry is the last disk block for that file. 
![[Screenshot 2024-11-13 at 9.13.41 PM.png |  600]]
*/foo* occupies two disk blocks: 30 and 70. The *next* field of entry 30 contains the value 70, the address of the next disk block. The next field of entry 70 is -1 meaning its the last block for *foo*. 
If */foo* were to grow, the scheme will allocate a free disk block and fix the FAT accordingly. 

**Pros vs. Cons**
- **Less chance of errors** compared to linked allocation. Caching FAT in memory leads to efficient allocation times compared to linked allocation.
- **Performs worse** for sequential file access **compared to contiguous file allocation** much like linked allocation.
- **Performs better than linked allocation** for random access since that FAT contains the next block pointer for a given file.
- **Biggest downside** is logical partitioning of a disk.
- Go to [[File System Questions|question 2]] for an example of **FAT**

## Index Allocation
___
Allocates an *index* disk block for each file. The index block for a file is a fixed-size data structure that contains addresses for data blocks that are part of that file. This scheme aggregates data block pointers for a file scattered all over the FAT data structure. This table called i-node occupies a disk block. The *directory* (on the disk) contains the file name to index node mapping for each file. Also contains a free list as a bit vector of disk blocks. 
![[Screenshot 2024-11-13 at 9.28.13 PM.png]]
- **Performs better for random access** than FAT
- Downside is that the limitation on the maximum size of a file.
	- Since i-node is a fixed size data structure per file with direct pointers to data blocks. The number of data block pointers in a i-node bounds the maximize size of the file. 

## Multilevel Indexed Allocation
___
This scheme fixes the limitation in the indexed allocaiton by making the i-node for a file an indirection table. For example, with one level indirection, each i-node entry points to a first level table. The number of first level tables equals the number of pointers that an i-node can hold. This scheme can be extended to make an i-node a two (or higher) level indirection table depending on the size of the files that need to be supported. Downside is that even small files that may fit in a few data blocks have to go through extra levels. 
![[Screenshot 2024-11-13 at 9.46.55 PM.png]]
## Hybrid Indexed Allocation
___
![[Screenshot 2024-11-13 at 9.51.03 PM.png]]
- This combines multi-indexed and regular index allocation. 
- Each file has an i-node. It accommodates all data bocks for small files with direct pointers. 
- If the file size exceeds the capacity for direct blocks, then the scheme uses single or more levels of indirection for additional data blocks. 
If the file size does not exceed the amount of space available in the direct blocks then there is no need to create additional index block. As file grow and exceeds capacity of direct data blocks, then it will allocate first, second, and third level index blocks.

![[Screenshot 2024-11-14 at 2.25.11 PM.png]]
**Question**: What is the maximum file size in bytes possible in the ext2 system? Assume a disk block is 1 KB and pointers to disk blocks are 4 bytes.

**Answer**: 
- Direct data blocks: 12
- Single Indirect Pointer: $1KB/4Bytes = 256$
- Double Indirect Pointer: $256*256$
- Triple Indirect Pointer: $256*256*256$
- The total disk blocks available to a file is $12+2^8+2^{16}+2^{24}$
- The maximum file size in bytes for data file is the disk blocks available times the size of one disk block which is 1 KB, $(12+2^8+2^{16}+2^{24}) \cdot 1 KB=16 GBytes$

