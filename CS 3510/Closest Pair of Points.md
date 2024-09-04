*Input*: A set of points in the plane, $\{p_1={x_1,y_1}, p_2=(x_2,y_2), ..., p_n=(x_n,y_n) \}$
*Output*: The closest pair of points: that is the pair $p_i \neq p_j$ for which the distance between $p_i$ and $p_j$ that is $$\sqrt{(x_i-x_j)^2+(y_i -y_j)^2}$$ is minimized . 
  
This problem's optimal solution is solved using a [[Divide and Conquer Algorithm]]. 
## Case 1 - Brute Force
___
**Assume** nothing on the geometry of your input. 
**Steps**: 
	1. Initialize a variable `minDistance` and set to Integer.MAX_VALUE
	2. Iterate over all pairs of points in first loop
	3. For each pair, loop through all other pairs to compare the Euclidean distance, $d$ between them
	4. If the $d$ is smaller than `minDistance`, set $d$ as new `minDistance`
	5. return `minDistance` after nested loop

**Complexity**
Brute force: $O(n^2)$ 

## Case 2 - Assumption
___
Input in $R^2$ and $y_i=0$ where $i$ is greater than or equal to 1 and less than or equal to $n$. Imagine that the points are on a linear line since $y_i=0$. To solve this algorithm, first sort the list. Then, use two pointers and keep an absolute value between the two points. This is because merge sort is $O(n \log n)$, and looping through the list is $O(n)$. This is $O(n\log n)$. 
**Ex:** 
**Input**: $[1,3,7,9,2,5]$. 
	$|1-3| = 2, max = 2$
	$|3-7|=4, max = 4$
	$|7-9|=2, max =4$
	$|9-2|=7,max =7$ 
	$|2-5|=3, max =7$
**Output:** $7$

## Case 3 - True Optimized
____
**Algorithm**:
Assume that $n$ is a power of two, and that all the $x$-coordinates $x_i$ are distinct as are the $y$-coordinates. The algorithm is such that:
- Find a value $x$ for which exactly half the points are lower than value $x$ and the other half is greater. This splits points into two groups, $L$ and $R$. 
- Recursively find the closest pair in $L$ and in $R$. These pairs are $p_L, q_L \in L$ and $p_R, q_R \in R$ where $d_L$ and $d_R$ represent the distance between the two pairs in $L$ and $R$. Let $d$ be the smaller of the two.
  ![[Closest Pair Figure 1.png| 400]]
- At each recursion, it divides the problem in two halves. When the base case is reached, combine to get the minimum of the two.  
  ![[Closest Pair Figure 2.png| 400]]
- However, one thing to consider is that the closest pair is not guaranteed.  
  ![[Closest Pair Figure 3.png  | 400]] It's safe to assume that any points that is less than the distance must be within $± d$ of the middle. We will sort the remaining points by y-coordinates. Inside this $±d$ strip. 
- We can continue to narrow down within the $d$ strip in the $y$ direction. There is a maximum limit on the number of points within this region.  ![[Closest Pair Figure 4.png]]
  
  - Another optimization is to pass pre sorted array as arguments. 
```
function closestPair(x,y): #x and y are list
	n = x.length;
	
	if (n==2): return dist(x[1], x[2]);
	if (n==3): return min(dist(x[1], x[2]), dist(x[1], x[3]), dist(x[3], x[2]));
	
	# divide
	mid = x[n/2];
	dl = closestPair(x[1...mid], y);
	dr = closestPair(x[mid+1...n], y);
	d = min(dl, dr);
	
	# combine
	S = points in Y whose x-coordinates are in the range of [mid.x-d, mid.x+d]
	for i=1 to S.length
		# the maximum number within this range is only 8
		# therefore check against the 7 others 
		for j=1 to j=7 
			d = min(d, dist[S[i], S[i+j]]);
			
	return d;
```

**Complexity**

```
function closestPair(x,y): #x and y are pre sorted list O(n log n)
	n = x.length; 
	
	if (n==2): return dist(x[1], x[2]); #O(1)
	if (n==3): return min(dist(x[1], x[2]), dist(x[1], x[3]), dist(x[3], x[2])); #O(1)
	
	# divide
	mid = x[n/2]; #O(1)
	dl = closestPair(x[1...mid], y); 
	dr = closestPair(x[mid+1...n], y);
	d = min(dl, dr); #O(1)
	
	# combine
	S = points in Y whose x-coordinates are in the range of [mid.x-d, mid.x+d] #O(n)
	for i=1 to S.length #O(n)
		# the maximum number within this range is only 8
		# therefore check against the 7 others 
		for j=1 to j=7 
			d = min(d, dist[S[i], S[i+j]]);  #O(1)
			
	return d; #O(1)
```
For `dl = closestPair(x[1...mid], y);` and `dr = closestPair(x[mid+1...n], y);`. $$ T(n) = \begin{cases} n>3 & :2T(\frac{n}{2}) + O(n) \\ n \le 3 &:O(1) \end{cases} = O(n\log n)$$
*Reference*
	https://www.youtube.com/watch?v=6u_hWxbOc7E
	https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/