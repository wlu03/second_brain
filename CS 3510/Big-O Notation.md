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

