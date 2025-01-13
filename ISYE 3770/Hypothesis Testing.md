## Notes Hypothesis
Statistical hypothesis testing of parameters are the fundamental methods used at the data analysis stage of a comparative experiment. For example, comparing the mean of a population to a specific value. 
![[Screenshot 2024-11-18 at 9.40.40 PM.png]]
Hypothesis testing procedure rely on using the information in a random sample from the population of interest. If the information is consistent with the hypothesis, then we will conclude that the hypothesis is **true**. If this information is inconsistent with the hypothesis, we will conclude that the hypothesis is **false**.
![[Screenshot 2024-11-18 at 9.45.03 PM.png]]

### Two-Sided Alternative Hypothesis
$H_0: \mu = 50$  null hypothesis
$H_1: \mu \ne 50$  alternative hypothesis


#### One-sided Alternative Hypotheses
$H_0: \mu = 50$
$H_1: \mu > 50$

and 

$H_0: \mu = 50$ 
$H_1: \mu < 50$

![[Screenshot 2024-11-18 at 10.00.19 PM.png | 400]]
### Testing Procedure
1. State the **null** ($H_0$) and **alternative** $(H_1)$ hypotheses specify sample size $n$ and significance level $\alpha$. 
2. Define the test statistic and its distribution
3. Find one of the test statistic and the **rejection region of the null.** 
4. Collect sample data and calculate the **test statistic** using the **sample**
5. **Compare** the test statistic of the sample with the rejection region
6. Make the decision and assess the risk.
 
*Example:* Test on the mean of a Normal Distribution with $\sigma^2=4$. 
$H_0: \mu = 50$
$H_1: \mu \ne 50$
$n=5, a=0.05$

Test Statistic
$Z_0=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$

Rejection Region
$Z_0$~$N(0,1)$
$|Z_0|>Z_{a/2}=Z_{0.025}=1.96$

![[Screenshot 2024-11-18 at 9.51.36 PM.png]]


## Hypothesis Testing Using Confidence Intervals Mean of A Normal Population - Known Variance
___
Collect a sample and construct a $100(1-\alpha)\%$ CI
![[Screenshot 2024-11-18 at 10.08.17 PM.png]]
*Example*
The response time of a distributed computer system is an important quality characteristic. The system manager wants to know whether the mean response time to a specific type of command exceeds 75 millisec. From past experience, he knows that the standard deviation of response time is 8 millisecond. If the command is executed 25 times and the response time for each trial is recorded. The sample average response time is 79.25 millisec. Formulate an appropriate hypothesis and test the hypothesis. 

*Solution*
	$H_0: \mu = 75$
	$H_1: \mu > 75$
	$\sigma = 8 ms$
	$\bar{X}=79.25$
	$n=25, \alpha =5\%$
	Test Statistic:
	Use lower CI
	CI: $[\bar{X}-Z_a \frac{\sigma}{\sqrt{n}}, +\infty)$ 
	CI: $[79.25-1.645(\frac{8}{\sqrt{25}}), +\infty)$ 
	CI: $[76.618, +\infty)$
	Since 75 is not within the confidence interval, we can reject $H_0$. 

## P-Value
___
**Definition**: The smallest significance level that would lead to the rejection of the null hypothesis.
**Calculation**: Pr(obtaining a test statistic at least as extreme as the one observed | H0 is true)
**Conclusion**: if the p-vale < predefined $\alpha$, reject the null hypothesis
![[Screenshot 2024-11-18 at 10.20.11 PM.png]]
![[Screenshot 2024-11-18 at 10.20.44 PM.png]]

## Inference on the Mean of a Normal Population - *Unknown* Variance
___
![[Screenshot 2024-11-18 at 10.27.46 PM.png]]
![[Screenshot 2024-11-18 at 10.27.56 PM.png]]
*Example*
The mean time it takes a crew to restart an aluminum rolling mill after a failure is of interest. The crew was observed over 25 occasions, and the results were $\bar{x} = 26.42$ minutes and variance $S^2 = 12.28$ minutes. If repair time is normally distributed:

(a) Find a 95% confidence interval of the true mean repair time.  
	Since we don't know the standard deviation, we are estimating using the variance. 
	1. Confidence Interval Formula $$\bar{x}-t_{a,n-1}\frac{s}{\sqrt{n}}$$ where the confidence interval is $26.42 \pm 1.446 = (24.974, 27.866)$. This the 95% confidence interval. 
(b) Test the hypothesis that the true mean repair time is 30 minutes.  
	Null: $H_0: \mu = 30$
	Alternative: $H_1: \mu \ne 30$ (two tailed test)
	$t=\frac{\bar{x}-\mu_0}{S/\sqrt{n}}=\frac{26.42-30}{3.504/5}=-5.108$
	For $a=0.05$ and the degrees of freedom equal to $n-1=24$, the critical t-values are $\pm 2.064$. Since, t is less than 2.064, we reject the null hypo.

## Inference on Variance of a Normal Population
___
![[Screenshot 2024-11-18 at 11.43.39 PM.png]]
![[Screenshot 2024-11-18 at 11.43.54 PM.png]]

## Inference on a Population
___
![[Screenshot 2024-11-18 at 11.44.46 PM.png]]

![[Screenshot 2024-11-18 at 11.44.53 PM.png]]

## [[Type I and Type II Errors]]
___
![[Screenshot 2024-11-18 at 11.46.40 PM.png]]