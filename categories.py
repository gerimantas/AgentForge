# /AgentForge/categories.py

"""
Kategorijų sistemos modulis.
Apibrėžia hierarchines užklausų kategorijas ir jų atpažinimo logiką.
"""

import yaml
import os

# Konstanta nurodanti kategorijų YAML failo kelią
CATEGORIES_FILE = "categories.yaml"

def load_categories():
    """Loads the category hierarchy from YAML file"""
    if not os.path.exists(CATEGORIES_FILE):
        create_default_categories()
    
    with open(CATEGORIES_FILE, 'r', encoding='utf-8') as file:
        categories = yaml.safe_load(file)
    return categories

def create_default_categories():
    """Creates default category structure if no file exists"""
    categories = {
        "categories": {
            "information_retrieval": {
                "name": "Information Retrieval",
                "description": "Queries focused on finding and retrieving information",
                "keywords": ["find", "search", "lookup", "research", "information about", "tell me about"],
                "subcategories": {
                    "search": {
                        "name": "Search",
                        "description": "General search queries",
                        "keywords": ["find", "search", "lookup", "where is", "what is"],
                        "example_prompt": "Find information about the effects of climate change on biodiversity"
                    },
                    "research": {
                        "name": "Research",
                        "description": "In-depth research queries",
                        "keywords": ["research", "investigate", "analyze", "study", "examine"],
                        "example_prompt": "Research the latest advancements in quantum computing"
                    },
                    "fact_check": {
                        "name": "Fact Check",
                        "description": "Fact verification queries",
                        "keywords": ["verify", "fact check", "is it true", "confirm", "debunk"],
                        "example_prompt": "Verify if drinking lemon water in the morning boosts metabolism"
                    }
                }
            },
            "creative_content": {
                "name": "Creative Content",
                "description": "Queries focused on creating artistic or creative content",
                "keywords": ["create", "write", "generate", "design", "compose", "draw"],
                "subcategories": {
                    "text": {
                        "name": "Text",
                        "description": "Text creation queries",
                        "keywords": ["write", "compose", "draft", "create text", "article", "blog", "story"],
                        "example_prompt": "Write a short story about a robot discovering emotions"
                    },
                    "images": {
                        "name": "Images",
                        "description": "Image generation queries",
                        "keywords": ["draw", "image", "picture", "illustration", "design", "visual"],
                        "example_prompt": "Generate an image prompt for a futuristic city with flying cars"
                    },
                    "video": {
                        "name": "Video",
                        "description": "Video concept creation queries",
                        "keywords": ["video", "film", "animation", "movie", "scene", "screenplay"],
                        "example_prompt": "Create a concept for a 2-minute explainer video about renewable energy"
                    }
                }
            },
            "analysis": {
                "name": "Analysis",
                "description": "Queries focused on analyzing data or situations",
                "keywords": ["analyze", "evaluate", "assess", "review", "interpret", "examine"],
                "subcategories": {
                    "data_analysis": {
                        "name": "Data Analysis",
                        "description": "Data processing and interpretation queries",
                        "keywords": ["data", "statistics", "numbers", "trends", "patterns"],
                        "example_prompt": "Analyze this dataset of monthly sales figures and identify patterns"
                    },
                    "critical_thinking": {
                        "name": "Critical Thinking",
                        "description": "Logical analysis and reasoning queries",
                        "keywords": ["critique", "analyze argument", "reasoning", "logic", "fallacy"],
                        "example_prompt": "Critically evaluate the arguments for and against universal basic income"
                    },
                    "summarization": {
                        "name": "Summarization",
                        "description": "Content summarization queries",
                        "keywords": ["summarize", "condense", "extract key points", "tldr", "main ideas"],
                        "example_prompt": "Summarize the main findings of this research paper on sleep patterns"
                    }
                }
            },
            "development": {
                "name": "Development",
                "description": "Queries focused on software development or technical solutions",
                "keywords": ["code", "program", "develop", "build", "debug", "technical", "software"],
                "subcategories": {
                    "coding": {
                        "name": "Coding",
                        "description": "Programming code creation queries",
                        "keywords": ["code", "program", "script", "function", "develop", "implement"],
                        "example_prompt": "Write a Python function that calculates Fibonacci numbers"
                    },
                    "debugging": {
                        "name": "Debugging",
                        "description": "Code error fixing queries",
                        "keywords": ["debug", "fix", "error", "issue", "problem", "not working", "bug"],
                        "example_prompt": "Debug this JavaScript code that's throwing an 'undefined' error"
                    },
                    "architecture": {
                        "name": "Architecture",
                        "description": "System design queries",
                        "keywords": ["architecture", "design", "system", "structure", "plan", "blueprint"],
                        "example_prompt": "Design a microservice architecture for an e-commerce platform"
                    }
                }
            }
        },
        "metadata": {
            "version": "1.0",
            "last_updated": "2025-07-10"
        }
    }
    
    with open(CATEGORIES_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(categories, file, sort_keys=False, default_flow_style=False)
    
    return categories

def get_category_description(category_id, subcategory_id=None):
    """
    Returns description for a given category/subcategory
    
    Args:
        category_id: Main category ID
        subcategory_id: Optional subcategory ID
    
    Returns:
        String description of the category
    """
    categories = load_categories()
    
    if category_id not in categories["categories"]:
        return "Unknown category"
    
    category = categories["categories"][category_id]
    
    if subcategory_id is None:
        return category["description"]
    
    if subcategory_id not in category["subcategories"]:
        return "Unknown subcategory"
    
    return category["subcategories"][subcategory_id]["description"]

def list_all_categories():
    """Returns a formatted list of all categories and subcategories"""
    categories = load_categories()
    result = []
    
    for cat_id, category in categories["categories"].items():
        result.append(f"{category['name']}:")
        for subcat_id, subcategory in category["subcategories"].items():
            result.append(f"  - {subcategory['name']}: {subcategory['description']}")
    
    return "\n".join(result)

if __name__ == "__main__":
    # Jei paleidžiama tiesiogiai, sukurti numatytąsias kategorijas
    print("Creating default categories...")
    create_default_categories()
    print("Done. Categories saved to", CATEGORIES_FILE)
    print("\nAvailable categories:")
    print(list_all_categories())