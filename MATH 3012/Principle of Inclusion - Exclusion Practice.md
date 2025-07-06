# Problem 1)
Let $$X=\{ x_1,x_2,x_3,...,x_8\} \text{ and } Y=\{y_1,y_2,...,y_5\}$$
Determine the number of functions $f : X \rightarrow Y$ that have exactly 3 elements in their range.

Let $c_i$ represent that fact that $y_i$ is **not** in the range of $f$. Since there 5 elements in the codomain, and we want the function to have exactly 3 elements in its range. There must be 2 of the 5 values missing. Thus only 2 of the $c_1,c_2,...,c_5$ must hold true.

$$E_2=S_2-\binom{2+1}{1}S_3+\binom{2+2}{2}S_4-\binom{2+3}{3}S_5$$
$$E_2=S_2-\binom{3}{1}S_3+\binom{4}{2}S_4-\binom{5}{3}S_5$$
$S_2 = \binom{5}{2}(3)^8$
	This reads: There is 5 elements to choose 2 not in the range. There is 3 other elements that can map to whatever values of $x$. 
$S_3=\binom{5}{3}(2)^8$
$S_4=\binom{5}{4}(1)^8$
$S_5=\binom{5}{5}(0)^8$ 

$$E_2=\binom{5}{2}(3)^8-\binom{3}{1}(\binom{5}{3}(2)^8)+\binom{4}{2}(\binom{5}{4}(1)^8)-\binom{5}{3}(\binom{5}{5}(0)^8)$$

$$E_2=\binom{5}{2}(3)^8-\binom{3}{1}\binom{5}{3}(2)^8+\binom{4}{2}\binom{5}{4}$$