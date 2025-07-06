A decision problem is one that has a binary answer (i.e. YES or NO). For example, give a path G with two vertices $s$ and $t$, does there exist a path from $s$ to $t$. The class $P$ contains all decision problems that can be **solved** efficiently by a computer in polynomial time $O(n^k)$ for some constant $k$. 

If a decision problem is **NP**, given a solution, we can verify whether it's correct in polynomial time. NP problems might be hard to solve, but you can check it quickly. **NP** stand for "nondeterministic polynomial time". 

If you combine or modify polynomial time algorithm, the result remains polynomial time. So the class P is stable under common algorithmic steps. 

**P vs NP**: The biggest question in complexity theory is whether every problem whose solution can be verified in polynomial time (NP) can be also solved in polynomial time (P). **NP-complete** problems are the hardest problems in NP, in the sense that if we find a polynomial time solution, we show that **P=NP**. 

## Complexity Classes 
$A\in NP$ if solutions to problems in A are verifiable in polynomial time. $A \in P \rightarrow ∃$ a polynomial time complexity (problem A exists a polynomial runtime algorithm). $A \in NP \rightarrow ∃ \text{ a poly time verifier } V$  which takes on input to *witness/solution* the solution to determine the binary decision. If $P$ is the class of decision problems solvable in polynomial time, $NP$  is the class of problems verifiable in polynomial time. The problems in $P$ have solvers or algorithms, the problems in $NP$ have verifiers. The **problems** that a verifier is verifying maybe not be solvable in poly. time, but can be checked easily. 

**Proof**. Let $A ∈ P$. We show $A ∈ NP$. Since this is $∀A ∈ P$, then we conclude $P ⊆ NP$. 
	If $A \in P$, $∃$ a poly time algorithm $f$ to decide $A$. We are given a poly time verifier $V$. $V$ on input (problem p, witness = "") returns $f(p)$. The verifier just solves the problem. Since $f$ is poly. time, so is $V$. Thus, $P ⊆ NP$. 

We believe its strict but cannot prove it. We have many problems in $NP$ that don't believe to be in $P$. However, we cannot prove this. Let EXP = problems solvable in exponential time. 

**P⊂EXP**
- We can **prove** that polynomial-time algorithms ($P$) are strictly contained within exponential-time algorithms ($EXP$).
- Concretely, there are known problems that can be solved in exponential time but **cannot** be solved in polynomial time.
**NP⊆EXP**:
- Any problem in $NP$ can be solved by “brute force” search in exponential time. So $NP$ does not exceed $EXP$.
Together this makes $P⊆NP⊆EXP$. 

If $NP=EXP$, then $P=NP$:
- If you manage to prove that nondeterministic polynomial time is as powerful as full exponential time, you effectively collapse the hierarchy so that $P$ and $NP$ become the same class.
“Are there decision problems that definitely require exponential time to **solve**, but still have solutions that can be **verified** in only polynomial time? If such problems exist, $P≠NP$. If no such problems exist (meaning every exponential-time problem is also hard to **verify**), that would push us toward $P=NP$ 

Let $L=SPACE(log \space n)$ and $PSPACE=U_{k=0}^{\infty} SPACE(n^k)$ be defined as polynomial and logarithmic space. By the space hierarchy theorem, we know $L⊊PSPACE$ but similarly have the chain $L ⊆ P ⊆ NP ⊆ PSPACE$.
- **L (Logspace)**: Problems solvable with _very little_ memory (logarithmic in the input size).
- **P (Polynomial Time)**: Problems solvable _quickly_ in polynomial time.
- **NP**: Problems where a solution can be _verified_ in polynomial time (or “guessed” nondeterministically).
- **PSPACE**: Problems solvable using _polynomial space_ (memory), though potentially more time.

What if certain classes were equal (not possible)?
If 𝐿 = 𝑃 and 𝑁 𝑃 = 𝑃 𝑆 𝑃 𝐴 𝐶 𝐸
- These two “big leaps” would imply that classes we normally think of as strictly contained within each other are actually the same. That kind of collapse would force 𝑃 ≠ 𝑁 𝑃 (under usual assumptions). Essentially, you can’t simultaneously have 𝐿 = 𝑃, 𝑁 𝑃 = 𝑃 𝑆 𝑃 𝐴 𝐶 𝐸, and 𝑃 = 𝑁 𝑃; it would be contradictory. 
If 𝑃 = 𝑃 𝑆 𝑃 𝐴 𝐶 𝐸: 
- Since 𝑁 𝑃 ⊆ 𝑃 𝑆 𝑃 𝐴 𝐶 𝐸, we would then have 𝑁 𝑃 ⊆ 𝑃. But we also know 𝑃 ⊆ 𝑁 𝑃. Putting those together gives 𝑃 = 𝑁 𝑃. In other words, showing 𝑃 = 𝑃 𝑆 𝑃 𝐴 𝐶 𝐸 is so strong that it immediately collapses 𝑃 P and 𝑁 𝑃 into one class.

## NP-completeness
How to solve a problem that is $NP-Complete$. First we define poly time reduction for two problems, A and B. We say $A \le _p B$ (A is poly time reducible to B) if exists $f$ which is computable in polynomial time that converts any input $z$ for problem $A$ into an input $f(z)$ for problem $B$ such that $$z\in A =f(x)\in B$$
- In other words, $f$ maps "yes" instances of A to "yes" instances of B, vice versa for "no". This ensures that if you can solve $B$ quickly, then you can solve $A$ quickly by using $f$ to turn your A-instance to B-instance, and running the solve for B (assumed faster). 

To prove B is NP-Complete you show:
- $B\in NP$ 
- $B$ is $NP-Hard$. If $A$ is some $NP-Complete$ problem, prove $A \le _p B$ by giving a poly time reduction form $A$ to $B$. 

