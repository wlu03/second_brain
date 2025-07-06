HDL for loop do not behave like software loops. In **Verilog**, `for` loops are used only at **compile time** to generate hardware structure. They are not runtime loops like in software. 

Example
```verilog
for (i = 0; i < N; i++) begin
	sample_buffer[i] <= 0
end
```
- This example initializes all elements of `sample_buffer` to `0`.
- it doesn't generate an actual loop that runs at runtime. The hardware uses for loops for **parallel assignments**. 