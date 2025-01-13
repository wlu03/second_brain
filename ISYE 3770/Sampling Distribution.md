A [[Statistics|statistic]] is a simply a function of the observation $X_1,...,X_n$ from a random sample. The function does not depend explicitly on any unknown parameters.  Since statistics are RV’s, it will sometimes be useful to figure out their distributions. The distribution of a statistic is called a **sampling distribution*.

**Central Limit Theorem (CLT)**
If $X_1,X_2,...,X_n$ are iid with mean $\mu$ and variance $\sigma^2$ then for large $n$ $$\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{}n}}=N(0,1)$$
**Example**
An electronics company manufactures resistors having a mean resistance of 100 ohms and a standard deviation of 10 ohms. The distribution of resistance is normal. What is the probability that a random sample of n = 25 resistors will have an average resistance of less than 95 ohms?

Remember that $E(\bar{X})=\mu$ and $s.d. (\bar{X})=\sigma/\sqrt{n}$ so, $\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{}n}}=\frac{\bar{X}-100}{\frac{10}{\sqrt{25}}}=\frac{\bar{X}-100}{2}=N(0,1)$ 
$P(\bar{X} < 95)=P(\frac{\bar{X}-100}{2} < \frac{95-100}{2})= P(Z<-2.5) = 0.0062$


**$X^2$ Chi Distribution** 
If Z~N(0,1), then $Z^2$~$x_{(1)}^2$ 
If a random variable $Z$ follows the standard normal distribution $N(0,1)$ then $Z^2$ follows a chi squared distribution with 1 degree of freedom as denoted above. 

Chi squared distribution add up when independent. If you have independent random variables $Y_1,Y_2,...,Y_n$ where $Y_i$ follows a chi-squared distribution $d_i$ degrees of freedom, then their sum $\sum_{i=1}^n Y_i$ follows a chi-squared distribution with $\sum_{i=1}^n d_i$ degrees of freedom.

If you ave $Z_1,Z_2,...,Z_k$ which are independent and identically distributed as $N(0,1)$ then the sum of their squares $Y=\sum_{i=1}^k Z_i^2$ follows a chi squared distribution with $k$ degrees of freedom, denoted as $Y$~$\chi^2(k)$ 

The PDF of a chi squared distribution with k degrees of freedom is $$f_Y(y)=\frac{1}{2^{k/2} \Gamma (k/2)} y^{(k/2)-1}e^{-y/2}$$
The expected value of $E(Y)=k$ and variance $Var(Y)=2k$.

Degrees of freedom corresponds to the number of "independent pieces of information" you have. For example, if you have RVs $X_1,...,X_n$ such that $\sum_{i=1}^n X_i=c$, a known constant, then you might have $n-1$ degrees of freedom. Since knowledge of any $n-1$ of the $X_i$'s gives you the remaining $X_i$.

The **exponential distributions are a special case**, In fact $\chi_{(2)}^2$~ Exp(1,2). 
- For k>2, the $\chi_{(k)}^2$ pdf is skewed to the right.
- for large k, the $\chi_{(k)}^2$ is approximately normal (by the CLT) 

### Table of Quantiles of Chi-squared Distributions
The $(1-\alpha)$ quantiles of a RV X is the value $x_{\alpha}$ such that $P(X>x_{\alpha})=1-F(x_{\alpha}) = \alpha$. Note that $x_\alpha=F^{-1}(1-a)$ where $F^{-1}(\cdot)$ is the **inverse cdf** of x.    
![[Screenshot 2024-11-11 at 3.16.48 PM.png]]
![[Screenshot 2024-11-11 at 3.17.52 PM.png]]

## t Distribution
_____
- Z~Nor(0,1): standard normal variable with mean of 0 and variance of 1. 
- Y~$\chi_{k}^2$: a chi squared variables with $k$ degrees of freedom
- Z and Y are independent of each other
- The statistic has the student t distribution with k degrees of freedom we write $T=\frac{Z}{\sqrt{Y/k}}$~$t_{(k)}$. 
- **Shape**: $t(k)$ looks like the Nor(0,1) but t has a fatter tails
- **Asymptotic Behaviors**:  As the degrees of freedom $k$ becomes large $t(k)\rightarrow Nor(0,1)$ 
- **Expected Values and Variance**: $E[T]=0$ and $Var(T)=\frac{k}{k-2} \text{ k>2}$
- If T~t(k) then we denote that (1-a) quantile by $t_{a,k}$. In other words, $P(T>t_{a,k})=a$. 
	- Example: If T~t(10) then
	  $$P(T>t_{0.05,10}=0.05)$$
	  *where we find $t_{0.05,10}=1.812$* 

## F distribution
____
- Suppose we have:
    - $X \sim \chi^2(n)$: a chi-squared random variable with $n$ degrees of freedom.
    - $Y \sim \chi^2(m)$: a chi-squared random variable with $m$ degrees of freedom.
    - X and Y are independent.
- Then the statistic $F = \frac{X/n}{Y/m}$~$F(n,m)$​ follows an **F-distribution** with $n$ and $m$ degrees of freedom, denoted as $F \sim F(n, m)$.
- The PDF of the F-distribution with parameters $n$ and $m$ is: $$
f_F(x) = \frac{\Gamma \left( \frac{n + m}{2} \right)}{\Gamma \left( \frac{n}{2} \right) \Gamma \left( \frac{m}{2} \right)} \left( \frac{n}{m} \right)^{n/2} x^{n/2 - 1} \left( \frac{n}{m} x + 1 \right)^{-(n + m)/2}, \quad x > 0
$$
- If $F$~$F(n,m)$, then we denote the (1-a) quantile by $F_{a,n,m}$. That is $P(F>F_{a,n,m})=a$. 
- **Example**:
	- If we have $F\sim F(5,10)$ then $$P(F>F_{0.05,5,10})=0.05$$ where we find that $F_{0.05,5,10}=3.33$ in the book.