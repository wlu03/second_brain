An arrangement of $n$ symbols in a *definite order* is a **permutation** of the $n$ symbols. 

**Example**: How many ways to arrange numbers 1,2,3? 6 ways - $123,321,213,231,132,312$ 

**Example**: How many ways to arrange $1,2,...,n$? $n(n-1)(n-2)...2\cdot1=n!$

## r-permutation
____
The number of ways to arrange $r$ elements from a set of $n$ distinct elements, where each element can only be used once in a particular arrangement. 
$P_{n,r}=\frac{n!}{(n-r)!}$

**Example**: How many ways can you take two symbols from $\{a,b,c,d\}$? $P_{n=4,r=2}=\frac{4!}{(4-2)!}=12$ 
## Repeating Object 
___
You have $n_1$ objects of type 1, $n_2$ objects of type 2, and so on. The number of arrangements for all these $n$ objects is $$\frac{n!}{n_1!n_2!\cdot\cdot\cdot n_k!}$$
**Example**: How many ways can "Mississippi" be arranged. $$\frac{11!}{1!2!4!4!}$$ This is because there is a total of 11 letters containing 1 m, 2 p, 4 i, and 4 s.