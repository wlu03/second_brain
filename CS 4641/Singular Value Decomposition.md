A SVD of a matrix is the factorization of the matrix into three matrix. The SVD of the matrix $A^{m \times n}$ is $A=U \Sigma V^T$ where:
	$U$: $m \times m$ matrix of the orthonormal eigenvector of $AA^T$
	$V^T$: Transpose of a $n \times n$ matrix containing the orthonormal eigenvectors of $A^TA$
	$\Sigma$: Diagonal matrix with $r$ elements equal to the root of the positive eigenvalues of $AA^T$ or $A^TA$. As you go down the diagonal, the values decrease. Its non-increasing.