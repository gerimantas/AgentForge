# /AgentForge/tasks_execution.py

from textwrap import dedent
from crewai import Task
from agents import prompt_analyst, prompt_critic, prompt_refiner

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

# === PATAISYMAS ČIA ===
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