# Probability Distribution
___
The **sample space S i**s the set of all possible outcomes. An **event** **A** is any subset of S. **Random variables X** represents outcome in sample space. The probability of an random variable to happen is $p(x)=P(X=x)$ where $p(x) \ge 0$.

**Continuous Variable/Probability Density Function**: 
It can also be called/includes *Continuous Probability Distribution, Probability Density Function, Density or Likelihood value, temperature, Gaussian Distribution.

$$\int_x p(x)dx=1$$

**Discrete Variable**:
Can also be called/includes *Discrete Probability Distribution, Probability mass function, Probability value, Coin flip (integer), Bernoulli Distribution
$$\sum_{x\in A}p(x)=1$$
![[Continuous Probability Functions.png | 500]]
![[Discrete Probability Functions.png | 500]]

# Joint and Conditional Probability Distributions
____
Use the table below
![[Probability and Statistics Table.png]]
**Probability**: $P(X=x_i)=\frac{c_i}{N}$ *ex: what are the odds of rolling a 6 given the events on the table? 6/35*
**Joint Probability**: $p(X=x_i,Y=y_j)=\frac{n_{ij}}{N}$ *ex: what are the odds of both occurring: heads and 6?  1/35*
**Conditional Probability**: $p(Y=y_{j}|X=x_i) =\frac{n_{ij}}{c_i}$ *ex: given that x occurs, what are the odds of y? For example, given that a 6 is rolled, what is the probability the dice rolls tails? 5/6*

**Sum Rule**: $p(X=x_i)=\sum_{j=1}^L p(X=x_i,Y=y_j) \rightarrow p(X)=\sum_Y P(X,Y)$
**Product Rule**: $P(X,Y)=P(Y|X)P(X)$

# Bayes' Rule
____
$P(X|Y)$: reads as "Given that Y is true, what is the probability that X is also true". 
	$$P(X|Y)=\frac{P(X,Y)}{P(Y)}=\frac{P(Y|X)P(X)}{P(Y)}$$
___

# Maximum Likelihood Estimation
____
