## Linear Algebra Basics
____
-  Linear Algebra represents and operates on sets of linear equations.
- For example, these two equations: $4x_1 -5x_2 = -13$  and  $-2x_1+3x_2=9$  can be represented using $Ax=b$, where $A=\begin{bmatrix}  4 & -5\\   -2 & 3 \end{bmatrix}$, $b=\begin{bmatrix}  -13\\  9 \end{bmatrix}$. 
- $A \in \mathbb{R}^{n \times d}$ represents a matrix with $n$ rows and $d$ columns where elements belong to real numbers. For example, the $b$ matrix earlier would be $b \in \mathbb{R}^{2 \times 1}$. 
- $x\in R^d$ denotes a vector with $d$ real entries. 

### Special Matrices
- A **identity** matrix is denoted by $I\in \mathbb{R}^{d \times d}$ is square matrix with ones on the diagonal and zeros everywhere else.
- A **diagonal** matrix is a matrix where all non diagonal elements are zero. Its denoted as $D=diag(d_1,d_2,...d_n)$
- Vector vectors $x,y \in \mathbb{R}^d$ are **orthogonal** if their dot product is zero, $x\cdot y = 0$. 
- A square matrix $U\in \mathbb{U}^{d \times d}$ is **orthonormal** if all its columns are orthogonal to each other and are normalized. 
- Orthogonality and Normality rules: 
	- $U^TU=I=UU^T$
	- $||Ux||_2=||x||_2$  
### Transpose Rules
- Transpose of a matrix results from flipping the rows and columns. Given $A\in \mathbb{R}^{n\times d}$, transpose is $A^T\in \mathbb{R^{d\times n}}$. 
- For the elements of the matrix, the transpose can be written as $A^{T}_{ij}=A_{ji}$. 
- The following properties are rule:
	- $(A^T)^T=A$
	- $(AB)^T=B^TA^T$
	- $(A+B)^T=A^T+B^T$
## Norms 
___
The **norm** of a vector $||x||$ is informally a measure of the length of a vector. Formally, a norm is any function $\mathbb{f}: \mathbb{R}^d \rightarrow \mathbb{R}$ that satisfies:
- Non-negative: for all $x\in \mathbb{R}^d,f(x)\ge0$
- Definiteness: $f(x)=0$ is and only if $x=0$
- Homogeneity: for $x\in \mathbb{R}^d, t\in\mathbb{R},f(tx)=|t|f(x)$
- Triangle Inequality: for all $x,y\in\mathbb{R}^d,f(x+y) \le f(x)+f(y)$ 
### Common Norms
- $l_1 \space norm : Manhattan \space norm$ 
	- $||x||_1=\\sum_{i=1}^d |x_i|$ 
	- **Example**: For $v=\begin{bmatrix}  3\\  -4 \\ 1 \end{bmatrix}$, $||v||_1=|3|+|-4|+|1|=8$
- $l_2 \space norm : Euclidean \space norm$ 
	- $||x||_2=\sqrt{\sum_{i=1}^d x_i^2}$ 
	- **Example**: For $v=\begin{bmatrix}  3\\  -4 \\ 1 \end{bmatrix}$, $||v||_2 = \sqrt{3^2+(-4)^2+1^2} =\sqrt{26}$
- $l_{\infty} \space norm:Maximum \space norm$ 
	- $||x||_{\infty}=max_i|x_i|$
	- **Example**: For $v=\begin{bmatrix}  3\\  -4 \\ 1 \end{bmatrix}$, $||v||_{\infty} = max(|3|,|-4|, |1|) = 4$
- These normals are in the family $l_p$ norms which is parameterized by a real number $p \ge 1$. 
	- $||x||_p=(\sum_{i=1}^n |x_i|^p) ^{1/p}$
- Norms can be defined for matrices such as the Frobenius Norm
	- $||A||_F=\sqrt{\sum_{i=1}^n \sum_{j=1}^d A_{ij}^2} = \sqrt{tr(A^T A)}$
	- $A=\begin{bmatrix}  1 & -2 & 3\\   -4 & 5 & -6 \end{bmatrix}$, $||A||_F=\sqrt{1^2+(-2)^2+3^2+(-4)^2+5^2+(-6)^2} = \sqrt{91}$
## Multiplications 
___
The product of two matrices $A\in\mathbb{R}^{n \times d}, B \in\mathbb{R}^{d \times p}$ is given by $C \in \mathbb{R}^{n \times p}$ where $C_{ij} = \sum_{k=1}^d A_{ik}B{kj}$  

**Dot Product**: Given two vectors $x,y \in R^d$, the dot product of these vector is denoted as $x\cdot y= \sum_{i=1}^{n}x_iy_i$.
	The product product has a geometrical interpretation with the angle $\theta$. $x\cdot y =|x||y|\cos \theta$
	$\theta = 90 \degree$, then orthogonal aka $x\cdot y=0$
	$\theta < 90 \degree$, then $x\cdot y$ is positive  
	$\theta > 90 \degree$, then $x\cdot y$ is negative
**Outer Product**: Given two vectors $x \in R^d, y \in R^n$ the term $x^Ty$ is called the outer product of the vectors: $x\otimes y$. 
	$x\otimes y=x^Ty=\begin{bmatrix}  x_1\\  x_2 \\ x_3 \end{bmatrix} \begin{bmatrix}  y_1 & y_2 & y_3 \end{bmatrix} = \begin{bmatrix}  x_1y_1 & x_1y_2 & x_1y_3\\  x_2y_1 & x_2y_2 & x_2y_3 \\ x_3y_1 & x_3y_2 & x_3y_3 \end{bmatrix}$ 
	
## Matrix Inversion
____
### Linear Independence and Matrix Rank
- A set of vectors $\{ x_1,x_2,...,x_d \} \subset \mathbb{R}^d$  is linearly independent if no vector can be represented as a linear combination of the remaining vector
- The **column rank** of a matrix $A\in \mathbb{R}^{n \times d}$ is the size of the largest subset of columns of A that is linearly independent. **Row rank** of a matrix is defined similarly.

### Inverse
- The inverse of the square matrix $A\in R^{d\times d}$ is denoted as $A^{-1}$ and is unique matrix that $A^{-1}A=I=AA^{-1}$. 
- If there is not inverse for some square matrix, then it's **singular or non-invertible**.
- Must be **full rank** to have inverse.
- A **pseudo inverse** is denoted as $A^+$ where $A$ is a non-square matrices. $A^+ = (A^TA)^{-1}A^T$ 
## Trace and Determinants
____
### Trace
The trace of a matrix $A \in \mathbb{R}^{d\times d}$ denoted as $tr(A)$ is the sum of the diagonal elements in the matrix. The trace helps compute the **norms** and **eigenvalues** of matrices.$$tr(A)=\sum_{i=1}^d A_{ii}$$
The following properties are for the trace given that $A\in \mathbb{R}^{d\times d},B\in \mathbb{R}^{d\times d}$:
- $tr(A)=tr(A^T)$
- $tr(A+B)=tr(A)+tr(B)$
- $tr(tA)=t\cdot tr(A)$ for some real value $t$
- For $A,B,C$ such that $ABC$ is a square matrix, any combination of their trace is equal
### Determinants
The determinant of a square matrix $A$, denoted by $|A|$ is defined as $$det(A)=\sum_{j=1}^d (-1)^{i+j}a_{ij} M_{ij}$$
where $M_{ij}$ is determinant of matrix $A$ without the row $i$ and column $j$.  

For a $2x2$ matrix $A= \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $|A|=ad-bc$.
**Properties**: 
	$|A|=|A^T|$
	$|AB|=|A||B|$
	$|A| = 0$ if and only if $A$ is not invertible/**singular**
	If A is invertible, then $|A^{-1}|=\frac{1}{|A|}$

## Eigen Values & Vectors
___
Given a square matrix $A$ we say that $\lambda \in \mathbb{C}$ is an eigenvalue of $A$ and $x\in\mathbb{C}^d$ is an eigenvector if $Ax=\lambda x, x\neq0$. This means that multiplying the matrix A with a vector $x$ we get the same vector bur scaled by the eigenvalue. To find the **eigenvalue**, use this equation: $$det(A-\lambda I)=0$$ ![[Eigenvalue.png]]
## [[Singular Value Decomposition]] (SVD)
____
A SVD of a matrix is the factorization of the matrix into three matrix. The SVD of the matrix $A^{m \times n}$ is $A=U \Sigma V^T$ where:
	$U$: $m \times m$ matrix of the orthonormal eigenvector of $AA^T$
	$V^T$: Transpose of a $n \times n$ matrix containing the orthonormal eigenvectors of $A^TA$
	$\Sigma$: Diagonal matrix with $r$ elements equal to the root of the positive eigenvalues of $AA^T$ or $A^TA$
**Singular values** of a matrix are the positive square roots of the eigenvalue of AA or A.
**Example**: 
	Find the SVD of the matrix $A=\begin{bmatrix} 3 &2&2 \\ 2&3&-2 \end{bmatrix}$ 
	To find the SVD, first compute the singular values by finding eigenvalues of $AA^T$
	$A\cdot A^T=\begin{bmatrix} 3 &2&2 \\ 2&3&-2 \end{bmatrix} \ cdot \begin{bmatrix} 3&2 \\ 2&2 \\ 2&-2 \end{bmatrix} = \begin{bmatrix} 17 & 8 \\ 8 & 17\end{bmatrix}$ 
	$AA^T-\lambda I=0$, the singular values are $\sigma_1 =5, \sigma_2 =3$
	The eigenvalues for $A^TA$ is $25, 9,0$.

https://www.geeksforgeeks.org/singular-value-decomposition-svd/