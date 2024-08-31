The ordering of the bytes within the word is called Endianness. With 4 bytes in each word, if the machine is byte-addressable then four consecutive bytes in memory starting at address 100 will have addresses 100, 101, 102, and 103. I'm assuming a word is 32 bits or 4 bytes.

## Example
____

| byte | byte | byte | byte |
| ---- | ---- | ---- | ---- |
| 100  | 101  | 102  | 103  |

| Word containing 4 bytes |
| ----------------------- |
| 100-103                 |
Assuming the words at location 100 contains the values `0x11223344`, the individual bytes in the word can be organized in two ways. 

**Big Endian** - MSB of the word containing the value 11 is at address 100.

| 11  | 22  | 33  | 44  |
| --- | --- | --- | --- |
| 100 | 101 | 102 | 103 |
**Small Endian** - LSB of the word containing the value 44 is at address 100.

| 44  | 33  | 22  | 11  |
| --- | --- | --- | --- |
| 100 | 101 | 102 | 103 |
the sending machine is Little-endian and the receiving machine is Big-endian there could even be correctness issues in the resulting network code. It is for this reason, network codes use format conversion routines between host to network format, and vice versa, to avoid such pitfalls. Little endian architecture is assumed. 