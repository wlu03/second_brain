Link: https://www.anthropic.com/engineering/building-effective-agents

Agents are fully autonomous systems that operate independently over extended periods using various tools to accomplish complex tasks. **Workflows** are system where LLM and tools are orchestrated through predefined code paths. **Agents** are systems where LLMs dynamically directs their own processes and tool usage, maintaining control over how they accomplish tasks. 

https://langchain-ai.github.io/langgraph/: used to build better workflow for agents

By defining and parsing tools, chaining calls it easy to create extra layers of abstraction that can obscure the underlying prompt and response.

# Example of An Effective Agent
- Prompt Chaining
- Routing
- Multi-LLM Parallelization  
- Orchestrator Subagents
- Evaluator-Optimizer

*Utils.py*
``` python
from anthropic import Anthropic
import os
import re

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def llm_call(prompt: str, system_prompt: str = "", model="claude-3-5-sonnet-20241022") -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): The system prompt to send to the model. Defaults to "".
        model (str, optional): The model to use for the call. Defaults to "claude-3-5-sonnet-20241022".

    Returns:
        str: The response from the language model.
    """
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    messages = [{"role": "user", "content": prompt}]
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=messages,
        temperature=0.1,
    )
    return response.content[0].text

def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text. Used for parsing structured responses 

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""
```

*basic Multi-LLM Workflows*
- **[[Prompt Chaining]]**: Decompose a task into sequential subtasks, where each step builds on previous results
- **[[Parallelization]]**: Distributes independent subtasks across multiple LLM for concurrent processing
- **[[Routing]]**: Dynamically selects specialized LLM paths based on input characteristics
```python

from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Callable
from util import llm_call, extract_xml

def chain(input: str, prompts: List[str]) -> str:
    """Chain multiple LLM calls sequentially, passing results between steps."""
    result = input
    for i, prompt in enumerate(prompts, 1):
        print(f"\nStep {i}:")
        result = llm_call(f"{prompt}\nInput: {result}")
        print(result)
    return result

def parallel(prompt: str, inputs: List[str], n_workers: int = 3) -> List[str]:
    """Process multiple inputs concurrently with the same prompt."""
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(llm_call, f"{prompt}\nInput: {x}") for x in inputs]
        return [f.result() for f in futures]

def route(input: str, routes: Dict[str, str]) -> str:
    """Route input to specialized prompt using content classification."""
    # First determine appropriate route using LLM with chain-of-thought
    print(f"\nAvailable routes: {list(routes.keys())}")
    selector_prompt = f"""
    Analyze the input and select the most appropriate support team from these options: {list(routes.keys())}
    First explain your reasoning, then provide your selection in this XML format:

    <reasoning>
    Brief explanation of why this ticket should be routed to a specific team.
    Consider key terms, user intent, and urgency level.
    </reasoning>

    <selection>
    The chosen team name
    </selection>

    Input: {input}""".strip()
    
    route_response = llm_call(selector_prompt)
    reasoning = extract_xml(route_response, 'reasoning')
    route_key = extract_xml(route_response, 'selection').strip().lower()
    
    print("Routing Analysis:")
    print(reasoning)
    print(f"\nSelected route: {route_key}")
    
    # Process input with selected specialized prompt
    selected_prompt = routes[route_key]
    return llm_call(f"{selected_prompt}\nInput: {input}")
```
See the basis workflow in Jupyter Notebooks in this folder. 

## Evalautor- Optimizer Workflow
In this workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. 

Use this workflow when you have clear evaluation criteria and value from iterative refinement. Good fit when LLM response can be demonstrably improve when feedback is provided. LLM can provide meaningful feedback. 

``` python 
from util import llm_call, extract_xml

def generate(prompt: str, task: str, context: str = "") -> tuple[str, str]:
    """Generate and improve a solution based on feedback."""
    full_prompt = f"{prompt}\n{context}\nTask: {task}" if context else f"{prompt}\nTask: {task}"
    response = llm_call(full_prompt)
    thoughts = extract_xml(response, "thoughts")
    result = extract_xml(response, "response")
    
    print("\n=== GENERATION START ===")
    print(f"Thoughts:\n{thoughts}\n")
    print(f"Generated:\n{result}")
    print("=== GENERATION END ===\n")
    
    return thoughts, result

def evaluate(prompt: str, content: str, task: str) -> tuple[str, str]:
    """Evaluate if a solution meets requirements."""
    full_prompt = f"{prompt}\nOriginal task: {task}\nContent to evaluate: {content}"
    response = llm_call(full_prompt)
    evaluation = extract_xml(response, "evaluation")
    feedback = extract_xml(response, "feedback")
    
    print("=== EVALUATION START ===")
    print(f"Status: {evaluation}")
    print(f"Feedback: {feedback}")
    print("=== EVALUATION END ===\n")
    
    return evaluation, feedback

def loop(task: str, evaluator_prompt: str, generator_prompt: str) -> tuple[str, list[dict]]:
    """Keep generating and evaluating until requirements are met."""
    memory = []
    chain_of_thought = []
    
    thoughts, result = generate(generator_prompt, task)
    memory.append(result)
    chain_of_thought.append({"thoughts": thoughts, "result": result})
    
    while True:
        evaluation, feedback = evaluate(evaluator_prompt, result, task)
        if evaluation == "PASS":
            return result, chain_of_thought
            
        context = "\n".join([
            "Previous attempts:",
            *[f"- {m}" for m in memory],
            f"\nFeedback: {feedback}"
        ])
        
        thoughts, result = generate(generator_prompt, task, context)
        memory.append(result)
        chain_of_thought.append({"thoughts": thoughts, "result": result})
```

``` python
evaluator_prompt = """
Evaluate this following code implementation for:
1. code correctness
2. time complexity
3. style and best practices

You should be evaluating only and not attemping to solve the task.
Only output "PASS" if all criteria are met and you have no further suggestions for improvements.
Output your evaluation concisely in the following format.

<evaluation>PASS, NEEDS_IMPROVEMENT, or FAIL</evaluation>
<feedback>
What needs improvement and why.
</feedback>
"""

generator_prompt = """
Your goal is to complete the task based on <user input>. If there are feedback 
from your previous generations, you should reflect on them to improve your solution

Output your answer concisely in the following format: 

<thoughts>
[Your understanding of the task and feedback and how you plan to improve]
</thoughts>

<response>
[Your code implementation here]
</response>
"""

task = """
<user input>
Implement a Stack with:
1. push(x)
2. pop()
3. getMin()
All operations should be O(1).
</user input>
"""

loop(task, evaluator_prompt, generator_prompt)
```

*Feedback*
=== GENERATION START ===
Thoughts:

The task requires implementing a Stack with constant time operations including finding minimum. 
To achieve O(1) for getMin(), we need to maintain a second stack that keeps track of minimums.
Each time we push, if the value is smaller than current min, we add it to minStack.
When we pop, if the popped value equals current min, we also pop from minStack.

Generated:
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
            
    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        
    def getMin(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1]
```

=== GENERATION END ===

=== EVALUATION START ===
Status: NEEDS_IMPROVEMENT
Feedback: 
While the implementation is generally correct and achieves O(1) time complexity for all operations, there are several areas for improvement:

1. Error Handling:
- pop() should raise an exception when stack is empty rather than silently returning
- getMin() should raise an exception when stack is empty rather than returning None
- These behaviors should be consistent with standard stack implementations

2. Type Hints:
- Return type hint for pop() should be None or void
- Missing type hints for class variables stack and minStack

3. Documentation:
- Missing docstrings for class and methods
- Missing parameter descriptions

4. Edge Cases:
- No explicit handling of invalid input types for push()

The core algorithm is correct and efficient, but the implementation could be more robust and better documented for production use.

=== EVALUATION END ===


=== GENERATION START ===
Thoughts:

Based on the feedback, I'll improve the implementation by:
1. Adding proper error handling with exceptions
2. Including type hints and docstrings
3. Adding input validation
4. Maintaining O(1) time complexity for all operations


Generated:

```python
from typing import List

class MinStack:
    """A stack that supports push, pop, and getting minimum element in O(1) time."""
    
    def __init__(self):
        """Initialize empty stack with two internal lists."""
        self.stack: List[int] = []
        self.minStack: List[int] = []
        
    def push(self, x: int) -> None:
        """
        Push element onto stack and update minimum stack.
        
        Args:
            x: Integer to push onto stack
            
        Raises:
            TypeError: If x is not an integer
        """
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")
            
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
            
    def pop(self) -> None:
        """
        Remove and return top element from stack.
        
        Raises:
            IndexError: If stack is empty
        """
        if not self.stack:
            raise IndexError("Cannot pop from empty stack")
            
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()
        
    def getMin(self) -> int:
        """
        Get minimum element in stack.
        
        Returns:
            int: Minimum element in stack
            
        Raises:
            IndexError: If stack is empty
        """
        if not self.minStack:
            raise IndexError("Cannot get minimum from empty stack")
        return self.minStack[-1]
```
=== GENERATION END ===

## Orchestrator-Workers Workflow
In this workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLM and synthesizes their results. This workflow is well-suited for complex tasks where you can't predict the subtasks needed. The key difference from simple parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

```python
from typing import Dict, List, Optional
from util import llm_call, extract_xml

def parse_tasks(tasks_xml: str) -> List[Dict]:
    """Parse XML tasks into a list of task dictionaries."""
    tasks = []
    current_task = {}
    
    for line in tasks_xml.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("<task>"):
            current_task = {}
        elif line.startswith("<type>"):
            current_task["type"] = line[6:-7].strip()
        elif line.startswith("<description>"):
            current_task["description"] = line[12:-13].strip()
        elif line.startswith("</task>"):
            if "description" in current_task:
                if "type" not in current_task:
                    current_task["type"] = "default"
                tasks.append(current_task)
    
    return tasks

class FlexibleOrchestrator:
    """Break down tasks and run them in parallel using worker LLMs."""
    
    def __init__(
        self,
        orchestrator_prompt: str,
        worker_prompt: str,
    ):
        """Initialize with prompt templates."""
        self.orchestrator_prompt = orchestrator_prompt
        self.worker_prompt = worker_prompt

    def _format_prompt(self, template: str, **kwargs) -> str:
        """Format a prompt template with variables."""
        try:
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required prompt variable: {e}")

    def process(self, task: str, context: Optional[Dict] = None) -> Dict:
        """Process task by breaking it down and running subtasks in parallel."""
        context = context or {}
        
        # Step 1: Get orchestrator response
        orchestrator_input = self._format_prompt(
            self.orchestrator_prompt,
            task=task,
            **context
        )
        orchestrator_response = llm_call(orchestrator_input)
        
        # Parse orchestrator response
        analysis = extract_xml(orchestrator_response, "analysis")
        tasks_xml = extract_xml(orchestrator_response, "tasks")
        tasks = parse_tasks(tasks_xml)
        
        print("\n=== ORCHESTRATOR OUTPUT ===")
        print(f"\nANALYSIS:\n{analysis}")
        print(f"\nTASKS:\n{tasks}")
        
        # Step 2: Process each task
        worker_results = []
        for task_info in tasks:
            worker_input = self._format_prompt(
                self.worker_prompt,
                original_task=task,
                task_type=task_info['type'],
                task_description=task_info['description'],
                **context
            )
            
            worker_response = llm_call(worker_input)
            result = extract_xml(worker_response, "response")
            
            worker_results.append({
                "type": task_info["type"],
                "description": task_info["description"],
                "result": result
            })
            
            print(f"\n=== WORKER RESULT ({task_info['type']}) ===\n{result}\n")
        
        return {
            "analysis": analysis,
            "worker_results": worker_results,
        }
```

``` python
ORCHESTRATOR_PROMPT = """
Analyze this task and break it down into 2-3 distinct approaches:

Task: {task}

Return your response in this format:

<analysis>
Explain your understanding of the task and which variations would be valuable.
Focus on how each approach serves different aspects of the task.
</analysis>

<tasks>
    <task>
    <type>formal</type>
    <description>Write a precise, technical version that emphasizes specifications</description>
    </task>
    <task>
    <type>conversational</type>
    <description>Write an engaging, friendly version that connects with readers</description>
    </task>
</tasks>
"""

WORKER_PROMPT = """
Generate content based on:
Task: {original_task}
Style: {task_type}
Guidelines: {task_description}

Return your response in this format:

<response>
Your content here, maintaining the specified style and fully addressing requirements.
</response>
"""

orchestrator = FlexibleOrchestrator(
    orchestrator_prompt=ORCHESTRATOR_PROMPT,
    worker_prompt=WORKER_PROMPT,
)

results = orchestrator.process(
    task="Write a product description for a new eco-friendly water bottle",
    context={
        "target_audience": "environmentally conscious millennials",
        "key_features": ["plastic-free", "insulated", "lifetime warranty"]
    }
)
```

=== ORCHESTRATOR OUTPUT ===

ANALYSIS:

This task requires creating marketing copy for an eco-friendly water bottle, which presents multiple angles for effective communication. The key challenge is balancing environmental benefits with practical features while maintaining appeal to different consumer segments.

Key variations would be valuable because:
1. Technical buyers need specific details about materials and environmental impact
2. Lifestyle-focused consumers respond better to emotional benefits and storytelling
3. Different tones can target distinct market segments while promoting the same core product

The technical approach serves those who make purchase decisions based on specifications and measurable impact, while the conversational approach connects with those who buy based on lifestyle alignment and emotional resonance.


TASKS:
[{'type': 'formal', 'description': '>Create a specification-focused description highlighting material composition, environmental certifications, capacity measurements, and quantifiable eco-impact (e.g., "plastic bottles saved per year"). Include technical details about manufacturing process and recycling capabilities.<'}, {'type': 'conversational', 'description': '>Develop a narrative-style description that focuses on the user experience, lifestyle benefits, and emotional connection to environmental protection. Use relatable scenarios and casual language to help readers envision the bottle as part of their daily routine.<'}, {'type': 'hybrid', 'description': '>Combine emotional appeal with key specifications by weaving technical details into a story-driven format. Balance environmental impact statistics with aspirational messaging about sustainability lifestyle choices.<'}]

=== WORKER RESULT (formal) ===

Introducing the EcoVessel Pro Series: A precision-engineered hydration solution crafted from 100% post-consumer recycled stainless steel, certified by the Global Recycled Standard (GRS).

Technical Specifications:
• Capacity: 750ml / 25.4 fl oz
• Material: 18/8 food-grade recycled stainless steel (304 grade)
• Wall thickness: 2mm double-wall vacuum insulation
• Temperature retention: 24 hours cold / 12 hours hot
• Weight: 340g / 12 oz (empty)

Environmental Certifications:
• Carbon Neutral Product certified by Climate Partner
• BPA-free verification from NSF International
• ISO 14001 Environmental Management certification

Manufacturing Process:
Manufactured using hydroelectric power in our carbon-neutral facility, each vessel undergoes a proprietary eco-sanitization process utilizing steam-based sterilization, eliminating chemical cleaning agents. The powder coating is applied through a zero-waste electrostatic process.

Environmental Impact Metrics:
• Eliminates approximately 167 single-use plastic bottles annually per user
• 87% lower carbon footprint compared to traditional bottle manufacturing
• 100% recyclable at end-of-life through our closed-loop recycling program
• Saves 2,920 liters of water annually through eliminated plastic bottle production

Each unit includes a digital tracking code for real-time impact monitoring and verification of authenticity. Engineered for a minimum 10-year service life under normal usage conditions.



=== WORKER RESULT (conversational) ===



=== WORKER RESULT (hybrid) ===

Meet the AquaVerde Elite - where your daily hydration ritual becomes a powerful statement for our planet's future.

Imagine starting your day knowing that every sip you take helps prevent up to 167 single-use plastic bottles from entering our oceans annually. The AquaVerde Elite isn't just a water bottle; it's your personal ambassador in the fight against plastic pollution, crafted from aerospace-grade recycled stainless steel that's been given a second life.

Built to accompany you through life's adventures, this 24oz companion features our innovative ThermaLock™ technology, maintaining your cold drinks frosty for 24 hours or your hot beverages steaming for 12 hours. The double-wall vacuum insulation isn't just about performance - it's engineered to use 30% less material than conventional designs while delivering superior temperature retention.

The bottle's sleek silhouette houses thoughtful details that enhance your daily experience: a leak-proof AutoSeal cap that operates with one hand, a built-in carrying loop made from recycled climbing rope, and our signature CloudTouch™ exterior finish that's both grippy and gorgeous. Available in four nature-inspired colors (Ocean Deep, Forest Canopy, Desert Dawn, and Mountain Mist), each bottle's finish is created using a water-based, zero-VOC coating process.

But perhaps the most beautiful feature is what you don't see - every AquaVerde Elite helps fund clean water projects in developing communities, with 2% of each purchase supporting water conservation initiatives worldwide. Your choice to carry the AquaVerde Elite isn't just about staying hydrated; it's about being part of a global movement toward a more sustainable future.

Specifications that matter:
• Capacity: 24oz/710ml
• Weight: 12.8oz
• Materials: 90% recycled 18/8 stainless steel
• BPA-free, phthalate-free
• Dishwasher safe
• Lifetime warranty

Join the growing community of AquaVerde carriers who've collectively prevented over 2 million single-use bottles from entering our ecosystems. Because every drop counts, and every choice matters.