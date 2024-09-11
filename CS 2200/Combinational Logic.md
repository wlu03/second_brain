The output of the circuit is a Boolean combination of the inputs of the circuit. There is no concept of memory. Basic logic gates  (AND, OR, NOT, NOR, NAND) are the building block for circuits. 
![[Combinational Logic All Gates Picture.png]]
## AND
____
**Syntax**: $AB, A\&B, A \cdot B, A \cap B$    

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |
## Inclusive Or
____
**Syntax:** $A+B, A v B, A \cup B, A|B$ 

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |
## Exclusive Or
___
**Syntax**: $A \oplus B$ 

| A   | B   | A XOR B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |
## Negate
___
**Syntax:** $¬A, Ā, A', ~A, !A$ 

| A   | Not A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |
## NAND
____
**Syntax**: $¬(A\& B)$  

| A   | B   | A NAND B |
| --- | --- | -------- |
| 0   | 0   | 1        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 0        |
In the LC 2200, we use `NAND t2, t1, t1` to inverse the bits of the value inside `t1`. If you notice the truth table, when the compared values are the exactly same it inverts the bits. In [[two's complement]], to invert a value to a negative, you must invert the bits and add one. Therefore to complete it, you would do:
```
NAND t2, t1, t1  //invert the bits
ADDI t1, t1, 1   //add 1
```

## NOR
___
**Syntax**: $¬(A | B)$

| A   | B   | A NOR B |
| --- | --- | ------- |
| 0   | 0   | 1       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 0       |
# De Morgan's Law
___
$(A \cdot B)' = A' + B'$

| A   | B   | A NAND B | A'  | B'  | A'+B' |
| --- | --- | -------- | --- | --- | ----- |
| 0   | 0   | 1        | 1   | 1   | 1     |
| 0   | 1   | 1        | 1   | 0   | 1     |
| 1   | 0   | 1        | 0   | 1   | 1     |
| 1   | 1   | 0        | 0   | 0   | 0     |
## Combining Boolean Operators
____
Converting a logical expression to a circuit

| C   | D   | ~D  | C\|(~D) |
| --- | --- | --- | ------- |
| 0   | 0   | 1   | 1       |
| 0   | 1   | 0   | 0       |
| 1   | 0   | 1   | 1       |
| 1   | 1   | 0   | 1       |
![[Combination Logic Figure 1.png]]

| A   | B   | A\|B | ~(A\|B) |
| --- | --- | ---- | ------- |
| 0   | 0   | 0    | 1       |
| 0   | 1   | 1    | 0       |
| 1   | 0   | 1    | 0       |
| 1   | 1   | 1    | 0       |
![[Combinational Logic Figure 2.png]]
![[Combinational Logic Figure 3.png]]
*Use AND gate to combine the two gates* 

# Bitwise Operators
___

| Bitwise Operator | Character |
| ---------------- | --------- |
| AND              | `&`       |
| OR               | `\|`      |
| XOR              | `^`       |
| NOT              | `~`       |
## Bit Mask
Bit masking is the process of getting the processor to ignore the bits that we don't want to work on and only process the digits we want to. Ex: 
```
1011 0101 <- Data 
0011 0000 <- Mask
-----------------
0011 0000 <- Result
```
![[Bitwise Operator Figure 1.png]]
![[Bitwise Operators Figure 2.png]]
