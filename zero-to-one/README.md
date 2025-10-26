source: https://www.philschmid.de/agentic-pattern

An agent characteristic is. the ability to dynamically plan and execute tasks (choose between tasks to reach a goal) leveraging external tools and memory to achieve complex goals.

Workflows: predefined paths (deterministic) 

Agents: Autonomy in deciding the course of action (non-deterministic)

### Agentic patterns

- Provide structure to build, grow and manage AI applications in complexity and adapt to changing requirements
- Seek for simplest solution first
    - If the steps are known use **workflow**
- High latency and computational cost
- Better solutions (complex, ambiguous, dynamic)
- If steps are well-defined (steps are known) use a **workflow**.
- Agents provide flexibility, adaptability, and model-driven decision-making.
- Keep it simple.
- Agency introduces inherent unpredictability and potential errors.
    - Because of this it must incorporate robust error logging, exception handling and retry mechanism
        - This allow the LLM to self-correct

### Workflow: Prompt Chaining

```bash
Query → LLM 1 → Ouput1 → LLM2 → Final Output
```

- One LLM call feeds the input of next LLM
- Predictable tasks (subtasks)
    - Generating a structured document: One LLM creates outline. Other LLM validates the outline against a criteria. The final LLM write the actual content based.
    - Multi-step data processing; ELT + summarizing information
    - Generating newsletters based on curated inputs

[Code](./prompt_chaining)

### Workflow Routing

```bash
User Query -> LLM Router ->            -> LLM Task A
														Decision ->       or      -> Final Ouput
																		   -> LLM Task B  
```

- LLM Router classify the users input and decide the most appropriate specialized task or LLM.
- Separation of concerns allows optimizing individual downstream tasks
    - Customer support systems: Routing queries toa gents specialized in billing, technical support, or product information
    - Tiered LLM usage: Routing simple queries to faster and cheaper models and complex questions to more capable models
    - Content generation: Routing requests for blog posts, social media updates or ad coy to different specialized prompts.

[Code](./routing.py)

### Workflow: Parallelization

```bash
					->	LLM1
User Query           -> LLM Agregator -> Final Output
					-> 	LLM2
```

- Task borken down into independent subtasks that are processed simultaneously (multiple LLMs)
- The initial query is sent to multiple LLMs in parallel with individual prompts
- Improve latency if subtasks does not depend on each other
    - RAG (Retrieval-Augmented Generation) with query decomposition: Breaking a complex query into sub-queries
    - Analyzing large documents: Dividing the document into sections, summarizing each section in parallel and then combining summaries
    - Generating multiple perspectives: Multiple LLM's + Multiple prompts
    - Map-reduce style operations in data

[Code](./parallelization.py)