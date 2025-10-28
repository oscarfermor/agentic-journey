# Agentic Journey

A comprehensive learning repository for building AI agents from scratch, covering foundational patterns to advanced multi-agent systems.

## 📚 Overview

This repository contains educational materials and implementations for learning agentic AI patterns and building sophisticated AI agents using modern frameworks like LangGraph and LangChain. It serves as a practical journey from understanding basic agent concepts to implementing complex multi-agent systems.

## 🗂️ Repository Structure

### `/zero-to-one`

**Learning Agentic Patterns** - Fundamental patterns for building AI agents

This section covers core agentic patterns with practical implementations:

- **Prompt Chaining** (`prompt_chaining.py`) - Sequential LLM workflows for predictable multi-step tasks
- **Routing** (`routing.py`) - Intelligent task routing to specialized agents
- **Parallelization** (`parallelization.py`) - Parallel processing of independent subtasks
- **Reflection** (`reflection.py`) - Self-evaluation and iterative refinement patterns
- **Function Calling** (`function_calling.py`) - Tool use and external API integration
- **Planning** (`planning.py`) - Orchestrator-worker pattern for complex task decomposition
- **Multi-Agent** (`multi_agent.py`) - Coordinator and swarm approaches for collaborative agents

**Key Concepts:**

- Workflows vs Agents: When to use deterministic workflows vs non-deterministic agents
- Complexity management: Seeking simplest solutions first
- Error handling and retry mechanisms
- Self-correction capabilities

**Technologies:** Google Generative AI, LangChain

### `/langchain/deep-agents`

**Deep Agents from Scratch** - Building production-ready agents using LangGraph

An educational course demonstrating how to build advanced AI agents with context engineering techniques. This section provides progressive tutorials for building research-capable agents.

**Core Components:**

- `src/deep_agents_from_scratch/` - Implementation source code
  - `state.py` - State management with TODOs and virtual files
  - `file_tools.py` - Virtual file system operations (ls, read, write, edit)
  - `todo_tools.py` - Task planning and tracking
  - `research_tools.py` - Web search and research capabilities

**Tutorial Notebooks:**

1. `0_create_agent.ipynb` - Basic ReAct loop implementation
2. `1_todo.ipynb` - Task planning foundations with TODO lists
3. `2_files.ipynb` - Virtual file systems for context offloading
4. `3_subagents.ipynb` - Sub-agent delegation and context isolation
5. `4_full_agent.ipynb` - Complete research agent combining all patterns

**Key Patterns:**

- Context engineering: Task planning, file offloading, context isolation
- ReAct loops: Reason-Act pattern for agent decision making
- Sub-agent spawning: Creating specialized agents for specific tasks
- Virtual file systems: Storing context in agent state

**Technologies:** LangGraph, LangChain, Anthropic (Claude), Tavily

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/) package manager (for deep-agents)
- API Keys for external services

### Quick Start

#### For Zero-to-One Learning Patterns

```bash
cd zero-to-one
pip install -r requirements.txt
python prompt_chaining.py  # Or any other pattern file
```

#### For Deep Agents from Scratch

```bash
cd langchain/deep-agents/deep-agents-from-scratch

# Install dependencies using uv
uv sync

# Create .env file with API keys
cp example.env .env
# Edit .env with your API keys:
# - TAVILY_API_KEY
# - ANTHROPIC_API_KEY
# - LANGSMITH_API_KEY (optional)

# Run Jupyter notebooks
uv run jupyter notebook

# Or use LangGraph Studio
langgraph up
```

## 📖 Learning Path

### Stage 1: Fundamentals (`/zero-to-one`)

Understand the foundational patterns:

1. Start with **Prompt Chaining** to understand sequential workflows
2. Learn **Function Calling** for tool integration
3. Explore **Routing** for intelligent task delegation
4. Practice **Reflection** for self-correction
5. Build **Planning** capabilities
6. Implement **Multi-Agent** collaboration

### Stage 2: Deep Agents (`/langchain/deep-agents/deep-agents-from-scratch`)

Build production-ready agents:

1. **Create Basic Agent** - Implement ReAct loop
2. **Add TODO Planning** - Task tracking and status management
3. **Virtual File System** - Context offloading and persistence
4. **Sub-Agents** - Context isolation and specialized delegation
5. **Full Agent** - Complete research agent with all capabilities

## 🛠️ Key Technologies

- **LangGraph** - Framework for building stateful, multi-actor AI applications
- **LangChain** - LLM application framework
- **Anthropic Claude** - Language model for agent reasoning
- **Google Generative AI** - Alternative LLM provider
- **Tavily** - Real-time web search API
- **Jupyter Notebooks** - Interactive learning environment

## 📝 Key Concepts

### Agentic Patterns

- **Workflows**: Deterministic, predefined execution paths
- **Agents**: Non-deterministic, autonomous decision-making
- **Tool Use**: External function calling and API integration
- **State Management**: Persisting context across interactions
- **Planning**: Task decomposition and orchestration
- **Multi-Agent**: Collaborative agent systems

### Context Engineering

- **Context Offloading**: Moving information to virtual file systems
- **Context Isolation**: Using sub-agents to prevent task interference
- **Task Tracking**: Maintaining structured progress with TODO lists
- **Virtual File Systems**: Ephemeral storage within agent state

## 🎯 Use Cases

This repository enables building:

- **Research Agents** - Conducting web research and analysis
- **Planning Agents** - Breaking down complex tasks into actionable steps
- **Multi-Step Agents** - Handling workflows with 50+ tool calls
- **Specialized Agents** - Focused agents for specific domains
- **Collaborative Systems** - Multi-agent coordination

## 📚 Resources

- [Deep Agents Course](https://academy.langchain.com/courses/deep-research-with-langgraph)
- [Agentic Patterns Guide](https://www.philschmid.de/agentic-pattern)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)

## 🤝 Contributing

This is a learning repository. Feel free to explore, experiment, and adapt the code for your own projects.

## 📄 License

See individual component licenses in their respective directories.

## 🎓 Learning Outcomes

After working through this repository, you will:

- Understand core agentic patterns and when to use them
- Be able to build agents using LangGraph
- Know how to manage context and state in AI agents
- Understand task planning and decomposition strategies
- Be capable of implementing multi-agent systems
- Have experience with virtual file systems and context offloading
