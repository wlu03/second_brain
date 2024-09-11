## Circuits
___
**[[Combinational Logic]]**: The output of the circuit is a Boolean combination of the inputs of the circuit. There is no concept of memory. Basic logic gates  (AND, OR, NOT, NOR, NAND) are the building block for circuits. Examples of combinational login circuits found in the datapath of a processor include multiplexers, de-multiplexers, encoders, decoders, ALU's.

[[Sequential Logic]]: The output of such a circuit is a Boolean combination of the current inputs to the circuits and the current state of the circuit. A memory element, called a flip flop, is a key building block of such a circuit in addition to the basic logic gates that make up a combinational logic circuit.

Memory: Store instruction and operands
Arithmetic Logic Unit: ALU does arithmetic and logic instruction
Register File: are used to store objects including address and numbers
Program Counter: datapath to point to the current instruction and for implementing the branch and jump instructions 
Instruction Register: IR holds the instruction As the name suggests, a register-file is a collection of architectural registers that are visible to the programmer. We need control and data lines to manipulate the register file. These include address lines to name a specific register from that collection, and data lines for reading from or writing into that register. A register-file that allows a single register to be read at a time is called a single ported register file (SPRF). A register-file that allows two registers to be read simultaneously is referred to as a dual ported register file (DPRF). The following example sheds light on all the control and data lines needed for a register-file.

![[Dual Ported Register File (DPRF).png]]
$Data_{in}$ has 32 wire for 32 bits
$Port_A$ has 32 wire
$Port_B$ has 32 wire
$A _{address}$ has 6 wire
$B _{address}$ has 6 wire
$C _{address}$ has 6 wire
$RegWrEn$ has 1 wire

# Edge Triggered Logic
___
The contents of a register changes from its current state to its new state in response to a clock signal. 
![[Register.png | 300]]
The precise moment when the output changes state with respect to a change in the input depends on whether a storage element works on level logic1 or edge-triggered logic. With level logic, the change happens as long as the clock signal is high. With edge triggered logic, the change happens only on the rising or the falling edge of the clock. If the state change happens on the rising edge, we refer to it as positive-edge-triggered logic; if the change happens on the falling edge, we refer to it as negative-edge-triggered logic.

![[Edge Triggered Logic Example 2.png]]
In one clock cycle, the load store each item in A, B, and C respectively. However, one more clock cycle moves the value from C->A, A->B, and B->A. Therefore, A = 432; B = 98; C = 765

# Memory
____
For the purposes of this discussion, we will say that memory is not edge-triggered. The MEMORY element is special. As we saw in the organization of the computer system in Chapter 1, the memory subsystem is in fact completely separate from the processor. However, for the sake of simplicity in developing the basic concepts in processor implementation, we will include memory in the datapath design.

![[Memory Figure.png]]
For example, to read a particular memory location, you supply the “Address” and the “Read” signal to the memory; after a finite amount of time (called the read access time of the memory) the contents of the particular address is available on the “Data out” lines. Similarly, to write to a particular memory location, you supply the “Address”, “Data in”, and the “Write” signal to the memory; after a finite amount of time (the write access time) the particular memory location would have the value supplied via “Data in”.


## Example
____
Let us consider what needs to happen to execute an ADD instruction of LC-2200 and from that derive how the datapath elements ought to be interconnected

1. Use PC to specify to memory what location contains the instruction
2. Once instruction is read from the memory then it has to be stored in the IR
3. Once instruction is available in IR we can use the register number to read the REGISTER-FILE, perform the addition using ALU, and write appropriate register in to the REGISTER-FILE.  

![[ADD Instruction Example.png | 400]]
All storage element (except memory) are positive edge triggered. What this means is that one clock cycle we can transfer one storage to another. Steps 1 and 2 can be completed in one block cycle. Step 3 cannot be completed in the same clock cycle. Step 3 is done in its own clock cycle. In the beginning of the next clock cycle the output of the IR can be used to index the specfici csource registers needed for reading out the register file. 

![[Clock Cycle.png]]

# Bus Design 
___
**Single Bus Design**: 
-  a single set of wires and have all the datapath elements share this single set of wires
- Bus denotes that the set of wires is shared. The first thing to notice is that the red line is a single bus (electrically), i.e., any value that is put on the bus becomes available on all segments of the wire
- There are the triangular elements that sit between the output of a datapath element and the bus. These are called drivers (also referred to as tristate2 buffers).
- There is one such driver gate for each wire coming out from a data path element that needs to be connected to a bus, and they isolate electrically the datapath element from the bus.
![[Single Bus Design.png]]
**Two Bus Design**:
- The register file is dual ported. Two registers can be read and supplied to there ALU in the same clock cycle. 
- Red and purple may carry address or data values depending on the need of the program. Usually red carries address values and purple carries data values. 

![[Two Bus Design.png]]
**First Clock Cycle**:
- PC to Red Bus
- Red Bus to Addr of memory
- Memory reads the location specified by Addr
- Data from Dout to purple bus
- Purple bus to IR
- Clock IR
**Second Clock Cycle**
- IR supplies register numbers to register file (two source, one destination)
- Read the register file and pull data out of source registers
- Register file supplies data values from the two source registers to the ALU
- Perform ALU Add operation
- ALU result to purple bus
- Purple Bus to Register File
- Write to the register file at t the destination register number specified by IR

# Finite State Machine (FSM)
___
![[Finite State Machine.png]]In Figure 3.11, S1, S2, and S3 are the states of the FSM.  The arrows are the transitions 
between the states.  FSM is an abstraction for any sequential logic circuit.  It captures the 
desired behavior of the logic circuit. The state of the FSM corresponds to some physical 
state of the sequential logic circuit.  Two things characterize a transition: (1) the external 
input that triggers that state change in the actual circuit, and (2) the output control signals 
generated in the actual circuit during the state transition.  Thus, the FSM is a convenient 
way of capturing all the hardware details in the actual circuit.  

## Fetch Macro State
FETCH Macro state fetches an instruction from memory at the address pointed to by the PC into the IR. It increments the PC in readiness for fetching the next instruction. 
- We need to send PC to the memory
- Read the memory contents
- Bring the memory contents read into the IR
- Increment the PC

The Macro State is broken up into these microstates:
```
ifetch1
	PC -> MAR
	PC -> A
ifetch2 
	MEM[MAR] -> IR
ifetch3
	A+1 -> PC
```

![[Fetch Macro State.png]]
We can fill out the contents of the ROM for the address associated with the microstates. 
![[Fetch Microstates.png]]

## Decode Macro State
After the fetch macro states you want to transition to the decode macro state. We examine the contents of IR (bits 31-28) to find what instruction it is. Since there are many different types of OPCODEs, there are many branches the FSM can take. 
![[FSM of Decode.png]]
**Example**
R type has the format

| 31-28  | 27-24 | 23-20 | 19-4   | 3-0   |
| ------ | ----- | ----- | ------ | ----- |
| Opcode | Reg X | Reg Y | Unused | Reg Z |
The ADD instruction does $R_x \leftarrow R_y + R_z$
- We need to read two registers from the register file and write a third register
- We need to send different parts of the IR to the regno input of the register file. The multiplexer is the logic element to do it.
![[Using IR bit field to specify register selection.png]]
- The **RegSel** control input comes from the microinstruction. We replace the 4-bit regno field of the microinstruction with a 2bit RegSel Field
![[add1.png]]
![[add2 & add3.png]]

## Execute Macro State
**J Type Instruction**

| 31-28  | 27-24 | 23-20 | 19-0   |
| ------ | ----- | ----- | ------ |
| Opcode | Reg X | Reg Y | Unused |
JALR instruction was introduced in LC2200 for supporting the subroutine calling. JALR stashes the return address in a register and transfer control to the subroutine:
```
Ry <- PC + 1
PC <- Rx
```

![[jalr1.png]]
![[jalr2.png]]

**I-Type Instruction**

| 31-28  | 27-24 | 23-20 | 19-0                              |
| ------ | ----- | ----- | --------------------------------- |
| Opcode | Reg X | Reg Y | Immediate value or address offset |
The LW instruction has the following semantics
```
Rx <- MEMORY[Ry + signed address - offset]
```
The signed address offset if given by immediate field that is part of the instruction. The immediate field occupies IR 19-0. There is a sign extend hardware that converts this 20-bit 2's complement value to a 32-bit 2's complement value. 
![[lw1, lw2, & lw3.png]]
![[lw4.png]]
![[Autoincrement Example 4.png]]
```
Answer:
lw1
	A <- Ry, MAR
	Control Signals: DrReg, LdMAR, RegSel = 01

lw2
	Rx <- MEM[Ry]
	Control Signals: DrMem, WrREG, RegSel = 00

lw3
	Ry <- A+1
	Control Signals: func=11, DrALU, RegSel = 01, WrReg
```
**BEQ instruction (Part of I-Type)**
The following are the semantics:
`if (Rx == Ry) then PC <- PC+1+Signed address-offset`
`else nothing`
The hardware detect if the value on the bus is a zero. The microstates for BEQ use this logic to set the Z register upon comparing the two registers. 
![[beq1, beq2, beq3.png]]
The actions following this microstate is tricky compared to the micro states for the other instruction. In the other instruction, we simply sequence through all the microstates for that instruction and then return to the FETCH macro state. BEQ instruction cause a control flow change depending on the outcome of the comparison. If the Z is not set meaning that it's not equal then we return to ifetch1 to continue execution. On the other hand, if Z is set then we want to continue with the microstates of BEQ to compute the target address of branch. 
![[beq4,5,6.png]]
*The FETCH macro state increment PC, so we add the sign extended offset to PC to compute the target address without adding one. *

![[FSM of BEQ.png]]
Let us assume the state register has 5 bits, beq4 has the binary encoding 01000, and the next state field of the beq3 microinstruction is set to beq4. We will prefix this encoding with the contents of the Z register to create a 6-bit address to the ROM. If the Z bit is 0 then the address presented to the ROM will be 001000 and if the Z bit is 1 then the address will be 101000. The latter address (101000) is the one where we will store the microinstruction corresponding to the beq4 microstate. The control logic of the processor has a 10-bit address: 
- top 4 bits from IR 31-28 
- next bit is the output of the Z register 
- the bottom 5 bits are from the 5-bit state register

![[LC2200 Control Unit.png]]

![[Comparison of Control Regime.png]]
# LC2200
____
![[LC-2200 Datapath.png]]
- This the datapath of a single bus LC2200. It uses the following logic below to build this little CPU. LC2200 is a 32 bit instruction-set architecture. All Instructions, address, and data operands are 32-bitsd in width. 

*Control Signal form the Control Unit:*
- Drive signals: DrPC, DrALU, DrREG, DrMEM, DrOFF 
- Load signals: LdPC, LdA, LdB, LdMAR, LdIR 
- Write Memory signal: WrMEM 
- Write Registers signal: WrREG 
- ALU function selector: func 
- Register selector: regno

**Clock Pulse**:
___ 
- Combinational logic element has latency for propagating a value from its input to the output called *propagation delay*
- Latency (access time) from the register to enable reading
- Write a value into register the input must be stable for some amount of time (*setup time*) before rising edge of the clock
- The input to the register has to continue to be stable (*hold time*) after the rising edge of the clock
- *Transmission delay* (*wire delay*) for a value placed at the output of a logic element to traverse on the wire and appear at the input of another logic element 

# ROM
___
![[Control Unit Figure 3.19.png | 500]]
This is a memory element. On every clock tick, the state register advances to the next state as specified by the output of the ROM entry accessed in the current clock cycle. This is the same clock that drives all the edge-triggered storage elements in the datapath. All the load signals come out of the ROM serve as masks for the clock signal in that they determine if the associated storage element they control should be clocked in a given clock cycle. 

Every Clock Cycle These Steps are repeated
1. The state register names the state that the processor is in for this clock cycle. 
2. The ROM is accessed to retrieve the contents at the address pointed to by the state register. 
3. The output of the ROM is the current set of control signals to be passed on to the datapath. 
4. The datapath carries out the functions as dictated by these control signals in this clock cycle. 
5. The next state field of the ROM feeds the state register so that it can transition to the next state at the beginning of the next clock cycle.
# State Register
____
State register holds the encoding of the microstates. The contents of this register shows the state of the processor. One simple way is to use the state register as an index into a table. Each entry of the table contains the control signals needed in that state.
![[State Register Figure 3.18.png]]