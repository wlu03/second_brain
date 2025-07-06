1. A manufacturer produces piston rings for an automobile engine. It is known that ring diameter is  normally distributed with σ = 0.001 millimeters. A random sample of 15 rings has a mean diameter of 𝑥̅ = 74.036 millimeters.
	a. Construct a 99% two sided confidence interval on the mean piston ring diameter
		$$\bar{X}\pm Z_{a/2}\frac{\sigma}{\sqrt{n}}$$
		where $Z_{a/2}$ corresponds to 99% confidence level, $\sigma =0.001, \bar{x}=74.036,\text{ and } n=15$
		This means that $$74.036\pm2.575 (\frac{0.001}{\sqrt{15}})=74.036\pm0.000665 =[74.035335,74.036665]$$
	b. Construct a 99% lower confidence bound on the mean
		$\bar{x}-Z_a \frac{\sigma}{\sqrt{n}}$ where $Z_a$ corresponds to 99% confidence level,  $\sigma =0.001, \bar{x}=74.036,\text{ and } n=15$. Then $$74.036-2.326(\frac{0.0001}{\sqrt{15}})=74.036-0.0006006=74.0354$$
	c. Compare the lower bound in part (b) with the confidence interval in part (a).
		The two sided provided a range of a 99% interval while (b) provided a lower bound without an upper bound. This means that the one-sided bound is slighter higher than (a).
2. A rivet is to be inserted into a hole. A random sample of n = 15 parts is selected, and the hole  diameter is measured. The sample standard deviation of the hole diameter measurements is s =  0.008 millimeters. Construct a 99% lower confidence bound for $\sigma^2$.
	a. Using the Chi-square distribution for a lower confidence bound on variance uses the formula: $$\frac{(n-1)s^2}{\chi_{a,n-1}^2}$$ where $s=0.008, n=15, \chi^2_{a,n-1}$ is the 99% confidence level. The lower confidence bound for the variance is: $$\frac{(n-1)s^2}{\chi^2_{0.01,14}}=\frac{(14)0.008^2}{29.141}=0.00003074705$$
3. An article in the Journal of the American Statistical Association (1990, Vol. 85, pp. 972–985)  measured the weight of 30 rats under experiment controls. Suppose that 12 were underweight rats
	a. Calculate a 95% two-sided confidence interval on the true proportion of rats that would show underweight from the experiment.
		For proportions p, the confidence interval is $$p\in \bar{X}\pm z_{a/2}\sqrt{\frac{\bar{X}(1-\bar{X})}{n}}$$
		where $\bar{X}=12/30$ and $n=30$ then the two sided confidence interval is $$=\frac{12}{30}\pm(1.96)\sqrt{\frac{(12/30)(18/30)}{30}}=[0.22556, 0.57444]$$
	b. Using the point estimate of p obtained from the preliminary sample, what sample size is  needed to be 95% confident that the error in estimating the true value of p is less than 0.02?
		Point estimate of p from (a) is $\hat{p}=0.4$. The margin of error less is 0.02. The Z-score for two sided confidence level is 1.96. 
		$$\text{sample size }= \frac{z^2_{a/2} * p(1-p)}{E^2}$$
		$$\text{sample size }= \frac{1.96^2 * 0.24}{0.02^2}=\frac{0.921984}{0.0004}=2304.96$$
		Therefore, the sample size need to be 2305.
	c. How large must the sample be if you wish to be at least 95% confident that the error in estimating p is less than 0.02, regardless of the true value of p?
		Regardless of proportion, you need the largest sample size. Therefore use p = 0.5. $$\text{sample size }= \frac{z^2_{a/2} * p(1-p)}{E^2}$$ $$\text{sample size }= \frac{1.96^2 *0.25}{0.02^2}=\frac{0.9604}{0.0004}=2401$$
		The required sample size needs to be 2401. 
	d. Find a 95% confidence interval on the difference in mean etch rates.
		Solution 1 $\bar{X_1}=\frac{9.9+9.4+9.3+9.6+10.2+10.6+10.3+10+10.3+10.1}{10}=10.07$ 
		Solution 2 $\bar{X_2}=\frac{10.2+10.6+10.7+10.4+10.4+10.5+10+10.2+10.7+10.4+10.3}{10}=10.5$ 
		Solution 1 Std = $0.396$
		Solution 2 Std = $0.271$
		To find the 95% confidence interval for the different in mean is: $$(\bar{X_1}-\bar{X_2})\pm z_{a/2}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}=10.5-10.07\pm(1.96)\sqrt{\frac{0.396^2}{10}+\frac{0.271^2}{10}}=0.43\pm0.298=[0.132, 0.728]$$
		The 95% confidence interval that $\bar{x}_2-\bar{x}_1$ is $[0.132, 0.728]$
		