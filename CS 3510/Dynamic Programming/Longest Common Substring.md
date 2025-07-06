**Motivation**: Take two string "EL GATO" and "GATER". They both share the letter E which is a common substring. They also share the string "GAT" which is the **longest** common substring. Given the two strings, we want to find the **longest common substring (LCS)** 

Let $a_1,a_2$ be any string with $a_1y,a_2y$ having the longest common suffix $y$. What is the longest common substring $a_1yb_1, a_2yb_2$. Let there be a 2D dimensional table $T$ indexed by the indices $i$ and $j$. Index $i$ is the index of the first string and $j$ is the index of the second. $$T[i,j]=T[i-1,j-1]+1 \space \text{if}\space x_i= y_j$$
$$T[i,j]=0 \space \text{if}\space x_i\neq y_j$$
**Pseudocode**
```
def lcs(x,y) # both x and y are strings
	initialize the dp table of size |x|+1 and |y|+1 and fill in with 0s
	max = 0
	maxpos = (0,0)

	for i in 1...(|x|+1)
		for j in 1...(|y|+1)
			if x[i-1] = y[j-1]
				dp[i,j] = dp[i-1,j-1] + 1
			else
				dp[i,j] = 0
			if max < dp[i,j]
				max = dp[i,j]
				maxpos = i,j
```

![[LCS Table.png| 400]]
*LCS Table of GATER and ELGATO* 

**Runtime**: The runtime of this LCS algorithm is $O(n \times m)$ and it takes $O(1)$ for each cell in the 2D array. 