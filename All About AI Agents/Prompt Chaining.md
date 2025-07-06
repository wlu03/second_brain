This function passes input through a sequence of prompts sequentially where the output of one step becomes the input for the next.

Use Case: 
Break down a complex task
"Summarize, then translate to French, then make it poetic"
``` python

def chain(input: str, prompts: List[str]) -> str:
    """Chain multiple LLM calls sequentially, passing results between steps."""
    result = input
    for i, prompt in enumerate(prompts, 1):
        print(f"\nStep {i}:")
        result = llm_call(f"{prompt}\nInput: {result}")
        print(result)
    return result


prompts = [
    "Summarize the following text.",
    "Translate the summary to French.",
    "Convert the French translation into a short poem."
]

input_text = "Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics."

final_result = chain(input_text, prompts)
print("\nFinal Result:\n", final_result)
```
