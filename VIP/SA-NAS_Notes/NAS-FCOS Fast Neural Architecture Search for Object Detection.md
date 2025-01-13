## Introduction
Object detection is one of the fundamental tasks in computer vision and methods for this task are using deep convolutional neural networks (like Faster R-CNN, RetinaNet). The reason why it's so computationally intensive is because it numerous hyper-parameters and complex structure. 

[[Neural Architecture Search (NAS)]] approach is effective as it automatically discovers top performing results in large scale search space for these architectures. The workflow of NAS can be divided into three processes:
1. Sampling architecture from search space following some search strategies. 
2. Evaluating the performance of sampled architecture
3. Updating the parameters based on performance

What stops NAS from being used more is its search efficiency. The evaluation process is the most time consuming part as it involves full training procedure of neural network. To reduce evaluation time, proxy task is used to lower cost substitution. In the proxy task, the input, network parameters and training iterations are often scaled down to speedup the evaluation. However, there is often a performance gap for samples between the proxy tasks and target tasks, which makes the evaluation process biased. 

## FCOS
This research paper uses their overall detection architecture based on FCOS. FCOS is a simple anchor-free one-stage object detection framework where feature pyramid network and prediction head are search using their NAS method.

**Anchor-Based vs Anchor-Free** 
In based models, prediction head use predefined bounding boxes at each location on the feature map to predict objects. These anchors are then adjusted based on detected feature to finalize the bounding box. Faster R-CNN and YOLO uses anchors.  

In free models, the prediction head doesn't rely on anchors. Instead, it directly predicts the bounding box for each detected object. This can simplify the model architecture and reduce the need for tuning anchor parameters.

**Parts of the Prediction Head**
- **Bounding Box Regressor**: Predicts the coordinates of bounding box around detected objects
- **Object Classifier**: Classifies the detected objects by assigned them a class label
- **Confidence Score**: Assigns a confidence level to each detected object

Prediction head is crucial because it translates the network's feature map into actual detection results. NAS can optimize the prediction head's structure to balance accuracy and efficiency.

## Object Detection
### One Stage vs Two Stage
**Two Stage**
- **Process**: First generate class independent region proposals using a region proposal network (RPN). Then classify and refine it using extra detection heads
- **Drawback**: Computationally expensive + many hyper-parameters
**One Stage**
 - Directly predict object categories, FPN, and head structure

## Method
- Search for anchor-free fully convolutional detection models with fast decoder adaption
- **Training**: Tuples $(x,Y)$ where consists of input images tensors $x$ of size $(3\times H\times W)$ (3 RBG channels)
- FCOS **output** targets $Y$ in a pyramid representation which is a list of tensors $y_l$ each size $((K+4+1) \times H_l \times W_l)$ where $H_l \times W_l$ is feature map size of level $p$ of the pyramid. K is the number of classes, 4 is bounding box regression targets, and 1 is center-ness score. 
- The network $g:x\rightarrow \hat{Y}$ 
	- **Backbone** $b$: Processes the input tensor to generate features $C=\{c_3,c_4,c_5\}$ which are multi level representation with resolutions decreasing by a factor of 2. $(H_i\times W_i)=(\frac{H}{2^i}\times \frac{W}{2^i})$ 
	- **Feature Pyramid Network (FPN)** $f$: Transforms $C$ into a multi-level feature pyramid $P=\{ p_3,p_4,p_5,p_6,p_7\}$ Each $p$ in $P$ represents a different scale. 
	- **Prediction Head** $h$: Applies predictions at each level to produce outputs $y$. 
- The design considers objects at different scales. They improve efficiency reusing the parameters in $b$