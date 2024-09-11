**Architecture vs. Organization**
____
**Architecture** – the abstraction involving programmer-visible details of a computer system, such as
- Instruction set
- Memory layout 
**Organization** – the details of the implementation of a particular architecture, involving many details that are not directly visible to a programmer, such as
- Register implementation
- Bus structure
- Memory hierarchy and bank organization
  
**Packing**
___
The amount of space occupied a program in memory is often referred to as its memory footprint. A compiler, if so directed during compilation, may try pack operands of a program in memory to conserve space. This is particularly meaningful if the data structure consists of variables of different granularities (e.g., int, char, etc.), and if an architecture supports multiple levels of precision of operands. As the name suggests, packing refers to laying out the operands in memory ensuring no wasted space. 

*Example #1*
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

*Example #2*
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

**Big and Little-Endian Representations**  
____
The ordering of the bytes within the word is called Endianness. With 4 bytes in each word, if the machine is byte-addressable then four consecutive bytes in memory starting at address 100 will have addresses 100, 101, 102, and 103. I'm assuming a word is 32 bits or 4 bytes.

*Example*:

| byte | byte | byte | byte |
| ---- | ---- | ---- | ---- |
| 100  | 101  | 102  | 103  |

| Word containing 4 bytes |
| ----------------------- |
| 100-103                 |
Assuming the words at location 100 contains the values `0x11223344`, the individual bytes in the word can be organized in two ways. 

**Big Endian** - MSB of the word containing the value 11 is at address 100.

| 11  | 22  | 33  | 44  |
| --- | --- | --- | --- |
| 100 | 101 | 102 | 103 |
**Small Endian** - LSB of the word containing the value 44 is at address 100.

| 44  | 33  | 22  | 11  |
| --- | --- | --- | --- |
| 100 | 101 | 102 | 103 |
the sending machine is Little-endian and the receiving machine is Big-endian there could even be correctness issues in the resulting network code. It is for this reason, network codes use format conversion routines between host to network format, and vice versa, to avoid such pitfalls. Little endian architecture is assumed. 

**Generating assembly code for loops and conditionals**
___
```
If Statements

if (a==b)
	c = d + e
else 
	c = f + g 

Assembly:
	 beq r1, r2, then
	 add r3, r6, r7
	 beq r1, r1, skip
then add r3, r4, r5
skip
```

```
While Loop

while (j != 0)
{
	t = t + a[j--]
}

loop 
	beq r1, r0, done
	// loop body
	beq r0, r0, loop
done
```

**Calculating Clock Width**    
____
Given the following parameters (all in picoseconds), determine the minimum clock width of the system. To calculate how wide a clock cycle be, add all the data path delays between edge-triggered devices and then take the maximum. PC 🡪 Mem 🡪 IR 🡪 Reg File 🡪 ALU 🡪 Reg File
![[Calculating Clock Minimum.png]]

**Edge-triggered vs. level-triggered logic**
____
Level Triggering:
- Outputs change based on inputs
- Gated D Latches only change when the clock is high
- LC-2200 memory reads are level triggered (for cost & complexity reasons)

The following is level triggered
- Memory - Read
- Register File - Read
- ALU
- Other Register reads
- Muxes 
- Decoders

Edge Triggering:
- Outputs change based on inputs only when clock transitions 
- Positive edge-triggered logic when leading edge cause triggering
- Negative edge-triggered when trailing edge causes triggering

The following is edge triggered
- Memory - Write 
- Register File - Write
- Other Register writes 

 **Microcontrollers - Flat ROM, 3 ROM**    
___
Think of a ROM as a truth table for describing the FSM. The **address** represents the inputs bits (including the state). The **contents** of the ROM produce the output bits (including the next state). **Problem**: If you had a truth table with 4 inputs, 3 state bits, and 4 outputs, what size ROm should you use to encode it?
**Answer**: 2^7 words of 7 bit. This is because with 7 lines total in the ROM. There is two possibilities  for 7 lines. Therefore, it's 2^7. 

ROM stores the control signals to drive the data path. 

|               | Drive Signal | ... | ... | ... | Drive Signal | Local Signals | ... | ... | ... | ... | Local Signals | Write Signals | Write Signals |      |        |            |
| ------------- | ------------ | --- | --- | --- | ------------ | ------------- | --- | --- | --- | --- | ------------- | ------------- | ------------- | ---- | ------ | ---------- |
| current state | PC           | ALU | REG | MEM | OFF          | PC            | A   | B   | MAR | IR  | Z             | MEM           | REG           | func | RegSel | Next State |
Current state is also the address of the word in the ROM.

Are we going to choose the right next state based on our opcode in IR. 
![[Current State.png]]
![[TM Register.png]]
The Z bit input to the modifier is the output of the Z register in the datapath. 

![[ifetch clone.png]]
Lets assume that the state register has 5 bits. beq4 has the binary encoding 01000, and the next state filed of the beq3 microinstruction is set to beq4. The prefix of the encoding can be used with the Z register cotents to create a 6-bit address. If the Z bit is 0, then the addresss is 001000, and if the Z bit is 1 then the address is 101000. **0**01000 lets us call ifetch clone. 


Flat ROM:
- More space (since we increased the ROM by a factor of 32 for the occasional address modifiers, but have extra ROM space)
- Faster since only one ROM access in each microinstruction

Micro sequencer (3-ROM control unit)
- Less space (main rom much smaller than flat ROM)
- Slower since additional ROM Access in every clock cycle 

![[M Bit.png]]
![[T & Z Bit.png]]
Flat ROM Address
Next State Address:
4 Bits (Opcode) | 1 Bit (Z) | 5 Bits (Next State)

**Addressing modes**    
____
Refers to the way the operands are specified in an instruction.
![[Addressing Modes.png]]
**PC-Relative**: Commonly used for branch instructions. The offset allows the instruction to jump within the program. PC-relative addressing is where instruction's immediate value is treated as an offset relative to the current value of the PC. `beq $t0, $t1, offset`
**Base + Offset**: Addressing is where the address is computed by adding a base register value (any register) and an offset (given by the immediate value) `lw $t0, offset($t1)`
**Immediate**: Operands is a constant value provided directly by instruction itself. `addi $t0, $t1, immediate`
**Register**: This is operand is stored directly in the register. The instruction operates using the registers contents. `add $r1, $r2, $r3`

**LC2200 ISA**\
____
R Type Instructions
- Sequence of machine states are similar
- Only the ALU op changes 
J Type Instructions
- Straightforward
I Type Instructions (LW, SW, ADDI)
- Straightforward
I Type Instructions (BEQ)
- `if Rx == Ry then PC<- PC + 1 + sign-offset`
- `else nothing`
- Read values of Rx and Ry. Subtract them, and use the Z register to see if it holds a value of 0. 

```
beq1 // Store value of Rx into A
	A <- Rx
	Controls Signals: LdA, DrREG, RegSel = 00
beq2 // Store value of Ry into B
	B <- Ry
	Controls Signals: LdB, DrREG, RegSel = 01
beq3 // subtract A and B using alu and load Z with result for zero detect
	A - B
	Control Signals: func = 10, DrALU, LdZ
	
/// If Z==1 compute the target address because A==B
/// Assuming we branched

beq4 // Load A with PC
	A <- PC
	Control Signals: DrPC, LdA
beq5 // Sign extended offset B
	B <- Sign-extended offset
	Control Signals: DrOFF, LdB
beq // PC <- A+B to jump to target address
	PC <- A + B
	Control Signals: func = 00, DrALU, LdPC
// the next state will be ifetch1
```

What does the ROM look like?
![[BEQ Instruction ROM.png]]
However, you cannot have two next states. Instead, we expand the ROM address to 6 bits so we can prepend a zero or one bit to the next state if we want to test Z. This will double the size of ROM Size. For example, if Next state was `01000`, we'd output `001000` unless we want to test Z. Then we'd either output `101000` or `001000` as the next state by sending the value in Z as the first bit of our next state ROM address. 



**Stack frames & calling convention**
___
![[Control Flow.png]]
- Registers s0-s2 are the caller's "save" registers
- Registers t0-t2 are the temporary registers
- Registers a0-a2 are the parameter-passing registers
- Register v0 is used for the return value
- Register ra is used for return address
- Register at is used for jump target address
- Register sp is used as a stack pointer

![[Stack Figure.png]]

**Callers Responsibilities:**
![[Caller Responsibilities.png]]
```
!Store Items on Stack using
! save t registers
! save additional parameters
! save additional return values
! save return address

addi  $sp, $sp, -1  !decrement 
sw    $ra, 0($sp)   !store MEM[$sp + 0] <- $ra storing ra (address) on the stack

lea $at, targetAddress
jalr  $at, $ra

!Pop off the stack after call
lw    $ra, 0($sp)   !store ra <- MEM[$sp + 0] load ra (address) from stack to ra
addi  $sp, $sp, 1   !go down on stack

! restore additional return values
! restore additional params
! restore t registers
```
- upon return the caller will restore the ra, additional return values, additional parameters, and saved t register off the stack in that respective order.
**Callee Responsibilities**
- Callee saves register s0-s2 that it plans to use during its execution on the stack
- Callee allocates space for local variables on the stack
- Before returning, callee restores any saved s0-s2 registers from the stack
- Then callee executes jump to return address
![[Callee Responsibilities.png]]
**Activation Record**
![[Activation Stack Frame.png]]
- Because the stack pointer moves during the execution of a program. Since the stack frame is based on the stack pointer, **a frame pointer** is a fixed point on each stack frame to maintains the address of this fixed point. Old frame pointer in each stack frame (callers frame pointer) needs to be stored. 
- The **frame pointer** will be stored by the **callee** after storing the return address. 
![[Frame Pointer Figure.png]]
- Callee stores the previous frame pointer then copies the content of the stack pointer into the frame pointer.
```
sw   $fp, 0($sp)    ! MEM[$sp + 0] = $fp
addi $fp, $sp, 0    ! $fp = $sp
```
*Example*
`main()->foo()->bar()`
`main()` uses `$s0, $s1, $t0`
	`$s0` and `$s1` are callee saved registers. If `main()` modifies these, it needs to be saved and restored before calling `foo()`
	`$t0 `is caller saved. foo and bar both access `$t0` thus need to be preserved  
`foo()` uses `$s0, $t0`
	`$s0` need to be saved and restore before returning to main
	`$t0` is caller saved. foo() need to preserve `$t0` before call to `bar()`
bar()` uses ``$s0, $t0, $t1, $t2`
	`$s0` is callee saved register, if `bar()` modifies it it must save and restore `$s0` before returning to `foo()`
	`$t1, $t2, $t3` are caller saved register so `bar()` doesn't need to save it. 


**Fetch, decode and execute states**
___
[[Datapath and Control]]

**Interrupts vs. Exceptions vs. Trap**
____
- **Interrupts**: Asynchronous events usually produced by I/O devices which must be handled by the processor by interrupting execution of the currently running process
- **Traps**: Synchronous events produced by special instructions typically used to allow secure entry into operating system code
- **Exceptions**: Synchronous events usually associated with software requesting something the hardware can’t perform i.e. illegal addressing, illegal op code, etc.
![[Program Execution Types.png]]