The famous fibonacci sequence is known as the sum of its immediate predecessors. The numbers: $$0,1,1,2,3,5,8,13,21,34,..$$For the $n^{th}$ number, the Fibonacci number can be denoted as $$F_n=F_{n-1}+F_{n-2}$$ where $n>1$. If $n=1$, then $F_n=1$. If $n=0$, then $F_n=0$.

## Exponential Algorithm
To solve for the $n^{th}$ number in the Fibonacci sequence, a naive solution is to use the following algorithm

```
function fib1(n) 
	if n=0: return 0
	if n=1: return 1
	return fib1(n-1) + fib(n-2)
```

Let $T(n)$ be the number of computer steps needed to compute $fib(n)$. If $n$ is less than 2, $T(n) \le 2$ for $n \le 1$. For large values of $n$, there are two recursive invocations of $fib$, taking $T(n-1)$ and $T(n-2)$, plus three computer steps to check the value of $n$ and a final addition. The computer steps needed would be $$T(n)=T(n-1)+T(n-2)+3 \space for \space n>1$$The runtime for the algorithm grows as fast as the Fibonacci numbers. For example, to compute $F_{200}$ the algorithm will take $T(200)\ge F_{200} \ge 2^{138}$ elementary computers steps. 
## Polynomial Algorithm
A more sensible way to store intermediate result would be to store the value as soon they are computed.
```
function fib2(n)
	if n=0: return 0
	create an array f[0,...,n]
	f[0] = 0, f[1] = 1
	for i=2,...n:
		f[i] = f[i-1] + f[i-2]
	return f[n]
```
This algorithm for Fibonacci numbers is linear.