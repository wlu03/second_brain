**DP** is a technique that combines the complete search and greedy algorithm. It can be applied if the problem can be divided into sub-problems that are solved independently.

When to use:
- **Finding an optimal solution**: Find a solution that is as large as possible or as small as possible
- **Counting the number of solutions**: Calculate the total number of possible solution

## Coin Problem
Given a set of coin values and a target sum of money `n`. Our task is to form the sum `n` using as few coins as possible. The DP algorithm is based on a recursive function that goes through all possibilities how to form the sum, but it is efficient because it uses *memoization* and calculates the answer to each subproblem once. 

The recursive nature repeated in the problem: what is the smallest number of coins required to form a sum of `x`. Let `solve(x)` denote the minimum number of coins required for a sum `x`. Given that `coins = {1,3,4}`.  The first values of the function are

```
solve(0) = 0
solve(1) = 1
solve(2) = 0
solve(3) = 1
solve(4) = 1
solve(5) = 2
solve(6) = 2
solve(7) = 2
solve(8) = 2
solve(9) = 3
solve(10) = 3
```

The property of `solve` is that its values can be recursively calculated from its smaller values. The idea is to focus on the first coin that we choose for the sum. The first coin can be either 1, 3, or 4. If we choose coin 1, the remaining task is to form sum 9 using the minimum number of coins. Same for coin 3 and 4.

`solve(x) = min(solve(x-1)+1, solve(x-3)+1, solve(x-4)+1)`

The base case of the recursion is `solve(0)=0`

**Solution**:
```c++
int solve(int x) {
	if (x<0) return INF;
	if (x==0) return 0;
	int best = INF;
	for (auto c : coins) {
		best = min(best, solve(x-c)+1);
	}
	return best;
}

```
- to optimize this you can use **memoization**

## Memoization
Memoization is used to efficiently calculate values of a recursive function. This means that the values of the function are stored in an array after calculating them. For each parameter, the value of the function is calculated recursively only once. 

In the coin problem, we can use arrays for memoization
```c++

bool ready[N];
int value[N];

int solve(int x) {
	if (x<0) return INF;
	if (x==0) return 0;
	if (ready[x]) return value[x];
	int best = INF;
	for (auto c : coins) {
		best = min(best, solve(x-c)+1);
	}
	value[x] = best;
	ready[x] = true;
	return best;

}
```
- This function handles the base cases `x<0` and `x=0`. 
- It stores values inside of `ready` and `value` array to it doesn't need to do more work. 
- The runtime of this algorithm is $O(n \cdot k)$ where `n` is the target sum and `k` is the number of coins.

Another solution without recursive functions is building the DP array.
```c++
value[0] = 0;
for (int x = 1; x <= n; x++) {
	value[x] = INF;
	for (auto c : coins) {
		if (x-c >= 0) {
			value[x] = min(value[x], value[x-c]+1)
		} 
	}
}
```
# Counting the number of solutions
Let us consider another version of the coin problem where our task is to calculate the total number of ways to produce a sum `x` using the coins. For example, if `coins = {1,3,4}` and `x=5`, there is a total of 6 ways. 

Recursive Formula:
```
solve(x) = solve(x-1) + solve(x-3) + solve(x-4)
```

If `x<0`, the value is 0. If `x=0`, the value is 1 because there is exactly one way to make an empty sum. 

Algorithm
```c++
count[0] = 1;
for (int x = 1; x <=n; x++) {
	for (auto c : coins) {
		if (x-c >= 0) {
			count[x] += count[x-c]
		}
	}
}
```