# /AgentForge/dynamic_agents.py

"""
Dinaminių agentų parinkimo modulis.
Parenka optimaliausius agentus pagal užklausos kategoriją.
"""

from categories import load_categories
from agent_skills import load_agent_skills, get_best_agents_for_category
from crewai import Agent

def create_agent_from_config(agent_id, agent_config, role_suffix=""):
    """
    Creates a CrewAI agent from configuration
    
    Args:
        agent_id: The agent ID in the configuration
        agent_config: The agent configuration dictionary
        role_suffix: Optional suffix to add to the agent role
        
    Returns:
        A configured CrewAI Agent object
    """
    # Build a role with suffix if provided
    role = agent_config["name"]
    if role_suffix:
        role = f"{role} ({role_suffix})"
        
    # Create the agent with appropriate configuration
    agent = Agent(
        role=role,
        goal=f"Optimize prompts with a focus on {agent_config.get('specialties', [])}",
        backstory=agent_config["description"],
        verbose=True,
        allow_delegation=False
    )
    
    return agent

def get_dynamic_crew_for_category(category_id, subcategory_id=None):
    """
    Creates a crew of agents optimized for a specific category
    
    Args:
        category_id: The main category ID
        subcategory_id: Optional subcategory ID for more specialized agents
        
    Returns:
        List of CrewAI Agent objects optimized for the category
    """
    categories = load_categories()
    agent_skills = load_agent_skills()
    
    # Get the category and subcategory information
    category = categories["categories"].get(category_id)
    if not category:
        return []  # Category not found
        
    subcategory_name = None
    if subcategory_id and subcategory_id in category["subcategories"]:
        subcategory = category["subcategories"][subcategory_id]
        subcategory_name = subcategory["name"]
    
    # Get the best agents for this category
    best_agent_ids = get_best_agents_for_category(category_id, count=3)
    
    # Create agents from configuration
    agents = []
    for agent_id in best_agent_ids:
        agent_config = agent_skills["agents"].get(agent_id)
        if not agent_config:
            continue
            
        # Add specialty suffix based on subcategory if available
        suffix = subcategory_name if subcategory_name else category["name"]
        agent = create_agent_from_config(agent_id, agent_config, role_suffix=suffix)
        agents.append(agent)
    
    return agents

def print_dynamic_agents_info(agents):
    """Prints information about the dynamic agents"""
    print("\n===== Dynamic Agent Team =====")
    for i, agent in enumerate(agents, 1):
        print(f"Agent {i}: {agent.role}")
        print(f"  Goal: {agent.goal}")
        print(f"  Backstory: {agent.backstory}")
        print("-" * 30)
    print("=============================\n")

if __name__ == "__main__":
    # Test the dynamic agent creation with different categories
    for category_id in ["information_retrieval", "creative_content", "analysis", "development"]:
        print(f"\nTesting agents for category: {category_id}")
        agents = get_dynamic_crew_for_category(category_id)
        print_dynamic_agents_info(agents)