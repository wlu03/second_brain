Arrays store an array of variables also referred to as *vectors*. Programming languages allows arrays to be dynamically sized at run time as opposed to compile time. A compiler will typically use memory to allocate space for vector variables. The compiler will lay out an array such as: 

| 100 | ... | a[0] |
| --- | --- | ---- |
| 104 | ... | a[1] |
| 108 | ... | a[2] |
| ... | ... | ...  |
| ... | ... | ...  |
| 132 | ... | a[8] |
| 136 | ... | a[9] |
| ... | ... | ...  |
| ... | ... | ...  |
## Manipulating Values
____
To manipulate the array as shown below 
`a[7] = a[7] + 1`
To compile the statement above `a[7]` must be loaded from memory. You can do this with the **base+offset** [[addressing mode]] `ld r1, 28(rb)`. Assuming the base register is loaded with the value 100. Then, this will successfully load register 1 with the value of a[7]. 
```
ld r1, 28(rb); ## r1 <- MEM[100 + 28] because a[7] = 100 + 4*7 = 128
```
