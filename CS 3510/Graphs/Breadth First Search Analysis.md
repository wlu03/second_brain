I want to calculate the shortest paths in a graph. DFS is one way to search the graph. By using the stack, we can explore the graph deeply. However, BFS can also be used . The shortest path algorithm takes on input of a graph and a starting node. It will compute the shortest path from that node to other.

BFS uses a **queue** data structure to pop and push from where DFS uses a stack. The queue helps us to see the children of a node before it's grandchildren. 

**Pseudocode**
 ```
from collections import deque

def bfs(graph, start):
    """
    Perform a Breadth-First Search on the given graph starting from the 'start' node.
    
    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The node from which BFS traversal begins.
    """
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize a queue with the start node
    visited.add(start)       # Mark the start node as visited

    while queue:
        # Dequeue a node from the front of the queue
        vertex = queue.popleft()
        
        # Process the node (for demonstration, we'll print it)
        print(vertex)
        
        # Get all adjacent vertices (neighbors) of the dequeued node
        for neighbor in graph[vertex]:
            # If this neighbor hasn't been visited yet, enqueue it
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

The **total runtime** is $O(|V|+|E|)$ because each vertice is push and popped from the queue once in constant time and adjacency list are looped over once for each, their sum of length being $O(E)$.  