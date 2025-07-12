"""
AgentForge Simplified Agents
============================

Simplified agent implementations for Stage 2 that don't rely on CrewAI.
This allows testing the workflow architecture without complex dependencies.
"""

# Create a base class that's compatible with CrewAI's BaseAgent structure
class BaseAgent:
    """Base agent class for compatibility with CrewAI."""
    def __init__(self, role, goal, backstory, verbose=True, allow_delegation=False, tools=None):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose
        self.allow_delegation = allow_delegation
        self.tools = tools or []

# Simple agent classes that simulate the CrewAI agents
class SimpleAgent(BaseAgent):
    def __init__(self, role, goal, backstory, verbose=True, allow_delegation=False, tools=None):
        super().__init__(role, goal, backstory, verbose, allow_delegation, tools)
        
    def execute(self, input_text):
        """Simulate agent execution."""
        return f"Agent {self.role}: Processed '{input_text}' - {self.goal}"

# Create simplified agents
prompt_analyst = SimpleAgent(
    role='Prompt Engineering Analyst',
    goal='To structure and improve the initial user prompt by applying fundamental prompt engineering best practices.',
    backstory='You are an experienced AI analyst specializing in transforming vague user ideas into clear, machine-readable instructions.'
)

prompt_critic = SimpleAgent(
    role='Advanced Prompt Strategy Critic',
    goal='To critically evaluate the improved prompt and suggest advanced, state-of-the-art techniques for even greater effectiveness.',
    backstory='You are a world-class AI researcher. Your goal is not to praise but to find flaws and propose how to elevate the prompt to an expert level.'
)

prompt_refiner = SimpleAgent(
    role='Final Prompt Optimization Master',
    goal='To merge the structured prompt with the critic\'s suggestions into a single, cohesive, and maximally optimized final version.',
    backstory='You are an AI architect with a deep understanding of both stable fundamentals and experimental techniques.'
)

researcher_agent = SimpleAgent(
    role="Specialized Prompt Engineering Researcher",
    goal="To systematically review approved sources, identify the most significant 'prompt engineering' techniques, and provide a FACT-BASED summary.",
    backstory="You are an AI researcher who strictly follows instructions. Your highest value is factual accuracy."
)

synthesizer_agent = SimpleAgent(
    role="Prompt Engineering Strategy Synthesizer",
    goal="To analyze the Researcher's report and synthesize its findings into a concise, actionable insight.",
    backstory="You are an expert strategist who can see the bigger picture."
)

rule_engineer_agent = SimpleAgent(
    role="Prompt Engineering Rules Engineer",
    goal="To convert strategic insights into formal, structured rules that can be applied systematically.",
    backstory="You are a systematic engineer who creates clear, actionable rules from strategic insights."
)

librarian_agent = SimpleAgent(
    role='AI Information Source Curator (Librarian)',
    goal='To evaluate the credibility of new information sources and decide if they should be added to the Source Registry.',
    backstory='You are a meticulous and skeptical academic librarian specializing in AI.'
)

# Create a simplified Task class for Stage 2 compatibility
class SimpleTask:
    """Simplified task class for Stage 2 implementation."""
    def __init__(self, description, agent=None, expected_output=None, tools=None):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output
        self.tools = tools or []
        
    def execute(self):
        """Execute the task."""
        if self.agent:
            return self.agent.execute(self.description)
        return f"Task executed: {self.description[:50]}..."

# Helper functions for compatibility
def fact_check_agent(fact: str) -> bool:
    """Simple fact checking simulation."""
    return True  # Simplified for Stage 2

def is_source_trusted(url: str) -> bool:
    """Simple source trust checking simulation."""
    return True  # Simplified for Stage 2

def add_knowledge_entry(topic, fact, source, verified=True, notes=""):
    """Simple knowledge entry addition simulation."""
    return True  # Simplified for Stage 2
