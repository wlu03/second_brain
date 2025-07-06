**Setup for Writing Code**
```
module load anaconda3/2023.03
module load cuda/11.8.0
salloc -N1 -t5:00:00 --gres=gpu:H100:1 --ntasks-per-node=1
conda activate nas
```

| File                      | `graph_data.x`                                 | `graph_data.hyperparams`                  | Node-feature interpretation                                                                                                                                                           |
| ------------------------- | ---------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **data.pt**               | a float tensor of shape `[num_nodes, 28]`      | **(none)**                                | Each row is a 28-dim **one-hot** encoding of the module’s type. You had 28 unique module types.                                                                                       |
| **data_with_encoding.pt** | a long (integer) tensor of shape `[num_nodes]` | a float tensor of shape `[num_nodes, 43]` | • `x[i]` is the **type‐index** (0…N_types–1) for node i.  <br>• `hyperparams[i]` is the 43-dim vector of all that module’s numeric constructor arguments (your “universal template”). |
# `Data.pt`
- `data.pt` file is a pre-processed dataset that feeds into the GNNs (simple ones) `data = torch.load(data.pt)`
- This un-pickle the Python object 
- Then wrap it `dataset = MyDataset(data)`
- This is used as training data for the GNN
``` python
train_dataset, test_dataset = random_split(dataset, [...])
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader  = DataLoader(test_dataset, batch_size=32, shuffle=False)
```
- Each batch's `data` object (a `torch_geometric.data.Data` instance) and its corresponding `labels` coms from `data.pt`
- Within `data_handling.py` is where the data is currently generated

# `Data_withEncoding.pt`
- Make a new function called `generate_data_withencoding_pt` to generate a `data.pt` to include the hyper-parameters

Here's how I did it:
- Encoding functions in `data_handling.py`
	- `encode_module_index()`: assigns an integer index to each module type
	- `encode_module_hyperparams_v1()`: encodes module hyper-parameters into a fixed length vector 
- Graph Creation in `data_handling.py`
	- `create_graph_repr_custom()`: Creates a PyG data object with your encoding strategy:
		- `combined`: stores module type indices in `data.x` and a hyper-parameter vector in `data.hyperparams`
- Data Object Creation in `data_handling.py`
	- `create_data_object()`: uses `create_graph_repr_custom()` with `encoding_strategy="combined"` currently to create an object
- Data Generation in `data_handling.py`
	- `generate_data_pt()`: creates and saves the data.pt file

``` python
def generate_data_withencoding_pt(csv_path, set_types_pkl, selected_metrics, output_file="data_with_encoding.pt"):

"""
Generate a new data_with_encoding.pt file that includes the combined encoding strategy.

This is to be used by CombinedGCN for training in GNN.py

Parameters:
	csv_path (str): Path to the CSV file (e.g. compiled_data_valid_only.csv).
	set_types_pkl (str): Path to the pickle file containing the set of module types.
	selected_metrics (list): List of metric names (e.g. ["iou_loss", "giou_loss", "ciou_loss"]).
	output_file (str): Name of the output file to save the dataset.

	Returns:
		None
"""
	
	dataframe = pd.read_csv(csv_path) ## compiled_data_valid_only.csv
	## loading set_types
	
	with open(set_types_pkl, "rb") as f:
		set_types = pickle.load(f)
	
	## loading selected_metrics
	# selected_metrics = ["iou_loss", "giou_loss", "ciou_loss"]
	
	data_dict = {}
	for i in range(len(dataframe)):
		genome = dataframe["genome"][i]
		label = torch.tensor(dataframe.loc[i, selected_metrics].values)
		
		model_info_vector, datum, _ = create_data_object(genome, set_types) # create data object (already has combined encoding in function)
		data_dict[i] = (model_info_vector, datum, label) # store dictionary
		
		if i % 100 == 0:
			print(f"Processed {i} samples...")
	
	## save the data
	torch.save(data_dict, output_file)
	print(f"Saved dataset with {len(dataframe)} samples to {output_file}")
```

- run `data_handling.py` using:
``` python
if __name__ == "__main__":
	csv_path = "./data/compiled_data_valid_only.csv"
	set_types_pkl = "./set_prims.pkl"
	selected_metrics = ["iou_loss", "giou_loss", "ciou_loss"]
	generate_data_withencoding_pt(csv_path, set_types_pkl, selected_metrics, output_file="data_with_encoding.pt")
```
- This should generate the file correctly
- `oom-kill: Memory cgroup out of memory`: ran into an issue where it was killed because my process hit the memory limit and the kernel's OOM killer terminated it. 

New Functions
``` python
def get_rss_mb():
    """
    Reads VmRSS from /proc/self/status and returns it in MB.
    """
    with open(f"/proc/{os.getpid()}/status") as f:
        for line in f:
            if line.startswith("VmRSS:"):
                # Format is: "VmRSS:   123456 kB"
                return int(line.split()[1]) / 1024
    return 0.0
```
- checks how much resident memory (RSS) your python process is using in MB since my process kept getting KILLED

``` python
def generate_data_withencoding_pt(
    csv_path,
    set_types_pkl,
    selected_metrics,
    output_file="data_with_encoding.pt",
    chunk_size=500,
    debug_limit=None
):
    """
    Like generate_data_withencoding_pt, but logs memory before/after each step.
    If debug_limit is set, stops after that many samples.
    """
    df = pd.read_csv(csv_path)
    with open(set_types_pkl, "rb") as f:
        set_types = pickle.load(f)

    # sanity check
    for m in selected_metrics:
        if m not in df.columns:
            raise ValueError(f"Metric '{m}' not found in dataframe")

    buffer = {}
    total = len(df)
    print(f"[START] RSS = {get_rss_mb():.1f} MB")

    for i in range(total):
        if debug_limit is not None and i >= debug_limit:
            print(f"[DEBUG LIMIT] Stopping at i={i}")
            break

        print(f"[{i:04d}] before create_data_object: RSS = {get_rss_mb():.1f} MB")

        genome = df["genome"][i]
        # parse metrics
        vals = []
        for m in selected_metrics:
            try:
                vals.append(float(df.loc[i, m]))
            except:
                vals.append(0.0)
        label = torch.tensor(vals, dtype=torch.float)

        try:
            model_info_vector, datum, _ = create_data_object(genome, set_types)
        except Exception as e:
            print(f"[{i:04d}] ERROR in create_data_object: {e}")
            continue

        print(f"[{i:04d}] after create_data_object: RSS = {get_rss_mb():.1f} MB")

        buffer[i] = (model_info_vector, datum, label)

        # flush when buffer full or last sample
        if (i + 1) % chunk_size == 0 or (i + 1) == total or (debug_limit is not None and i + 1 == debug_limit):
            start = i + 1 - len(buffer)
            end = i
            chunk_name = output_file.replace(
                ".pt", f"_chunk_{start:06d}_{end:06d}.pt"
            )
            torch.save(buffer, chunk_name)
            print(f"[{i:04d}] flushed samples {start}–{end} to {chunk_name}")
            buffer.clear()
            gc.collect()
            torch.cuda.empty_cache() 
            print(f"[{i:04d}] after gc.collect(): RSS = {get_rss_mb():.1f} MB")

    print("[DONE] All done.")
```
- Earlier I took every sample's `(model_info_vector, datum, label)` in RAM so the python process owned the entire dataset in memory which passed the 4 GB limit
- Then I split the data into files statically (didn't know when or where memory spiked in usage) and I flushed memory every 500 samples however I still ran into OOM
- the new function calls `get_rss_mb()` before and after `create_data_object()` call because it's so expensive
- I print out the RSS used in each iteration 
- I will flush after each sample

- Additionally, run the preprocessing on the CPU and not the GPU. After flushing the block `gc.collect()`, I will clear any CUDA memory using `torch.cuda.empty_cache()`

## Viewing Data
- I am going to view the difference between `data.pt` and `data_withencoding.pt` chunks using `view_data.py`
- 
# Training CombinedGCN
## Difference of Simple and CombinedFeature GCN
Simple and CombinedFeature GCN are both two-layers that produce a graph-level output via pooling and a final linear layer but they differ in what information they feed into the layers.
**SimpleGCN**
- **Input features (`data.x`)** are treated as _already_ real-valued node feature vectors of size `input_dim` (in your case 28).
- You don’t do any separate embedding or unpacking—whatever lives in `data.x` goes straight into the first `GCNConv`.
- Typically you’d have encoded each module as a one-hot or numeric vector of its parameters, and that _is_ your node feature.
**CombinedFeatureGCN**
- Splits the node information into two pieces:
	1. A **categorical module-type index** (an integer from `0…num_module_types-1`) stored in `data.x`.
	2. A **real-valued hyperparameter vector** stored in `data.hyperparams` (length `hyperparam_dim`, e.g. 43).
- It first looks up a **learned embedding** of that type index (`nn.Embedding(num_module_types, type_embedding_dim)`), producing a dense `type_embedding_dim`-vector per node.
- Then it **concatenates** that embedding with the node’s hyperparameter vector → a combined feature of size `type_embedding_dim + hyperparam_dim`.
- That richer feature is what goes into the first `GCNConv`.

- **SimpleGCN** is straightforward when all your node features are already numeric (e.g. you’ve one-hot-encoded types plus flattened real params).
- **CombinedFeatureGCN** is more flexible if you:
    - Want a _low-dimensional_ learned embedding for module types rather than a large one-hot, and
    - Have additional per-node hyper-parameters that you’d like to feed in _alongside_ that embedding.
- In short, CombinedFeatureGCN explicitly separates and then learns how to mix _categorical type_ information and _continuous hyperparameter_ information at each node, whereas SimpleGCN treats the entire node feature vector as generic floats from the start.


# Problems 
```
Epoch 25/25 - Total Loss: 1124999907493090280079360.0000, IOU: 374999969164363426693120.0000, GIOU: 374999969164363426693120.0000, CIOU: 374999969164363426693120.0000
```
- My Loss on 3 metrics were all $10^{23}$ or $10^{24}$
- My learning rate might be too large (currently using 0.01)
- The CombinedFeatureGCN uses unnormalized, concatenated embedding + hyperparameters which probably causes high gradients causing the parameters to blow up in size.
- No feature-wise normalization for my `node=[type_embedding, raw_hyperparameter_vector]` which can have different scales including counts and floats
- Some fixes:
	- decrease my learning rate to like 0.001 or 0.0001. Here are my reasoning for this, with higher learning rate maybe I am overshooting the minina since earlier in the EPOCH I was rapidily jumping LOSS rates: `ex. EP1: (9) -> EP2: (6) -> EP3: (9)` 
	- Increasing epoch training runs. Reasoning: give it more time to train? Maybe this will convergence to a better loss value 
	- To fix the hyperparameter vector to have more normalized values, I should add zero-mean and std before feeding it into the model to ensure that values are not hilariously large 
	- Added `nn.MSELoss()`, gradient clipping, and regularization

# Doing Research Regarding Improvement
## [[FR NAS]]
https://arxiv.org/html/2404.15622v1#:~:text=We%20integrate%20two%20distinct%20GINs,layer%20extracts%20the%20embedding
-  However, training and assessing numerous architectures introduces considerable computational overhead. One method to mitigating this is through performance predictors, which offer a means to estimate the potential of an architecture without exhaustive training.
- Given that neural architectures fundamentally resemble Directed Acyclic Graphs (DAGs), Graph Neural Networks (GNNs) become an apparent choice for such predictive tasks.
- the scarcity of training data can impact the precision of GNN-based predictors
- training dataset ranging from 50 to 400 samples
- The Graph Neural Networks (GNNs), including models such as the Graph Convolutional Networks (GCNs) Graph Isomorphism Networks (GINs), and Graph Attention Networks (GATs) 
- Due to GNNs’ inherent ability to handle graph data, they become ideal for capturing both topological structures and associated operations
### Methodology
- Their Framework FR-NAS (forward - reverse NAS): architectures are assessed by performance predictor and represented using **both forward and reverse graph encodings**. They are processed by two GIN encoders into feature vectors which are fed into MLPs. Two training losses, Instance Relationship Graph (IRG), and Mean Square Error (MSE) losses are incorporated targeting feature and predictions. 
- Most studies use *undirectional* (forward) representation of the computations graphs using predictor training. NAS are inherently bidirectional involving both forward and backward propagation phase. 
- the proposed FR-NAS framework, every architecture is depicted as a DAG and its inverse, and fed into distinct GINs
- incorporate a feature loss during the training phase at the embedding layer of the GINs
### Method
#### Architecture Encoding
- Neural Architectures are modeled as DAGs with an adjacency matrix A capturing directed edges and a sequence of one-hot vectors X encoding the operation at each node. The forward graph encoding uses $(A,X)$, while the reverse encoding transposes the adjacency matrix to $(A^T,X)$ while the reverse encoding captures the backward propagation structure.
#### Encoder and Predictor
- Two separate Graph Isomorphism Network Encoders each with three layers of MLP+ReLu and a final Global Mean Pooling process the forward and reverse encoding independently, producing embeddings $h_1$ and $h_2$. To avoid bias from merged features each embedding is passed through its own predictor network. Their output are then averaged to yield a final performance estimate $$\hat{y}=\frac{1}{2}(FC_{fwd}(h_1) + FC_{rev}(h_2))$$
#### Training Loss
Training minimizes a composite loss $$L=\lambda \; L_{IRG} +L_{MSE}$$
where IRG loss encourages similar pairwise relationships with two embedding spaces and the MSE losses penalizes the square error between predicted and true performances for each predictor branch.

The sole new hyperparameter, λ (feature‐loss weight), is set to 0.8 based on sensitivity analysis. All GIN layers use hidden size 32 (first layer sized to one-hot dimension), MLP heads use size 16, batch-norm and 0.1 dropout follow each block, and Adam with cosine annealing optimizes over 300 epochs, batch 16

Across NAS-Bench-101, NAS-Bench-201, and DARTS (with 50–400 training samples and 5 000 test samples), FR-NAS consistently achieves 3%–16% higher Kendall’s τ than NPENAS and NPNAS, with the largest gains in the smallest data regimes
#### Experiment
- https://github.com/auroua/NPENASv1: GIN-Based Predictor
- C. Wei, C. Niu, Y. Tang, Y. Wang, H. Hu, and J. Liang, “NPENAS: Neural predictor guided evolution for neural architecture search,” _IEEE Transactions on Neural Networks and Learning Systems_, pp. 1–15, 2022.
- https://github.com/automl/naslib:

## Bidirectional Message Parsing
https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123740647.pdf#:~:text=The%20original%20GCNs%20,we%20always%20use%20the%20average
- Incorporate **forward and reverse information flow** in the DAG. A directed architecture graph naturally only propagates information one way, but performance is influenced by both upstream (inputs) and downstream (outputs). A simple but effective trick is to perform two message-passing steps per layer – one with the adjacency matrix and one with its transpose – then combine them (e.g. average)​


## Architecture Encoding and Feature Representation
- Instead of fixed one-hots, learn an embedding vector for each operation type. This allows the predictor to learn similarity relationships between ops (e.g. two different sizes of convolution might end up with similar embeddings if they have similar effect). In advanced encodings like **GATES (Graph-based Architecture Encoding Scheme)**, operations are modeled as learnable transformations of the messages passing through them
- Architectural Metadata: Augment the graph with additional features that can improve prediction. Example of useful features include: 
	- **Node Attribute**: filter sizes, number of channels, layer parameters, or activation types if these vary between architectures
	- **Global Feature**: total parameter count, theoretical FLOPs or network depth. (ReNAS) computes a “type matrix, FLOPs matrix, and parameter matrix” from the architecture and combines them as a feature tensor for the predictor​[nature.com](https://www.nature.com/articles/s41598-025-94187-8#:~:text=SemiNAS9%20%20and%20GATES%2040,These).
	- **Path encodings:** Represent each distinct input-to-output path in the architecture (a path is a sequence of ops from network input to output). This can be a powerful explicit feature – the BANANAS predictor introduced a binary vector indicating which potential paths exist in a cell, greatly improving prediction on NAS-Bench-101​[arxiv.org](https://arxiv.org/pdf/2104.01177#:~:text=is%20much%20more%20diverse%20with,we%20see%20that%20these%20methods). You can include path features by either feeding them through a separate network (e.g. a transformer as in AE-NAS​[nature.com](https://www.nature.com/articles/s41598-025-94187-8#:~:text=model%20based%20on%20Transformer16%20,critical%20paths%20in%20the%20architecture)) or by designing the GNN to capture long paths (e.g. using longer-range message passing or adding virtual “super node” that connects to all input/output nodes).
- **Hierarchical Architecture**: If the search space is hierarchical (an architecture consists of multiple cells or modules) decide whether to predict at cell level or whole network level. 
	- **Two Level Encoding**: Us a GNN to encode each cells graphs into a embedding then represent the whole network as a small graph of cells (where nodes are cell embeddings, and edges represent their connectivity in the network) 
		- Ensures that surrogate accounts for both micro-architecture and macro-architecture

## Bidirectional Proposal by Google Brain
https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123740647.pdf#:~:text=The%20original%20GCNs%20,we%20always%20use%20the%20average		  
![[Screenshot 2025-04-23 at 7.20.54 PM.png]]
- One way to alleviate this is to identify a small subset of promising models. If this is done with reasonably high precision (i.e., most models selected are indeed of high quality) then we can train and validate just this limited set of models to reliably select a good one for deployment
- To achieve this, the proposed Neural Predictor uses the following steps to perform an architecture search: 
	- (1) Build a predictor by training N random architectures to obtain N (architecture, validation accuracy) pairs. Use this data to train a regressor. 
	- (2) Quality prediction using the regression model over a large set of random architectures. Select the K most promising architectures for final validation. 
	- (3) Final validation of the top K architectures by training them. Then we select the architecture with the highest validation accuracy to deploy.
**Neural Predictor**
![[Screenshot 2025-04-23 at 7.23.30 PM.png]]
- A neural network architecture with 5 candidate operations per node. Each node is represented by a one-hot code of its operation. The one-hot codes are inputs of a bidirectional GCN, which takes into account both the original adjacency matrix (middle) and its transpose (right).
Step 1: Build the predictor using N samples. We train N models to obtain a small dataset of (architecture, validation accuracy) pairs. The dataset is then used to train a regression model that maps an architecture to a predicted validation accuracy.

Step 2: Quality prediction. Because architecture evaluation using the learned predictor is efficient and trivially parallelizable, we use it to rapidly predict the accuracies of a large number of random architectures. We then select the top K predicted architectures for final validation. 

Step 3: Final validation on K samples. We train and validate the top K models in the traditional way. This allows us to select the best model based on the actual validation accuracy. Even if our predictor is somewhat noisy, this step allows us to use a more reliable measurement to select our final architecture for deployment. Training N+K models is by far the most computationally expensive part of the Neural Predictor. If we assume a constant compute budget, N and K are key hyper-parameters which need to be set; we will discuss this next. Note that the two most expensive steps (Step 1 and Step 3) are both fully parallelizable.
