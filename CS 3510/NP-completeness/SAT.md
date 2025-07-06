SAT (Boolean Satisfiability): "Given a Boolean formula, can we assign True/False values to the variables so that the formula evaluates to True?" We represent formula in CNF (conjuction normal form) which is an AND of clauses where each clause is an OR of some variable or their negation (ex. $(x∨y∨¬z)∧(¬x∨z)$). 

The SAT is universal as:
- Constraint encoding: Any logical or combinatorial constraint can be turn into clauses in a Boolean formula. For example, "You want either a burger or a gyro is encoded as $(b ∨ g)$."
- Combining all constraints with AND, we get a single big formula. If there is a way to assign each variable to a binary answer so that **every** constraint is satisfied, then the formula is **satisfiable**. 

If you could solve SAT in polynomial time, you could solve all NP problems in polynomial time, implying $P=NP$. This is why SAT is considered the central NP-complete problem. SAT is NP-complete meaning SAT is in NP (if someone gives you a variable assignment, you can quickly check it satisfies all clauses).

## k-SAT
k-SAT is a special case where each clause has at most $k$ literals (a literal is a variable or its negation). 

3-SAT is NP complete but sometimes restricting the number of literals can make the problem easier (2-SAT can be solved in polynomial time P) while 3-SAT is NP-complete. 

Proof. 3-SAT is NP Complete by reduction
	First we show that $3SAT \in NP$. Our witness is simply the assignment of variables for the problem instance solution. All these computations can be done in polynomial time. Prove that $SAT \le _p 3SAT$. For a general SAT formula, we convert it to a $3SAT$ instance such that $Φ$ is satisfiable if and only if $F(Φ)$ is satisfiable. We describe our reduction $F$ as follows. For an input $Φ$ of every SAT formula has some max clause size $k$. If $k \le 3$ then $Φ$ is both in SAT and 3SAT. Suppose $Φ$ has max clause size $k>3$. We convert a clause of size $k>3$ to a pair of clauses, one of size $k-1$ and the other of size 3.