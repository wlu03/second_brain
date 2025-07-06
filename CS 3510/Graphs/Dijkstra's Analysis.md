Dijkstra's algorithm is a weighted BFS where it considers the weight of each edge in the BFS. Thus, a simple data structure change can be made from a *queue* to a *priority queue*. When run, this algorithm should return the path itself of the shortest path.  

**Pseudocode**
```
import heapq

def dijkstra(G, s):
    """
    Compute shortest distances from a source vertex s to all other vertices
    in a weighted graph G using Dijkstra's algorithm.

    Parameters:
    -----------
    G : dict
        Adjacency list representation of the graph:
        {
            u: [(v1, w1), (v2, w2), ...],
            ...
        }
        where u, v_i are vertices and w_i is the weight of edge (u, v_i).
    s : hashable
        The starting vertex.

    Returns:
    --------
    dist : dict
        Dictionary of shortest distances from s to each vertex in G.
    prev : dict
        Dictionary that maps each vertex to the predecessor on its shortest path
        from s. Useful for reconstructing paths.
    """

    # Initialize distances to infinity and predecessors to None
    dist = {vertex: float('inf') for vertex in G}
    dist[s] = 0
    prev = {vertex: None for vertex in G}

    # Priority queue (min-heap) for managing vertices to explore
    # Each entry in the heap is a tuple (distance, vertex)
    pq = [(0, s)]
    heapq.heapify(pq)

    while pq:
        # Extract the vertex with the smallest distance
        current_dist, u = heapq.heappop(pq)

        # If this distance is outdated (larger than the stored), skip
        if current_dist > dist[u]:
            continue

        # Relax edges out of u
        for v, weight in G[u]:
            alt_dist = dist[u] + weight
            if alt_dist < dist[v]:
                dist[v] = alt_dist
                prev[v] = u
                # Push the updated distance to the priority queue
                heapq.heappush(pq, (alt_dist, v))

    return dist, prev

```

**Runtime** 

| Data Structure | deleteMinimum                       | decreaseKey                        | Total Runtime                              |
| -------------- | ----------------------------------- | ---------------------------------- | ------------------------------------------ |
| array          | $O(\|V\|)$                          | $O(1)$                             | $O(V^2)$                                   |
| binary heap    | $O(log \cdot V)$                    | $O(log \cdot V)$                   | $O((V+E)log\cdot V)$                       |
| d-ary heap     | $O(\frac{dlog\cdot v}{log\cdot d})$ | $O(\frac{log\cdot v}{log\cdot d})$ | $O((Vd+E)\frac{log \cdot V}{log \cdot d})$ |
If G is a dense graph meaning there is a lot edges where $E \equiv V^2$, use an array. However, a binary heap is better when $E = \frac{V^2}{logV}$   


**Output**: From a starting vertex $v$, this algorithm returns an array of $dist[u]$ where $u$ is all other nodes reachable from $v$ given the shortest distance. If it's not reachable, the value remains as $\infty$. The $prev$ array can reconstruct the actual shortest path for each vertex by following the chain of predecessors back to the source. 
## Validity
___
Dijkstra’s Algorithm works when:
- **Non-negative Edge Weights**
- **Connectedness**: if a vertex is not reachable, it's distance remains as $\infty$ 
- **Directed or Undirected**: Works on both types of graphs provided that it follows the first rule.

**Key Property**: Once a vertex $u$ is removed from the priority queue in the algorithm, $dist[u]$ is the final shortest path distance from the source $s$ to $u$. 