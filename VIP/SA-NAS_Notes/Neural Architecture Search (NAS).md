NAS is a technique for automating the design of artificial neural networks used in machine learning. NAS has design networks that are on par or outperform hand designed architecture. The methods for NAS is categorized in **search space, search strategy, and performance estimation**.

An approach to NAS is based on evolutionary algorithms. An evolutionary algorithm for NAS performs the following. The pool consists of candidate architectures along with their validation score. At each step the architecture are mutated (3x3 convolution instead of a 5x5 convolution). Next the new architecture are trained from scratch. Replaces lowest scoring architectures in the candidate pool with better ones.

**Bayesian Optimization** is a method for hyperparameter optimization which can also be applied to NAS. The objective function maps an architecture to its validation error after being trained for a number of epochs. BO uses a surrogate to model this objective function based on previously obtained architecture.

RL or evolution based NAS required thousands of GPU days of searching/training to achieve state of the art results. To reduce computation cost, many recent NAS methods rely on the weight sharing idea. A supernetwork is a very large [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph "Directed acyclic graph") (DAG) whose subgraphs are different candidate neural networks.Thus, in a supernetwork, the weights are shared among a large number of different sub-architectures that have edges in common, each of which is considered as a path within the supernet. The essential idea is to train one supernetwork that spans many options for the final design rather than generating and training thousands of networks independently. 

Neural Architecture Search (NAS) has traditionally required substantial computational resources due to its intensive training and evaluation phases, leading to a significant carbon footprint. To address this, **NAS benchmarks** have been developed, which allow rapid querying or prediction of final performance for neural architectures, thereby drastically reducing computational requirements.

A **NAS benchmark** is a dataset structured with a predetermined train-test split, a defined search space, and a consistent training pipeline (fixed hyperparameters). These benchmarks fall into two main categories:

1. **Surrogate NAS Benchmarks**: These use a **surrogate model** (often a neural network) to predict the performance of an architecture within the search space, enabling faster evaluation by bypassing full training.
   
2. **Tabular NAS Benchmarks**: These provide a precomputed **lookup table** with actual performance metrics for architectures trained to convergence. Querying these tables yields precise results without needing to perform new, costly training runs.

Both types of benchmarks are highly **queryable** and can simulate many NAS algorithms effectively, often using only a CPU for queries. This approach streamlines the NAS process, saving both time and energy by eliminating the need to train each candidate architecture from scratch.