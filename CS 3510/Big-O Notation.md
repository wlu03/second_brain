Simplification is important to denote runtime. Instead of reporting that an algorithm takes $5n^3+4n+3$ steps on an input size of $n$. It's simpler to leave out the lower order terms such as $4n$ and $3$. The 5 is also insignificant too. This is because we assume that computer will be that much faster. So instead, we say the algorithm takes $O(n^3)$ time. 

Let $f(n)$ and $g(n)$ as the running times of two algorithms on inputs of size $n$ with function from positive integers to positive reals. We say that $f=O(g)$ ($f$ grows no faster than $g$) if there is a constant $c>0$ such that $f(n)\le c\cdot g(n)$.

## Analogs for $\ge, \le, =$
However, there are some function that perform better when $n$ is smaller than a constant $c$. Let $f_1(n)=n^2$ steps while $f_2(n)=2n+20$. For $n \le 5$, $f_1$ is smaller, therefore $f_2$ is better. $f_2$ scales better as $n$ grows thus: $f_2 = O(f_1)$. In short, $O(\cdot)$ is an analog of $\le$. 

For the analogs of $\ge$, $f=\Omega (g)$ means $g=O(f)$. This means $g$ grows at least as fast $f$.  For the analog of $=$, $f=\Theta (g)$ means that $f$ and $g$ grow at the same rate.

## Rules
1. Multiplicative constants can be omitted: $14n^2$ becomes $n^2$.
2. $n^a$ dominates $n^b$ if $a>b$ for instance $n^2$ dominates $n$. 
3. Any exponential dominate any polynomial: $3^n$ dominates $n^5$ (also for $2^n$)
4. Any polynomial dominates any logarithm: $n$ dominates $(\log n)^3$ 

# General Rule
___
$O(1)<O(\log^\beta n)<O(n^{\alpha})<O(n^{\alpha}\log^\beta n)<O(n^{\beta})<O(2^n)<O(N!)$ for $\alpha < \beta$

## Practice Problems
____
1. In each of the following situation, indicate whether $f=O(g)$ or $f=\Omega(g)$ or both (In which case $f=\Theta(g)$)
	a. $f(n)=n-100,\space g(n)=n-200$
		$f(n)=n-100,\space g(n)=n-200$
		$O(n-100)=O(n), O(n-200)=O(n)$ This is because the constant is ignored for Big-O. 
		Therefore, $f=\Theta(g)$.
	b. $f(n)=n^{1/2},\space g(n)=n^{2/3}$ 
		$f(n)=n^{1/2},\space g(n)=n^{2/3}$ 
		$1/2 \le 2/3$. This means that $f(n) \le g(n)$. Therefore, $f=O(g)$. $n^a$ dominates $n^b$ if $a>b$. 
	c. $f(n)=100n+\log n,\space g(n)=n+(\log n)^2$
		$f(n)=100n+\log n,\space g(n)=n+(\log n)^2$
		This biggest term in both equations is $n$. Ignoring the second term all together, $f=\Theta(g)$. This is because multiplicative constant can be omitted where $100n$ becomes $n$. 
	d. $f(n)=n\log n,\space g(n)=10n \log 10n$
		The equation are equivalent since multiplicative constant are equal. Therefore, $f=\Theta(g)$. 
	e. $f(n)=\log 2n, \space g(n)=\log 3n$
		$O(\log 2n)=O(\log 2)+O(\log n)=O(\log n + constant)=O(\log n)$ 
		$O(\log 3n)=O(\log 3)+O(\log n)=O(\log n + constant)=O(\log n)$ 
		Therefore, $f=\Theta(g)$.
	f. $f(n)=10 \log n, \space g(n)=log(n^2)$ 
		$O(10\log n) =O(\log n)$
		$O(log(n^2))=O(2\log n)=O(\log n)$
		Therefore, $f=\Theta(g)$ 
	g. $f(n)=n^{1.01}, \space g(n)=n \log^2 n$ 
		Generally, any polynomial dominates any logarithm. Therefore $f>g$ where $f=\Omega (g)$.
	h. $f(n)=n^2/\log n, \space g(n)=n(\log n)^2$ 
		$f(n)= n^2$ grows faster than $g(n)=n(\log n)^2$. Therefore, $f=\Omega (g)$.
	i. $f(n)=n^{0.1}, \space g(n)=(\log n)^10$
		Generally, any polynomial dominates any logarithm. Therefore $f>g$ where $f=\Omega (g)$.
	j. $f(n)=(\log n)^{\log n}, \space g(n)=n/\log n$
		Assuming that $1/ \log n$ is a constant then $n$ would grow bigger than any logarithm. Therefore $f<g$ where $f=O(g)$.
	k. $f(n)=\sqrt{n}, \space (\log n)^3$
		Generally, any polynomial dominates any logarithm. Therefore $f>g$ where $f=\Omega (g)$.
	l. $f(n)=n^{1/2}, \space 5^{\log _2 n}$ 
		Any exponential dominates any polynomial. Therefore $f<g$ where $f=O(g)$ 
	m. $f(n)=n2^n, \space g(n)=3^n$
		$3^n$ grows faster than $n2^n$. Therefore $f<g$ where $f=O(g)$. 
	n. $f(n)=2^n, \space g(n)=2^{n+1}$
		$O(2^{n+1})=O(2 \cdot 2^n)=O(2^n)$ The constant is dropped so $f=g$ where $f=\Theta (g)$ 
	o. $f(n)=n!, \space g(n)=2^n$ 
		Factorial functions grow faster than exponential. Therefore $f>g$ where $f=\Omega (g)$.
	p. $f(n)=(\log n)^{\log n}, \space g(n) =2(\log n)^2$
		$O(2(\log n)^2)=O((\log n)^2)$. Since $\log n>2$,  then $f>g$ which $f = \Omega (g)$.
	q. $f(n)=\sum_{i=1}^{n}i^k, \space g(n)=n^{k+1}$ 
		$f(n)=\sum_{i=1}^{n}i^k= 1^k + 2^k + 3^k +...+n^k$. All the constants are ignored where $O(f)=O(n^k)$.
		$O(g)=O(n^{k+1})=O(k\cdot n^k)=O(n^k)$. 
		Therefore $f=g$ where $f=\Theta g$.
2. Show that if $c$ is a positive real number, then $g(n)=1+c+c^2+...+c^n$ is 
	a. $\Theta(1)$ if $c<1$
		By taking the limit $$\lim_{n \rightarrow \infty} \sum_{i=0}^{n}c^i=\frac{1}{1-c}$$ for $c<1$. This limit is constant, so $g=\Theta(1)$.
	b. $\Theta(n)$ if $c=1$ 
		By using example, you can observe that $\Theta(n)$ if $c=1$. 
		$$n=1, g(1)=1+1^1=1+1=n+1$$
		$$n=2, g(2)=1+1^1+1^2=2+1=n+1$$
		$$n=3, g(3)=1+1^1+1^2+1^3=3+1=n+1$$
		For any case where $n$ equals some integer, $g(n)$ will always result in $n+1$. This is true because Big-O notation ignores constants. 
	c. $\Theta (c^n)$ if $c>1$
		Each term $c^i$ is dominated by $c^n$ for $i<n$, so $g(n)=\Theta(c^n)$
3. The Fibonacci numbers $F_0,F_1,F_2,...,$ are defined by the rule 
   $$F_0=0,F_1=1, F_n=F_{n-1}+F_{n-2}$$
	a. Use induction to prove that $F_n \ge 2^{0.5n}$ for $n\ge6$.
		**Prove**:  $F_n \ge 2^{0.5n}$ for $n\ge6$.
		**Basis**: For $n=6, n=7$, $F_6=8, F_7=11.3$. For all these value $F_n \ge 2^{0.5n}$ holds true.
		**Induction**: Assume true that $n=k+2$ for $F_n\ge2^{0.5n}$. Then
		$$F_{k+2}=F_k+F_{k+1}$$
		$$\ge2^{0.5k} +2^{0.5k+0.5}=\frac{2^{0.5}+1}{2}2^{0.5k+1}$$
		$$\ge2^{0.5(k+2)}$$
		Therefore by induction $F_n\ge 2^{0.5n}$ for $n\ge6$. 		
	b. Find a constant $c<1$ such that $F_n \le 2^{cn}$ for all $n\ge0$. 
	c. What is the largest $c$ you. can find for which $F_n=\Omega (2^{cn})$?
	   