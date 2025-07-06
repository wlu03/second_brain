1. Initialization 
	Start by **initializing a population** of candidates neural network architectures. This population can be generated randomly or guided by prior knowledge. 
2. Population Selection (Sustainable vs. Unsustainable)
	- Keep **better-performing** ones
	- Worse performing ones get replaced or evolve through mutation and crossovers
3. Train and Evaluate
	- For the promising architectures, do a expensive, direct training and obtain real performance metrics (accuracy, loss curves) 
	- This is a computationally heavy step thus can't do for all. 
4. Surrogate Evaluator
	- Instead of fully training _every_ architecture, you build a **surrogate model** that predicts how well a given architecture would perform if fully trained
	- Surrogate can be trained on:
		- Architecture features (numbers of layer, connectivity, filter sizes)
	- The surrogate model’s job is to give a **fast approximation** of the final performance of an architecture.
5. Surrogate Evaluator Trust
	- The system checks **how accurate** the surrogate's model performance are by comparing to the real metrics 
	- If the surrogate is trust is high enough, you can rely on its estimates
6. Down Selection and Error Calculation
	- You use the surrogate’s predicted performance to **filter (down select)** candidate architectures
	- Those with poor predicted performance get discarded (or go into the “Unsustainable Population”)
	- The error between the surrogate’s predictions and the real metrics is used to **update or retrain** the surrogate, improving its accuracy over time
7. Crossover/Mutations
	- To explore new architectures, you apply **genetic operations** such as crossover and mutation to the current best designs:
	- **Crossover**: Combine parts of two or more architectures
	- **Mutation**: Randomly alter parts of an architecture (e.g., adding or removing layers, changing kernel sizes)
8. Data Augmentation and Training
	- You might apply **data augmentation** (or other advanced training tricks) to improve generalization or to enhance the diversity of training samples used to update the surrogate
9. Iterative Loop
	1. Generate new architectures (via crossover/mutations)
	2. Evaluate them with surrogate
	3. Down select the best
	4. Fully train some of the best to get the real performance of the arch.
	5.  Update the surrogate model with those real measurements

## Search Space
____
In NAS, the search space defines the possible network architecture that can be explored. Must be discrete so can be searched yet rich to contain high performing models. Search space paradigms include: 
	Cell-based search space: These define a small computational graph called a cell and construct a full network by stacking or repating cells. Each cell is a micro-arch