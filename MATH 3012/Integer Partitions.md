An integer partition of a positive integer $n$ is a way of writing $n$ as a sum of positive integer, where the order of the summands dont matter. For example, partitions of 4:
- 4 
- 3+1
- 2+2
- 2+1+1
- 1+1+1+1
The notation $p(n)$ is used to denote the number of partitions of n with $p(0)=1$ 

A generating function for partition is given by: $$f(x)=\Pi_{i=1}^{\infty}\frac{1}{1-x^i}$$
Partition into Odd Summands
$$f(x)=\Pi_{i=1}^{\infty}\frac{1}{1-x^{2i+1}}$$Partition into Even Summands
$$f(x)=\Pi_{i=1}^{\infty}\frac{1}{1-x^{2i}}$$
Partitions into Distinct Summands
$$f(x)=\Pi_{i=1}^{\infty} (1+x^i)$$