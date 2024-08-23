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
