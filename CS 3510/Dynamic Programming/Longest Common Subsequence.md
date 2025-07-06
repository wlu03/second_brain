Subsequences are not contiguous so for example we have $x=a,b,c,b,d,a,b$ and $y=b,d,c,a,b,a$ the subsequence $b,c,b,a$ and $b,d,a,b$ are both valid for the **longest common subsequence**. If we add one character, how does that change our state. Let $X=x_1,...,x_m$, $Y=y_1,...,y_n$, $Z=z_1,...z_k$ where Z is the longest common subsequence. Then if $x_m=y_n$, then $z_k=x_m=y_n$ and $z_1,...,z_k-1$ is the longest common subsequence. If it doesn't equal, then $Z$ remains the LCS. Therefore, the length of $Z$ doesn't change regardless if the current is equal or not. 

Let's define our recurrence $T[i,j]$ is the longest common subsequence of $x_1,...,x_i$ and $y_1,...,y_j$. If either the $i$ or $j$ is a zero, we want zero because there would not be a single subsequence. If the two are equal we want to add that character so we take the character of both string and add it to the LCS. 
$$T[i,j]= 0, \text{if i=0 or j=0}$$
$$T[i,j]=T[i-1,j-1]+1 \space \text{if} \space x_i=y_j$$
$$T[i,j]=max(T[i-1,j],T[i,j-1])\space \text{if} \space x_i\neq y_j$$
**Pseudocode**
```
def lcsubsequence(x,y):
	initialize dp as a table of size |x|+1 by |y|+1 as 0s

	for i in 1...(|x|+1)
		for j in 1...(|y|+1)
			if x[i] = y[j]
				dp[i,j] = dp[i-1,j-1] + 1
			else
				## taking the maxif not equal
				if dp[i, j-1] < dp[i-1,j]
					dp[i,j] = dp[i-1,j]
				else
					dp[i,j] = dp[i,j-1]
``` 

![[Longest Common Subsequence.png | 400]]
*Longest Common Subsequence Table*

**Runtime**: The runtime is $O(n \times m)$ with $O(1)$ for each entry. 