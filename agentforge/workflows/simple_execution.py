"""
AgentForge Simplified Execution Cycle
====================================

Simplified execution cycle implementation for Stage 2 testing.
"""

import sys
from typing import Optional

def run_execution_cycle(query: str, verbose: bool = True) -> Optional[str]:
    """
    Simplified execution cycle for Stage 2.
    
    Args:
        query: Vartotojo užklausa
        verbose: Ar rodyti detalią informaciją
        
    Returns:
        Optimizuotas prompt'as arba None jei klaida
    """
    try:
        if verbose:
            print(f"\\n🚀 Simplified execution cycle started")
            print(f"📝 Query: {query}")
            print("-" * 50)
        
        # Stage 2: Simplified processing
        # Step 1: Analysis
        if verbose:
            print("📊 Step 1: Analyzing query...")
        
        analyzed_query = f"[ANALYZED] {query}"
        
        # Step 2: Criticism
        if verbose:
            print("🔍 Step 2: Applying criticism...")
        
        criticized_query = f"[IMPROVED] {analyzed_query}"
        
        # Step 3: Refinement
        if verbose:
            print("✨ Step 3: Refining result...")
        
        final_result = f"[OPTIMIZED] {criticized_query}\\n\\nOptimization suggestions:\\n- Make the query more specific\\n- Add context for better results\\n- Consider the target audience"
        
        if verbose:
            print("✅ Execution cycle completed successfully!")
            print(f"📊 Result:")
            print("-" * 50)
            print(final_result)
        
        return final_result
        
    except Exception as e:
        print(f"❌ Error in execution cycle: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return None

def test_execution_cycle():
    """
    Test function for execution cycle.
    """
    print("\\n🧪 Testing execution cycle...")
    
    test_query = "How to create a good prompt for AI?"
    result = run_execution_cycle(test_query, verbose=True)
    
    if result:
        print(f"\\n✅ Test successful!")
        return True
    else:
        print("\\n❌ Test failed!")
        return False

if __name__ == "__main__":
    test_execution_cycle()
