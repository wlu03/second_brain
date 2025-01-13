## Question 1
___
A melting point test of $n = 10$ samples of a binder used in manufacturing a rocket propellant resulted in $x̄ = 154.2°F$. Assume that the melting point is normally distributed with $σ = 1.5°F$.

(a) Test $H₀: μ = 155$ versus $H₁: μ ≠ 155$ at the $α = 1\%$ level of significance?
null: $H_0: \mu = 155$
alternative: $H_1: \mu \ne 155$
$n=10, a=0.01$

Test Statistic
$Z_0=\frac{\bar{X} - \mu}{\sigma/\sqrt{10}}=\frac{154.2-155}{1.5 / \sqrt{10}}= -1.688$
Rejection Region
$|Z_0| > Z_{0.01/2}$
$1.688 > 2.576$
This is not true, thus the null hypothesis is not rejected.

(b) What is the p-value for this test?
This is a two sided test. Thus the p-value is $2[1-\Phi(Z_0)]= 0.0914$  
 Since the pvalue is greater than $a=0.01$ we fail to reject the null. 
 
(c) What is the probability of committing a Type II error (i.e., β-error) if the true mean is μ = 150?
A type II error is where we don't reject $H_0$ and $H_0$ is not true.
$H_0: \mu =155$
$H_1: \mu \ne 155$
True mean $\mu_1: 150$
Sample Size = 10
Standard Deviation: 1.5
Significance Level $\alpha=0.01$

$$\beta=\Phi(Z_{a/2}-\frac{\delta\sqrt{n}}{\sigma})-\Phi(-Z_{a/2}-\frac{\delta\sqrt{n}}{\sigma})$$
$$Z_{a/2}=\Phi^{-1}(1-a/2)=\Phi^{-1}(1-0.005)=2.576$$
$$ \delta = u_0-u_1 = 155-150=5$$
$$\frac{\delta\sqrt{n}}{\sigma}=\frac{5\sqrt{10}}{1.5}=10.54$$
$$\beta=\Phi(Z_{a/2}-\frac{\delta\sqrt{n}}{\sigma})-\Phi(-Z_{a/2}-\frac{\delta\sqrt{n}}{\sigma})=\Phi(2.576-10.54)-\Phi(-2.576-10.54)=0$$
The probability is approximately zero. This means that if the true mean is 150, the test is always going to reject that $\mu=155$ because its so far away from the hypothesis. It's also zero because the std is relatively small. 

## Question 2
___
Cloud seeding has been studied for many decades as a weather modification procedure. 
The rainfall in acre-feet from 20 clouds that were selected at random and seeded with silver nitrate are as follows:
18.0, 30.7, 19.8, 27.1, 22.3, 18.8, 31.8, 23.4, 21.2, 27.9,  
31.9, 27.1, 25.0, 24.7, 26.9, 21.8, 29.2, 34.8, 26.7, 31.6

(a) Can you support a claim that mean rainfall from seeded clouds is 28.5 acre-feet? Use $𝛼 = 0.05$. 
Since the standard deviation is not known and you want to inference mean use the t test for hypothesis testing. 
$H_0: \mu=28.5$
$H_1: \mu \ne 28.5$
$a=0.05$
The sample mean is 
$t_0=\frac{\bar{X}=\mu_0}{S / \sqrt{n}}=\frac{23.54 - 28.5}{5.42/\sqrt{20}} = -4.10$
$|t_0|>t_{a/2,n-1}=2.093$. This statement is true so we reject the null hypothesis. There is sufficient evidence to conclude the population mean $\mu$ is not equal to 28.5.

(b) Explain how the question in part a could be answered by constructing a suitable confidence interval on the mean diameter.

$CI=[\bar{x}-t_{a/2,n-1}\frac{s}{\sqrt{n}}, \bar{x}+t_{a/2,n-1}\frac{s}{\sqrt{n}}]$
$t_{a/2,n-1}=2.093$
$\frac{5.42}{\sqrt{20}}=1.212$
$CI=[23.54-2.54, 23.54+2.54]=[21,26.08]$
Therefore, the hypothesis is not with the confidence interval. 

## Question 3
____
Suppose that 1000 customers are surveyed and 850 are satisfied or very satisfied with a corporation's products and service.

(a) Test the hypothesis $H_0:p=0.9$ against $H_1:p \ne 0.9$ at the significant level $\alpha=0.05$. Find the p-value.
$H_0: p=0.9$
$H_1: p\ne 0.9$
$Z_0=\frac{0.85 - 0.9}{\sqrt{\frac{0.9(0.1)}{1000}}}=-5.27$
$|Z_0|>Z_{a/2}=1.96$. Since this is true we reject the null hypothesis
The p-value is $\text{p-value}=2(P(Z\le -5.27))=0$. Since the p-value is smaller than the significance value we reject the null hypothesis. 

(b) Explain how the question in part (a) could be answered by constructing a 95% two-sided confidence for p.
$H_0: p=0.9$
$H_1: p\ne 0.9$
$CI=[\hat{p}-Z_{a/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}},\hat{p}+Z_{a/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} ]$
$CI=[0.85-0.0221, 0.85+0.0221]=[0.8279,0.8721]$
Therefore, it's clear to see that 0.9 is not in the confidence interval.

## Question 4
___
The deflection temperature under load for two different types of plastic pipes is being investigated. Two random samples of 15 pipe specimens are tested, and the deflection temperatures observed are as follows (in °F):

**Data**:
- **Type 1:** 206, 188, 205, 187, 194, 193, 207, 185, 189, 213, 192, 210, 194, 178, 205
- **Type 2:** 177, 197, 206, 201, 180, 176, 185, 200, 197, 192, 198, 188, 189, 203, 192

(a) Do the data support the claim that the deflection temperature under load for **Type 1** pipes exceeds that of **Type 2** pipes? Use $a=0.05$ 
$\bar{X}_1=196.4, S_1^2=116.17$
$\bar{X}_2=192.07, S_2^2=77.4$ 
$H_0: \mu_1 = \mu_2$
$H_1: \mu_1 > \mu_2$
$t=\frac{\bar{X}_1-\bar{X}_2}{S\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}=\frac{196.4-192.07}{9.8\sqrt{\frac{1}{15} + \frac{1}{15}}}=1.21$  
For a one tail test the critical t value is $t_{a,27}=1.703$. Since 1.21 < 1.703 we fail to reject the null hypothesis. There is insufficient evidence to support that type 1 exceeds type 2. 

(b) Calculate a P-value and make decision again
degrees of freedom: $v=\frac{(\frac{S_1^2}{n_1}+\frac{S_2^2}{n_2})^2}{\frac{(\frac{S_1^2}{n_1})^2}{n_1-1}+ \frac{(\frac{S_2^2}{n_2})^2}{n_2-1} }=27$
$p=1-t_v(t_0)=1-(0.881)=0.119$
Because the p-value is greater than the significance value 0.05 we fail to reject $H_0$ again. 

## Question 5
___
Fifteen adult males between the ages of 35 and 50 participated in a study to evaluate the effect of diet and exercise on blood cholesterol levels. The total cholesterol was measured in each subject initially and then three months after participating in an aerobic exercise program and switching to a low-fat diet. The data are shown in the following table
![[Screenshot 2024-11-19 at 1.48.04 AM.png]]

  
(a) Do the data support the claim that low-fat diet and aerobic exercise are of value in producing 
a mean reduction in blood cholesterol levels? Use α = 0.05.

| Subject | D_i |
| ------- | --- |
| 1       | 36  |
| 2       | 9   |
| 3       | 31  |
| 4       | 55  |
| 5       | 13  |
| 6       | 4   |
| 7       | 53  |
| 8       | 58  |
| 9       | 13  |
| 10      | 40  |
| 11      | 37  |
| 12      | 22  |
| 13      | 19  |
| 14      | -1  |
| 15      | 14  |
$t_0=\frac{\bar{d}-\Delta_0}{s_d/\sqrt{n}}=\frac{26.87}{19.04/\sqrt{15}}=5.47$
$\bar{d}=405/15=26.87$
$s_d=19.04$
The degree of freedom is n-1=14 and a=0.05
$t_{0.05,14}=1.761$
$5.47 > 1.761$ we reject $H_0$

(b) Find the P-value.  
The p-value is: $$\text{p-value}=1-t_{n-1(t_0)}=1-0.9999584=\text{near 0}$$
Because p is smaller than a, we reject the null hypothesis.

(c) Calculate a one-sided confidence limit that can be used to answer the question in part (a)
$\bar{d}-t_{a,n-1}\frac{s_d}{\sqrt{n}}$
$\bar{d}=26.87$
$s_d=19.04$
$n=15$
$t_{0.05,14}=1.761$
$$[26.87-(1.761\cdot(\frac{19.04}{\sqrt{15}})), \infty)=[18.21,\infty)$$
This means we are 95% confident that the true mean reduction is greater than 18.21.
## Question 6
___
Two chemical companies can supply a raw material. The concentration of a particular element in 
this material is important. The mean concentration for both suppliers is the same, but you suspect  that the variability in concentration may differ for the two companies. The standard deviation of concentration in a random sample of $n_1 = 10$ batches produced by company 1 is $s_1 = 4.7$ grams per liter, and for company 2, a random sample of $n_2 = 16$ batches yields $s_2 = 5.8$ grams per liter. Is there sufficient evidence to conclude that the two population variances differ? Use α = 0.05.

Use the inference on variance of two normal populations formula. 
$H_0: \sigma^2 = \sigma^2$
$H_1: \sigma^2 \ne \sigma^2$
Test Statistic: $F_0=\frac{s_1^2}{s_2^2} = \frac{4.7^2}{5.8^2}=0.656$

If both are true then $H_0$ is rejected.
$F_0 > F_{a/2, n_1-1, n_2-1}$
$F_0 > F_{0.025, 9, 15}$
$0.656 > 0.2653$
or 
$F_0 > F_{a/2, n_1-1, n_2-1}$
$F_0 < F_{0.975, 9, 15}$
$0.656 < 3.1227$

$F_0$ lies between the critical values thus it's not in the rejection region. There is insufficient evidence at a=0.05 to conclude the variance differs. 