## Addition Rule
____
If only one method can be used, you have $n_A + n_B$ ways of doing so.  

**Example**: Go to Starbucks and have a muffin (blueberry or oatmeal) or  
a bagel (sesame, plain, salt), but not both. 2 + 3 = 5 choices.

## Multiplication Rule 
___
Two operations are performed one after the other:  
(a) The first operation can be done in $n_1$ ways. 
(b) Regardless of the way in which the first operation was performed the second can be performed in $n_2$ ways.  
The # ways to perform the two operations together is $n_1n_2$ 

**Example**: Flip 3 coins. 2 ⇥ 2 ⇥ 2 = 8 possible outcomes.

## [[Permutations]]
___
An arrangement of $n$ symbols in a *definite order* is a **permutation** of the $n$ symbols. 

**Example**: How many ways to arrange numbers 1,2,3? 6 ways - $123,321,213,231,132,312$ 

**Example**: How many ways to arrange $1,2,...,n$? $n(n-1)(n-2)...2\cdot1=n!$

$$P_{n,r}=\frac{n!}{(n-r)!}$$
## Combinations
____
Count the numbers of ways to choose $r$ out of $n$ objects without order. Counting the number of different subsets of these $n$ objects that contain exactly $r$ objects.

**Example**: How many subsets of $\{1,2,3\}$ contains 2 elements? 3 - $\{1,2\}, \{1,3\},\{2,3\}$

**Notation**: $\binom{n}{r}$ reads as "n choose r". This is also called binomial coefficients 

$$\binom{n}{r}=\frac{n!}{(n-r)!r!}$$

### Useful Properties
$$\binom{n}{r} =\binom{n}{n-r}$$
$$\binom{n}{0}=\binom{n}{n}=1$$
$$\binom{n}{1}=\binom{n}{n-1}=n$$

## Sampling with Replacements
___
**Example**: 25 socks in a box. 15 red, 10 blue. Pick 7 without replacement. $$P(3\space red)=\binom{7}{3}(\frac{15}{25})^3(\frac{10}{25})^{7-3}$$
A general formula is $$=\binom{n}{k}(\frac{a}{a+b})^k(\frac{b}{a+b})^{n-k}$$
Picking $k$ elements from $n$ numbers given the probability.

## Sampling without Replacements
____
You have $a$ objects and $b$ objects. Select $n$ objects without replacement from $a+b$ objects. 
$$P=\frac{\binom{a}{k} \binom{b}{n-k}}{\binom{a+b}{n}}$$This is a hypergeometric distribution. 

**Example**: 25 socks in a box. 15 red, 10 red. Pick 7 w/o replacement
$$P(exactly \space 3 \space reds)=\frac{\binom{15}{3}\binom{10}{4}}{\binom{25}{7}}$$