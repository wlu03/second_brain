# How to find the Prufer Code
Let $T$ be a labeled tree on $n$ vertices
- Remove the degree 1 vertex (leaf) with the label label and record its neighbor
- Repeat until 2 vertices remain then stop.

# How to decode a Prufer Code
- List down all vertices and count appearances
- assume that every edge has a edge slot or a degree of 1.
- For each number in the Prufer code, add an extra count to that vertex. 
- Find the smallest leaf. Connect the smallest leaf with the first number in the Prufer Sequence. Remove leaf 3 and reduce the degree count of vertex by 1. 
- When there is two vertices left, connect them as the final edge.