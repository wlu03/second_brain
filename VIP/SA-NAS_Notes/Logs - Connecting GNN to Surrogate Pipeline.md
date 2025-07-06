**Setup for Writing Code**
```
module load anaconda3/2023.03
module load cuda/11.8.0
salloc -N1 -t5:00:00 --gres=gpu:H100:1 --ntasks-per-node=1
conda activate nas
```

To connect GNN-based surrogate (SimpleGCN in `GNN.py`) into the surrogate pipeline:
- I will wrap GNN into the surrogate model so the pipeline can view it
- Extend surrogate dataset builder so it hands the GNN PyG `Data` objects

____

`surrogate_models.py`
- I will add a new class called GNNSurrogate: currently using SimpleGCN
- this is a small wrapper so that 
``` python
class GNNSurrogate(nn.Module):

def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
	super().__init__()
	self.net = SimpleGCN(input_dim, hidden_dim, output_dim)

def forward(self, data):
	# data: a torch_geometric.data.Data
	return self.net(data)
```
____

`surrogate_dataset.py`
- add new dataset class that turns each data frame into a PyG object for the GNN to use 
![[Screenshot 2025-04-24 at 9.58.04 PM.png]]
_____

`surrogate.py`
- add the GNN surrogate to enable the pipeline to use

``` python
self.models.appned({
	'name': 'gnn_surrogate',
	'model': sm.GNNSurrogate,
	'input_dim': model_config["num_module_types"],
	'hidden_dim': 64,
	'output_dim': len(self.METRICS),
	'optimizer': torch.optim.Adam,
	'lr': 0.001,
	'scheduler': torch.optim.lr_scheduler.ReduceLROnPlateau,
	'metrics_subset': list(range(len(self.METRICS))),	
	'validation_subset': list(range(len(self.METRICS))),
},
$```
- and added a GNN training block
![[Screenshot 2025-04-24 at 8.48.57 PM.png]]

___
`codec.py`
![[Screenshot 2025-04-24 at 8.53.40 PM.png]]![[Screenshot 2025-04-25 at 1.31.40 PM.png]]