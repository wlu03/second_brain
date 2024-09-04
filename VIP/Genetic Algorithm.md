Genetic Algorithms are **adaptive heuristic search algorithms** which optimize random searches by using old data to direct the search in a better solution space. They simulate natural selection. Genetic Algorithms chooses the samples which the "fittest" scores (ranked by heuristic) in which they combine to create a new generation of samples. Randomness is added to avoid local maximums through mutations on samples

```
1) Initialize population p
2) Determine fitness using heuristic 
3) Until convergence repeat:
	1) select parent from population
	2) crossover and generate new populaiton
	3) perform mutation on new population
	4) calculate fitness for new population
```

https://www.geeksforgeeks.org/genetic-algorithms/ finish