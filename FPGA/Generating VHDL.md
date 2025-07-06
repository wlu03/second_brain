### 1. **Module Definition**

```haskell
module MAC where
```

This declares a module named `MAC`, which defines a **Multiply-Accumulate (MAC)** circuit.

---
### 2. **Imports**

```haskell
import Clash.Prelude
```

- This imports `Clash.Prelude`, which provides Clash-specific functionality for describing circuits.

---

### 3. **Multiply-Accumulate Function**

```haskell
ma acc (x,y) = acc + x * y
```

- `ma` takes an accumulator (`acc`) and a tuple `(x, y)`.
- It computes the **multiply-accumulate operation**: $\text{new acc} = \text{acc} + (x \times y)$
- This is a standard MAC operation often used in digital signal processing (DSP).

---

### 4. **State Transition Function for `mealy`**

```haskell
macT acc (x,y) = (acc',o)
  where
    acc' = ma acc (x,y)
    o    = acc
```

- This function is used in a **Mealy machine** (a type of finite state machine with outputs depending on states and inputs).
- **Inputs:** `(acc, (x, y))`
- **Computation:**
    - `acc'` is the new accumulated value using `ma acc (x, y)`.
    - `o` (the output) is the **previous** accumulator value.
- **Returns:** A tuple `(new_state, output)`, where:
    - `new_state = acc'`
    - `output = acc` (i.e., the previous accumulator value)

---

### 5. **Defining the `mac` Circuit**

```haskell
mac xy = mealy macT 0 xy
```

- This defines `mac` using `mealy`, which is a function in Clash to define **stateful** circuits.
- **Initial State:** `0`
- **State Transition Function:** `macT`
- **Input:** A stream of `(x, y)` pairs (a `Signal` of tuples).
- **Output:** A `Signal` of accumulated values.

**How it works:**
- The **first output** is `0` (initial state).
- The **next output** is the accumulator before the current `(x, y)` multiplication.
- This is useful for **pipelining** since the output lags behind the computation.

---

### 6. **Top-Level Entity (Exposing MAC as a Hardware Component)**

```haskell
topEntity
  :: Clock System
  -> Reset System
  -> Enable System
  -> Signal System (Signed 9, Signed 9)
  -> Signal System (Signed 9)
topEntity = exposeClockResetEnable mac
```

- `topEntity` is the entry point for Clash to generate **hardware (VHDL/Verilog)**.
- **Parameters:**
    - `Clock System`: Clock signal for synchronization.
    - `Reset System`: Reset signal to initialize the circuit.
    - `Enable System`: Enable signal to control when the circuit runs.
    - `Signal System (Signed 9, Signed 9)`: Input signal of **signed 9-bit integer pairs** (multiplication operands).
- **Returns:** `Signal System (Signed 9)`, the accumulated output.

**Purpose:**

- `exposeClockResetEnable` makes the `mac` function available as a **hardware module** that can be instantiated with a clock, reset, and enable signals.

---

### **Summary**

This module defines a **Multiply-Accumulate (MAC) circuit** using a **Mealy machine** in Clash:

- It continuously takes a pair of signed 9-bit numbers `(x, y)`.
- It computes the **accumulation of their product**.
- The output at any time is the **previous accumulator value**.
- The module is **ready to be synthesized into hardware (FPGA/ASIC)**.


## `topEntity`
- This is the starting point for the clash compiler to transform your circuit description into a VHDL netlist. It must meet the following restrictions in order for the clash compiler to work:
	- Monomorphic
	- First-order
	- expose Hidden clock and reset arguments

- Now you can create a [[Circuit Testbench]] for the generated HDL
- You want to compare post-synthesis / post-place&route behavior to that of the behavior of the original generated HDL.
- Need representative stimuli for your dynamic power calculations.
- Verify that the HDL output of the Clash compiler has the same behavior as the Haskell / Clash specification.