# /AgentForge/prompt_templates.py

"""
Prompt'ų šablonų sistema.
Leidžia išsaugoti, keisti ir naudoti sėkmingus prompt'ų šablonus.
"""

import os
import yaml
import json
from datetime import datetime

# Konstantos
TEMPLATES_DIR = "templates"
TEMPLATES_INDEX_FILE = os.path.join(TEMPLATES_DIR, "index.yaml")

def ensure_templates_dir():
    """Ensures templates directory exists"""
    if not os.path.exists(TEMPLATES_DIR):
        os.makedirs(TEMPLATES_DIR)
    
    # Create index file if it doesn't exist
    if not os.path.exists(TEMPLATES_INDEX_FILE):
        create_template_index()

def create_template_index():
    """Creates a new template index file"""
    index = {
        "templates": {},
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "count": 0
        }
    }
    
    save_template_index(index)

def load_template_index():
    """Loads the template index"""
    ensure_templates_dir()
    
    with open(TEMPLATES_INDEX_FILE, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def save_template_index(index):
    """Saves the template index"""
    ensure_templates_dir()
    
    # Update metadata
    index["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    index["metadata"]["count"] = len(index["templates"])
    
    with open(TEMPLATES_INDEX_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(index, file, sort_keys=False, default_flow_style=False)

def generate_template_id(name):
    """Generates a template ID from the name"""
    # Convert to lowercase, replace spaces with underscores
    template_id = name.lower().replace(' ', '_')
    # Remove special characters
    template_id = ''.join(c for c in template_id if c.isalnum() or c == '_')
    
    # Add timestamp to ensure uniqueness
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{template_id}_{timestamp}"

def save_template(template_data):
    """
    Saves a template
    
    Args:
        template_data: Dictionary with template information
            - name: Template name
            - description: Template description
            - category: Template category (e.g., creative, technical)
            - original_prompt: The original prompt
            - optimized_prompt: The optimized prompt
            - tags: List of tags
    
    Returns:
        Template ID
    """
    ensure_templates_dir()
    
    # Generate ID if not provided
    if "id" not in template_data:
        template_data["id"] = generate_template_id(template_data["name"])
    
    # Add creation timestamp
    template_data["created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save template to its own file
    template_file = os.path.join(TEMPLATES_DIR, f"{template_data['id']}.json")
    with open(template_file, 'w', encoding='utf-8') as file:
        json.dump(template_data, file, indent=2)
    
    # Update index
    index = load_template_index()
    index["templates"][template_data["id"]] = {
        "name": template_data["name"],
        "description": template_data["description"],
        "category": template_data["category"],
        "created": template_data["created"],
        "tags": template_data["tags"]
    }
    save_template_index(index)
    
    return template_data["id"]

def load_template(template_id):
    """Loads a template by ID"""
    template_file = os.path.join(TEMPLATES_DIR, f"{template_id}.json")
    
    if not os.path.exists(template_file):
        return None
    
    with open(template_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def delete_template(template_id):
    """Deletes a template by ID"""
    template_file = os.path.join(TEMPLATES_DIR, f"{template_id}.json")
    
    # Delete the file
    if os.path.exists(template_file):
        os.remove(template_file)
    
    # Update index
    index = load_template_index()
    if template_id in index["templates"]:
        del index["templates"][template_id]
        save_template_index(index)
        return True
    
    return False

def list_templates(category=None, tag=None):
    """
    Lists templates with optional filtering
    
    Args:
        category: Filter by category
        tag: Filter by tag
    
    Returns:
        List of templates (dictionaries)
    """
    index = load_template_index()
    templates = []
    
    for template_id, template_info in index["templates"].items():
        # Apply filters
        if category and template_info["category"] != category:
            continue
        
        if tag and tag not in template_info["tags"]:
            continue
        
        # Add template to results
        template_info["id"] = template_id
        templates.append(template_info)
    
    # Sort by creation date (newest first)
    templates.sort(key=lambda x: x["created"], reverse=True)
    return templates

def search_templates(query):
    """
    Searches templates by keywords
    
    Args:
        query: Search terms
    
    Returns:
        List of matching templates
    """
    # Convert query to lowercase for case-insensitive search
    query = query.lower()
    terms = query.split()
    
    index = load_template_index()
    templates = []
    
    for template_id, template_info in index["templates"].items():
        # Check if any term matches in name, description or tags
        name = template_info["name"].lower()
        description = template_info["description"].lower()
        tags = [tag.lower() for tag in template_info["tags"]]
        
        for term in terms:
            if (term in name or term in description or any(term in tag for tag in tags)):
                # Add template to results
                template_info["id"] = template_id
                templates.append(template_info)
                break
    
    return templates

def get_template_categories():
    """Returns a list of all used template categories"""
    index = load_template_index()
    categories = set()
    
    for template_info in index["templates"].values():
        categories.add(template_info["category"])
    
    return sorted(list(categories))

def get_template_tags():
    """Returns a list of all used template tags"""
    index = load_template_index()
    tags = set()
    
    for template_info in index["templates"].values():
        tags.update(template_info["tags"])
    
    return sorted(list(tags))

def format_template_list(templates):
    """Formats a list of templates for display"""
    if not templates:
        return "No templates found."
    
    result = []
    for i, template in enumerate(templates, 1):
        result.append(f"{i}. {template['name']}")
        result.append(f"   ID: {template['id']}")
        result.append(f"   Description: {template['description']}")
        result.append(f"   Category: {template['category']}")
        result.append(f"   Tags: {', '.join(template['tags'])}")
        result.append(f"   Created: {template['created']}")
        result.append("")
    
    return "\n".join(result)

if __name__ == "__main__":
    # Create sample templates if index is empty
    ensure_templates_dir()
    index = load_template_index()
    
    if len(index["templates"]) == 0:
        print("Creating sample templates...")
        
        # Sample creative writing template
        creative_template = {
            "name": "Creative Story Prompt",
            "description": "A template for generating creative short stories",
            "category": "creative",
            "original_prompt": "Write a short story",
            "optimized_prompt": "Write a 500-word short story with a surprising twist ending. Include a protagonist facing an unexpected challenge, and set the story in an unusual location. Use vivid sensory details and include at least one memorable piece of dialogue. The story should evoke a specific emotion (joy, fear, wonder, etc.) and conclude with a satisfying but unexpected resolution.",
            "tags": ["writing", "creative", "story"]
        }
        save_template(creative_template)
        
        # Sample technical template
        technical_template = {
            "name": "Python Function Template",
            "description": "A template for requesting Python function implementations",
            "category": "development",
            "original_prompt": "Write a Python function",
            "optimized_prompt": "Write a Python function that solves the following problem: [PROBLEM DESCRIPTION]. The function should:\n- Take these parameters: [PARAMETER DESCRIPTIONS]\n- Return: [RETURN VALUE DESCRIPTION]\n- Handle these edge cases: [EDGE CASES]\n- Have a time complexity of: [DESIRED COMPLEXITY]\n\nInclude docstrings following PEP 257 conventions, type hints, and at least 3 example test cases showing the function in use.",
            "tags": ["python", "coding", "function"]
        }
        save_template(technical_template)
        
        print("Sample templates created!")
    
    # Display all templates
    templates = list_templates()
    print("\nAvailable Templates:")
    print(format_template_list(templates))