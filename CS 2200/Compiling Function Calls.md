For example of a procedure call, the program is *main* and makes a call to function *foo*. The flow of control of the program is transferred to the entry point of the function. Exiting *foo* the flow of control returns to the statement following the call to *foo* in main. *Caller* is the entity that makes the procedure call (main) and *callee* is the procedure that is being called (foo). 

## Procedure Call
___
1. Parameter Passing: Processor registers reserved for parameter passing. Compiler can pass in additional parameters on the stack.
2. Return the return address.
	$JAL \space r_{target}, r_{link}$
	- remember the return address in $r_{link}$ ->another of the processor registers to hold the return address
	- Set program counter to the value in $r_{target}$ (start address of the callee) -> holds the address of the target of subroutine call. 
	
	Returning from the procedure is straightforward since we have unconditional jump instruction
	$J \space r_{link}$
3. Transfer control to callee by using JAL instruction
4. Space for callee local variables by using stack to allocate space needed for any local variables. 
5. Return values is stored on processor register for the return. If exceeds, then it can be placed on stack.
6. Return to the point of call by using jump. 

#### Registers
___
- Registers **s0-s2** are the caller’s s registers
- Registers **t0**-**t2** are the temporary registers
- Registers **a0**-**a2** are the parameter passing registers
- Register **v0** is used for return value 
- Register **ra** is used for return address 
- Register **at** is used for target address 
- Register **sp** is used as a stack pointer

## Stack
___
Push: Decrements the stack pointer and places the value at the memory 