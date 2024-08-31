**JAL**
___
$JAL \space r_{target}, r_{link}$
- remember the return address in $r_{link}$ ->another of the processor registers to hold the return address
- Set program counter to the value in $r_{target}$ (start address of the callee) -> holds the address of the target of subroutine call. 

Returning from the procedure is straightforward since we have unconditional jump instruction
$J \space r_{link}$
