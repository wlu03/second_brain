Suppose you have an input of one string $x=a_1,...,a_n$ and we want to find the longest palindromic subsequence. We can construct a DP array $dp[n][n]$ with $dp[i][j]$ as the largest palindromic subsequence from $a_i...a_j$. We have the base cases where empty strings and single characters have LPS of 1. 

The recurrence is such that:
$$T[i,j]=2+T[i+1,j-1] \space \text{if} \space x_i=x_j$$
$$T[i,j]=max(T[i+1,j], T[i,j-1]) \space \text{if} \space x_i\neq x_j$$
**Pseudocode**
```
def lpalindromesubsequence(x_1...x_n):
	initialize dp as a table of n by n as 0s

	for i in 1...(n)
		dp[i][i] = 1

	for s in range 1...(n)
		for i in range n-s
			j = i + s
			if x[i] = x[j] 
				dp[i][j] = 2 + dp[i+1][j-1]
			else 
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
```