# Graphs
____
Graphs are described by a set of vertices $V$ and by a set of edges which are pairs of vertices. This is represented as $G = (V, E)$. Graphs with ordered edges (where there is a direction) are called directed graphs; graphs with unordered edges (where there is no direction) are called undirected graphs. It is sometimes useful to apply a weight or value to edges; the weight of an edge is denoted as $w_e$ where $e$ is the edge.
![[Graphs Representation.png | 300]]
## Encoding Graphs
### Adjacent Matrix
____
This is a square matrix of size $|V| \times |V|$. We associate each element of the matrix as an edge in the graph. Without a lot of edges, the graph stores a lot of edges. Graphs without many edges are sparse, and those with many edges are dense. If $|E|$ approximates equals $|V|^2$, we say a graph is dense
![[Adjacency Matrix.png | 600]]
*for the node zero, a 1 represents that it's connected.*
![[Adjacency Matrix with Weights.png | 600]]
*it's the same as last time however, instead of representing with 1's and 0's. It uses the weights are the connection.*
![[Adjacency Matrix with Weights and Direction.png | 500]]
*Direction is now stored. For example, 0-1 (weight: 5). The rows store the node and each column stores which node $i$ points to which $j$ node.* 

### Adjacency List
___
We can store sparse graphs where there aren't many edges using a linked list of size $|V|$. These would represent the outgoing edges from each node. The space-time trade-off is the difference between the adjacency list and matrix. With a constant access of $O(1)$ time complexity, a matrix makes it quick to look up values. Comparatively, for a sparse graph, it would be less space intensive, but you would need to iterate to find your value. 
```
# adjaceny list with a dictionary
adjacency_list = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4], 
    4: [2, 3]   
}
```
*in Java, you would implement this with a HashMap and in python you would use a dict*
## Graph Traversal

[[Depth First Search Analysis]]
[[Topological Sort Analysis]]
[[Strongly Connected Components]]
[[Breadth First Search Analysis]]
[[Dijkstra's Analysis]]
[[Kruskal's Algorithm for MST Analysis]]