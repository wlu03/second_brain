## Sync vs Async
___
**Synchronous** event: Occurs at well defined points aligned with activity of the system.
- Making a phone call
- Opening a file
**Asynchronous** event: Occurs unexpectedly with respect to ongoing activity
- Receiving a call 
- User presses a key on keyboard
## Discontinuities
___
**Interrupt**: *Asynchronous* event that is produced by an external source like I/O devices which must be handled by the processor by interrupting execution. 
**Traps**: *Synchronous* events produced by internal source, special instruction typically used to allow secure entry into the OS code
**Exceptions**: *Synchronous* event usually associated with internal software request something that hardware cannot preform. i.e. illegal addressing, illegal opcode

## Handling Discontinuities
___
- ETR will contain a unique number stashed by the hardware to indicate the type of discontinuity
- In the INT macro states, the handler: 
	- saves $k0
	- enables interrupts (EI)
	- saves processor registers 
	- executes device code
	- restores processor registers
	- disables interrupts
	- restores $k0
	- execute RETI instruction
- RETI
	- Transfer $k0 to PC
	- Enable interrupt
	- Go back to ifetch1
- Create a new processor register IE that is 1 when interrupts are enabled
- For an interrupt to be recognized, an interrupt must be asserted and IE must be 1
- In the INT macro states turn off IE before fetching the first instruction of handler
- EI and DI to respectively set IE to 1 and 0
- Use EI after pushing $k0 on the stack

## Wiring for INT
___
![[Wiring for INT.png | 400]]
- Device asserts the INT bus (its wired so multiple devices can do this simultaneously)
- CPU sees the INT signal and microcode cycle into the INT macro states. Microcode raises the INTA signal line
- Device pass through the INTA signal if they are not interrupting otherwise the first interrupting device asserts its ID on the data-bus
- Microcode reads the data-bus and uses the ID as an index to determine which entry in the IVT to use to set the PC.

![[Priorities for Interrupt.png | 400]]
- Priority encoder takes $2^n$ inputs and produces a 1-bit INT output and an n-bit ID output
- If any of the input lines is high, the PE asserts the INT output
- The PE asserts the encoded value of the first high input line onto the ID output 
	- E.g. if input 5 and 7 are high on a 3-bit PE, then it asserts INT and ID=101 
	- If only input 7 is high, then it asserts INT and ID=111
## User/System Stack
____
- Use system stack for saving all necessary information
- A user/kernel mode flag record which stack to use

![[User and System Stack Example.png | 500]]


### Microcode Interrupt Actions
___
INT
- $k0 <- PC 
- Assert INTA to acknowledge INT
- Receive Interrupt Vector from the device on data bus
- PC <- MEM of interrupt vector which is from IVT
- If User Mode
	- USP <- $sp
	- $sp <- SSP
	- This means that stack point is saved in user stack, and stack point uses system's stack
	- turn mode to kernel
- Push previous mode on stack
- Disable Interrupt
RETI
- PC <- $k0 ; return address
- Pop Mode from system stack 
- If user mode
	- SSP <- $sp
	- $sp <- USP
- Enable Interrupts

## Completed Working INT Handler
____
Handler
- //Handler starts with interrupts disabled
- push $k0 onto system stack
- enable interrupts
- save processor registers to system stack
- execute device code (IV)
- restores processor register from system stack
- disable interrupts
- pop $k0 from system stack
- //Handler ends with interrupts disabled
- return to original program with RETI

