Variable are in memory and the arithmetic/logic instruction work only with registers. They have to be brought into the register through the *load* instruction ($register \leftarrow memory$) and *store* ($memory \leftarrow register$).
```
ld r2, b; r2 <- b
st r1, a; a <- r1
```

**Example**
____
```
a = b + c

ld r2, b
ld r3, c
add r1, r2, r3
st r1, a 

add a, b, c
```

**Example 2**
____
An architecture has ONE register called an Accumulator (ACC), and instructions that manipulate memory locations and the ACC as follows:
```
LD ACC, a; ACC <- contents of memory location a
ST a, ACC; memory location of a <-- ACC
ADD ACC, a; ACC <- ACC + contents of a
```
Using the above instructions, show how to realize the semantics of the following instruction:
```
ADD a, b, c; memory location a <- contents of memory location b + contents of memory location c
```

**Answer**: 
To get a = b + c
```
LD ACC, b;  ACC <- contents of b
ADD ACC, c  ACC <- ACC + c     ACC <- b + c
ST a, ACC;   a <- ACC or  a <- b + c
```


## Memory Address
____
The [[addressing mode]] $base + offset$ computes the instruction as the sum of the contents of a register in the processor (called the base register) and an offset (contained in the instruction as an immediate value) from that register. 
```
LD r2, offset(rb);  //r2 <- MEMORY[rb+offset]
```
If $r_b$ contains the memory address of variable $b$, and the offset is 0 then the above instruction equivalent to loading the program b into the processor register $r_2$.

**Example**
____
Given the following instructions
```
LW Rx, Ry, OFFSET;     Rx <- MEM[Ry + OFFSET] 
ADD Rx, Ry, Rz;        Rx <- Ry + Rz 
ADDI Rx, Ry, Imm;      Rx <- Ry + Immediate value
```
Show how you can realize a new addressing mode called autoincrement for use with the load instruction that has the following semantics: 
```
LW Rx, (Ry)+;   Rx <- MEM[Ry]; 
				Ry <- Ry + 1;
```

**Answer**:
```
LW Rx, Ry, 0;    Rx <- MEM[Ry+0]
ADDI Ry, Ry, 1;  Ry <- Ry + 1
```