**Derangement** is a a permutation $\sigma$ such that $$\sigma(i)\neq 1 \text{ for all }i\in \{1,2,...,n\}$$This means that no element is mapped to its own position. 

**Example**
Total permutations of $n=3, 3!=6$. We want permutation where none of the positions is "correct". By direct listing there is 2 such permutation that $(2,3,1) \text{ and } (3,1,2)$. 
$$N(\overline{c_1}\overline{c_2}\overline{c_3})=3!-\binom{3}{1}(3-1)!+\binom{3}{2}(3-2)!-\binom{3}{3}(3-3)!=2$$
**Formula for Derangement**
For general $n$, define $c_i$ as "$i$ is in position $i$." We want permutation that avoid $c_i$. 
$$d_n=n!-\binom{n}{1}(n-1)!+\binom{n}{2}(n-2)!-...+(-1)^n\binom{n}{n}(n-n)!$$
As $n$ grows large, it is known that $d_n=\frac{n!}{e}$

**Problem 1)** In how many ways can integers $\{1,2,3,...,10\}$ be arranged so that no even integer is in its original position.

We forbid 5 positions: $2,4,6,8,10$ 
$c_2:$ 2 is in position 2
...
$c_{10}$: 10 is in position 10

By PIE $$N(\overline{c_1}\overline{c_2}\overline{c_3}\overline{c_4}\overline{c_5})=10!-\binom{5}{1}9!+\binom{5}{2}8!-\binom{5}{3}7!+\binom{5}{4}6!-\binom{5}{5}5!$$ We fix r even positions, the remaining 10-r positions can be any permutation of 10-r elements so that (10-r)! multiplied by $\binom{5}{r}$ ways to choose which $r$ even positions are fixed. 