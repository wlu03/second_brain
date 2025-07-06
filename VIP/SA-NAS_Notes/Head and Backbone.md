In a genome string, the **backbone** is the feature extractor network (e.g. Inception_V3, DenseNet, convolutional layers) that process raw inputs into feature maps. The **head** is the task specific module that takes those features and produces final outputs 

- **Backbones** are deep, often pre-trained convolutional networks that transform raw images into rich, hierarchical feature maps.
- **Heads** are comparatively shallow, task-specific layers (or sets of layers) that take those feature maps and produce final outputs—classification scores, bounding-box coordinates, segmentation masks, etc. 

## Backbone Architectures

### Role & Function
Backbones serve as general-purpose feature extractors, encoding low-level edges up through high-level semantics in a feed-forward hierarchy. They are typically pre-trained on large datasets (e.g., ImageNet) to accelerate convergence and improve representation quality. 
### Common Designs

- **ResNet** uses residual shortcuts to enable very deep networks without vanishing gradients
    
- **Inception** modules run parallel convolutions at multiple kernel sizes, then concatenate, for multi-scale processing.
- **DenseNet** densely connects each layer to every other, maximizing gradient flow and feature reuse. 
Each backbone balances depth, width, and computational cost to suit different deployment constraints.

## Head Architectures

### Role & Function
Heads attach to backbone (or intermediate “neck”) outputs to perform the model’s ultimate task. In detection, heads simultaneously predict class probabilities and bounding-box offsets; in segmentation, they predict pixel-wise masks; in classification, a simple fully-connected head outputs class scores.

### Variations & Examples

- **Single-Stage vs. Two-Stage**:
    - SSD-style heads compute class and box outputs in one pass over feature maps. 
    - Two-stage detectors (e.g. Faster R-CNN) use an RPN head to propose regions, then a second ROI head to classify and refine boxes.
        
- **Separate vs. Shared Branches**:
    
    - RetinaNet employs two decoupled heads—one for classification, one for regression—on each feature level. 

    - FCOS uses a single convolutional head that outputs both in one tensor.
- **Head Structure**:
    
    - **Fully-Connected Heads** (fc-head) often excel at classification, thanks to spatial sensitivity.
    - **Convolutional Heads** (conv-head) better capture localization cues, thanks to spatial invariance. 
        

## Key Differences

|Aspect|Backbone|Head|
|---|---|---|
|**Purpose**|Feature extraction|Task-specific prediction|
|**Pretraining**|Almost always pretrained (ImageNet et al.)|Random start; trained jointly with backbone|
|**Depth & Parameters**|Very deep (50–200+ layers), millions of params|Shallow (few layers), relatively lightweight|
|**Connectivity**|Residual, Inception, dense connections|Typically simple conv or FC stacks|
|**Data Flow**|Input → hierarchical feature maps|Feature maps → outputs (scores, boxes, masks)|
|**Parameter Sharing**|Across all spatial positions|May share heads across feature pyramid levels|
