# Zero to One: Learning Agentic Patterns

source: [https://www.philschmid.de/agentic-pattern](https://www.philschmid.de/agentic-pattern)

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

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image.png)

- One LLM call feeds the input of next LLM
- Predictable tasks (subtasks)

**Cases**

- Generating a structured document: One LLM creates outline. Other LLM validates the outline against a criteria. The final LLM write the actual content based.
- Multi-step data processing; ELT + summarizing information
- Generating newsletters based on curated inputs

[Code](./prompt_chaining)

### Workflow Routing

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%201.png)

- LLM Router classify the users input and decide the most appropriate specialized task or LLM.
- Separation of concerns allows optimizing individual downstream tasks

**Cases**

- Customer support systems: Routing queries toa gents specialized in billing, technical support, or product information
- Tiered LLM usage: Routing simple queries to faster and cheaper models and complex questions to more capable models
- Content generation: Routing requests for blog posts, social media updates or ad coy to different specialized prompts.

[Code](./routing.py)

### Workflow: Parallelization

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%202.png)

- Task borken down into independent subtasks that are processed simultaneously (multiple LLMs)
- The initial query is sent to multiple LLMs in parallel with individual prompts
- Improve latency if subtasks does not depend on each other

**Cases**

- RAG (Retrieval-Augmented Generation) with query decomposition: Breaking a complex query into sub-queries
- Analyzing large documents: Dividing the document into sections, summarizing each section in parallel and then combining summaries
- Generating multiple perspectives: Multiple LLM's + Multiple prompts
- Map-reduce style operations in data

[Code](./parallelization.py)

### Reflection Pattern (Evaluator-Opitimizer)

![Screenshot 2025-10-26 at 15.37.15.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/Screenshot_2025-10-26_at_15.37.15.png)

- Agente evaluates its own output and uses the feedback ro refine its response iteratively.
- Self-correction loop

**Cases**

- Code generation: Writing code, executing it, error message or test results
- Writing and refinement: Generating a draft reflecting on its clarify and tone.
- Complex problem solving: Generating a plan, evaluate feasibility and refining based on evaluation
- Information retrieval: Searching for information and evaluate if all required details were found before presenting the answer.

[Code](./reflection.py)

### Tool Use Pattern (Function Calling)

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%203.png)

- LLM has the ability to invoke external functions or APIs to interact with the outside world, retrieve information or perform actions.
- LLM can decide to call one or more tools by generating a structured output matching the required schema

**Cases**

- Booking appointments using calendar API
- Retrieval real-time stock prices via a financial API
- Searching a vector database for relevant documents
- Controlling smart home devices
- Executing code snippets

[Code](./function_calling.py)

### Planning Pattern (Orchestrator-Workers)

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%204.png)

- Central planning LLM breaks down a complex task into a dynamic list of subtasks and delegated to specialized worker agents.
- Solves complex problems (multi-step reasoning)
- A plan is generated then subtasks are assigned to worker agents to execute them (potentially in parallel if dependencia allow)
- A collector collects the results from the workers, reflects if goal has been achieved
    - Potentially initiates a re-planning step if necessary
- Reduces cognitive load on a single LLM call
- Improves reasoning quality, minimizes errors and allows for dynamic adaptation

**Cases**

- Complex software development tasks: Breaking down “build a feature” into planning, coding, testing and documentation tasks
- Research and report generation: Planning steps search, data extraction, analysis and report writing
- Multi-modal tasks: Planning steps involving image generation, text analysis, data integration
- Executing complex user request like “Plan 3-day trip to Paris, book flights and a hotel within this budget”

[Code](./planning.py)

### Multi-Agent Pattern

Coordinator (Manager Approach)

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%205.png)

Swarm approach

![image.png](Zero%20to%20One%20Learning%20Agentic%20Patterns%202973106cd76180e7abb9e21bbb163cb5/image%206.png)

- Multiple agents each assigned a specific role
- Automous or semi-automous agents
- Agents interact and collaborate often coordinated by a central coordinator or manager
- One agent pass the control to another agent

**Cases**

- Simulating debates or brainstorming sessions with different AI
- Complex software creation involving agents for planning, coding, testing and deployment
- Running virtual experiments or simulations with agents representing different actors
- Collaborative writing or content creation process

[Code](./multi_agent.py)