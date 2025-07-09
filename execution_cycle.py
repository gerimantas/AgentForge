# /AgentForge/execution_cycle.py

# Importuojame 'config' modulį, kad galėtume pasiekti nustatymus
import config
from crewai import Crew, Process
from agents import prompt_analyst, prompt_critic, prompt_refiner
from tasks_execution import analysis_task, critique_task, refinement_task
from custom_tools import detect_language, translate_text_tool

def run_execution_cycle(user_prompt: str):
    """
    Funkcija, kuri sukuria ir paleidžia Vykdymo Ciklo komandą,
    o po to pasiūlo vertimą.
    """
    print("### Pradedamas Užklausos Optimizavimo Vykdymo Ciklas... ###")
    print("### Tai gali užtrukti kelias minutes... ###")
    
    original_lang = detect_language(user_prompt)
    print(f"--- Aptikta pradinė kalba: {original_lang} ---")

    prompt_engineering_crew = Crew(
      agents=[prompt_analyst, prompt_critic, prompt_refiner],
      tasks=[analysis_task, critique_task, refinement_task],
      process=Process.sequential,
      verbose=True,
      # PATAISYMAS ČIA: Naudojame reikšmę iš config.py failo
      max_iter=config.MAX_ITERATIONS
    )

    final_prompt_en = prompt_engineering_crew.kickoff(
        inputs={'raw_prompt': user_prompt}
    )

    # ... (likusi spausdinimo ir vertimo logika lieka nepakitusi) ...
    print("\n\n" + "="*50)
    print("|| Initial User Prompt:")
    print("="*50)
    print(user_prompt)

    print("\n\n" + "="*50)
    print("|| Final Optimized Prompt (in English):")
    print("="*50)
    print(final_prompt_en)
    print("="*50)

    if original_lang != 'en':
        while True:
            choice = input(f"\nAr išversti galutinę užklausą į pradinę kalbą ({original_lang})? (y/n): ").lower()
            if choice in ['y', 'yes']:
                print("--- Verčiama... Tai gali užtrukti minutėlę... ---")
                translated_prompt = translate_text_tool.run(
                    text_to_translate=final_prompt_en,
                    target_language=original_lang
                )
                
                print("\n\n" + "="*50)
                print(f"|| Išversta Užklausa ({original_lang}):")
                print("="*50)
                print(translated_prompt)
                print("="*50)
                break
            elif choice in ['n', 'no']:
                print("Vertimas atšauktas.")
                break
            else:
                print("Neteisingas pasirinkimas. Įveskite 'y' arba 'n'.")