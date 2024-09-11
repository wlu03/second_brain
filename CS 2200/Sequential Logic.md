# Mux
____
- Select between inputs using a selector
- if there are 2^n inputs then there are n selector bits
- There are is always just one output
![[MUX.png | 350]]

## 1-Bit Adder Using Mux 
- A and B is the two 1 bit numbers
- Cin is the carry-in from the sum
- A, B, and Cin are the inputs
- S is the sum
- Co is the carry-out

| A   | B   | C in | Sum | C out |
| --- | --- | ---- | --- | ----- |
| 0   | 0   | 0    | 0   | 0     |
| 0   | 0   | 1    | 1   | 0     |
| 0   | 1   | 0    | 1   | 0     |
| 1   | 0   | 0    | 1   | 0     |
| 0   | 1   | 1    | 0   | 1     |
| 1   | 1   | 0    | 0   | 1     |
| 1   | 0   | 1    | 0   | 1     |
| 1   | 1   | 1    | 1   | 1     |
Making a K-map: https://www.youtube.com/watch?v=0iQJsKVpSUY&ab_channel=StevenPetryk
## 1-Bit Subtract
[_1 Bit Substract_](https://www.youtube.com/watch?v=7Ell1saTBM4&ab_channel=NesoAcademy)

| A   | B   | Cin | Difference | Cout |
| --- | --- | --- | ---------- | ---- |
| 0   | 0   | 0   | 0          | 0    |
| 0   | 0   | 1   | 1          | 1    |
| 0   | 1   | 0   | 1          | 1    |
| 0   | 1   | 1   | 0          | 1    |
| 1   | 0   | 0   | 1          | 0    |
| 1   | 0   | 1   | 0          | 0    |
| 1   | 1   | 0   | 0          | 0    |
| 1   | 1   | 1   | 1          | 1    |
![[1-Bit Subtractor.png]]
## Chaining 1-Bit Adder
A and B are both inputs. The carry-in bit is first routed from the initial carry-in, and then linked from the carry-out bit. the sum is added to a splitter combining each bit together.


# Latch
________
## RS Latch
Remembers 1 bit
![[RS Latch Using NAND.png | 400]] ![[RS Latch Using NOR.png | 400]]

|S|R|Out|
|---|---|---|
|1|1|Stays Same|
|0|1|Sets to 1|
|1|0|Reset to 0|
|0|0|Invalid|
## Gated D-Latch
![[Gated D Latch.png]]

|D|WE (Write Enable)|Out|
|---|---|---|
|0|0|Stays Same|
|0|1|Set to 0|
|1|0|Stays Same|
|1|1|Set to 1|

## Memory
This is a 4x1 memory
- 1 Gated D-Latch per bit of memory
- 4 different addresses: row
- 1 bit at each address: column
![[Memory.png]]We use a decoder and a mux built from a 4-1 decoder to selector between different latches

### Addressability and Address Space
- 4 unique address from 4 different rows
- 1 bit at each address
- total memory = address space * addressability
- a memory component that has 4-bit long address and 1 bit stored at each address. 2^4 possible addresses = 16 (address space)

## D Flip Flop
Gated D-latches updates when WE is 1. The output changes when the WE changes from 0 to 1.![[D Flip Flop.png]]
[SR Flip Flop](https://www.youtube.com/watch?v=QKLWSs3z0C4&ab_channel=TheOrganicChemistryTutor)

## Master-Slave Flip Flop
![[Master Slave Flip Flop.png]]![[Clock Edge and Master Slave.png]]
![[Master Slave Flip Flop More.png]]