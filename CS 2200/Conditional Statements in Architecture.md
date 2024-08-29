**Motivating Example**
___
Consider
```
	if (j==k) go to L1;
	a = b + c;
L1: a = a + 1;
```
*If j equals k, then just added b to c together onto a. However, if the predicate evaluates to TRUE, then a new instruction need to added to jump.* 

`beq r1, r2, L1;` 
- Compares `r1` and `r2` 
- If equal, then next instruction executed is at address L1
- If unequal, then the next instruction is the following

### Conditional - BEQ
___
BEQ is an example of a conditional branch instruction change the flow of control. Usually, it's fine to use a memory address as part of the instruction for branch instruction to specify the target of the branch. The branch format has the format:
`beq r1, r2, offset` 
- Compares r1 and r2
- If equal, then next instruction is at address `PC+offset`
- If unequal, then next instruction is the one following under `beq`

This [[addressing mode]] is called **PC-relative** addressing. It takes the [[Program Counter (PC)]] which is where the program is current running and adding an offset to where the `beq` takes place.

The instruction-set architecture may have different flavors of conditional branch instructions such as BNE (branch on not equal), BZ (branch on zero), and BN (branch on negative).

### Else Statement - Conditional Jump (J)
___
```
	if (j==k) {
		a = b + c;
	} else {
		a = b - c;
	}
L1: 
```
To enable the else statement, an unconditional jump need to be introduced. `j r_{target}` where $r_{target}$ contains the target address of the unconditional jump. This can also be done with **beq** such that the same register is set : `beq r1, r1, offset`.  However, the range of the unconditional jump is only by the offset size. With offset size of 8 bits (offset is 2's complement -> both positive and negative are possible), then the range is $PC-128$ to $PC + 127$. 

### Switch Statements 
___
```
switch (k) {
	case 0:
	case 1: 
	case 2: 
	case 3:
	default:
}
```
To implement this it's possible to use a jump table that holds the starting address for the code segment of each of the cases. Also, for bounds checking some architectures provide a set on less than instruction: `SLT s1, s2, s3`. If $s2 < s3$, then s1 is set to 1. Else s1 is set to 0. Then, you can use **BEQ** or **J** to jump to the address of the case. 

### Loop Statements
___
```
loop: ...
      ...
      ...
      bne r1, r2, loop; //set a conditional where if fails then loop
```