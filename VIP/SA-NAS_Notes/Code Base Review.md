`utils.py`
- **Summary**: Support object-detection evaluation and some data-pre utils.
- `match_boxes(pred_boxes, true_boxes, iou_thresh, conf_thresh, mode, iou_type)`


`pipeline.py`
- This is the main class for the entire evolutionary process.
- Integrates a surrogate model to speed up/guide the evolutionary search.
- the workflow is:
	- initialize or resume run
		- It updates the pipeline's record in memory in order to resume a run
	- generation/expand a population (crossover, mutation, elite selection)
	- dispatch jobs to clusters to evaluate individuals
		- writes a csv output `eval_input_gen{self.gen_count}.csv` containing genome strings
	- Collect evaluation results
	- use surrogate to downselect
		- `prepare_surrogate(self)` builds training and validation dataset for the surrogate from historical data. trains the surrogate and choose the best sub-surrogate for each objective. Calculates and stores trust values for chosen surrogate.
	- record data 
	- repeat
`main.py` vs. `main_ssi.py`
- both scripts:
	- parse command arguments for slurm
	- initialize `pipeline`
	- runs the evolutionary loop 
- SSI:
	- the simulated surrogate injection logic 
	- SSI is a process where the evolutionary loop uses the surrogate to. guide the creation and selection of offsprings. 
	- this is injected when `GaPipeline.gen_count - ssi_start_gen) % ssi_freq == 0
	- For example, if `ssi_start_gen=5` and `ssi_freq=2`, then SSI will run at generation 5, 7, 9, 11, and so on. this is the case in `config.toml` file
## Surrogate
____
`surrogate.py`
- Class that handles:
	- Reading surrogate configs
	- Building and training different regression/classification models 
		- models are imported from `surrogate_models.py`
	- Encoding genomes for input into these models
		- encodes genomes using `codeC`
	- Infer classification predictions for new genomes
		- inference is imported from `surrogate_eval.py`
	- Assign predicted fitnesses to individuals
		- `deap` for individual/fitness
	- Measure "trust" of surrogates on validation set

`surrogate_models.py`


# Output Files
____
`holy_grail`: complete record of all individuals that were actually evaluated 
