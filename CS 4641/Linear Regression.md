# Dimensionality Reduction: PCA
___
- **PCA** is a technique used for dimensionality reduction. It's goal is to **maximize the variance** in the data by transforming the original features $X_{n\times d}$ (n is the number of samples, d is the number of features) into a new set of components $Z_{n \times d}$. 
- Each principal component $Z$ is a linear combination of the original features $X_1,X_2,...,X_d$ weighted by coefficient $w$ (e.g. $Z_1=w_{11}X_1+w_{21}X_2+...+w_{d1}X_d$). 
- This is called **feature engineering** when transforming feature space. 

**Example**
Image you have a dataset with two features: Height and Weight for a set of people. You want to use PCA to reduce these two features into one principal component that captures most of the variance in the data. 

1. **Standardize the Data**: PCA requires the data to be standardized (mean = 0, variance = 1) because it’s sensitive to the scale of the features.

| Person | Height | Weight |
| ------ | ------ | ------ |
| A      | 1.0    | 0.8    |
| B      | 0.5    | 0.4    |
| C      | -0.5   | -0.6   |
| D      | -1.2   | -1.1   |
2. **Calculate the Covariance Matrix**: The covariance matrix shows how each pair of features varies form the mean with respect to each other.  $$\text{Covaraince Matrix} = \begin{bmatrix}  
Var(Height) & Cov(Height, Weight)\\  
Cov(Weight, Height) & Var(Weight)  
\end{bmatrix} = \begin{bmatrix} 1.0 & 0.9 \\ 0.9 & 1.0\end{bmatrix}$$
3. **Calculate Eigenvalues and E-Vectors**: determine the direction (principal components) and magnitude (variance) of each component. Suppose we get eigenvalues: **1.9** and **0.1**.
	- Corresponding eigenvectors (principal component directions) could be:
    - First eigenvector: **[0.71, 0.71]** (for the eigenvalue 1.9)
    - Second eigenvector: **[-0.71, 0.71]** (for the eigenvalue 0.1)
4. **Select Principal Component**
	- The E-vectors with the largest eigenvalues in the first principal component (it explains the most variance)
	- Since we're reducing to one dimension. We keep only the first principal component
5. **Transform the Data**: Project the original data onto the new principal component. For each person, calculate the new value by multiplying the original height and weight values with the first principal component vector **[0.71, 0.71]**.
	- For instance, for **Person A**: $\text{New Value}: (1.0 \times 0.71) + (0.8 \times 0.71) = 1.278$
	- Repeat this for each person to get a new dataset with one principal components instead of two.
6. **Results**: Now, we have a single component that captures most of the variance in the data. The transformed dataset might look like this:

| Person | Principal Component |
| ------ | ------------------- |
| A      | 1.278               |
| B      | 0.639               |
| C      | -0.781              |
| D      | -1.491              |
This single component summarizes the height and weight features while retaining as much of the data's variance as possible, achieving dimensionality reduction. PCA helps simplify the dataset, making it easier to visualize or use in further modeling while preserving most of the essential information.
## Forward Feature Selection
____
Supervised method where features are added one by one and each addition is evaluated using a predictive model, LR in the case. The features like **height**, **weight**, and **age** are considered. Each feature is independently tested with LR and then their accuracies are compared. The features are added in combinations and their impact on the model's accuracy is tested. For example, (Age and Height give an accuracy of 0.87). The process continues by adding features that improve the model accuracy until a satisfactory performance is achieved. 

### Step-by-Step Forward Feature Selection Process

1. **Start with No Features**:
    
    - Begin with an empty set of selected features.
2. **Evaluate Each Feature Individually**:
    
    - Train a Logistic Regression model using each feature individually and evaluate its performance (e.g., accuracy or other relevant metric on a validation set).
    
    Suppose the results are as follows:
    
    - **Age**: 70% accuracy
    - **Income**: 72% accuracy
    - **Gender**: 65% accuracy
    - **Education Level**: 68% accuracy
    - **Marital Status**: 66% accuracy
3. **Select the Best Feature**:
    
    - Choose the feature that gives the highest accuracy. Here, **Income** (72% accuracy) is the best single feature, so we select it.
    
    **Selected Features**: `Income`
    
4. **Add the Next Best Feature**:
    
    - Now, evaluate each of the remaining features in combination with **Income** and pick the one that improves the model the most.
    
    Results with combinations:
    
    - **Income + Age**: 75% accuracy
    - **Income + Gender**: 73% accuracy
    - **Income + Education Level**: 74% accuracy
    - **Income + Marital Status**: 71% accuracy
    
    The combination **Income + Age** yields the highest accuracy (75%), so we add **Age** to the selected features.
    
    **Selected Features**: `Income, Age`
    
5. **Continue Adding Features**:
    
    - Repeat the process by testing the remaining features in combination with the selected features (`Income` and `Age`).
    
    Results with three-feature combinations:
    
    - **Income + Age + Gender**: 76% accuracy
    - **Income + Age + Education Level**: 78% accuracy
    - **Income + Age + Marital Status**: 74% accuracy
    
    Adding **Education Level** gives the best improvement (78% accuracy), so we include it in the selected features.
    
    **Selected Features**: `Income, Age, Education Level`
    
6. **Stop When No Further Improvement**:
    
    - Continue the process until adding more features no longer improves the model significantly.
    
    Suppose adding any of the remaining features (Gender, Marital Status) does not improve accuracy beyond 78%.
    

### Final Model

The selected features are **Income, Age,** and **Education Level**, which provide the highest accuracy for predicting **Purchase**. This subset of features gives the best trade-off between model complexity and performance.

## Backward Feature Selection
___
This is the opposite approach where all features are initially included in the model. The features are removed one at a time and each removal is evaluated to see if it improves or maintains models accuracy. This approach can help in identifying and discarding redundant features. 




# Intro
___
1. **Supervised Learning**:
   - The setup here shows a **supervised learning** problem, where the data consists of input features $X$ and corresponding target outputs $Y$.
   - The input data matrix $X$ has dimensions  $n \times d$, where $n$ is the number of samples, and $d$ is the number of features.
   - The target variable $Y$ is a column vector of dimension $n \times 1$, containing the output values associated with each sample in $X$.

2. **Regression**:
   - If the target variable $Y$ contains **continuous values** (e.g., 1.5, 7.6, 75.2), then the problem is a **regression** task.
   - In regression, the goal is to predict a continuous numerical value. Examples include predicting house prices, temperature, or any numerical measurement.

3. **Classification**:
   - If the target variable $Y$ contains **categorical values** (e.g., "cat," "dog," etc.), then the problem is a **classification** task.
   - In classification, the goal is to assign each sample in $X$ to a category or class label. Examples include predicting whether an email is spam or not, identifying an animal in an image, or categorizing types of products.

- In supervised learning, if $Y$ has continuous values, it's a **regression problem**.
- If $Y$ has categorical values, it's a **classification problem**.
![[Regression vs. Classification.png]]
- When there is more than two labels in a classification problem, it's a multi-class classification
## Overview
___
1. **Data and Function Representation**:
    
    - In supervised learning, we have a set of input features $X$ and corresponding output labels $Y$, where each data point is represented as a pair (xi,yi)(x_i, y_i)(xi​,yi​).
    - The goal is to find a function $f$ from a set of possible functions $\mathcal{F}$ that best maps $X$ to $Y$ by approximating the relationship between inputs and outputs.
2. **Data Split**:
    - The data is split into three parts:
        - **Training Data (70%)**: Used to train the model.
        - **Validation Data (10%)**: Used to tune model parameters and assess generalization.
        - **Testing Data (20%)**: Used to evaluate the final model performance after training.
    - This split ensures that the model is not overfitting or underfitting and can generalize well to unseen data.
3. **Learning Process**:
    
    - During the **learning phase**, the model tries to find the function fff that best approximates the true function that maps XXX to YYY.
    - The objective is to find $f∈\mathcal{F}$ such that for each input $x_i$​, the predicted output $\hat{y}_i=f(x_i)$ is as close as possible to the actual output $y_i$
    - This is achieved by minimizing some form of error (e.g., mean squared error for regression or cross-entropy for classification).
4. **Prediction Phase**:
    - After training, the learned function $\hat{f}$​ (often called the "learning machine" here) is used to make predictions on new, unseen data.
    - When new data xxx is input into the model, it produces a predicted output $\hat{y}=\hat{f}(x)$, allowing us to make predictions on data that the model has not encountered before.

# Linear Regression 
___
- Assume $y$ is a linear function of $x$ (features) plus noise $\epsilon$. $$\hat{y}_p=\theta_0+\theta_1x_1+...+\theta_dx_d+\epsilon$$
	- $\theta_0$ is the **intercept** of the line
	- $\theta_1,\theta_2,...,\theta_d$ are **coefficients** (weights) for each feature $x_1,x_2,...,x_d$
	- $\epsilon$ is the **random noise** or an **error term** which captures discrepancy between model and actual data. 
- Let $\theta =(\theta_0,\theta_1,...,\theta_d)^T$, and the augment data by one dimension, then $$y=x\theta +\epsilon$$
- $x$ is the feature vector $(x_1,x_2,...,x_d)$
- $\theta$ is the vector of parameters $(θ_0​,θ_1​,…,θ_d​)^T$ 
## Least Mean Squared Method
- Given $n$ data points, find the optimal parameters 𝜃 in linear regression by minimizing the mean squared error (MSE) between the predicted values and actual values.
$$L(\theta)=\frac{1}{n}\sum_{i=1}^{N}(y_i-x_i\theta)^2$$
- $y_i$ is the actual value
- $x_i\theta$ is the predicted value from $\hat{y}_p$ 
- N is the number of data points
- This calculates the average squared different (error) between actual and predicted values
- The MSE function is **convex** with respect to $\theta$ which means that it has a single global minimum. This property ensures that optimizing $\theta$ will converge 

- To minimize the MSE, set the gradient of the loss function with respect to $\theta$ to zero. 
- The gradient of $L(\theta)$ with respect to theta is: $$\frac{∂θ}{∂L}(θ)​=−\frac{2}{n}\sum_{i=1}^{N}​ x_i^T​(y_i​−x_i​θ)=0$$
- Setting this gradient to zero allows us to find optimal $\theta$
- Expanding the gradient, we get: $$\frac{∂θ}{∂L}(θ)​=−\frac{2}{n}\sum_{i=1}^{N}​ x_i^Ty_i+\frac{2}{n}\sum_{i=1}^{N}​ x_i^Tx_i\theta =0$$By setting the gradient to zero and solving, we can find $\theta$ (often done using matrix algebra, where $\theta =(X^TX)^{-1}X^Ty$

### SGD
1. Matrix Inversion can be costly for larger datasets $\theta =(X^TX)^{-1}X^Ty$. Therefore, we can use Gradient Descent and Stochastic Gradient Descent.
2. $$\frac{∂θ}{∂L}(θ)​=−\frac{2}{n}\sum_{i=1}^{N}​ x_i^T​(y_i​−x_i​θ)=0$$ This gradient tell us the direction and magnitude of change needed to minimize the loss. 
3. 