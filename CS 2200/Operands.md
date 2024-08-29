Processor support multiple precision in the instruction set: word, half-word, and byte. Word refers to maximum precision the architecture can support. Assume word is 32-bits, half word is 16 bits and byte is 8 bits. They respectively map to int, short, char in most C implementations. Instruction set could include instruction at multiple precision levels of operands such as:

```
ld r1, offset(rb); load a word at address rb+offset into r1 

ldb r1, offset(rb); load a byte at address rb+offset into r1 

add r1, r2, r3; add word operands in registers r2 and r3 and place the result in r1 

addb r1, r2, r3; add byte operands in registers r2 and r3 and place the result in r1
```