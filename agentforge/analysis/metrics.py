# /AgentForge/prompt_metrics.py

"""
Prompt'ų kokybės vertinimo metrikos modulis.
Apibrėžia ir skaičiuoja įvairias prompt'ų kokybės metrikas.
"""

import re
import string

def count_words(text):
    """Counts the number of words in a text"""
    if not text:
        return 0
    
    # Įsitikiname, kad turime tekstinę eilutę
    if not isinstance(text, str):
        try:
            text = str(text)
        except:
            return 0
    
    return len(text.split())

def analyze_clarity(prompt):
    """
    Analyzes the clarity of a prompt
    
    Metrics considered:
    - Presence of clear instructions
    - Average sentence length (shorter is often clearer)
    - Use of technical jargon
    - Presence of ambiguous terms
    
    Returns:
        Score from 0-100
    """
    if not prompt:
        return 0
    
    score = 70  # Start with a base score
    
    # Check for instruction keywords
    instruction_keywords = ["create", "write", "analyze", "explain", "describe", 
                          "summarize", "find", "list", "compare", "evaluate"]
    if any(keyword in prompt.lower() for keyword in instruction_keywords):
        score += 10
    
    # Check sentence length
    sentences = re.split(r'[.!?]+', prompt)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if sentences:
        avg_length = sum(len(s.split()) for s in sentences) / len(sentences)
        if avg_length < 15:  # Short sentences are clearer
            score += 10
        elif avg_length > 25:  # Long sentences reduce clarity
            score -= 10
    
    # Check for ambiguous terms
    ambiguous_terms = ["maybe", "perhaps", "somehow", "something", "sometime", 
                      "some", "several", "various", "different", "certain"]
    ambiguity_count = sum(1 for term in ambiguous_terms if term in prompt.lower().split())
    score -= ambiguity_count * 5
    
    # Ensure the score is within 0-100 range
    return max(0, min(100, score))

def analyze_specificity(prompt):
    """
    Analyzes the specificity of a prompt
    
    Metrics considered:
    - Presence of specific numbers, dates, names
    - Use of specific vs. general terms
    - Level of detail
    
    Returns:
        Score from 0-100
    """
    if not prompt:
        return 0
    
    score = 50  # Start with a base score
    
    # Check for specific quantities/numbers
    number_pattern = r'\d+'
    specifics_count = len(re.findall(number_pattern, prompt))
    score += specifics_count * 5
    
    # Check for specific formatting instructions
    format_patterns = ["format", "structure", "layout", "style", "organize"]
    if any(pattern in prompt.lower() for pattern in format_patterns):
        score += 10
    
    # Check for detailed requirements
    detail_patterns = ["specific", "exactly", "precisely", "in detail", "step by step"]
    detail_count = sum(1 for pattern in detail_patterns if pattern in prompt.lower())
    score += detail_count * 5
    
    # Check prompt length - more detailed prompts tend to be longer
    word_count = count_words(prompt)
    if word_count > 50:
        score += 10
    if word_count > 100:
        score += 5
    
    # Ensure the score is within 0-100 range
    return max(0, min(100, score))

def analyze_context(prompt):
    """
    Analyzes the context richness of a prompt
    
    Metrics considered:
    - Background information provided
    - Examples given
    - Constraints specified
    
    Returns:
        Score from 0-100
    """
    if not prompt:
        return 0
    
    score = 50  # Start with a base score
    
    # Check for background information
    background_patterns = ["background", "context", "previously", "history", "situation"]
    if any(pattern in prompt.lower() for pattern in background_patterns):
        score += 15
    
    # Check for examples
    example_patterns = ["example", "instance", "such as", "for instance", "like this"]
    if any(pattern in prompt.lower() for pattern in example_patterns):
        score += 15
    
    # Check for constraints or limitations
    constraint_patterns = ["constraint", "limitation", "restriction", "must", "should", "only"]
    constraint_count = sum(1 for pattern in constraint_patterns if pattern in prompt.lower().split())
    score += constraint_count * 5
    
    # Check for formatting with sections/paragraphs
    if prompt.count('\n') > 2:  # Has multiple paragraphs
        score += 10
    
    # Ensure the score is within 0-100 range
    return max(0, min(100, score))

def analyze_structure(prompt):
    """
    Analyzes the structure of a prompt
    
    Metrics considered:
    - Organization into sections
    - Use of bullet points or numbering
    - Clear beginning, middle, end
    
    Returns:
        Score from 0-100
    """
    if not prompt:
        return 0
    
    score = 50  # Start with a base score
    
    # Check for section headers
    section_pattern = r'\n[A-Z][A-Za-z\s]+:'
    section_count = len(re.findall(section_pattern, prompt))
    score += section_count * 5
    
    # Check for bullet points or numbered lists
    bullet_pattern = r'\n\s*[-*•]\s+'
    bullet_count = len(re.findall(bullet_pattern, prompt))
    
    numbered_pattern = r'\n\s*\d+\.\s+'
    numbered_count = len(re.findall(numbered_pattern, prompt))
    
    list_count = bullet_count + numbered_count
    score += list_count * 5
    
    # Check for delimiters
    delimiter_patterns = ["###", "---", "===", "```", "***"]
    delimiter_count = sum(prompt.count(delim) for delim in delimiter_patterns)
    score += delimiter_count * 5
    
    # Check for organization markers
    org_markers = ["first", "second", "third", "finally", "next", "then", "lastly", "in conclusion"]
    marker_count = sum(1 for marker in org_markers if marker in prompt.lower().split())
    score += marker_count * 3
    
    # Ensure the score is within 0-100 range
    return max(0, min(100, score))

def analyze_outcome_clarity(prompt):
    """
    Analyzes how clearly the expected outcome is defined
    
    Metrics considered:
    - Explicit statement of expected output
    - Format specifications
    - Success criteria
    
    Returns:
        Score from 0-100
    """
    if not prompt:
        return 0
    
    score = 40  # Start with a base score
    
    # Check for output specification
    output_patterns = ["output", "result", "produce", "create", "generate", "I want", "I need"]
    if any(pattern in prompt.lower() for pattern in output_patterns):
        score += 15
    
    # Check for format specifications
    format_patterns = ["format", "style", "length", "structure", "words", "paragraphs"]
    format_count = sum(1 for pattern in format_patterns if pattern in prompt.lower().split())
    score += format_count * 5
    
    # Check for success criteria
    criteria_patterns = ["criteria", "requirements", "must include", "should contain", "expected"]
    if any(pattern in prompt.lower() for pattern in criteria_patterns):
        score += 15
    
    # Check for examples of expected output
    if "example output" in prompt.lower() or "sample output" in prompt.lower():
        score += 15
    
    # Ensure the score is within 0-100 range
    return max(0, min(100, score))

def evaluate_prompt(prompt):
    """
    Evaluates a prompt using all metrics
    
    Args:
        prompt: The prompt text to evaluate
        
    Returns:
        Dictionary with scores for each metric and overall score
    """
    # Konvertuojame į tekstą, jei gautas kitokio tipo objektas
    if not isinstance(prompt, str):
        try:
            prompt = str(prompt)
        except:
            prompt = ""
    
    if not prompt or not prompt.strip():
        return {
            "clarity": 0,
            "specificity": 0,
            "context": 0,
            "structure": 0,
            "outcome_clarity": 0,
            "overall": 0,
            "word_count": 0
        }
    
    # Calculate each metric
    clarity = analyze_clarity(prompt)
    specificity = analyze_specificity(prompt)
    context = analyze_context(prompt)
    structure = analyze_structure(prompt)
    outcome = analyze_outcome_clarity(prompt)
    
    # Calculate overall score (weighted average)
    weights = {
        "clarity": 0.25,
        "specificity": 0.2,
        "context": 0.2,
        "structure": 0.15,
        "outcome_clarity": 0.2
    }
    
    overall = (
        clarity * weights["clarity"] +
        specificity * weights["specificity"] +
        context * weights["context"] +
        structure * weights["structure"] +
        outcome * weights["outcome_clarity"]
    )
    
    return {
        "clarity": clarity,
        "specificity": specificity,
        "context": context,
        "structure": structure,
        "outcome_clarity": outcome,
        "overall": overall,
        "word_count": count_words(prompt)
    }

def print_evaluation_result(result):
    """Prints the evaluation result in a readable format with visual bars"""
    print("\n===== Prompt Quality Evaluation =====")
    
    metrics = [
        ("Clarity", result["clarity"]),
        ("Specificity", result["specificity"]),
        ("Context", result["context"]),
        ("Structure", result["structure"]),
        ("Outcome Clarity", result["outcome_clarity"]),
        ("OVERALL", result["overall"])
    ]
    
    for name, score in metrics:
        bar_length = int(score / 5)  # 20 characters for 100%
        bar = "█" * bar_length
        print(f"{name.ljust(15)}: {bar} {score:.1f}/100")
    
    print(f"\nWord Count: {result['word_count']}")
    print("===================================\n")

if __name__ == "__main__":
    # Test the evaluation with some example prompts
    test_prompts = [
        "Write something about dogs.",
        
        "Write a detailed blog post about the impact of artificial intelligence on healthcare. Include at least 3 examples of current applications, discuss potential future developments, and address concerns about data privacy. The post should be structured with clear headings and be approximately 1000 words long.",
        
        "Debug this Python function:\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n+1)"
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\nExample {i}:")
        result = evaluate_prompt(prompt)
        print_evaluation_result(result)