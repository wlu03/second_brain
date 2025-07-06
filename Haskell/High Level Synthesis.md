Verilog is a programming language to describe chip design. It means that engineers can write code that would be compiled into the physical layout of a chip than drawing the details. **Register-Transfer Level (RTL) Abstractions** is one of these abstractions. Designers specify **registers** (storage elements in chips) and **operations** (operations performed on data stored in registers). This is such that the physical implementations were trivial compared to the behaviors of the registers and operations. 

Electronic Design Automation (EDA) tools take the RTL descriptions and automatically translate them into digital circuit models. HLS is another step in abstraction that enables a designer to focus on larger architectural questions rather than individual registers and operations. One of the first tools to implement such a flow was based on behavioral Verilog and generated an RTL level architecture also captured in Verilog. Now tools use C/C++ as input language.

High-level synthesis (HLS) is the process of converting an algorithm described in a high-level programming language (such as C, C++, or SystemC) into a hardware description at the register-transfer level (RTL). Essentially, HLS automates the translation of software-like code into a digital hardware implementation that can be used for designing FPGAs or ASICs.

Example
```
int adder(int a, int b) {
	return a+b;
}
```
- HLS tool examines the function identifying inputs (a and b)
- The tool maps the addition operation into arithmetic unit
- hardware implementation is optimized to use appropriate digital components to perform operation 
- tool generates the corresponding RTL code (verilog) which can be further synthesized to physical circuit.

HLS does things automatically that RTL designer does manually:
- analyzes and exploits the [[Concurrency |concurrency]] in an algorithm
- inserts registers as necessary to limit critical path and achieve a desired clock freq.
- generates control logic that directs the data path
- implements interface to connect to the rest of the system
- maps data onto storage elements to balance resource usage
- maps computation onto logic elements performing user specified and automatic optimizations 