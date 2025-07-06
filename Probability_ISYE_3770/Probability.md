**Definition**: With each event $A\in S$, we associate a number P(A), called the probability of A satisfying the following axioms:
1. $0\le P(A) \le 1$, probability is always between 0 and 1
2. $P(S)=1$ probability of some outcome is 1. $P(Dice) = \{1,2,3,4,5,6\}=1$
3. If $A\cap B = \phi$, then $P(A\cup B)$ then $P(A)$ and $P(B)$. Example: $P(1 or 2) = P(1) + P(2) = 1/6+1/6=1/3$
4. Suppose $A_1,A_2,...$ is a sequence of disjoint events where the intersection of two events is the empty set then the probability of all the union events is equal to the probability $$P(\bigcup_{i=1}^{\infty} A_i)=\sum_{i=1}^{\infty}P(A_i)$$
**Theorem**: The probability of the empty set is 0. $e.g. P(\phi)=0$ 
**Proof**: Since $A \cap \phi = \phi$ we have that $A$ and $\phi$ are disjoint. Therefore $$P(A)=P(A \cup \phi)=P(A)+P(\phi)$$
**Theorem**: $P(\bar{A})=1-A$
**Proof**: $$1= P(S)$$
$$=P(A\cup \bar{A})$$ $$P(A) + P(\bar{A})$$
**Theorem**: For any two events $A$ and $B$, $$P(A\cup B) = P(A) + P(B)-P(A\cap B)$$*Example*. Suppose that there's 40% of being cold, 10% of rain and being cold, and 80% chance of rain or being cold. Find the chance of rain.
$$P(C)=.4, P(R \cup C) = .8, P(R \cap C)=.1$$
$$P(R)=P(R\cup C)-P(C)+P(R\cap C) = 0.5$$

**Theorem**: For any three events $A, B$, and $C$ 
$$P(A \cup B \cup C) = P(A) + P(B)+P(C)-P(A \cap B) - P(A \cap C)-P(B \cap C) + P( A \cap B \cap C)$$
This is the inclusion exclusion principle 

![[Inclusion-Exclusion.png]]
**Theorem**: $A ⊆ B \implies P(A) \le P(B)$

