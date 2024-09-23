**Def**: A set is a collection of objects. Members of a set are called elements.

**Notation**: 
- $A, B, C$ for sets
- $a,b,c$ for elements
- $\in$ standing for element in a set. $e.g.,  x\in A$ 
- $\cancel{\in}$ for non-membership $e.g. x\cancel{\in} A$  
- $U$ is the universal set
- $∅$ is the empty set

**Example**:
- $A=\{1,2,...,10\}$. $2\in A. 49\cancel{\in}A$ 
- $B =\{x|0 \le x \le 1\}$, where "|" means "such that"
- $C=\{x|x^2=9\}, x={+3,-3}$ 
- $D=\{x |  x\in \mathbb{R},x^2-1 \}=∅$ 

# Subset
____
**Definition**: If every element set A is an element of set B than A is a subset of set B. $A ⊆ B$. 

**Theorem**: $A=B$ if and only if $A⊆B$ and $B⊆A$

**Properties**:
- $∅⊆A$, $A ⊆ U$, $A⊆A$
- $A⊆B$, and $B⊆C \implies A⊆C$ 

# Definition
____
- **Complement** of $A$ with respect $U$ to $\bar{A} = \{ x|x \in U \space \text{and} \space x\cancel{\in} A \}$ 
- **Intersection** of $A$ and $B$ is $A\cap B = \{ x|x\in A \space and \space x\in B \}$   
- **Union** of $A$ and $B$ is $A\cup B = \{ x|x\in A \space or \space x\in B \}$  
- If $A \cap B = ∅$, then $A$ and $B$ are **disjoint** (or **mutually exclusive**) 
- **Minus**: $A-B = A\cap \bar{B}$ 
- **Symmetric Different** Or **XOR**: $$A\Delta B= (A-B)\cup (B-A)=(A\cup B)-(A\cap B)$$
- The **cardinality** of $A$, or $|A|$ is the number of elements in $A$. 

## Laws
___
Complement Law
- $A\cup \bar{A}=U$
- $A\cap \bar{A}=∅$ 
- $\bar{\bar{A}}=A$

Commutative Law
- $A \cup B = B\cup A$
- $A \cap B = B\cap A$

De Morgan's
- $\overline{A \cup B} = \bar{A} \cap \bar{B}$    
- $\overline{A \cap B} = \bar{A} \cup \bar{B}$    

Associative
- $A\cup (B \cup C)=(A\cup B) \cup C$
- same for intersections

Distributive
- $A\cup (B \cap C) = (A \cup B) \cap (A \cup B)$
- same for opposite

Prove using Venn Diagram

