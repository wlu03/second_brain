In your **Clash project**, the best place to edit your **circuit description code** is inside the src directory. Typically, the **source files for your hardware descriptions** (Haskell-based Clash code) are located in src/.

**Where to Edit Code?**

1. **Navigate to the src directory.**

- This is where Clash expects to find the main Haskell files that describe your circuit.

2. **Edit or create Haskell files in src/.**

- For example, if you have `src/<FILENAME>.hs`, edit that file to define your circuit components.

3. **Testing Code (tests/ Directory)**

- Your tests/ directory contains files for **unit tests** (unittests.hs) and **doctests** (doctests.hs).
- If you’re writing tests for your circuit, edit these files.

**How to Load and Run Your Code in clashi**
After making changes, you can test your circuit using the Clash interactive shell:

1. Open the Clash interpreter:

```
stack run -- clashi  # If using Stack
```
or
```
cabal run -- clashi  # If using Cabal
```

2. Load your circuit file:

```
:l src/MyCircuit.hs
```

3. If you modify the file, reload it:

```
:r
```


____
In your **Clash project**, you can generate different types of **hardware description languages (HDLs)**, such as **VHDL, Verilog, and SystemVerilog** from your Haskell-based circuit designs.

**Where to Edit Circuit Code?**

1. **Edit your circuit logic inside src/**
- This is where you define your hardware using Haskell functions.
- For example, if you have a file src/MyCircuit.hs, you would define your Clash circuit there.

2. **Generate HDL from Clash Code**
- Once you define your circuit, Clash allows you to convert it into different hardware description languages.

**Generating Hardware Description Languages (HDLs)**

After writing your circuit in Clash, you can generate **VHDL, Verilog, or SystemVerilog** using the following commands inside clashi:


**1. Generate Verilog Code**
```
:verilog
```
- This will generate Verilog files from your Clash circuit.

**2. Generate SystemVerilog Code**
```
:systemverilog
```
- This will generate SystemVerilog files.

  
**3. Generate VHDL Code**
```
:vhdl
```
- This will generate VHDL files.

**Example Workflow**

1. **Write a simple Clash circuit in src/MyCircuit.hs**
```
module MyCircuit where

import Clash.Prelude

-- Simple AND gate
andGate :: Signal System Bool -> Signal System Bool -> Signal System Bool
andGate a b = (&&) <$> a <*> b
```

2. **Start the Clash interpreter**
```
stack run -- clashi
```

3. . **Load the circuit file**
```
:l src/MyCircuit.hs
```

4. **Generate Verilog**
```
:verilog
```
- This will create a verilog/ directory with your generated files.

5. **Check the generated Verilog file**

```
ls verilog/
```

**Where Do the Generated Files Go?**
-  When you run :verilog, :systemverilog, or :vhdl, Clash will create a corresponding folder (e.g., verilog/, systemverilog/, or vhdl/).
- Inside that folder, you’ll find .v, .sv, or .vhdl files that describe your circuit in hardware terms.

**When to Use Each HDL?**
- **Verilog** – Commonly used in FPGA and ASIC design. 
- **SystemVerilog** – An extension of Verilog with advanced features (better for simulation and verification).
- **VHDL** – Often used in aerospace and defense industries due to its strict typing.
