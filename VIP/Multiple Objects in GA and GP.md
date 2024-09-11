**Terminology**
______
Multiple objective is the power of supplying a population of solution not just a single objective. Gene pool is the set of genome to be evaluated during the current generation. Genome can be: DNA, set of values (GA), and tree structure/string (GP). The search space is the set of all possible genomes. 

The **evaluation** of a genome associates a genome with a set of scores. *True Positive* (TP) is the value we want - how often are we identifying the desired object.*False Positive* (FP) is how often we are identifying something else as the desired object. 

**Classification**
_____
In [[genetic algorithm]], specifically classification tasks, these metrics are used to serve as part of the fitness function. The fitness function in GA evaluates how a given solution performs using the maximizing metrics the **true positive rate** (TRP/Sensitivity/hit rate/recall) is equal to $$TPR =TP/P=TP/(TP+FN)$$Another maximization measure is the **specificity (SPC)** or  **true negative rate (TNR)** where it equals $$TNR =TN/N=TN(TN+FP)$$
![[Multiple Objects in GA and GP Figure 1.png]]
**Minimization** measures the **false negative rate (FNR)** where it equals $$FNR =FN/P=FN/(TP+FN)$$ $$=1-TPR$$
Another minimization used is the **fallout** or **false positive rate (FPR)** $$FPR=FP/N=FP/(FP+TN)$$
$$=1-TNR=1-SPC$$
![[Multiple Objects in GA and GP Figure 2.png]]

![[Multiple Objects in GA and GP Figure 3.png]]
The metrics from the confusion matrix can be used to provide feedback in GA. This feedback fine the parameters like *mutation rate, crossover rate,* and *population size* to explore the solution space.
![[Multiple Objects in GA and GP Figure 4.png]]

**Objective Space**
___
Each individual is evaluated using objective functions: *mean squared error, cost, complexity, TPR, FPR, etc.* The objective score gives each individual a point in object space. 

**Pareto Optimality**
____
If there is no other individual in the population that outperforms the individuals on all objective, that individual is **Pareto**. The set of all Pareto individuals is known as the Pareto Frontier (*as shown below*). These individuals are factors we want to drive selection from, but maintaining diversity by giving them all probability of mating.
![[Multiple Objects in GA and GP Figure 5.png | 400]] 

### Algorithms
Below are algorithms that find a set of Pareto-Optimal Solutions for problems with multiple conflicting objectives. 

**Nondominated Sorting GA II (NSGA II)**
____
- **Sorting**: This algorithm divides population into different fronts based on Pareto dominance. First front consists of solutions not dominated by other. Second front consists of solutions dominated by only one. This trend continues til the last front. Individuals are selected through a binary tournament where $higher\space pareto > lower \space pareto$. 
- **[[Crowding Distance]]**: Uses CD to maintain diversity and ensures that the solutions are spread across the Pareto front by preferring solutions with higher crowding distance. Ties are broken this way.
![[NSGA II.png]]
**Strength Pareto Evolutionary Algorithm 2**
____
- **Strength & Rank Assignment**: SPEA2 assigns strength value to each individuals - represents number of solutions it dominates. The rank is the sum of all strength value of the individual dominates. Pareto individuals are nondominated and have a rank of 0.
- **K-nearest neighbor density estimation**: SPEA2 uses a density estimator based on distance to the $k-$th nearest neighbor ensuring diversity for solutions. This value is $\sigma ^k$ and a fitness of $\frac{R+1}{\sigma ^k +2}$ is obtained.
- **Archive**: SPEA2 maintains archive updated in each generation to store and refine the best solution. 
![[SPEA2.png]]

