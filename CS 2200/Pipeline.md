![[Pipeline Example Figure.png | 500]]
**Fetch** - *Always*
- Fetch into IR & increment PC (IF)
**Decode** - *Always*
- Decode instruction & read register contents (ID/RR)
**Execute** - *Sometimes*
- Perform arithmetic/log and/or address computation (EX)
- Fetch/store memory operands (MEM)
- Write to Register (WB)

![[Buffers.png]]
**BUFFERS** (registers) you need to isolate between stages. The buffers are different because they output different things. 

*Example*
____
To calculate the size of the buffer DBUF that is required for the decode stage, we need to list all the bits that are needed to be passed down the pipeline for each stage and then take the union of this information: ADD, NAND, ADDI, LW, SW, BEQ, JALR, HALT

**ADD**: opcode, Rx, B, C 
**NAND**: opcode, Rx, B, C
**ADDI**: opcode, Rx, B, imm
**LW**: opcode, Rx, B, imm
**SW**: opcode, A, B, imm
**BEQ**: opcode, A, B, imm, PC
**JALR**: opcode, A, Ry, PC
**HALT**: opcode

What bits need to be included in the Decode Buffer to handle all of the below instructions? Take the union of everything so take **opcode, Rx, A, B, imm, PC**. We don't need Ry from JALR because Rx is a placeholder for a register number. It could be any arbitrary register. A and B are place holders for register values. 

*Example 2* 
![[ADD Instruction Buffer Example Figure.png | 500]]
## Data Hazards 
___
### Structural Hazards
- Occurs due to a lack of hardware components
- If we lack the hardware to do multiple similar operations simultaneously, we must create bubbles in the processor until that resource is free.
- ex: Needing 2 ALUs for branching 

### Data Hazards
![[Data Hazard Figure.png | 400]]
How do you solve this? The LC stalls the pipeline to ensures that we have the registers for the other instructions. 
#### Tracing 
![[Screenshot 2024-10-17 at 1.43.35 PM.png | 400]]
![[Screenshot 2024-10-17 at 1.43.52 PM.png | 400]]
![[Screenshot 2024-10-17 at 1.44.02 PM.png | 400]]

![[Screenshot 2024-10-17 at 1.44.12 PM.png | 400]]
![[Screenshot 2024-10-17 at 1.44.22 PM.png | 400]]

![[Screenshot 2024-10-17 at 1.44.36 PM.png | 400]]
![[Screenshot 2024-10-17 at 1.44.45 PM.png | 400]]
There were 3 bubble. Use bubble to resolve RAW data hazard.

**LW**:
Loads LW creates an inevitable data hazard that cannot be forwarded. This is because data is not ready fro the load when the next instruction is decoding. 
### Control Hazards
- Happens when dealing with branching

**Conservative Branching**:
Pass bubbles until BEQ leaves the execute state.
![[Screenshot 2024-10-17 at 5.12.07 PM.png | 400]]

**Branch Prediction**:
When incorrectly predicting branches, you would need to **flush** the pipeline/ dropping instructions that are not suppose to be there. The result of the prediction is discovered once BEQ enters the EX stage. Therefore, all instructions before that stage in IF and ID/RR need to be flushed so that the correct instruction can execute following BEQ.
![[Screenshot 2024-10-17 at 5.14.31 PM.png]]


![[Screenshot 2024-10-17 at 5.26.21 PM.png]]
**Data Forwarding**
![[Screenshot 2024-10-17 at 6.40.32 PM.png]]
![[Screenshot 2024-10-17 at 6.43.46 PM.png]]
 