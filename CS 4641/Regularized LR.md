A quick overview of [[Linear Regression]] is that we are given the training set of $N$ observations for points $x_1$ to $x_N$ and $y_1$ to $y_N$. The regression problem is to estimate $y(x)$ from this data. We want to fit the polynomial regression model $y=\theta_0+\theta_1 x + \theta_d x^d+\epsilon$ where $z={1,x,x^2,..,x^d}$ and $\theta = (\theta_0,\theta_1,...,\theta_d)^T$.   Given $z$ and $\theta$, $y=z\theta$.

We can increase the maximum polynomial degree to very large such that the curve passes through each training point. However, this would **overfit** the model on the training data and would **perform poorly on testing or new data**. 
## Overfitting and Regularized Learning
___
Overfitting occurs when a model learns not only the underlying pattern but also the noise and random fluctuations. As a result the overfitted model performs well on training set but poor on new, unseen data. This can cause high variance within predictions. 
![[Screenshot 2024-11-03 at 1.50.40 PM.png | 250]] 
In regression, **overfitting** is associated with large weights. **Regularization** comes into play. This puts a "brake" on fitting. Regularization adds a term to the loss function discouraging complex models. 
![[Screenshot 2024-11-03 at 1.51.41 PM.png | 300]]

**Hard Constraint Example**
Regularization is just constraining the weights. For example a hard constraint would look something like this: $$\theta_d=0 \text{ for d > 2}$$
$$\text{Before: } y=\theta_0+\theta_1z_1+\theta_2z_2+...+\theta_dz_d$$
$$\text{After: } y=\theta_0+\theta_1z_1+\theta_2z_2+0+...+0$$
#### Error Function
The error function $E(\theta)$ represents the discrepancy between the predicated values of the model and the actual values. In the content of LR, the error function is defined as $$E(\theta)=\frac{1}{N}\sum_{i=1}^{N}(y^i-z_i\theta)^2$$
- $N$ is the number of data points 
- $y^i$ is the actual outputs for the $i$-th data point
- $z_i$ is the input feature vector for the data point
- $\theta$ is the vector of parameters (weights) the model is learning

The error function is **convex** meaning it has a single minimum. Minimizing the error function means finding the parameter  values that makes the predictions as close as possible to the output. 
#### Constraint Function
The constraint function $g(\theta)$ is to control the complexity of the model by restricting parameter values. One common form is: $$g(\theta)=\theta_0^2+\theta_1^2=\theta^T\theta=C$$ where $C$ is the constant that limits the size of the params. This is to enforce regularization and keeping the values to grow too large. This function creates the **iso-surface** in the parameter space. 
#### Lagrange Function
This function combines the error and constraint functions. This is to balance minimizing the error while keeping the $\theta$ constrained. $$L(\theta,\lambda)=E(\theta) +\lambda g(\theta)$$
- $\lambda$ is the Lagrange multiplier which controls this trade off of error and constraint.
By taking the gradient of $L(\theta,\lambda)$ and setting it to zero, we find the points where the balance between error and constraint is achieved.  $$\nabla L(\theta,\lambda)=0$$
$$\nabla[E(\theta)+\lambda\theta^T\theta]=0$$
$$\nabla[E(\theta)] +\lambda\nabla[\theta^T\theta ]=0$$
$$\nabla[E(\theta)]=-\lambda\nabla[\theta^T\theta ]$$
$$\nabla[E(\theta)]+2\lambda\theta=0$$
![[Screenshot 2024-11-03 at 2.23.39 PM.png | 300]]
#### Low Lambda vs. High Lambda
**Low**
- The regularization term is set to: $\frac{\lambda}{N}\theta^T\theta$ 
- When the $\lambda$ is low, the regularization term has little effect allowing the model to prioritize minimizing $E(\theta)$ without restricting the values of $\theta$. 
- This can cause larger values of $\theta$.
- Might cause overfitting.
**High**
- With higher values of lambda, the regularization term becomes more dominant. 
- Prevents $\theta$ from growing to large.
- Might cause underfitting.

### Regularized Learning
Minimize: $E(\theta)+\lambda\theta^T\theta$ 
**Regularized learning**, the goal is to minimize the **regularized error function**: $$\tilde{E}(\theta)=\frac{1}{N}\sum_{i=1}^{N}(y^i-z_i\theta)^2+\frac{\lambda}{2N}||\theta||^2_2$$
The second term is the L2 regularization term. 
## Ridge Regression
___
This is a type of LR that includes the L2 regularization term to prevent overfitting by penalizing large parameter values. $$\tilde{E}(\theta)=\frac{1}{N}\sum_{i=1}^{N}(y^i-z_i\theta)^2+\lambda||\theta||^2_2$$$||\theta||^2_2=\theta^T\theta$ is the L2 Norm (sum of the squared parameter values)

- The L2 regularization penalizes large param values shrinking the $\theta$ near zero. 
- This prevents model from fitting the noise in the data.

**General Form**
$$\tilde{E}(\theta)=\frac{1}{N}\sum_{i=1}^{N}(y^i-z_i\theta)^2+\frac{\lambda}{2}||\theta||^2_2$$
**Matrix Form**
$$\tilde{E}(\theta)=\frac{1}{N}(y-Z\theta)^T(y-Z\theta)+\frac{\lambda}{2}||\theta||^2_2$$
- $y$ is the vector of observed outputs
- Z is the matrix of input features

*Derivative of Ridge Regression*
$$\frac{\partial \tilde{E}(\theta)}{\partial \theta} = -Z^T(y-Z\theta)+\lambda \theta$$
$$-Z^T(y-Z\theta)+\lambda \theta=0$$
$$(Z^TZ+\lambda I)\theta =Z^Ty$$
- $Z^TZ$ is the covariance matrix of the features.
*Solve for $\theta$* 
$$(Z^TZ+\lambda I)^{-1}Z^Ty=\theta$$
**Example** 
![[Screenshot 2024-11-03 at 2.58.31 PM.png | 300]]
![[Screenshot 2024-11-03 at 2.58.38 PM.png | 300]]
![[Screenshot 2024-11-03 at 2.59.00 PM.png | 300]]
## Lasso Regression
___
Lasso Regression stands for Least Absolute Shrinking and Selection Operator. It uses the L1 norm. L1 norm induces sparsity. This means that some of the weights become zero and the feature contribution will completely remove. L1 regularizer could be used for feature selection. Lasso tends to eliminate certain features from the model. 
![[Screenshot 2024-11-03 at 3.03.34 PM.png]]
$$\tilde{E}(\theta)=\frac{1}{N}\sum_{i=1}^{N}(y^i-z_i\theta)^2+\lambda||\theta||_1$$
*Minimizing Error Function*
$$E(\theta)=\frac{1}{N}(zw-y)^T(z\theta-y)+\lambda||\theta||_1$$
$$\lambda ||\theta||_1=\lambda\sum_{j=1}^{d}|\theta_j|$$
- The absolute values is not differentiable at zero.
- We use **sub-gradients** for the L1 norm. This is a generalization of the gradient. 
	- If $\theta_j>0$, the sub-gradient is +1
	- If $\theta_j<0$, the sub-gradient is -1
	- If $\theta_j=0$, the sub-gradient is 0
Therefore: $$\frac{\partial \tilde{E}(\theta)}{\partial \theta}=-z^T(y-z\theta)+\lambda \text{sign}(\theta)$$
- The sign function is just the **sub-gradient** shown above. 

## Diff and Sim
____
![[Screenshot 2024-11-03 at 3.07.11 PM.png]]
## Determining Regularization Strength
___
### Leave One Out Cross Validation 
![[Screenshot 2024-11-03 at 4.09.50 PM.png | 300]] 
### K-Fold Cross Validation
![[Screenshot 2024-11-03 at 4.09.42 PM.png | 300 ]]
