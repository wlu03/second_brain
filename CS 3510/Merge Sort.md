**Merge Sort**
____
**Pseudocode**:
```
def mergesort(A[1...n]):
	## Base Case
	if n == 1: return A
	## Split problem into two subarrays, recursviely call mergesort on both
	L = mergesort(A[1...floor(n/2)])
	R = mergesort(A[floor(n/2)+1...n])
	## return the merge of the left and right
	return merge (L,R)
```
![[Merge Sort 2.png | 500]] 

**Merge()** 
___
**merge()** takes two parameters $x[1..k]$ and $y[1...m]$ ew can assume that both these halves are sorted by induction for the smallest case 2. Our base case will handle the P(2) case. Merging two sorted arrays $x[1...k]$ and $y[1...l]$ to efficiently merge them into a single sorted array $z[1...k+1]$ you can use the merge subroutine. 

**Pseudocode:**
```
def merge(x[1...k], y[1...m]):
	if x is length 0
		return y
	if y is length 0
		return x
	if x[1] <= y[1]:
		return x[1].join(merge(x[2...k], y[1...k]))
	else:
		return y[1].join(merge(x[1...k], y[2...k]))
```
The addition means to concatenate the two list. The merge procedure does a constant amount of work per recursive call for a total running time of $O(k+1)$. Thus merge is linear. The overall time taken by merge sort is $$T(n)=2T(n/2)+O(n)$$
The work is done in merging when recursion gets down to singleton arrays. 
![[Merge Sort.png]]