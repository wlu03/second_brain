# 2002 Toward Automated Exploration of Interactive Systems
The authors set out to create **an autonomous system** that can navigate and evaluate graphical user interfaces (GUIs) much like a human tester:

> “We have designed a system to carry out an autonomous, exploratory navigation through the graphical user interface of interactive, off-the-shelf software applications.”

This proof-of-concept both **maps interface connectivity** and **records navigational paths**, aiming to make routine what is usually a manual, user-driven exploration.

## Underlying Architecture
At the core is a **cognitive model** based on ACT-R, augmented with a perception/action layer:

> “The reasoning component of the system is based on the ACT-R architecture, while the perceptual and motor components of the system are built on top of the SegMan perception/action substrate.”

This division mirrors human cognition—**declarative memory** for storing learned facts and **production rules** for procedural behavior.

### Screens-as-Rooms Metaphor
A key insight is treating each window or menu as a “room,” with widgets acting as “doorways” between rooms:

> “In our cognitive model, the graphical user interface is treated as a set of distinct screens that are causally connected but graphically separate.”

By cataloguing these rooms and their connectors, the agent can reconstruct **depth-first** navigation paths through the interface.
### Perception and Widget Identification
SegMan segments the live display into textual and graphical objects, but the model focuses on text labels:

> “At this time all other features except text are disregarded… we are able to utilize a significant portion of any standard Windows application when only considering textual information.”

Transitional widgets (those that open dialogs or menus) are identified via conventions—ellipses on labels, menu-bar positioning, or a small built-in vocabulary (e.g., “Properties,” “Cancel,” “OK”)

### Production Rules and Exploration Strategy

The exploration follows a **simple iterative pattern** encoded as ACT-R productions:

1. **Scan** the current screen for unvisited transitional widgets.
2. **Select** one such widget.
3. **Move** the mouse and **click** it.
4. **Record** the new screen and **repeat**.

> “This pattern causes the agent to explore the application interface in a depth-first-like fashion.”

A total of **42 productions** drive attention shifts, widget identification, mouse movements, and screen registration.
### Quantitative Interface Metrics

From the crawl, the system derives simple but informative metrics:

> “Maximum depth: 4  
> Mean depth: 2.45  
> Maximum transitions: 6  
> Mean transitions: 2.3”

Such metrics can be compared across applications to gauge **relative navigability** and potentially correlate with **usability**
### Limitations
The authors are candid about the system’s fragility:

> “The exploration model relies heavily on its understanding of conventions and vocabulary… if the conventions, such as the use of ellipses, are violated, the model will fail to recognize transitional widgets.”

Moreover, the **tabula-rasa** approach means the agent cannot handle context-sensitive operations (e.g., Cut/Copy) without preloaded domain knowledge, and it struggles when screens change only slightly.
### Future Directions

To overcome these issues, the paper suggests:

- **Grammar-based models** of interface transformations, reducing the need for hard-coded conventions.
- **Customizable background knowledge**, allowing agents of varying expertise to explore in more targeted ways.
- **Broader validation**, applying the system to diverse, real-world applications beyond the simple proof-of-concept.

**As a student**, I find this work both inspiring and cautionary: it demonstrates the **promise** of cognitive architectures for GUI evaluation while also underlining the **practical challenges** of scaling such systems to the heterogeneity of modern software.