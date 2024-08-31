**Instruction Set** and the **Organization of the Machine** are two architectural issues around processor design. Programming languages exerts influence on the instruction set design. The constructs in high-level language such as assignment statements and expressions map to arithmetic and logic instructions and load/store instructions. High level languages support data abstraction that may require precision of operands and addressing modes in the instruction set. Conditional statements and looping constructs would require conditional and unconditional branching instructions.  **Applications** influence the instruction set design as well. 

The **instruction set** is the prescription given by the computer architect as to the capabilities needed in the machines that should be made visible to the machine language programmer. Instruction set serves as a "contract" between the software and the actual hardware implementation. High level languages were developed such that the attention shifted from implementation feasibility to whether the instructions were actually useful (producing highly efficient code for programs).
## Hardware
____
Registers
Arithmetic
Logic Unit
Data-path

## Example: High Level Language Feature Set
____
1. *Expression and Assignment Statements*: Instruction-set architecture (ISA)'s nuances come from the different kind of arithmetic, logic operations, size, and location of the operation needed in an instruction.
2. *High-Level Data Abstraction*: Refers to the concept of hiding complex detail of data storage and management from the user. For example, ADTs or Abstract Data Types include: **Stacks**, **Queues**, and **Lists**. Another example is **data base management systems** like **Tables** and **Queries**. 
3. *Conditional Statements and Loops*: while loops, do while loops, for loops, and other iterations of for loops are included in this compilation. 
4. *Procedure Calls*: These calls are also known as **function calls** or **subroutine calls** are instructions that allow a program to temporarily transfer control to a different set of instructions and then return to the point where the procedure was called once it completes. Compiling this will require remembering the state of the program before and after executing the procedure. 

## Expression and Assignment Statements
____
In high level languages, arithmetic nad logical expression and assignment statements are the following: 
```
a = b + c;
d = e - f;
x = y & z; 
```
Each statement takes two operands as inputs and take another operand to store the results. In the processor instruction set:
```
add a, b, c; a <- b+c
sub d, e, f; d <- d-f
and x, y, z; x <- y&z
```
These instructions are called *binary* instruction since they work on two operands to produce a result. They are also called *three operand* instructions. 

Within a processor, registers are used to store values, addresses, return addresses, and etc. Instruction look like
```
add r1, r2, r3; r1 <- r2 + r3
```

### Immediate
___
A specific constant values is used in the program. For example, to initialize a register to some starting value or clearing a register that is used as an accumulator. The easiest way to meet this need is to have such constant values be part of the instruction itself. Such values are called immediate values.
```
addi r1, r2, imm; r1 <- r2 + imm
```
## Example 1
____
Given the following instructions
```
ADD Rx, Ry, Rz; Rx <- Ry + Rz
ADDI Rx, Ry, Imm; Rx <- Ry + Immediate Value
NAND Rx, Ry, Rz; Rx <- NOT (Ry AND Rz)
```
Show how you can use the above instruction to acheive the effect of the following
```
SUB Rx, Ry, Rz; Rx <- Ry - Rz
```

**Answer**:
```
NAND Rz, Rz, Rz;  1's complement of Rz in Rz
ADDI Rz, Rz, 1;   2's complement of Rz in Rz, Rz now contains -Rz
ADD Rx Ry, Rz;    Rx <- Ry + (-Rz)

//Restore the values of Rz
NAND Rz, Rz, Rz;
ADDI Rz, Rz, 1;
```
[[Two's Complement]] is utilized to flip $R_z$ to a negative number. Addressing Mode refers to how the operands are specified in an instruction. The addressing mode is called **register addressing** since the operands are in registers. 