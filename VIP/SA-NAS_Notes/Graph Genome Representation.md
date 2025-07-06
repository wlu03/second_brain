## Genome String Input and Decoding
The system starts with a genome string that is a DEAP PrimitiveTree representation. This string encodes the different architectural choices (backbone, head, optimizer settings) for a network. `codec` class is responsible for converting the **string** to a **PyTorch model**. `decode_genome(genome, num_loss_components)` is the function to decode the genome. It parses the genometring and builds a **module list**. Once all layers are added, it creates a full model by adding a detection head and returns a dictionary containing them model and additional information

## Graph Conversion
After decoding the PrimitiveTree into a PyTorch model, the model dictionary's backbone (feature portion) is extracted from the model (`model._modules["backbone"]`). The backbone is transformed into a graph representation using the function `create_graph_repr(backbone, set_types)` in `data_handling.py`. It calls `create_model_dict(backbone)` to recursively collect all submodules of the backbone into a dictionary. For each node in the graph, it assigns a feature vector which is a one-hot encoding of the module type using a set of predefined types (`set_prims.pkl`). The function builds an edge list by examining the node connections. Finally, it assembles the node features and edge list into a `torch_geometric.data.Data` object (the standard graph data structure used by PyG) and returns it along with a mapping of node indices to descriptive names.

`data_handling.py`
``` python
def encode_module_repr_2(module, set_types):
    vocab_to_index = {word: idx for idx, word in enumerate(set_types)}
    num_types = len(set_types) + 1
    mod_type = type(module)
    if mod_type in vocab_to_index:
        idx = vocab_to_index[mod_type] + 1
    else:
        idx = 0
    encoding = [0] * num_types
    encoding[idx] = 1
    return encoding

```
- builds a dictionary mapping each module type from the `set_types`
- given a module it produces a one-hot vector (a vector with all zeros expect for 1 at the index to the correspond type)

```python
for node in nodes:
    node.value = encode_module_repr_2(model_dict.get(node.name), set_types)
    if node.name in model_dict:
        node.descriptive_name = model_dict[node.name]._get_name()
    else:
        node.descriptive_name = node.name
```


**Change**: One Hot Encoding to Learning Embeddings
- return the index instead of one hot vector
``` python
def encode_module_index(module, set_types):
    """
    Instead of returning a one-hot vector, return the index of the module's type.
    """
    vocab_to_index = {word: idx for idx, word in enumerate(set_types)}
    mod_type = type(module)
    # Return the index if found; otherwise, use index 0 as default.
    return vocab_to_index.get(mod_type, 0)
```

```python 
for node in nodes:
    # Store the index instead of a one-hot vector.
    node.module_index = encode_module_index(model_dict.get(node.name), set_types)
    if node.name in model_dict:
        node.descriptive_name = model_dict[node.name]._get_name()
    else:
        node.descriptive_name = node.name
```
When constructing the node features for the graph, create a tensor of these indicies 
```python
# Build a tensor of module indices for all nodes.
node_indices = torch.tensor([node.module_index for node in nodes], dtype=torch.long)
```
Set these indicies as node features
```python 
datum = Data(x=node_indices, edge_index=edge_index)
```
In GNN module, add embedding layers to convert indices into dense vectors.
``` python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool

class SimpleGCN(nn.Module):
    def __init__(self, num_module_types, embedding_dim, hidden_dim, output_dim):
        super(SimpleGCN, self).__init__()
        # Embedding layer: converts module indices to dense vectors.
        self.embedding = nn.Embedding(num_embeddings=num_module_types, embedding_dim=embedding_dim)
        # GCN layers now expect inputs of size embedding_dim.
        self.conv1 = GCNConv(embedding_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.linear = nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        # data.x now contains indices. 
        # If data.x has shape [N] or [N, 1], we convert it to indices.
        x = data.x.squeeze()  # Ensure shape is [N]
        # Look up the dense embedding for each node.
        x = self.embedding(x)
        x = self.conv1(x, data.edge_index)
        x = F.relu(x)
        x = self.conv2(x, data.edge_index)
        x = global_mean_pool(x, data.batch)  # Pool to get a graph-level representation.
        x = self.linear(x)
        return x

# Example of how to instantiate the model:
# Suppose your set_types list has 10 unique module types.
num_module_types = 10  
embedding_dim = 8  # You can choose a suitable embedding dimension.
hidden_dim = 64
output_dim = 3  # For example, predicting 3 performance metrics.

model = SimpleGCN(num_module_types, embedding_dim, hidden_dim, output_dim)

```
___
# Example
The current setup, each node feature is a vector like:
``` csharp
[0, 0, 0, 0, 1, 0, 0]
```
This tells the module type to the fifth category. Instead the new approach uses learned embedding, the node stores the single integer index. During GNN's forward pass, the index is fed through an embedding layer. The embedding converts 4 in to a dense vector like:
``` csharp
[0.12, -0.05, 0.33, 0.78, 0.01, -0.44, 0.57, 0.09]
```

A **dense vector** is a compact fix-length representation that encodes information in continuous values. In the context of neural network and GNN dense vectors are used to represent categorical data. Instead of using a high-dimensional and sparse one-hot vector, a dense vector (often produced by an embedding layer) captures the essence of a categorical variable in a much lower-dimensional space. This makes computations more efficient and can lead to better learning. When you feed an index (representing a module type) into an embedding layer, the layer learns a dense representation (a set of continuous numbers) for that type during training. This means that the dense vector can capture semantic similarities – modules that behave similarly might end up with similar dense vectors.

Additionally, I can append hyper parameters to the dense vector representing the module type. Since different modules might have a different number of hyperparameters, you can use one of the following strategies:
- **Universal Template:** Define a template that covers all potential hyperparameters (e.g., `[out_channels, kernel_size, stride, padding, dilation, extra]`) and fill in missing values with defaults (like zeros).
- **Module-Specific Encoders:** Use a small neural network (or a simple padding/truncation scheme) to convert the variable-length list of hyperparameters into a fixed-size vector.

**Concatenation with the Dense Embedding:**  
Once you have both:
- A dense vector from the embedding layer (e.g., a 8-dimensional vector for the module type), and
- A fixed-size hyperparameter vector (say, 8 dimensions after encoding),

You can concatenate them to form a combined feature vector (e.g., 16 dimensions). This combined vector now carries both the learned representation of the module type and its explicit hyperparameter settings.

You can then feed this combined vector into further layers (like additional fully-connected layers, GNN layers, etc.) to process the information jointly.
# Encoding Hyperparameter Strategy
Each node in your genome graph gets a combined representation that: 
- A **dense vector** from an embedding layer represents the module type
- A fixed-size vector encodes the module's hyperparameters

Concatenating these two, you get features for each node that the GNN can process allowing it to consider both the categorical identity of the module and specific details as well. 

To handle the variability in hyperparameters so that every module maps to a fixed size vector with consistent index positions. I am going to use the universal hyperparameter template. 

1. `module_hyperparameters.py`: This will find the hyperparameters of each module to find the universal list. 
	 Universal Hyperparameter Template:
	`['_random_samples', 'affine', 'align_corners', 'approximate', 'args', 'bias', 'ceil_mode', 'count_include_pad', 'device', 'dilation', 'dims', 'divisor_override', 'dtype', 'elementwise_affine', 'eps', 'groups', 'in_channels', 'in_features', 'inplace', 'kernel_size', 'kwargs', 'mode', 'momentum', 'negative_slope', 'norm_type', 'normalized_shape', 'num_features', 'out_channels', 'out_features', 'output_padding', 'output_ratio', 'output_size', 'p', 'padding', 'padding_mode', 'recompute_scale_factor', 'return_indices', 'scale_factor', 'size', 'stride', 'threshold', 'track_running_stats', 'value']`
	This is the size of the hyperparameter template: 43
	Some parameters like `kernel size`, `stride`, `padding` could appear more frequently than `args`. I can potentially filter the non-important parameters out.

2. `data_handling.py`: I will add a function to encode and extract a module's hyperparameter to build 43-dimension vector
``` python
def encode_module_hyperparams(module, universal_template):
    """
    Encodes the hyperparameters of a module into a fixed-length vector.
    It uses module.extra_repr() to get the parameter string, then parses it,
    and finally maps the available parameters to positions in the universal template.
    Any missing parameter gets a default value (e.g., 0).
    """
    # Initialize the vector with zeros (length is the size of the universal template)
    vector = [0.0] * len(universal_template)
    try:
        # Use the provided parse_representation function to get kwargs from extra_repr
        _, kwargs = parse_representation(module.extra_repr())
    except Exception as e:
        # If parsing fails, just return a zero vector.
        return torch.tensor(vector, dtype=torch.float)

    # For each expected hyperparameter in the universal template,
    # if it exists in kwargs, convert it to float and store it.
    for i, key in enumerate(universal_template):
        if key in kwargs:
            try:
                vector[i] = float(kwargs[key])
            except Exception:
                vector[i] = 0.0
        else:
            vector[i] = 0.0  # Default value for missing hyperparameters

    return torch.tensor(vector, dtype=torch.float)

```
3. `data_handling.py`: Add to the `create_graph_repr` function where instead of getting a one-hot vector (of the module) update the loop so that each node:
	- a module type index using `encode_module_index` and
	- a hyperparameter vector (using the helper function above)

before:
``` python
for node in nodes:
    node.value = encode_module_repr_2(model_dict.get(node.name), set_types)
    if node.name in model_dict:
        node.descriptive_name = model_dict[node.name]._get_name()
    else:
        node.descriptive_name = node.name

```

after:
``` python
for node in nodes:
    module_instance = model_dict.get(node.name)
    # Store the index for the module type.
    node.module_index = encode_module_index(module_instance, set_types)
    # Store the fixed-length hyperparameter vector.
    node.hyperparams = encode_module_hyperparams(module_instance, universal_template)
    
    if node.name in model_dict:
        node.descriptive_name = model_dict[node.name]._get_name()
    else:
        node.descriptive_name = node.name

```

4. When constructing the node features for the graph, you have two sets of data for each node. 
``` python
def create_graph_repr_custom(backbone, set_types, encoding_strategy="normal"):
    """
    Convert the backbone into a PyG Data object using one of two encoding strategies:
    
    - If encoding_strategy == "normal", each node is represented only by its module type
      (stored as an integer index to be fed to an embedding layer later).
    
    - If encoding_strategy == "combined", each node is represented by its module type index
      and a fixed-length hyperparameter vector, based on a universal hyperparameter template.
    
    Returns:
        datum: A torch_geometric.data.Data object.
        node_index_to_name: A mapping from node indices to descriptive names.
    """
    import torch
    from torch_geometric.data import Data

    device = "cuda" if torch.cuda.is_available() else "cpu"
    backbone = backbone.to(device)
    model_dict = create_model_dict(backbone)
    model_graph = symbolic_trace_with_custom_tracer(backbone)
    nodes = model_graph.graph.nodes

    if encoding_strategy == "normal":
        # Strategy: Only use the module type index.
        for node in nodes:
            module_instance = model_dict.get(node.name)
            # Get the type index (using your existing function)
            node.module_index = encode_module_index(module_instance, set_types)
            if node.name in model_dict:
                node.descriptive_name = model_dict[node.name]._get_name()
            else:
                node.descriptive_name = node.name
        # Build tensor of module type indices.
        node_features = torch.tensor([node.module_index for node in nodes], dtype=torch.long)
    
    elif encoding_strategy == "combined":
        # Define your universal hyperparameter template (adjust as needed).
        universal_template = [
            '_random_samples', 'affine', 'align_corners', 'approximate', 'args', 'bias', 'ceil_mode', 
            'count_include_pad', 'device', 'dilation', 'dims', 'divisor_override', 'dtype', 
            'elementwise_affine', 'eps', 'groups', 'in_channels', 'in_features', 'inplace', 'kernel_size', 
            'kwargs', 'mode', 'momentum', 'negative_slope', 'norm_type', 'normalized_shape', 'num_features', 
            'out_channels', 'out_features', 'output_padding', 'output_ratio', 'output_size', 'p', 'padding', 
            'padding_mode', 'recompute_scale_factor', 'return_indices', 'scale_factor', 'size', 'stride', 
            'threshold', 'track_running_stats', 'value'
        ]
        for node in nodes:
            module_instance = model_dict.get(node.name)
            node.module_index = encode_module_index(module_instance, set_types)
            node.hyperparams = encode_module_hyperparams(module_instance, universal_template)
            if node.name in model_dict:
                node.descriptive_name = model_dict[node.name]._get_name()
            else:
                node.descriptive_name = node.name
        # Build tensor for module type indices.
        type_indices = torch.tensor([node.module_index for node in nodes], dtype=torch.long)
        # Build tensor for hyperparameter vectors.
        hyperparams_tensor = torch.stack([node.hyperparams for node in nodes])
        # We'll use the type indices as the primary node feature for the embedding.
        node_features = type_indices
    else:
        raise ValueError("Invalid encoding_strategy. Choose either 'type' or 'combined'.")

    # Build edge list from the traced graph.
    node_name_to_index = {node.name: idx for idx, node in enumerate(nodes)}
    edge_list = []
    for node in nodes:
        src_id = node_name_to_index[node.name]
        for target in node.users.keys():
            tgt_id = node_name_to_index[target.name]
            edge_list.append([src_id, tgt_id])
    edge_index = torch.tensor(edge_list).T.contiguous()

    datum = Data(x=node_features, edge_index=edge_index)
    
    # For the "combined" strategy, attach hyperparameters as a custom attribute.
    if encoding_strategy == "combined":
        datum.hyperparams = hyperparams_tensor

    # Create a mapping from node index to descriptive name.
    node_index_to_name = {idx: node.descriptive_name for idx, node in enumerate(nodes)}
    return datum, node_index_to_name
```

5. The combination of the **dense vector** and **hyperparameter vector** happens in the forward pass in my GNN. In `data_handling.py` I use the combine strategy to store the type index as the primary node feature and attach the hyperparameter tensor as a custom attribute (`data.hyperparams`). In my GNN module, I will:
	1. Use embedding layer to convert type indicies `data.x` to a dense vector (for embedded learning)
	2. Concatenate the resulting dense vector with hyperparameter vectors in `data.hyperparams`
	3. Feed combined vector into GNN layers
```python
class CombinedFeatureGCN(nn.Module):
    def __init__(self, num_module_types, type_embedding_dim, hyperparam_dim, hidden_dim, output_dim):
        super(CombinedFeatureGCN, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=num_module_types, embedding_dim=type_embedding_dim)
        # Input to the first GCN layer is the concatenation of the type embedding and the hyperparameter vector.
        self.conv1 = GCNConv(type_embedding_dim + hyperparam_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.linear = nn.Linear(hidden_dim, output_dim)

    def forward(self, data):
        # data.x contains the module type indices.
        type_embeds = self.embedding(data.x.squeeze())  # Dense vector representation.
        # data.hyperparams contains the fixed-length hyperparameter vector.
        x = torch.cat([type_embeds, data.hyperparams], dim=1)
        x = self.conv1(x, data.edge_index)
        x = F.relu(x)
        x = self.conv2(x, data.edge_index)
        x = global_mean_pool(x, data.batch)
        x = self.linear(x)
        return x

```
- This GNN takes a graph data object (PyTorch Geometric)
	- **Node features** (`data.x`): contains the tensor of module type. Each node index corresponds to a module type from the set of possible module types
	- **Node Hyperparameters** (`data.hyperparams`): tensor where each row is a fixed-length vector encoding the hyperparameters
	- **Edge List** (`data.edge_index`): describes how each module is connected of the structure of the backbone network
	- **Batch Information** (`data.batch`): used when I have a mini-batch of graph indicating which node belongs to which graph
- **Embedding Module Type**
	- This contains an integer index. GNN's forward pass is to convert it to a dense continuous vector using embedding layer: `self.embedding = nn.Embedding(num_embeddings=num_module_types, embedding_dim=type_embedding_dim)`
	- This layer maps each module type to a learned dense vector. 
	- ex: index 4 could be mapped to vector like `[0.12, -0.05, 0.33, 0.78, 0.01, -0.44, 0.57, 0.09]` 
- **Handling Hyperparameters**
	- For each node, the dense vector and hyperparameters are connected along the feature dimension. This produces a feature vector of both the module type and parameters
	- `type_embeds = self.embedding(data.x.squeeze()) # Shape: [N, type_embedding_dim] x = torch.cat([type_embeds, data.hyperparams], dim=1) # Shape: [N, type_embedding_dim + hyperparam_dim]`
- **Graph Convolutional Layers (GCNConv)**: 
	- These combined layer is passed through the GCN layers
	- First layer: `self.conv1 = GCNConv(type_embedding_dim + hyperparam_dim, hidden_dim)`
	- Pooling: `x = global_mean_pool(x, data.batch)`
		- this aggregates the node-level features into a single vector per graph by averaging them. The resulting graph-level vector summarizes the network
	- Linear Layer: `x = self.linear(x)`
		- produces a final prediction

1. Because the new GCN requires the data to have an attribute `data.hyperparam` I will need to generate a new set of data to contain this. In `data_handling.py`, I changed `create_data_object` to have `datum, index_to_name = create_graph_repr_custom(backbone, set_types, encoding_strategy="combined")` instead of `datum, index_to_name = create_graph_repr(backbone, set_types)`.  This makes it such that I will have the combined strategy in place. 
   
   Thus, I need to figure out how to run the pipeline to recreate my data from genome to a PyG object to contain the `hyperparams`.