Divide and conquer algorithms follow a generic pattern. They tackle a problem of size $n$ by recursively solving $a$ subproblems of size $n/b$ and then combining these answers in $O(n^d$) time. The running time can be captured by the equation $$T(n)=aT(\lceil \frac{n}{b} \rceil) +O(n^d)$$
![[Recurrence Relation.png]]
[[Master Theorem]]
___
The master theorem tells us the running times of most of the divide and conquer procedure. 


## Binary Search
___
The ultimate divide and conquer algorithm, binary search: to find a key $k$ in an array $[0,1,...,n-1]$ in sorted order. We compare $k$ with $[n/2]$ and depending on the result we recurse either on the first half of the file $[0,...,n/2-1]$ or on the second half $[n/2,...,n-1]$. The recurrence is now $T(n)=T(\lceil \frac{n}{2} \rceil)+O(1)$ which is the case $a=1,b=2,d=0$. Pulling in the masters theorem we get the solution $O(\log n)$. 

