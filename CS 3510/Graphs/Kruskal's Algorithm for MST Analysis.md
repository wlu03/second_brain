## Minimum Spanning Tree
Given a weighted undirected graph, give a graph which is still connected but with smallest weights. An MST is a set of edges that is:
- Minimum, the sum of the edges weights is less than or equal to any other MST
- Spanning, each vertex is an endpoint of at least on edge in the MST
- Tree, there is no cycles and $|V|-1$ edges
![[Minimum Spanning Tree.png| 500]]
**No Cycles**: There is no cycles in the MST because if there was a cycle, we could remove the highest value edge and get a smaller MST. 

**Pseudocode**
```
def kruskals(G, w):
	for all v in V
		makeSet(v)
	X = {}
	sort E by weights
	for all (u, v) in E:
		if find(u) is not find(v):
			x = x + {(u,v)}
			union(find(u), find(v))
```
Kruskal’s algorithm is a classic method for finding a **Minimum Spanning Tree (MST)** of a weighted undirected graph. The idea is:
1. Sort all edges by their weight (ascending).
2. Initialize a **Union-Find** structure where each vertex is in its own set.
3. Traverse the sorted edges in order:
    - For each edge $(u,v)$, use Union-Find to check if $u$ and $v$ are already in the same set.
        - If they **are in the same set**, ignore this edge (it would form a cycle).
        - If they **are in different sets**, unite them (Union-Find “union” operation) and include this edge in the MST.
4. Stop once you have $n-1$ edges in the MST (where $n$ is the number of vertices) or after examining all edges.
Because Union-Find can quickly tell us whether two vertices are in the same connected component, it prevents cycles efficiently and ensures we get the MST with minimal overhead.

**Runtime**: Making the sets for union find will take $O(|V|)$ time. By sorting $E$ by weight will be $O(|E|log |E|)$. There will be $|E|$ iterations over the sort edges each doing $log|V|$. Adding these together:
$$O(|V|+|E|log|E|+|E|log|V|)=O(|E|log|E|)$$
## Cut Property
___
The **cut property** says that if you partition (or “cut”) the vertices of a weighted, undirected graph into two nonempty sets, then any edge with the **minimum weight** crossing from one set to the other in that partition must be part of **some** Minimum Spanning Tree of the graph.

**Formally:**

- Consider an undirected, weighted graph $G=(V,E)$
- A “cut” is a partition of the vertex set V into two disjoint, non-empty subsets $S$ and $V∖S$
- An edge “crosses” the cut if one of its endpoints lies in $S$ and the other lies in $V∖S$
- The cut property states that if we look at all edges that cross the cut, at least one of the edges with the minimum weight among them must be part of any MST of $G$.