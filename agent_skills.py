# /AgentForge/agent_skills.py

"""
Agentų įgūdžių matricos modulis.
Apibrėžia agentų specializacijas ir įgūdžius skirtingoms kategorijoms.
"""

import yaml
import os

# Konstanta nurodanti agentų įgūdžių YAML failo kelią
AGENT_SKILLS_FILE = "agent_skills.yaml"

def load_agent_skills():
    """Loads the agent skills matrix from YAML file"""
    if not os.path.exists(AGENT_SKILLS_FILE):
        create_default_agent_skills()
    
    with open(AGENT_SKILLS_FILE, 'r', encoding='utf-8') as file:
        skills = yaml.safe_load(file)
    return skills

def create_default_agent_skills():
    """Creates default agent skills matrix if no file exists"""
    skills = {
        "agents": {
            "prompt_analyst": {
                "name": "Prompt Analyst",
                "description": "Analyzes user queries and identifies patterns and intentions",
                "skills": {
                    "information_retrieval": 4,
                    "creative_content": 3,
                    "analysis": 5,
                    "development": 3
                },
                "specialties": ["query understanding", "intent detection", "prompt structuring"]
            },
            "prompt_critic": {
                "name": "Prompt Critic",
                "description": "Evaluates and provides critique on proposed prompts",
                "skills": {
                    "information_retrieval": 3,
                    "creative_content": 4,
                    "analysis": 5,
                    "development": 3
                },
                "specialties": ["prompt evaluation", "weakness identification", "improvement suggestion"]
            },
            "prompt_refiner": {
                "name": "Prompt Refiner",
                "description": "Refines and optimizes prompts for maximum effectiveness",
                "skills": {
                    "information_retrieval": 3,
                    "creative_content": 4,
                    "analysis": 3,
                    "development": 3
                },
                "specialties": ["prompt optimization", "clarity enhancement", "structure improvement"]
            },
            "creative_specialist": {
                "name": "Creative Specialist",
                "description": "Specializes in creative content generation prompts",
                "skills": {
                    "information_retrieval": 2,
                    "creative_content": 5,
                    "analysis": 2,
                    "development": 1
                },
                "specialties": ["creative writing", "image prompting", "narrative design", "artistic direction"]
            },
            "technical_specialist": {
                "name": "Technical Specialist",
                "description": "Specializes in technical and development-related prompts",
                "skills": {
                    "information_retrieval": 3,
                    "creative_content": 1,
                    "analysis": 3,
                    "development": 5
                },
                "specialties": ["code generation", "debugging assistance", "technical explanation", "system design"]
            },
            "research_specialist": {
                "name": "Research Specialist",
                "description": "Specializes in information retrieval and research prompts",
                "skills": {
                    "information_retrieval": 5,
                    "creative_content": 2,
                    "analysis": 4,
                    "development": 2
                },
                "specialties": ["research methodologies", "source evaluation", "fact verification", "data collection"]
            }
        },
        "metadata": {
            "version": "1.0",
            "last_updated": "2025-07-10",
            "skill_scale": "1-5 (novice to expert)"
        }
    }
    
    with open(AGENT_SKILLS_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(skills, file, sort_keys=False, default_flow_style=False)
    
    return skills

def get_best_agents_for_category(category_id, count=2):
    """
    Returns the best agents for a specific category
    
    Args:
        category_id: The category to find agents for
        count: Number of agents to return
        
    Returns:
        List of agent IDs sorted by skill level for the category
    """
    skills = load_agent_skills()
    
    # Create a list of (agent_id, skill_level) tuples for the category
    agent_skills = []
    for agent_id, agent_data in skills["agents"].items():
        if category_id in agent_data["skills"]:
            agent_skills.append((agent_id, agent_data["skills"][category_id]))
    
    # Sort by skill level (descending) and return the top 'count' agent IDs
    agent_skills.sort(key=lambda x: x[1], reverse=True)
    return [agent_id for agent_id, _ in agent_skills[:count]]

def get_agent_specialties(agent_id):
    """Returns the specialties of a specific agent"""
    skills = load_agent_skills()
    
    if agent_id not in skills["agents"]:
        return []
    
    return skills["agents"][agent_id].get("specialties", [])

if __name__ == "__main__":
    # Jei paleidžiama tiesiogiai, sukurti numatytąjį įgūdžių matricą
    print("Creating default agent skills matrix...")
    create_default_agent_skills()
    print("Done. Agent skills saved to", AGENT_SKILLS_FILE)
    
    # Testuojame agentų gavimą pagal kategoriją
    for category in ["information_retrieval", "creative_content", "analysis", "development"]:
        best_agents = get_best_agents_for_category(category)
        print(f"\nBest agents for {category}:")
        for agent_id in best_agents:
            specialties = get_agent_specialties(agent_id)
            print(f"  - {skills['agents'][agent_id]['name']}: {', '.join(specialties)}")