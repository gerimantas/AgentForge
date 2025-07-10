# /AgentForge/tasks_execution.py

from textwrap import dedent
from crewai import Task
from agents import prompt_analyst, prompt_critic, prompt_refiner
# Importuokite naujas funkcijas
from custom_tools import load_knowledge_base_tool

# --- EXECUTION CYCLE TASKS ---

# Task for the Prompt Analyst (lieka nepakitęs)
analysis_task = Task(
    description=dedent("""
        Analyze the following raw user prompt: '{raw_prompt}'.

        Your goal is to rewrite this prompt applying fundamental best practices.
        Specifically:
        1. Assign a clear role (persona) to the AI executor.
        2. Use delimiters (e.g., ###) to separate instructions from context.
        3. Refine the wording to eliminate any ambiguity.
        4. Specify a clear output format if one is implied.
    """),
    expected_output="A structured and improved version of the prompt.",
    agent=prompt_analyst
)

# Task for the Prompt Critic (lieka nepakitęs)
critique_task = Task(
    description=dedent("""
        Critically evaluate the structured prompt provided by the Analyst.
        First, check for any FACTUAL inaccuracies.
        Second, propose how to improve it using ADVANCED techniques.
        Would "Chain-of-Thought" reasoning be beneficial?
        What about "Few-shot" examples?
        Provide specific, actionable suggestions to elevate this prompt to an
        expert level. Refer to the rules in 'kanonine_sistema.md'.
    """),
    expected_output="""A numbered list of specific, actionable suggestions
    and critical notes.""",
    agent=prompt_critic,
    context=[analysis_task]
)

# Task for the Prompt Refiner (ATNAUJINTOS instrukcijos)
refinement_task = Task(
    description=dedent("""
        Merge the initial structured prompt (from the Analyst) with the
        suggestions from the Critic into a final, cohesive version. Your goal is
        not to simply copy-paste, but to elegantly integrate the Critic's
        advanced suggestions into the already structured prompt framework.
        The final result must be a complete, ready-to-execute prompt.

        IMPORTANT: Your final output MUST be ONLY the ready-to-use prompt text
        and nothing else. Do not add any conversational phrases, introductions,
        or explanations like 'Here is the final prompt:'.
    """),
    expected_output="""A single block of text representing the final,
    fully optimized prompt, ready to be copied and used directly. For example:
    'You are an expert shopping assistant. Your task is to find online stores in
    Lithuania that sell water pumps. Provide the answer as a Markdown table
    with columns: Store Name, URL, and a brief description.'""",
    agent=prompt_refiner,
    context=[analysis_task, critique_task]
)

# Funkcija, kuri priima user_prompt parametrą
def create_knowledge_analysis_task(raw_prompt):
    """Create a task that uses the knowledge base to analyze a user prompt.
    
    Args:
        raw_prompt: The original prompt from the user
        
    Returns:
        A Task object
    """
    return Task(
        description=f"""Analyze the user's prompt: '{raw_prompt}'.
        First, load the knowledge base using the Knowledge Base Loader tool to understand
        what techniques we have information about.
        Then, identify which prompt engineering techniques would be most relevant for optimizing
        this user's request. Consider the intent, complexity, and specific requirements.""",
        expected_output="""A clear analysis identifying:
        1. The user's primary intent or goal
        2. The 2-3 most relevant prompt engineering techniques from our knowledge base
        3. Justification for why these techniques would help optimize the prompt""",
        agent=prompt_analyst  # Naudojame esamą prompt_analyst vietoj nedefinuoto analyzer_agent
    )

# Užrašas, kad ši funkcija turi būti kviečiama su konkrečia užklausa
# Pavyzdys: 
# knowledge_analysis_task = create_knowledge_analysis_task("Padėk man parašyti CV")