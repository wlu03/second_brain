**Problem**: Find a path from the upper-left corner to the lower-right corner of an `nxn` grid, such that we only move down and right. Each square contains a positive integer, where the path should be constructed so that the sum of the values long the path is as large as possible.
![[Paths in a grid.png]]
*the sum is 67 for this path*

Assume that the rows and columns of the grid are numbered from 1 to $n$, and $value[y][x]$ equals the value of the square $(y,x)$. Let $sum(y,x)$ denote the maximum sum on a path from the upper left corner to the square $(y,x)$. Therefore, $sum(n,n)$ tells us the maximum sum from the upper-left corner to the lower-right corner. The recursive relation is as follows: $$sum(y,x)=max(sum(y,x-1),sum(y-1,x)) + value[y][x]$$
```python
def solve(grid):
	n = len(grid)
	value = [[0] * n for _ in range(n)]
	value[0][0] = grid[0][0]

	# fill first row so that values only come from the left
	for j in range(1,n):
		value[0][j] = value[0][j-1] + grid[0][j]

	# fil the first column so it can only come from above
	for i in range(1,n):
		value[i][0] = value[i-1][0] + grid[i][0]

	for i in range(1,n):
		for j in range(1,n):
			value[i][j] = max(value[i-1][j], value[i][j-1]) + grid[i][j]

	return value[n-1][n-1]
```
- $O(n^2)$ time complexity