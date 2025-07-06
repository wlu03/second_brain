**Knapsack** refers to problems where a set of objects is given and subset with some properties have to be found. 

Given a list of weights $[w_1,w_2,w_3,...,w_n]$ determine all sums that can be constructed using the weights. For example, if the weights are $[1,3,3,5]$ the following sums are possible $[0,1,3,4,5,6,7,8,9,11,12]$. For example, the sum 7 is possible because using weights $[1,3,3]$. 

To solve this problem, we focus on subproblems where we only use the first $k$ weights to construct sums. Let $possible(x,k) = True$ if we can construct a sum $x$ using the first $k$ weights otherwise it is $False$. The values can be recursively calculated as follows:
$$possible(x,k) = possible(x-w_k,k-1)∨ possible(x,k-1)$$
The formula comes from the fact we can use or not use the weight $w_k$ in the sum. If we use $w_k$, the remaining task is to form the sum $x-w_k$ using the first $k-1$ weights and if we don't use $w_k$, the remaining task is to form the sum $x$ using the first $k-1$ weights. The base case is:
$$possible(x,0)= True \text{ if x=0}$$
$$possible(x,0)= False \text{ if } x\ne0$$

```c++
possible[0] = true;
for (int i = 0; i < n; i++) {
    for (int k = sum; k >= a[i]; k--) {
        possible[k] = possible[k] || possible[k - a[i]];
    }
}
```

```python
def subset_sum_possible(weights, target_sum):
    # Create a DP array initialized to False
    possible = [False] * (target_sum + 1)
    possible[0] = True  # Base case: sum of 0 is always possible

    # Iterate over each weight
    for weight in weights:
        # Update from right to left to avoid overwriting previous results
        for k in range(target_sum, weight - 1, -1):
            possible[k] = possible[k] or possible[k - weight]

    return possible

# Example Usage:
weights = [1, 3, 5]
target_sum = 12  # We want to check all sums up to 12
possible_sums = subset_sum_possible(weights, target_sum)

# Display all possible sums
for k in range(target_sum + 1):
    print(f"Sum {k}: {'Possible' if possible_sums[k] else 'Not Possible'}")

```
- $O(n \times sum)$ time complexity

## 0/1 Knapsack Solution Explanation Deeper
A common way to solve 0/1 Knapsack is using a DP table. $dp[i][w]$ represents the maximum value achievable with the first $i$ items and with a knapsack capacity of $w$. For each item $i$ and for each capacity $w$,  I will decide to include or exclude the item

- If you don't include $i$-th item
	$dp[i][w] = dp[i-1][w]$ 
- If you include $i$-th item ($w_i \le w$)
	$dp[i][w]=dp[i-1][w-w_i] +v_i$

The recurrence relation is:
$$dp[i][w]=dp[i-1][w] \text{   if } w_i>w$$
$$dp[i][w]=max(dp[i-1][w], dp[i-1][w-w_i]+v_i)$$
The answer will be $dp[n][W]$. 

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]  # Can't include this item
            else:
                # Either take the item or don't take it
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    # The maximum value that can be achieved is stored in dp[n][capacity]
    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]   # Weights of items
values = [3, 4, 5, 6]    # Values of items
capacity = 5             # Maximum capacity of knapsack

max_value = knapsack(weights, values, capacity)
print("Maximum value achievable:", max_value)

```
- $O(n×capacity)$ runtime 