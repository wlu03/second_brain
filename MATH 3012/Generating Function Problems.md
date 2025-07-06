**Problem 1)** Find a generating function (GF) that gives the number of integer solutions to $$y_1+y_2+y_3+y_4=N$$ where $y_i \ge 0$ and 
- $y_1$ is odd
- $y_2$ is even
- $y_3 \le 4$ 
- $y_4 > 7$
$$f(x)=(\sum_{y_1})(\sum_{y_2})(\sum_{y_3})(\sum_{y_4})$$
$y_1$ is odd and $y_1 \ge 1$ 
$$y_1:\sum_{i=0}^{\infty} x^{2i+1} = x+x^3+x^5+...$$
$y_2$ is even and $y_2 \ge 0$ 
$$y_2:\sum_{i=0}^{\infty} x^{2i} = 1+x^2+x^4+...$$
$y_3$ 
$$y_3:x^0+x^1+x^2+x^3+x^4$$

$y_4 > 7, y_4\ge8$ 
$$y_4:\sum_{i=8}^{\infty}x^i =x^8+x^9+...$$
The generating function is: $$f(x)=(\sum_{i=0}^{\infty} x^{2i+1}) (\sum_{i=0}^{\infty} x^{2i+1}) (x^0+x^1+x^2+x^3+x^4) (\sum_{i=8}^{\infty}x^i)$$
**Problem 2)**: A student wants N chicken nuggets. The restaurant sells nuggets in boxes of 2, 3, and 7. How many ways can she order N nuggets. 
$$2a+3b+7c=N$$where $a,b,c \ge 0$ represents the number of boxes of 2, 3, and 7. 

2a: 0, 2, 4, 6 
$x^0+x^2+x^4+...=\sum_{i=0}^{\infty}x^{2i}$

3b: 0, 3, 6, 9 
$x^0+x^3+x^6+...=\sum_{j=0}^{\infty}x^{3j}$

7c: 0, 7, 14, 21
$x^0+x^7+x^{14}+...=\sum_{k=0}^{\infty}x^{7k}$

The generating function (GF) is $f(x)$ which is the product of the individual generating functions $$f(x)=(\sum_{i=0}^{\infty}x^{2i})(\sum_{j=0}^{\infty}x^{3j})(\sum_{k=0}^{\infty}x^{7k})$$
# Rook Polynomial
The rook polynomial is the generating function for the number of ways (sequence) to place non attacking rooks on a general board.

The rook polynomial $r(C,x)$ for a board $C$ can be written as $$r(C,x)=\sum_{k=0}^{\infty}r_kx^k$$ where $r_k$ is the number of ways to place $k$ non-attacking rooks on the board

**Problem 1)**: Find the rook polynomial for the $2\times 1$ board.
$r_0=1$, zero ways to put 0 rook
$r_1=2$, two ways to put 1 rook
$r_2=r_3=...=r_n=0$, ways to put 2 to n rooks

**Sequence**: $r_0,r_1,r_2,r_3,...=1,2,0,0,0,...$
The rook polynomial is $$r(C,x)=1+2x$$
**Problem 2)**: Find the rook polynomial for the $2 \times 2$ board.
$r_0=1$, zero ways to put 0 rook
$r_1=4$, 4 ways to place 1 rook
$r_2=2$, 2 ways to place 2 rooks
$r_3=...=r_n=0$, ways to put 3 to n rooks

**Sequence**: $r_0,r_1,r_2,r_3,...=1,4,2,0,0,...$
The rook polynomial is $$r(C,x)=1+4x+2x^2$$
**Problem 3)**: Find the rook polynomial for the board where rooks are not allowed in the shaded squares. 
![[rook polynomial figure 1.png| 200]]
$r_0=1$
$r_1=6$
$r_2=8$
$r_3=2$

$r(C,x)= 1+6x+8x^2+2x^3$

**Problem 4)**: Rook polynomial for a $5 \times 5$ board. 
$r_0=1$
$r_1=25$
$r_2$: 
	**First Method:**
	There are $5\times 5$ choices for the first rook and $4 \times 4$ choices for the second rook. Since order doesn't matter divide by 2! $\frac{25 \times 16}{2}=200$
	**Second Method:**
	Choose 2 rows from 5 $\binom{5}{2}$ ways
	Choose 2 columns from 5 $\binom{5}{2}$ ways
	There is 2! ways to pick the two rooms. 
	$\binom{5}{2}\binom{5}{2}2!=200$
$r_3: \binom{5}{3}\binom{5}{3}3!=600$
$r_4: \binom{5}{4}\binom{5}{4}4!=600$
$r_5: \binom{5}{5}\binom{5}{5}5!=120$

$r(C,x)=1+25x+600x^2+600x^3+600x^4+120x^5$
 	


## Disjoint Sub-Board and Multiplicative Property
If a board can be split into disjoint sub-boards (meaning they share no common rows or columns) then the overall rook polynomial is the product of the individual rook polynomial.
![[rook polynomial figure 2.png | 400]]

![[Screenshot 2025-03-10 at 5.18.47 AM.png | 400]]
Finding the rook polynomial (4)

Let S be the set of all unrestricted arrangements of the 4 rooks. 
$|S|=5\times 4\times 3\times 2=120$
Define $c_i$ where $R_i$ is placed in a forbidden position. 

$N(\overline{c_1c_2c_3c_4})=|S|-S_1+S_2-S_3+S_4$

$N(c_1)$:
	Count arrangements where $R_1$ is placed in $T_1$ or $T_2$.
	$T_1$: The remaining rooks can be placed in $R_3,R_3,R_4$ are placed in the remaining 4 columns of non-forbidden: $4\times 3\times 2=24$
	$T_2$: 24
$N(c_2)$: 24
$N(c_3)=N(c_4)$: 48
...

Or you can divide it up into the two section $C_1, C_2$ 
![[Screenshot 2025-03-10 at 5.27.49 AM.png]]
$r(C_1,x)=1+3x+x^2, r(C_2,x)=1+4x+3x^2$
Thus, the rook polynomial is for forbidden is: $r(C_1,x) \cdot r(C_2,x)=1+7x+16x^2+13x^3+3x^4$
**NOT COMPLETE**
# Closed Form (GFs) 

**Problem 1)**: Given $y_1+y_2+...+y_n=k$ where $y_i \ge 0$, how many integer solutions are there?
$$f(x)=(\sum_{i=0}^{\infty} x^i)^n = (\sum_{i=0}^{\infty}x^i)(\sum_{i=0}^{\infty}x^i)(\sum_{i=0}^{\infty}x^i)...(\sum_{i=0}^{\infty}x^i)$$
The number of solutions is the coefficient of $x^k$. Since $(\sum_{i=0}^{\infty}x^i)=\frac{1}{1-x}$
$$f(x)=(\frac{1}{1-x})^n = \sum_{i=0}^{\infty}\binom{n+i-1}{i}x^i$$$$\frac{1}{1-x}$$
## Shift and Subtract
A generating function is a formal power series where the coefficients of $x^n$ represents the $n$th term of a sequence. For example, the gf of the sequence $1,1,1,1,...$ is $S=1+x+x^2+x^3+...$

The idea is to multiple the generating function by $x$ to shift the series and then subtract from original. 

$$S=1+x+x^2+x^3+...$$
$$xS=x+x^2+x^3+...$$
$$S-xS=1\rightarrow (1-x)S=1$$
$$S=\frac{1}{1-x}$$

## Differentiating
Use derivatives to find related sequences. When you differentiate a gf by term, the exponent $n$ comes down as a coefficient

**Example** 
$$\frac{1}{1-x}=1+x+x^2+x^3+...$$
$$\frac{1}{(1-x)^2}=1+2x+3x^2+4x^3+...$$By differentiating with respect to $x$ this gives the sequence $1,2,3,4,...$ 

## Convolution and Multiplication
Two generating functions $f(x)$ for a sequence $a_n$ and $g(x)$ for sequence $b_n$ then the product is a gf for the convolution of the two sequences. 

For $f(x)=\frac{1}{1-x}$ which represents ($1,1,1,1,...$) and $g(x)=\frac{1}{1+x}$ which represents ($1,-1,1,-1,...$) their product is $$\frac{1}{1-x^2}$$ which expands to $1,0,1,0,1,0,..$

A convolution is:
$$c_n=\sum_{i=0}^n a_i b_{n-i}$$

## Partial Fraction
When a gf is a rational function, you can decompose into simpler whose series expansions are known. This helps in finding the coefficient for a specific power $x$

$f(x)=\frac{1}{(x-3)(x-2)^2}=\frac{A}{x-3}+\frac{B}{x-2}+\frac{C}{(x-2)^2}$ 
Solving for the constants $A$, $B$, and $C$ make it easier to identify the series expansion. 