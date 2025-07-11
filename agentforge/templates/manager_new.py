"""
Simple template manager to replace the problematic one
"""

import os
import yaml
import json
from datetime import datetime

# Constants
TEMPLATES_DIR = "templates"
TEMPLATES_INDEX_FILE = os.path.join(TEMPLATES_DIR, "index.yaml")

class TemplateManager:
    """Simple template manager without recursion issues"""
    
    def __init__(self):
        self.ensure_dir()
    
    def ensure_dir(self):
        """Ensure templates directory exists"""
        if not os.path.exists(TEMPLATES_DIR):
            os.makedirs(TEMPLATES_DIR)
        
        if not os.path.exists(TEMPLATES_INDEX_FILE):
            self.create_index()
    
    def create_index(self):
        """Create empty index file"""
        index = {
            "templates": {},
            "metadata": {
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "count": 0
            }
        }
        with open(TEMPLATES_INDEX_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(index, f)
    
    def load_index(self):
        """Load template index"""
        if not os.path.exists(TEMPLATES_INDEX_FILE):
            self.create_index()
        
        with open(TEMPLATES_INDEX_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def save_index(self, index):
        """Save template index"""
        index["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        index["metadata"]["count"] = len(index["templates"])
        
        with open(TEMPLATES_INDEX_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(index, f)
    
    def list_templates(self, category=None, tag=None):
        """List templates with optional filtering"""
        index = self.load_index()
        templates = []
        
        for template_id, template_info in index["templates"].items():
            if category and template_info.get("category") != category:
                continue
            if tag and tag not in template_info.get("tags", []):
                continue
            
            template_info["id"] = template_id
            templates.append(template_info)
        
        return templates

# Create singleton instance
_manager = TemplateManager()

# Export functions for compatibility
def list_templates(category=None, tag=None):
    """List templates"""
    return _manager.list_templates(category, tag)

def format_template_list(templates):
    """Format template list for display"""
    if not templates:
        return "No templates found."
    
    result = []
    for template in templates:
        result.append(f"ID: {template['id']}")
        result.append(f"Name: {template.get('name', 'Unknown')}")
        result.append(f"Category: {template.get('category', 'Unknown')}")
        result.append(f"Description: {template.get('description', 'No description')}")
        result.append("-" * 40)
    
    return "\n".join(result)

def get_template_categories():
    """Get all template categories"""
    templates = list_templates()
    categories = set()
    for template in templates:
        categories.add(template.get('category', 'Unknown'))
    return list(categories)

def get_template_tags():
    """Get all template tags"""
    templates = list_templates()
    tags = set()
    for template in templates:
        for tag in template.get('tags', []):
            tags.add(tag)
    return list(tags)

def search_templates(query):
    """Search templates by query"""
    templates = list_templates()
    results = []
    query_lower = query.lower()
    
    for template in templates:
        if (query_lower in template.get('name', '').lower() or
            query_lower in template.get('description', '').lower()):
            results.append(template)
    
    return results

def load_template(template_id):
    """Load a template by ID"""
    template_file = os.path.join(TEMPLATES_DIR, f"{template_id}.json")
    if os.path.exists(template_file):
        with open(template_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_template(template_data):
    """Save a template"""
    import uuid
    import json
    
    # Generate unique ID
    template_id = str(uuid.uuid4())[:8]
    
    # Add metadata
    template_data["created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template_data["id"] = template_id
    
    # Save template file
    template_file = os.path.join(TEMPLATES_DIR, f"{template_id}.json")
    with open(template_file, 'w', encoding='utf-8') as f:
        json.dump(template_data, f, indent=2, ensure_ascii=False)
    
    # Update index
    index = _manager.load_index()
    index["templates"][template_id] = {
        "name": template_data.get("name", "Unknown"),
        "description": template_data.get("description", ""),
        "category": template_data.get("category", "general"),
        "tags": template_data.get("tags", []),
        "created": template_data["created"]
    }
    _manager.save_index(index)
    
    return template_id

def delete_template(template_id):
    """Delete a template"""
    template_file = os.path.join(TEMPLATES_DIR, f"{template_id}.json")
    if os.path.exists(template_file):
        os.remove(template_file)
        
        # Update index
        index = _manager.load_index()
        if template_id in index["templates"]:
            del index["templates"][template_id]
            _manager.save_index(index)
            return True
    return False
