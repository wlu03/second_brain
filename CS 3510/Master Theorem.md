**Theorem**: If $T(n)=aT(\lceil \frac{n}{b} \rceil) +O(n^d)$ for some constant $a>0, b>1,$ and $d\ge0$, then
$$Case \space 1:T(n)=O(n^d) \space\space if \space \space d>\log_ba$$
$$Case \space 2:T(n)=O(n^d\log n) \space\space if \space \space d=\log_ba$$
$$Case \space 3:T(n)=O(n^{\log_ba}) \space\space if \space \space d<\log_ba$$
- The size of the subproblems decrease by a factor of $b$ with each level of recursion
- It reaches the base case after $\log_b (n)$ levels. This is the height of the recursion tree
- The branching factor is $a$, so the $k$-th level of the tree is made up of $a^k$ subproblems each of size $n/b^k$ 
![[Master Theorem.png]]
- The total work done at this level is $a^k \times O(\frac{n}{b^k})^d = O(n^d) \times (\frac{a}{b^d})^k$
- As $k$ goes from 0 (the root) to $\log _b n$ (the leaves), these numbers form a geometric series with the ratio $a/b^d$
- Finding the sum of the series in big-O comes down to three cases
	1. The ratio is less than 1. The series is **decreasing**, and its sum is just given by its first term, $O(n^d)$
	2. The ratio is greater than 1. The series is **increasing** and its sum is given by its last term $O(n^{\log_ba})$ 
	3. The ratio is exactly 1. In the case of all $O(\log n)$ terms of the series are equal to $O(n^d)$

## Example
For each of the following recurrence, give an expression for the runtime $T(n)$ if the recurrence can be solve with the Master Theorem. 
1. $T(n)=3T(\frac{n}{2})+n^2$ 
	$d=2, b=2, a=3$
	$2 > \log_2(3)$ 
	Therefore, $T(n)=O(n^d)=O(n^2)$
2. $T(n)=4T(\frac{n}{2})+n^2$ 
	$d=2, b=2, a=4$
	$2=2$
	Therefore, $T(n)=O(n^d\log n)=O(n^2 \log(n))$
3. $T(n)=16T(n/4)+n$
	$d=1, b=4, a=16$
	$1 <4$ 
	Therefore, $T(n)=O(n^{\log_b(a)})= O(n^{\log_4 (16)})=O(n^2)$ 
1. $T (n) = 2^nT(n/2) + n^n$ 
	The cannot be solved using the masters theorem because $a$ is not a constant.