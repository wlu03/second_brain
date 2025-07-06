`register` function is one of the sequential primitives
```haskell
register 
 :: (HiddenClockResetEnable dom, NFDataX a)
 => a
 -> Signal dom a
 -> Signal dom a

```
- `HiddenClockResetEnable dom`: Means the register function assume an implicit clock, rest, and enable signal to the domain `dom`.
- `NFDataX a`: Constraint means the type `a` supports deep evaluation
- The type of arguments (`a` and `Signal dom a`)
- The return type (`Signal dom a`).
All sequential circuits work on values of type `Signal`. Combinational circuits always on work on values of **not** type `Signal`. A `Signal` is an (infinite) list of sample where the samples correspond to the values of the `Signal` at discrete ticks of the clock. You can only modify `Signal` values through a set of primitives such as the register function above.



```haskell
sampleN @System 4 (register 0 (pure (8 :: Signed 8)))
```
### **Understanding `register` in Clash**

The function **`register`** behaves as a **synchronous register** with an **initial value** and an **input signal**. It updates on every clock cycle **but with a one-cycle delay** because registers only update after the clock edge.

#### **Breaking Down `register 0 (pure 8)`**
- `register 0` means:
    - **Cycle 1:** Outputs **initial value** `0`.
    - **Cycle 2:** Outputs **previous input** (which was `0` at time 0).
    - **Cycle 3:** Outputs **previous input** (which was `8` at time 1).
    - **Cycle 4:** Outputs **previous input** (which was `8` at time 2).

---

### **Step-by-Step Execution**

|**Cycle**|**Register Output**|**Input Signal (`pure 8`)**|
|---|---|---|
|1st|`0` (initial value)|`8`|
|2nd|`0` (previous cycle's input)|`8`|
|3rd|`8` (previous cycle's input)|`8`|
|4th|`8` (previous cycle's input)|`8`|

Thus, the **correct result is**:

```haskell
[0, 0, 8, 8]
```

### **Why Two Zeros?**

Registers in Clash have **one-cycle delay** due to synchronous behavior. Since the input (`pure 8`) does not affect the register immediately, the first cycle holds the initial value (`0`), and the second cycle still outputs `0` before picking up `8` in the third cycle.
### **Key Takeaways**

- `register i s` **outputs `i` in the first cycle**.
- On subsequent cycles, it **outputs the previous cycle’s input**.
- Since `register` delays updates by **one clock cycle**, it takes two cycles before showing the constant `8`.

```haskell
sampleN @System <ARR_SIZE> (register <INITIAL_VALUES> (pure (<INPUT> :: Signed 8)))
```