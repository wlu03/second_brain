This function takes in an input and a dictionary of routes where each key is a route name and each value is a specialized prompt. The LLM first analyzes the input to decide which route is most appropriate explains why and then processes the input using the prompt for the chosen route.

Use Case: 
Say you're building a support agent that can route queries to different departments:
- `billing`: questions about charges and invoices
- `technical`: help with bugs, issues
- `general`: broad or unclassified queries

```python 
routes = {
    "billing": "You are a billing support agent. Help the user with their payment or invoice related issue.",
    "technical": "You are a technical support agent. Help the user troubleshoot bugs or system issues.",
    "general": "You are a general support agent. Help the user with their general inquiry."
}

input_text = "I was charged twice for my last subscription renewal. Can someone explain why?"

final_response = route(input_text, routes)
print("\nFinal Response:\n", final_response)

```

Behind the Scene:
- A classifier prompt is built 
``` xml
<reasoning>Looks like this issue involves being charged twice — clearly a billing problem.</reasoning>
<selection>billing</selection>
```
- LLM picks `billing` route based on key terms like charged, subscription, etc. 
- The input is passed to the billing specific prompt 
``` python
"You are a billing support agent. Help the user with their payment or invoice related issue." 
```
- You get a tailored response from the LLM in the context of a **billing agent**.
- 