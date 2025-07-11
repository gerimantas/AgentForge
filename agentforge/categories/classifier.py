# /AgentForge/category_classifier.py

"""
Kategorijų klasifikavimo modulis.
Atpažįsta vartotojo užklausos kategoriją naudodamas zero-shot klasifikavimą.
"""

import os
import re
import json
from .manager import load_categories
from ..core import config

def extract_keywords(text):
    """
    Extracts keywords from the text to help with classification
    
    Args:
        text: The input text to analyze
        
    Returns:
        List of extracted keywords
    """
    # Basic keyword extraction - in real implementation, use NLP techniques
    # For now, just lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    
    # Remove common stop words
    stop_words = {"the", "a", "an", "and", "in", "on", "at", "to", "for", "with", "by", "about", "like"}
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    return keywords

def classify_zero_shot(query):
    """
    Classifies the query using zero-shot classification
    
    Args:
        query: The user query to classify
        
    Returns:
        Dictionary with main_category, subcategory and confidence scores
    """
    try:
        # In a production environment, use an actual API call to a language model
        # Here we use keyword-based classification as a placeholder
        categories = load_categories()
        keywords = extract_keywords(query)
        
        # Calculate match scores for each category and subcategory
        scores = {}
        
        for cat_id, category in categories["categories"].items():
            # Check main category keywords
            cat_score = sum(1 for kw in category["keywords"] if any(kw.lower() in keyword.lower() for keyword in keywords))
            
            # Check each subcategory
            subcat_scores = {}
            for subcat_id, subcategory in category["subcategories"].items():
                subcat_score = sum(1 for kw in subcategory["keywords"] if any(kw.lower() in keyword.lower() for keyword in keywords))
                subcat_scores[subcat_id] = subcat_score
            
            # Find the best subcategory
            if subcat_scores:
                best_subcat = max(subcat_scores.items(), key=lambda x: x[1])
                best_subcat_id = best_subcat[0]
                best_subcat_score = best_subcat[1]
            else:
                best_subcat_id = None
                best_subcat_score = 0
            
            # Add subcategory score to main category score
            total_score = cat_score + best_subcat_score
            scores[cat_id] = {
                "total_score": total_score,
                "cat_score": cat_score,
                "best_subcategory": best_subcat_id,
                "subcat_score": best_subcat_score
            }
        
        # Find the best category
        if scores:
            best_category = max(scores.items(), key=lambda x: x[1]["total_score"])
            best_cat_id = best_category[0]
            best_subcat_id = best_category[1]["best_subcategory"]
            
            result = {
                "main_category": best_cat_id,
                "main_category_name": categories["categories"][best_cat_id]["name"],
                "subcategory": best_subcat_id,
                "subcategory_name": categories["categories"][best_cat_id]["subcategories"][best_subcat_id]["name"] if best_subcat_id else None,
                "confidence": min(best_category[1]["total_score"] / 5 * 100, 100)  # Convert score to percentage
            }
            
            return result
        
        return {
            "main_category": "unknown",
            "subcategory": None,
            "confidence": 0
        }
            
    except Exception as e:
        print(f"Error in zero-shot classification: {e}")
        return {
            "main_category": "unknown",
            "subcategory": None,
            "confidence": 0
        }

def classify_with_language_model(query):
    """
    Uses a language model to classify the query
    
    This is a placeholder for actual implementation that would use
    OpenAI, Anthropic, or other LLM APIs to perform the classification
    """
    # In actual implementation, make an API call to the language model
    # For now, fall back to keyword-based classification
    return classify_zero_shot(query)

def get_query_category(query):
    """
    Main function to determine the category of a user query
    
    Args:
        query: The user query text
        
    Returns:
        Dictionary with classification results
    """
    # First try with language model if available
    if hasattr(config, 'OPENAI_API_KEY') and config.OPENAI_API_KEY:
        result = classify_with_language_model(query)
    else:
        # Fall back to keyword-based classification
        result = classify_zero_shot(query)
    
    # Add the original query for reference
    result["query"] = query
    return result

def print_classification_result(result):
    """Prints the classification result in a readable format"""
    print("\n===== Query Classification =====")
    print(f"Query: {result['query']}")
    print(f"Main Category: {result['main_category_name']} ({result['main_category']})")
    if result['subcategory']:
        print(f"Subcategory: {result['subcategory_name']} ({result['subcategory']})")
    print(f"Confidence: {result['confidence']:.1f}%")
    print("===============================\n")

if __name__ == "__main__":
    # Test the classification with some examples
    test_queries = [
        "Find information about quantum computing advances",
        "Write a short story about a robot discovering emotions",
        "Analyze this dataset of monthly sales figures",
        "Debug my Python function that keeps returning None"
    ]
    
    for query in test_queries:
        result = get_query_category(query)
        print_classification_result(result)