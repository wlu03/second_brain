## Abstract
___
- This paper is about the **problem of learning control policies for complex tasks given by logical specifications**. 
- Recent Approaches: auto-generate reward function from given specification and use RL algo to learn a policy to maximize expected reward. 
	- Problem: Scales Poorly to complex tasks. 
	- Solution: DIRL encodes specification as abstract graph. 
	  Vertices and Edges of graph correspond to regions of the state space and simpler sub tasks.
	  Uses RL to learn NN polices for each edge (sub-task) within a Djikstra planning algo to compute high level plans in the graph
## Intro
___
- RL automatically learns controlling policies for continuous control tasks. 
- Challenge for RL is specifying the goal due to the reward function ( hard to encode ). Thus, poor reward functions make it hard to RL algo to achieve goal 
- Recent works: Achieve short term subgoals to achieve complex task. 
- DIRL is a novel RL algorithm that leverages the structure in the specification to decompose the policy synthesis problem into a high level planning problem and set a low level control problem.