The product of two complex numbers
$$(a+bi)(c+di)=ac-bd+(bc+ad)i$$ can be done in three instead of four real number multiplication $$bc +ad=(a+b)(c+d)-ac-bd$$
## Bit Multiplication for Integers
____
Suppose that $x$ and $y$ are two $n$-bit integers, and assume for convenience that $n$ is a power of 2. As the first step toward multiplying $x$ and $y$, split each of them into their left and right halves, which $n/2$ bits long. For example, if $x=10110110_2$ then $x_L=1001_2, x_R=0110_2$, and $x=1011_2 \times 2^4 + 0110_2$ The product of $x$ and $y$ can be written as $$xy=(2^{n/2}x_L+x_R)(2^{n/2}y_L+y_R)=2^nx_Ly_L+2^{n/2}(x_Ly_R+x_Ry_L) + x_Ry_R$$
**Analysis of Complexity and Recurrence**
The additions take linear time and the multiplication by powers of 2 are left shifts. The four $n/2$-bit multiplication can be done recursively (four subproblems of half the size). Evaluating the preceding expression in $O(n)$ time. The overall running time on $n$-bits inputs gives the recurrence relation $$T(n)=4T(n/2)+O(n)$$
Using the [[Master Theorem]] the runtime is $O(n^2)$. 

### Optimization of Bit Multiplication
___
Instead of doing the four $n/2$-bit multiplications, we can just do three: $x_Ly_L,x_Ry_R$ and $(x_L+x_R)(y_L+y_R)$, since $x_L y_R +x_R y_L = (x_L +x_R )(y_L +y_R )−x_L y_L −x_R y_R$. The algorithm has an improved running time of $$T(n)=3T(n/2)+O(n)$$This leads to a lower time bound of $O(n^{1.59})$. 

**Algorithm**
```
function multiply(x,y) 

Input: Positive integers x and y, in binary 
Output: Their product 

n = max(size of x, size of y) 
if n = 1: return xy 

xL , xR = leftmost ceil(n/2), rightmost ceil(n/2) bits of x 
yL , yR = leftmost ceil(n/2), rightmost ceil(n/2) bits of y 

P1 =multiply(xL , yL ) 
P2 =multiply(xR , yR ) 
P3 =multiply(xL + xR , yL + yR ) 

return P1 × 2^n + (P3 − P1 − P2) × 2^{n/2} + P2
```