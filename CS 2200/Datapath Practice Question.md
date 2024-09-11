1. What is the difference between level logic and edge-triggered logic? Which do we use in implementing an ISA? Why?
	**Answer**: Level logic is triggered by the change of movement on the clock when it's either 0 or 1. Edge triggered logic is trigger by the change in movement from 0 to 1 (rising edge) or 1 to 0 (falling edge). Register is edge triggered. Register File - read is level trigger and writing is edge triggered. This is the same for memory. ALU is level triggered. IR is rising edge triggered.
2. Given the FSM and state transition diagram for a garage door opener (Figure 3.12-a and Table 3.1) implement the sequential logic circuit for the garage door opener (Hint: The sequential logic circuit has 2 states and produces three outputs, namely, next state, up motor control and down motor control).
	**Answer**:
	 ![[Datapath Practice Question 2.png | 400]] 
	 
3. Re-implement the above logic circuit using the ROM plus state register approach detailed in this chapter.
4. Compare and contrast the various approaches to control logic design.
5. One of the optimizations to reduce the space requirement of the control ROM based design is to club together independent control signals and represent them using an encoded field in the control ROM. What are the pros and cons of this approach? What control signals can be clubbed together and what cannot be? Justify your answer.
6. What are the advantages and disadvantages of a bus-based datapath design?
7. Consider a three-bus design. How would you use it for organizing the above datapath elements? How does this help compared to the two-bus design?
8. Explain why internal registers such as the instruction register (IR), and memory address register (MAR) may not be usable for temporary storage of values in implementing the ISA by the control unit.
9. An engineer would like to reduce the number of microstates for implementing the FETCH macrostate down to 2. How would she able to accomplish that goal?
10. How many words of memory will this code snippet require when assembled? Is space allocated for “L1”?
```    
	beq $s3, $s4, L1
	add $s0, $s1, $s2
L1: sub $s0, $s0, $s3
```
11. What is the advantage of fixed length instructions?
12. What is a leaf procedure?
13. Assume that for the portion of the datapath shown below that all the lines are 16 bits wide. Fill in the table below.
![[Datapath Question 13.png]]
![[Datapath Practice Question 13.2.png| 400]]
14. In the LC-2200 processor, why is there not a register after the ALU?
15. Extend the LC-2200 ISA to include a subtract instruction. Show the actions that must be taken in microstates of the subtract instruction assuming the datapath shown in Figure 3.15.
16. In the datapath diagram shown in Figure 3.15, why do we need the A and B registers in front of the ALU? Why do we need MAR? Under what conditions would you be able to do without with any of these registers?
17. Core memory used to cost $0.01 per bit. Consider your own computer. What would be a rough estimate of the cost if memory cost is $0.01/bit? If memory were still at that price what would be the effect on the computer industry?
18. If computer designers focused entirely on speed and ignored cost implications, what would the computer industry look like today? Who would the customers be? Now consider the same question reversed: If the only consideration was cost what would the industry be like?
19. Consider a CPU with a stack-based instruction set. Operands and results for arithmetic instructions are stored on the stack; the architecture contains no general purpose registers. The data path shown on the next page uses two separate memories, a 65,536 ($2^{16}$) byte memory to hold instructions and (non-stack) data, and a 256 byte memory to hold the stack. The stack is implemented with a conventional memory and a stack pointer register. The stack starts at address 0, and grows upward (to higher addresses) as data are pushed onto the stack. The stack pointer points to the element on top of the stack (or is -1 if the stack is empty). You may ignore issues such as stack overflow and underflow. Memory addresses referring to locations in program/data memory are 16 bits. All data are 8 bits. Assume the program/data memory is byte addressable, i.e., each address refers to an 8-bit byte. Each instruction includes an 8-bit opcode. Many instructions also include a 16-bit address field. The instruction set is shown below. Below, "memory" refers to the program/data memory (as opposed to the stack memory).
![[Datapath Practice Question 19.png]]
20. Show a state diagram for the control unit indicating the control signals that must be asserted in each state of the state diagram.
21. 