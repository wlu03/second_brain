# Alternating/Diagonal Vanishing
- Sign Change property: By definition an alternating polynomial satisfies $$A(y,x,z)=-A(x,y,z)$$
Setting $x=y$ makes the left and right sides identical forcing $A(x,x,z)=0$

**Alternating Polynomial**: In $n$ variables $x_1,x_2,...,x_n$ is one that changes sign under any transpositions of two variables. 
*Ex:*
	$f(x,y)=x-y$
	$f(y,x)=y-x = -(x-y)=-f(x,y)$
____
# Factor Theorem (1-var)

If a polynomial $f(x) \in Q[x]$ satisfies $f(a)=0$ ($a$ is a root/zero) then (x-a) divides $f(x)$. 

*Ex*
	I view $A(x,y,z)$ as a polynomial in x (with y, z fixed). Since $A(x,x,z)=0$, we get $(x-y)|A(x,y,z)$
____
# Pairwise Co-prime Divisibility in a UFD
If a polynomial is divisible by each of several pairwise relatively prime factors then its divisible by their product.

**Pairwise Co-prime**: A collection of integers are called pairwise co-prime if every two distinct elements in the collection share no prime factors. $gcd(x,y)=1$ for two arbitrary integers $x$ and $y$. 
*Ex*
	{2,3,5,7}: every pair is prime to each other
	{4,9,25}: gcd(4,9)=1 and all permutations of gcd within the set.

Two polynomial $f$ and $g$ in a UFD like ($K[x,y,z]$) are called co-prime when their greatest common divisor is a unit.
	$(x-y)$ and $(z-x)$ are both irreducible linear forms
	They are not associates of one another (there is no constant $c$ with $x-y=c(z-x)$)
	Hence the polynomial that can divide both of them is a constant
Thus: $gcd(x-y,z-x)=1$ 
____
# Root-Degree Lemma
A nonzero polynomial of degree $d$ can have at most $d$ distinct roots. By finding $x$ distinct roots, we know that any nonzero solution must be degree $\ge 11$ and contain all those linear factors.
____
# Periodicity Lemma for P(x)
The only polynomial satisfying $S(x+1)=S(x)$ for all $x$ is a constant. Since $S(x+1)-S(x)$ would be then be a nonzero-degree polynomial with infinitely many roots, it must be zero, forcing degree of $S(x)$ be 0. 