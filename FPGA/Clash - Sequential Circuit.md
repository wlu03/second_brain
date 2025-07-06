The `register` function is the primary sequential building block to capture *state*. It's used by one of the `Clash.Prelude` functions. 

``` haskell
macT acc (x,y) = (acc', o) 
	where
		acc' = ma acc (x,y) -- Update state by multuplying x and y, then adding to acc
		o    = acc          -- output the previous state
```

without loss of sharing we can also write
``` haskell
macT acc inp = (ma acc inp, acc)
```
- `acc` is the current state of the circuit
- `(x,y)` is the input
- `acc'` is the updated, or next, state
- `o` is the output
Type Signature: 
``` haskell
macT :: Num a => a -> (a, a) -> (a, a)
```
This function is **purely combinational** because it just maps inputs to outputs without any internal clock-driven behavior.

## Creating Sequential Circuit Using `mealy`
To make `macT` sequential, we use the `mealy` function from `Clash.Prelude`:

``` haskell
mealy
  :: (HiddenClockResetEnable dom, NFDataX s)
  => (s -> i -> (s,o))  -- Transition function (Mealy Machine)
  -> s                  -- Initial state
  -> (Signal dom i -> Signal dom o)  -- Sequential circuit

```

``` haskell
`mac inp = mealy macT 0 inp`
```
- use `macT` as the transition function
- sets initial state to 0
- converts it to a sequential circuit

The `Clash.Prelude` library contains a function to create sequential circuit from a combinational circuit that has the same Mealy machine type.