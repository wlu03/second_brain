**Definition**: Two graphs can be represented by diagrams that look exactly the same but lies in the different between the labels of their vertices and edges. Although the two might be different, they can have the same *structure* thus **isomorphic**.

Two graph $G_1=(V_1,E_1)$ and $G_2=(V_2,E_2)$ are isomorphic if there exists a bijection $f:V_1 \rightarrow V_2$ such that $x$ and $y$ are adjacent in $G_1$ if and only if $f(x)$ and $f(y)$ are adjacent in $G_2$. 
$$xy\in E_1 \text{ iff } f(x)f(y)\in E_2$$
**Observations of Isomorphic Graphs** 
- same order $|V_1|=|V_2|$
- same size $|E_1|=|E_2|$
- same degree sequence, the list of degrees of all the vertices of the graph in decreasing order.
- adjust drawing of one of $G_1,G_2$ to check if they have the same structure. if yes then isomorphic. 
# How to solve?
1. Count vertices
2. Analyze degree of each vertex
3. To confirm isomorphism find corresponding vertices of same degree and make sure the "neighbors" match
