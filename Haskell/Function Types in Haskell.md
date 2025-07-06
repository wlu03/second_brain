``` haskell
add :: (Num a) => a -> a -> a

add x y = x + y
```
- `add` is function name
- `::` separates the function name from its type
- `(Num a)` is a **type constraint** that ensures `a` belongs to a `Num` type-class like an integer
- `a -> a -> a` is the function type where the first and second `a` are parameters and the last `a` is the return value
- it is **curried**, meaning `add 5` is still a function waiting for another argument
``` 
ghci> add 5 5
10

ghci> add 5 1
6
```

## Partial Function
Partial function application means that it only supplies some arguments to a function which results in a new function waiting for the remaining parameters. 

``` haskell
add5 :: (Num a) => a -> a
add5 y = add 5 y
```
- `add5`  takes in a number and returns a number
- it uses `add 5` which partially applies the `add` function by fixing `x=5`. 
- `y` is a free variables as `add5` requires only one arg.
- calling `add5 3` is the same as `add 5 3`