https://arxiv.org/html/2404.15622v1#:~:text=We%20integrate%20two%20distinct%20GINs,layer%20extracts%20the%20embedding

## How to implement
For an example genome, split parentheses and commas to recover the operation names and nesting structure
 - Build an AST to make edges and nodes
 - Build adjacency and feature matrix
 - Define dual GIN encoders + MLP predictors
 - Training with IRG + MSE Loss

## Helper Code


```
import torch
from torch_geometric.data import Data

# 2.1. Suppose `nodes` is your list of unique operation names,
#      and `edges` is a list of (parent_name, child_name) tuples.
nodes = sorted(nodes)                # e.g. ['FCOS_Head','Inception_V3','LazyConvTranspose2d',…]
node2idx = {name: i for i,name in enumerate(nodes)}

# 2.2. Build edge_index for the _forward_ graph
edge_list = [(node2idx[p], node2idx[c]) for p,c in edges]
edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()  # [2, E]

# 2.3. One‐hot node features
X = torch.eye(len(nodes), dtype=torch.float)  # [N, N], each row i is one-hot for op nodes[i]

# 2.4. Create PyG Data for forward and reverse
data_fwd = Data(x=X, edge_index=edge_index)
# reverse: swap source/target
edge_index_rev = edge_index[[1,0], :]
data_rev = Data(x=X, edge_index=edge_index_rev)


import torch.nn as nn
from torch_geometric.nn import GINConv, global_mean_pool

# 3.1. A small MLP for GINConv
def make_mlp(in_dim, hidden_dim):
    return nn.Sequential(
        nn.Linear(in_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, hidden_dim),
        nn.ReLU()
    )

class DualGINPredictor(nn.Module):
    def __init__(self, num_features, hidden=32, pred_hidden=16):
        super().__init__()
        # forward‐graph GIN
        self.gin_f = nn.ModuleList([
            GINConv(make_mlp(num_features if i==0 else hidden, hidden))
            for i in range(3)
        ])
        # reverse‐graph GIN
        self.gin_r = nn.ModuleList([
            GINConv(make_mlp(num_features if i==0 else hidden, hidden))
            for i in range(3)
        ])
        # two separate MLP predictors
        self.pred_f = nn.Sequential(
            nn.Linear(hidden, pred_hidden),
            nn.ReLU(),
            nn.Linear(pred_hidden, 1)
        )
        self.pred_r = nn.Sequential(
            nn.Linear(hidden, pred_hidden),
            nn.ReLU(),
            nn.Linear(pred_hidden, 1)
        )

    def forward(self, data_fwd, data_rev):
        x_f, edge_f = data_fwd.x, data_fwd.edge_index
        x_r, edge_r = data_rev.x, data_rev.edge_index

        # encode forward
        for conv in self.gin_f:
            x_f = conv(x_f, edge_f)
        h_f = global_mean_pool(x_f, batch=torch.zeros(x_f.size(0), dtype=torch.long))

        # encode reverse
        for conv in self.gin_r:
            x_r = conv(x_r, edge_r)
        h_r = global_mean_pool(x_r, batch=torch.zeros(x_r.size(0), dtype=torch.long))

        # predict and average
        y_f = self.pred_f(h_f)
        y_r = self.pred_r(h_r)
        return 0.5*(y_f + y_r)


# IRG loss: encourage pairwise distances in h_f and h_r to match
def irg_loss(Hf, Hr):
    # Hf, Hr shape [B, D]; compute pairwise distance matrices Df, Dr
    Df = torch.cdist(Hf, Hf, p=2)
    Dr = torch.cdist(Hr, Hr, p=2)
    return nn.functional.mse_loss(Df, Dr)

model = DualGINPredictor(num_features=len(nodes))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(epochs):
    Hf, Hr = [], []
    preds, trues = [], []
    for data, y in train_loader:
        # data: yields batched Data for both forward/rev
        yf = model(data['fwd'], data['rev'])
        preds.append(yf)
        trues.append(y)
        # store embeddings by modifying forward() to also return h_f, h_r if desired
        Hf.append(model.h_f); Hr.append(model.h_r)

    preds = torch.cat(preds); trues = torch.cat(trues)
    Hf = torch.cat(Hf); Hr = torch.cat(Hr)
    loss = λ*irg_loss(Hf, Hr) + nn.functional.mse_loss(preds, trues)
    opt.zero_grad(); loss.backward(); opt.step()

```