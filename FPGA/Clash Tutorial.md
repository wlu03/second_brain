Link: https://hackage.haskell.org/package/clash-prelude-1.8.1/docs/Clash-Tutorial.html#g:12

**Clash** is a functional hardware description language that borrows syntax and semantics from the functional programming language **Haskell**. 
- familiar structural design to both combinational and syncrhous sequential circuits. 
- Clash complier transforms high level descriptions to low level VHDL, Verilog or SystemVerilog

## Features
- [[Strongly typed]] - very high degree of type inference enabling safe and fast prototyping
- Interactive REPL - load design in an interpretor and read all components without a test bench
- Compile designs for fast simulation
- High-order functions with type inference
- Synchronous sequential circuit design based on streams of values called **Signals**, leads to natural description of feedlback looks
- Multiple clock domains
____

**Key Difference: Functional vs. Structural View**
- In **Haskell**, functions describe computations: applying a function means evaluating an expression.
- In **Clash**, functions describe **hardware components**: applying a function means **instantiating a hardware block**.

**No Infinite Recursion in Hardware:**
- A Haskell function can be recursively defined (like fib n = fib (n-1) + fib (n-2)), but in hardware, this would require **infinite depth**, which is **impossible** to synthesize into a circuit.
- Clash restricts general recursion to avoid infinite hardware structures.

``` haskell
counter = s
  where
    s = register 0 (s+1)
```
The above definition, which uses value-recursion, _can_ be synthesized to a circuit by the Clash compiler.

[[Running Clash]]
[[Editing and Running a Clash File]]
[[Clash - Num]]
[[Clash - Sequential Circuit]]
[[Generating VHDL]]  