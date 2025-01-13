**Example 1:**
____
Given the following:
- **Number of cylinders on the disk** = 10,000
- **Number of platters** = 10
- **Number of surfaces per platter** = 2
- **Number of sectors per track** = 128
- **Number of bytes per sector** = 256
- **Disk allocation policy** = contiguous cylinders

**Questions**
1. **How many cylinders should be allocated to store a file of size 3 Mbyte?**
2. **How much is the internal fragmentation caused by this allocation?**

**Background Information:**
- Sector is a small portion that contains data. Cluster is a sequential # of sectors. Sectors are arranged into tracks. A cylinder can contain a certain number of tracks. 

**Solutions**
1. 3 MB is 3,145,728 bytes. Within a cylinder, there contains $10\cdot 2 \cdot 128 \cdot 256=655,360 \text{ bytes}$.  There needs to be 5 cylinders to store this information since $\frac{ 3,145,728 \text {bytes}}{655,360 \text{ bytes}} =4.8 \text{ cylinders}$. I got 5 by rounding up. This means that there is $0.2$ of space that is not used
2. Therefore $0.2 \cdot 655,360 =  131072 \text{ bytes}$ of internal fragmentation. 

**Example 2:**
___
This question is with respect to the disk space allocation strategy referred to as **FAT**. Assume there are 20 data blocks numbered 1 through 20.  
There are three files currently on the disk:
	**foo** occupies disk blocks 1, 2 and 3;  
	**bar** occupies disk blocks 10, 13, 15, 17, 18 and 19
	**gag** occupies disk blocks 4, 5, 7 and 9
Show the contents of the **FAT** (show the free blocks and allocated blocks per convention used in this section).

**Solution**: 

| File Name | Start Index |
| --------- | ----------- |
| */foo*    | 1           |
| */bar*    | 10          |
| */gag*    | 4           |


**FAT**

| free/busy | next | *index* |
| --------- | ---- | ------- |
| 1         | 2    | 1       |
| 1         | 3    | 2       |
| 1         | -1   | 3       |
| 1         | 5    | 4       |
| 1         | 7    | 5       |
| 0         | 0    | 6       |
| 1         | 9    | 7       |
| 0         | 0    | 8       |
| 1         | -1   | 9       |
| 1         | 13   | 10      |
| 0         | 0    | 11      |
| 0         | 0    | 12      |
| 1         | 15   | 13      |
| 0         | 0    | 14      |
| 1         | 17   | 15      |
| 0         | 0    | 16      |
| 1         | 18   | 17      |
| 1         | 19   | 18      |
| 1         | -1   | 19      |
| 0         | 0    | 20      |

**Example 3**
____
Consider an indexed allocation scheme on a disk
- The disk has 10 platters (2 surfaces per platter)
- There are 1000 tracks in each surface
- Each track has 400 sectors
- There are 512 bytes per sector
- Each [[i-node]] is a fixed size data structure occupying one sector.
- A data block (unit of allocation) is a contiguous set of 2 cylinders
- A pointer to a disk data block is represented using an 8-byte data structure. 

a) **What is the minimum amount of space used for a file on this system?**
b) **What is the maximum file size with this allocation scheme?**

**Solution:**
1. Size of a track = # of sectors per track * size of sector. $$400 * 512 \text{ bytes}=200 \text{ KBytes}$$Number of tracks in a cylinder = number of platters * number of surfaces per platter $$10*2=20$$ Size of a cylinder = number of tracks in a cylinder * size of track $$20 * 200 \text{ KByte} = 4000 \text{ KBytes}$$Unit of allocation (data block) = 2 cylinder = 8000 Bytes
   Size of i-node = size of sector = 512 bytes
   Min space for a file = size of i-node + size of data block = 512+(8000 * 1024) = 8,192,512 bytes. 
   Number of data block pointers in an i-node = size of i-node / size of data block pointer = 512/8 = 64. 
2. Maximum size of file = Number of data block pointers in i-node * size of data block= 64 * 8000 K bytes (K = 1024) = 524,288,000 bytes

**Example 4:**
___
Given the following:
- Size of index block = 512 bytes
- Size of Data block = 2048 bytes    
- Size of pointer = 8 bytes (to index or data blocks)
The i-node consists of    
- 2 direct data block pointers,
- 1 single indirect pointer, and 
- 1 double indirect pointer.
An index block is used for the i-node as well as for the index blocks that store pointers to other index blocks and data blocks. Pictorially the organization is as shown in the figure on the right. Note that the index blocks and data blocks are allocated on a need basis.

(a) **What is the maximum size (in bytes) of a file that can be stored in this file system?** 
(b) **How many data blocks are needed for storing a data file of 266 KB?**  
(c) **How many index blocks are needed for storing the same data file of size 266 KB?**
![[Screenshot 2024-11-13 at 11.57.08 PM.png]]
**Answer:**
1. The number of pointers an index block can store is calculated by dividing the block size by the pointer size. This would be $\frac{512 \text{ bytes}}{8 \text{ bytes per pointer}} = 64 \text{ pointers}$. 
	- An i-node contains 1 single indirect pointer that points to an index block containing pointers to data blocks. The number of data block pointers in an index block is 64. 
	- An i-node contains 1 double indirect pointer that points to an index block containing 64 single indirect pointers. Each of these contains 64 pointers to data blocks as well. Thus, the number of data block pointers is $64 \cdot 64$
	- The max file size in blocks is the number of data blocks $$2+64+64*64=4162 \text{ data blocks}$$ Multiple this by the size of each data block. This max value is $4162 \text{ blocks} \cdot 2048 \text{ (bytes per block)}=8,523,776 \text{ bytes}$.
2. The data blocks that are needed for storing 272,384 bytes is:
	- size of file / size of data block
	- 272,384/2048 = 133
3. 5 direct pointers
	- i-node
		- 2 direct data blocks
	- 1 single indirect index block
		- 64 data blocks
	- 1 double indirect index block
		- The double indirect index blocks holds 2 single points.
		- 2 single indirect index block -> 64 + 3 data blocks
			- One holds 64, The other holds 3 

**Example 5:**
_____
Current directory: /tmp 
I-node for /tmp: 20
The following Unix commands are executed in the current directory:
```
touch foo           /* creates a zero byte file */
ln foo bar          /* create a hard link */
ln –s /tmp/foo baz  /* create a soft link */
ln baz gag          /* create a hard link */

```
Note:

- Type of i-node can be one of directory-file, data-file, sym-link
    if the type is sym-link then you have to give the name associated with that sym-link; otherwise the name field in the i-node is blank
- reference count is a non-zero positive integer  
    In the picture below fill in all the blanks to complete the contents of the various i-nodes.

**Answer:** 
![[Screenshot 2024-11-14 at 12.16.46 AM.png]]

**Example 6:**
____
Consider the following:
```
touch foo;
ln foo bar;
ln -s foo baz;
rm foo;

what happens if we call 
cat baz; /* tries to view the contents of baz */
```

**Answer:**
Let the i-node for foo be 20. When we create the hard link bar, the refcount for i-node 20 goes up to 2. When foo is removed, the refcount for [[i-node]] drops to 1 but the i-node is not removed since bar has a hard link to it. However, foo is removed from the current directory. When we attempt to look at the soft link, it will return an error because the file doesn't exist in the directory any more. 

