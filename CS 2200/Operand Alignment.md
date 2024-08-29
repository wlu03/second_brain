The amount of space occupied a program in memory is often referred to as its memory footprint. A compiler, if so directed during compilation, may try pack operands of a program in memory to conserve space. This is particularly meaningful if the data structure consists of variables of different granularities (e.g., int, char, etc.), and if an architecture supports multiple levels of precision of operands. As the name suggests, packing refers to laying out the operands in memory ensuring no wasted space. 
## Example #1
____
Consider the following data structure
```
struct {
	char a;
	char b[3];
}
```
One layout of this structure is as shown

| +3  | +2   | +1   | +0   |     |
| --- | ---- | ---- | ---- | --- |
|     |      |      | a    | 100 |
|     | b[2] | b[1] | b[0] | 104 |
*The amount of memory for this layout is 8 bytes such that the empty space is all wasted. This is the unpacked layout. A compiler can eliminate this wasted space and pack the above data structure as below* 

| b[2] | b[1] | b[0] | a   |
| ---- | ---- | ---- | --- |
| 103  | 102  | 101  | 100 |
*Packing is done by the compiler for precision of data types and addressability supported in the architecture. In addition to being frugal with respect to space, one can see that this layout would result in less memory accesses to move the whole structure (consisting of the two variables a and b) back and forth between the processor registers and memory. Thus, packing operands could result in time efficiency as well.*
## Example #2
____
Consider the following
```
struct {
	char a;
	int b;
}
```
One possible layout is:

| +3        | +2        | +1        | +0        |     |
| --------- | --------- | --------- | --------- | --- |
| $b_{...}$ | $b_{...}$ | $b_{lsb}$ | $a$       | 100 |
|           |           |           | $b_{msb}$ | 104 |
*The problem with this layout is that $b$ is an int and it starts at address 101 and end at address 104. To load $b$ two words have to be brought from memory. Architectures will usually require word operands to start at word addresses. This is usually referred to alignment restriction of word operands to word addresses.* 

The instruction `ld r2, address` will be illegal if the address is not a word boundary (100, 104, etc.). The compile can generate code to load two words and do manipulation inside the processor. It's inefficient. Therefore, a compiler will most likely layout the structure like below. 

| +3        | +2        | +1        | +0        |     |
| --------- | --------- | --------- | --------- | --- |
|           |           |           | $a$       | 100 |
| $b_{lsb}$ | $b_{...}$ | $b_{lsb}$ | $b_{msb}$ | 104 |
Although it wasted space, it's more efficient to access the operands. 