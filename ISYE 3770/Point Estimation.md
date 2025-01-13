A [[Statistics |statistic]] is a function of observations and not explicitly dependent on any unknown parameters. 

Let $X_1,...,X_n$ be random variables. Let $T()=T(X_1,...,X_n)$ be statistic based on the $X_i$'s. Suppose we show the real value statistic $T()$ for the observations $x_1,x_2,...,x_n$ for $\hat{\theta}$ to estimate some unknown parameter $\theta$. $\hat{\theta}$ is called a point estimator for $\theta$. An example would be $\tilde{X}$ is a point estimator for the mean $\mu=E[X_i]$, so $\hat{\mu}=\tilde{X}$. $S^2$ is often a point estimator for the variance $σ^2 = Var(X_i)$. Therefore, $\hat{σ}^2 = S^2$. 

**Definition**: The difference between expectation of an estimator and the parameter is defined as **bias** of an estimator. $$Bias(\hat{\theta})=E(\hat{\theta})-\theta$$
Since the $\tilde{X}$ is always unbiased for $\mu$. That's why $\tilde{X}$ is called the sample mean.

## Example
___
We have a sample $X_1, X_2, \dots, X_n$ drawn independently and identically from a continuous uniform distribution $U(0, \theta)$, meaning each $X_i$ is uniformly distributed on the interval $(0, \theta)$. The probability density function of $X_i$ is:  
$$
f(x) = \frac{1}{\theta} \text{ for } 0 < x < \theta
$$  
Check if $Y_1$ and  $Y_2$ are unbiased estimators of $\theta$. An estimator $Y$ of a parameter  $\theta$ is unbiased if:  
$$
E[Y] = \theta
$$  

**Estimator $Y_1$**

- **Given**:  
  $$  
  Y_1 = 2\bar{X}  
  $$  
  where $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$  

- **Calculation**:  
  Since $X_i \sim U(0, \theta)$, we know that $E[X_i] = \frac{\theta}{2}$. Thus, the expectation of  $\bar{X}$ is:  
  $$  
  E[\bar{X}] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \frac{1}{n} \cdot n \cdot \frac{\theta}{2} = \frac{\theta}{2}  
  $$  

- **Expectation of $Y_1$**:  
  $$  
  E[Y_1] = E[2\bar{X}] = 2 \cdot E[\bar{X}] = 2 \cdot \frac{\theta}{2} = \theta  
  $$  

- **Conclusion**:  
  Since $E[Y_1] = \theta$, $Y_1$ is an **unbiased estimator** of $\theta$.

**Estimator $Y_2$**

- **Given**:  
  $$  
  Y_2 = \begin{cases}  
  12\bar{X} & \text{with probability } \frac{1}{2} \\  
  -8\bar{X} & \text{with probability } \frac{1}{2}  
  \end{cases}  
  $$  

- **Expectation of $Y_2$**:  
  To find $E[Y_2]$, we calculate the expectation based on the probabilities:  
  $$  
  E[Y_2] = \frac{1}{2} \cdot E[12\bar{X}] + \frac{1}{2} \cdot E[-8\bar{X}]  
  $$  

- **Calculations**:  
  Since $E[\bar{X}] = \frac{\theta}{2}$:  
  $$  
  E[12\bar{X}] = 12 \cdot \frac{\theta}{2} = 6\theta  
  $$  
  $$  
  E[-8\bar{X}] = -8 \cdot \frac{\theta}{2} = -4\theta  
  $$  

- **Result**:  
  $$  
  E[Y_2] = \frac{1}{2} \cdot 6\theta + \frac{1}{2} \cdot (-4\theta) = 3\theta - 2\theta = \theta  
  $$  

- **Conclusion**:  
  Since $E[Y_2] = \theta, Y_2$ is also an **unbiased estimator** of $\theta$.  

## Variance
___
Between two unbiased estimators, we prefer the one with a lower variance. Let $\hat{\theta}_1$ and $\hat{\theta}_2$ be unbiased estimators of the parameters $\theta$, $E(\hat{\theta}_1)=\theta$ and $E(\hat{\theta}_2)=\theta$. We prefer $\hat{\theta}_1$ over $\hat{\theta}_2$ if $$Var(\hat{\theta}_1)<Var(\hat{\theta}_2)$$
The **standard error** of an estimator is its standard deviation $\sqrt{Var(\hat{\theta})}$

## Mean Squared Error
___
The **MSE** of an estimator $\hat{\theta}$ of the parameter $\theta$ is $$MSE(\hat{\theta})=E[(\hat{\theta}-\theta)^2]$$ 
$$MSE(\hat{\theta}) =[Bias(\hat{\theta})]^2+Var(\hat{\theta})$$
**The lower the MSE the better**. 

#### Example 
Let $\mu$ and $\sigma^2$ be the mean and variance of the normal distribution. We’re given three estimators:

1. $\hat{θ}_1=\bar{X}$ (Sample mean)
2. $\hat{θ}_2=X_3$ (Single observation)
3. $\hat{θ}_3=0.5\bar{X}$​

**Bias for Each**
$\hat{\theta}_1$:
$$E[\hat{\theta}_1]=E[\bar{X}]=\mu$$
*this is an unbiased estimator*
$\hat{\theta}_2$:
$$E[\hat{\theta}_2]=E[X_3]=\mu$$
*this is an unbiased estimator*
$\hat{\theta}_3$:
$$E[\hat{\theta}_3]=E[0.5\bar{X}]=0.5E[\bar{X}]=0.5\mu$$
*this is a biased estimator*

**Variance for Each**
$\hat{\theta}_1$:
$$Var(\hat{\theta}_1)=Var(\bar{X})=\frac{\sigma^2}{n}$$
$\hat{\theta}_2$:
$$Var(\hat{\theta}_2)=Var(X_3)=\sigma^2$$$\hat{\theta}_3$:
$$Var(\hat{\theta}_3)=Var(0.5\bar{X})=0.5^2\cdot Var(\bar{X})=0.25 \cdot \frac{\sigma^2}{n}=\frac{\sigma^2}{4n}$$
**MSE of Each**
$\hat{\theta}_1$:
$$MSE(\hat{\theta}_1)=0+Var(\hat{\theta}_1)=\frac{\sigma^2}{n}$$
$\hat{\theta}_2$:
$$MSE(\hat{\theta}_2)=0+Var(\hat{\theta}_2)=\sigma^2$$$\hat{\theta}_3$:
$$MSE(\hat{\theta}_3)=(0.5\mu)^2+Var(\hat{\theta}_3)=\frac{\sigma^2}{4n} +(0.5\mu)^2 = \frac{\sigma^2}{4n} + 0.25\mu^2$$
*The third estimator should not be used because it is biased and has a higher MSE compared to 1 and 2. The first one should be the best estimator as it has the lowest MSE*

## Method of Moments
___
The $k^{th}$ moment of a random variable (RV) x is $$\mathbb{E}[X^k] = \begin{cases} \sum_x x^k f(x) & \text{if } X \text{ is discrete} \\ \int_{\mathbb{R}} x^k f(x) \, dx & \text{if } X \text{ is continuous} \end{cases}$$
**Definition:** Suppose $X_1, \dots, X_n$ are iid from pmf/pdf $f(x)$. Then the **method of moments (MOM)** estimator for $\mathbb{E}[X^k]$ is:
$$
\frac{1}{n} \sum_{i=1}^n X_i^k
$$
**Find MOM:** Let $$\mathbb{E}[X^k] = \frac{1}{n} \sum_{i=1}^n X_i^k$$Then try to find the parameter of your interest.
![[Screenshot 2024-11-11 at 1.08.46 PM.png]]
![[Screenshot 2024-11-11 at 1.09.09 PM.png]]
![[Screenshot 2024-11-11 at 1.09.19 PM.png]]

## Maximum Likelihood Estimators
____
Consider an random sample $X_1,...,X_n$ where each $X_i$ has a pdf/pmf $f(x)$. We suppose that $\theta$ is some unknown parameter from $X_i$. The likelihood function is defined as $$L(\theta)=\Pi_{i=1}^{n}f(x_i)$$
The maximum likelihood estimator (MLE) of $\theta$ is the value of $\theta$ that maximizes $L(\theta)$. The MLE is a function of $X_i$'s and is a RV.

Steps:
- Find $L(\theta)=\Pi_{i=1}^nf(x_i)$ 
- Take the natural log $ln(L(\theta))$
- Take the derivative with respect to $\theta$
- Solve $\frac{\partial ln(L(\theta))}{\partial \theta}=0$  and the answer is MLE for $\theta$ 

![[Screenshot 2024-11-11 at 1.38.24 PM.png]]
![[Screenshot 2024-11-11 at 1.56.47 PM.png]]
![[Screenshot 2024-11-11 at 1.57.06 PM.png]]



![[Screenshot 2024-11-11 at 1.48.29 PM.png]]
![[Screenshot 2024-11-11 at 1.48.58 PM.png]]

**Example**
We start with a set of observations $X_1, X_2, ..., X_n$ which are independent and identically distributed as $Normal(\mu,\sigma^2)$. The probability density function of a single observation $X_i$ from a normal distribution with mean $\mu$ and variance $\sigma^2$ is: $$f(x_i)=\frac{1}{\sqrt{2\pi \sigma^2}}exp(-\frac{(x_i-\mu)^2}{2\sigma^2})$$
The likelihood function for this example is: $$L(\mu, \sigma^2)=\Pi_{i=1}^{n}f(x_i)=\Pi_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}}exp(-\frac{(x_i-\mu)^2}{2\sigma^2})$$
Simplify the expression by factoring out constant across all terms. Because $\frac{1}{\sqrt{2\pi \sigma^2}}$ is a constant where it's multiplied $n$ times because of the capital Pi:
$$L(\mu, \sigma^2)= (\frac{1}{(2\pi \sigma^2)^{n/2}})exp(-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2)$$
Take the log-likelihood function
$$ln(L(\mu, \sigma^2))= ln((\frac{1}{(2\pi \sigma^2)^{n/2}})exp(-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2)) =ln((\frac{1}{(2\pi \sigma^2)^{n/2}})+ln(exp(-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2)) $$
Using the properties of $ln(a\cdot b)=ln(a)+ln(b)$ and $ln(e^x)=x$ we get:
$$ln(L(\mu, \sigma^2))= ln(\frac{1}{(2\pi\sigma^2)^{n/2}})-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2))$$
$$ln(L(\mu, \sigma^2))= ln(2\pi)^{-n/2}+ln(\sigma^2)^{-n/2}-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2))$$
$$ln(L(\mu, \sigma^2))= -\frac{n}{2}(2\pi)-\frac{n}{2}(\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2))$$

**Differentiate with respect to $\mu$**
$$\frac{\partial}{\partial \mu}ln(L(\mu, \sigma^2))=\frac{\partial}{\partial \mu}( -\frac{n}{2}(2\pi)-\frac{n}{2}(\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2))) $$
Since only the last term depends on $\mu$ then out the first two as they are constant in this equation
$$\frac{\partial}{\partial \mu}ln(L(\mu, \sigma^2))=-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2 $$
$$=-\frac{1}{2\sigma^2}(\frac{\partial}{\partial \mu}\sum_{i=1}^{n}(x_i^2 - 2x_i\mu+\mu^2 )) $$
$$=-\frac{1}{2\sigma^2}(-2\sum_{i=1}^nx_i+2n\mu)) $$
- This is because $x_i^2$ is a constant (equals 0), $-2x_i \mu$ is computed to $-2x_i$, and $\mu^2$ is computed to $2\mu$ (the $n$ comes from the summation).

Set it equal to zero to find the maximum
$$\frac{1}{\sigma^2}(\sum_{i=1}^nx_i-n\mu)=0 $$$$(\sum_{i=1}^nx_i-n\mu)=0$$
$$\frac{1}{\sigma^2}(\sum_{i=1}^nx_i-n\mu)=0 $$$$\sum_{i=1}^nx_i=n\mu$$
$$\frac{1}{n}\sum_{i=1}^nx_i=\mu$$
The MLE for $\mu$ is the sample mean
$$\bar{X}=\frac{1}{n}\sum_{i=1}^nx_i=\mu$$
**Differentiating by $\sigma^2$**
$$\frac{\partial}{\partial \sigma^2}ln(L(\mu, \sigma^2))=\frac{\partial}{\partial \sigma^2}( -\frac{n}{2}(2\pi)-\frac{n}{2}(\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2))) $$
take $\sigma^2$ dependent variables 
$$=\frac{\partial}{\partial \sigma^2}(-\frac{n}{2}(\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2)$$
- $\frac{\partial}{\partial \sigma^2}(-\frac{n}{2}(\sigma^2) =-\frac{n}{2}\cdot \frac{1}{\sigma^2}=-\frac{n}{2\sigma^2}$
- $\frac{\partial}{\partial \sigma^2}(-\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2)= -\frac{1}{2}(\sum_{i=1}^{n}(x_i-\mu)^2) \cdot (-\frac{1}{\sigma^4})$
$$= -\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}(\sum_{i=1}^n(x_i-\mu)^2) $$
Set the derivative to zero
$$-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}(\sum_{i=1}^n(x_i-\mu)^2)=0 $$
multiply both sides by $2\sigma^4$
$$-n\sigma^2+(\sum_{i=1}^n(x_i-\mu)^2)=0 $$
$$n\sigma^2=(\sum_{i=1}^n(x_i-\mu)^2) $$
$$\sigma^2=\frac{1}{n}(\sum_{i=1}^n(x_i-\mu)^2) $$
The MLE for $\sigma^2$ is the following above. This is the average squared deviation of each observation from the mea. This is different from the sample variance formula which is divided by $n-1$ instead of $n$.

## Properties of MLE
**Invariance Property**: If $\hat{\theta}$ is the MLE of some parameter $\theta$ and $h(\cdot)$ is a one to one function, then $h(\hat{\theta})$ is some MLE of $h(\theta)$. For instance although $E[s^2]=\sigma^2$, it is usually the case that $E[\sqrt{s^2}]\neq \sigma$ ![[Screenshot 2024-11-11 at 2.37.41 PM.png]]![[Screenshot 2024-11-11 at 2.37.56 PM.png]]