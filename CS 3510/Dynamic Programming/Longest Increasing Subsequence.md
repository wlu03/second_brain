**Problem**: Find the longest increasing subsequence in an array of `n` elements. This is a maximum length sequence of array elements that goes from left to right, and each element in the sequence is larger than the previous. The array `arr = [6,2,5,1,7,4,8,3]` has a longest increasing subsequence containing 4 elements of `longest_subsequence_arr = [2,5,7,8]`.

Let `length(k)` denote the length of the longest increasing subsequence that ends at position `k`. If we call the values of `length(k)` where $0 \le k \le n-1$, we find out the length of the longest increasing subsequence.

We define `length(k)` as the length of the longest increasing subsequence that **ends at index k**. If we compute `length(k)` for all $k$. 
```
length(0) = 1 (6)
length(1) = 1 (2)
length(2) = 2 (2,5)
length(3) = 1 (1)
length(4) = 3 (2,5,7)
length(5) = 2 (2,4)
length(6) = 4 (2,5,7,8)
length(7) = 2 (2,3)
```

To calculate a value of `length(k)`, we should find a position $i<k$ for which `array[i] < array[k]` and `length(i)` is as large as possible


**Algorithm**
```c++
for (int k = 0; k < n; k++) {
	length[k] = 1;
	for (int i = 0; i < k; i++) {
	    if (array[i] < array[k]) {
		    length[k] = max(length[k], length[i] + 1);
	    }
	}
}
```
- Outer loop iterates index $k$
- Inner loop find the longest increasing subsequence ending at $k$ by checking over all previous indices
- $O(n^2)$ runtime.
