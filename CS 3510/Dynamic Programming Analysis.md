Dynamic Programming is done top down (**recurrence** or **memoization**) or bottom up (**iteration**). 

## Example
____
Suppose you have $n$ stairs. You can leap one, two, or three steps at a time. What is the combination or the number of ways that you could reach $n$ steps. 

**Solution**: Create an array $T[0...n]$ where $T[i]$ represents the number of ways to reach step $i$. Our base case are $T[0]=1, T[1]=1, T[2]=2$. To reach step $n$, there was some last steps. You either jump 1, 2, or 3 steps, and you jumped from 1, 2 or 3 steps away. This gives us our recurrence of $T[i]=T[i-1]+T[i-2]+T[i-3]$ 

```
def numways(k) 
	initialize dp as table of size n+1 with 0s
	dp[0] = 0 
	dp[1] = 1
	dp[2] = 2

	for i in 3...(n+1):
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	return dp[k]
```
The runtime of this DP algorithm is the size of the table multiplied by the work done to calculate each cell: $O(n) \times O(1)=O(n)$ 

## Example
____
Suppose you had two operations: add one, multiply by two. How many operations does it take to get from 0 to some $k$. Here is the recurrence: $dp[0]=0, dp[1]=1$. 
$d(i)=d(i-1)+1$ if $i$ is odd
$d(i)=d(i/2)+1$ if $i$ is even

```
def minOperations(k):
	initialize dp as table of size k+1 with 0s
	dp[0] = 0
	dp[1] = 1

	for i in 2...(k+1)
		dp[i] = dp[i-1] + 1
		if i is even
			dp[i] = min(dp[i], dp[i/2]+1)

	return dp[k]
```

## Example
____
House robber. Given an array with values $H=[h_1...h_n]$, you want to rob them but you cannot rob adjacent houses or alarms will go off. What is the maximum amount you can steal? Here’s an example: $[2, 7, 9, 3, 1]$ would yield $2 + 9 + 1 = 12$. The base cases are that $T[0]=H[0], T[1]=max(H[0],H[1])$. The recurrence is as defined, you can either rob the previous house and not the next one or you can rob the house before and the current. The recurrence is therefore: 
$$T[i]=max(T[i-2]+H[i], T[i-1])$$

```
def houseroober(H):
	initialize dp as table of size n with 0s
	dp[0] = H[0]
	dp[1] = max(H[0], H[1])

	for i in range(2...n)
		dp[i] = max(dp[i-2] + H[i], dp[i-1])
	return dp[n-1]
``` 

## Example
____
**Problem**: Given $n, m$, what is the number of paths through an $n \times m$ grid from $(1, 1)$ to $(n, m)$ if you can only go down and right? For example, given a 3 × 3 matrix, there are 6 paths. This can be solved without dynamic programming, just some combinatorics. The recurrence is such that $$dp[i][j] = dp[i-1][j] +dp[i][j-1]$$ Imagine a 2x2 grid. The possible ways to go from $(1,1) \space \text{to} \space (2,2)$ is to either go right or down. Thus, by adding the previous 2 cells gets you the total number of paths. 

```
def uniquePaths(grid): 
	initialize a dp array with the size the same as a grid with all values at -1

	for i in range(0...n):
		dp[i][0] = 1

	for j in range(0...m):
		dp[0][j] = 1

	for i in range(1...n):
		for j in range(1...m):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[n][m]
```
The time complexity is just the size of the DP array: $O(n * m)$ 

## Example
____
Find the number of paths to reach cell (n, m). Additionally, the grid has bombs denoted by an input boms such that $bombs[i][j]=True$ denoted cell $(i,j)$ has a bomb. Find the number of paths from $(0,0)$ to $(n,m)$ such that no bombs are traversed. 

**Solution**: Define a DP array such that $DP[1...n][1...m]$ where $DP[i][j]$ represents the number of paths from $(1,1)$ to $(i,j)$. 

**Base Case** is such if the starting cell has a bomb then there is zero paths total to travel to. Therefore, $DP[1][1]=0$ if $bombs[1][1]=True$ else it would be $dp[1][1]=1$. Fill in the first row and column with 1 unless there is a bomb. 

**Recurrence** is defined as 
$$DP[i][j]=0 \space \text{if bombs[i][j]=True}$$
$$DP[i][j]=DP[i-1][j] + DP[i][j-1] \space \text{otherwise}$$

```
class Solution:

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

	## the trick is just to set the to zero if there is
	## a bomb there
	## obstacleGrid[i][j] = 1 -> bomb

	if obstacleGrid[0][0] == 1:
		return 0

	m = len(obstacleGrid)
	n = len(obstacleGrid[0])

	dp = [[0 for _ in range(n)] for _ in range (m)]
	dp[0][0] = 1

	# set the first row to 1 if there is not a bomb
	for i in range(1, m):
		if obstacleGrid[i][0] == 0:
			dp[i][0] = dp[i-1][0]

	# set the first column to 1 if there is not a bomb
	for j in range(1, n):
		if obstacleGrid[0][j] == 0:
			dp[0][j] = dp[0][j-1]

	# fill in the dp table
	for i in range(1, m):
		for j in range(1, n):
			if obstacleGrid[i][j] == 0:
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			## else then it's already 0
		
	return dp[m-1][n-1]
```

The time complexity is $O(n \times m)$ due to filling in the DP table. It takes constant time to fill in the DP table as well. 