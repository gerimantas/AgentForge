# /AgentForge/execution_cycle.py

# Importuojame 'config' modulį, kad galėtume pasiekti nustatymus
import config
from crewai import Crew, Process, Agent, Task
from agents import prompt_analyst, prompt_critic, prompt_refiner
from tasks_execution import analysis_task, critique_task, refinement_task
from langdetect import detect

# Importuojame naujus kategorijų modulius
from category_classifier import get_query_category, print_classification_result
from dynamic_agents import get_dynamic_crew_for_category

def run_execution_cycle(user_prompt: str):
    """
    Funkcija, kuri sukuria ir paleidžia Vykdymo Ciklo komandą,
    o po to pasiūlo vertimą.
    """
    print("### Pradedamas Užklausos Optimizavimo Vykdymo Ciklas... ###")
    print("### Tai gali užtrukti kelias minutes... ###")
    
    # Naudojame tiesioginį langdetect.detect importą
    try:
        original_lang = detect(user_prompt)
        print(f"--- Aptikta pradinė kalba: {original_lang} ---")
    except Exception:
        original_lang = "en"
        print("--- Nepavyko aptikti kalbos, naudojama anglų kalba ---")

    # NAUJAS FUNKCIONALUMAS: Atpažįstame užklausos kategoriją
    use_dynamic_agents = False
    try:
        category_result = get_query_category(user_prompt)
        print_classification_result(category_result)
        
        # Paklausti vartotojo, ar naudoti dinaminius agentus
        if category_result["confidence"] > 60:  # Jei pakankamai užtikrinti dėl kategorijos
            choice = input(f"Ar naudoti specializuotus agentus kategorijai '{category_result['main_category_name']}'? (y/n): ").lower()
            use_dynamic_agents = choice in ["y", "yes", "taip"]
    except Exception as e:
        print(f"Klaida atpažįstant kategoriją: {e}")
        use_dynamic_agents = False

    # Tiesiogiai įrašome prompt į análitiko užduotį
    analysis_task.description = analysis_task.description.replace('{raw_prompt}', user_prompt)

    # NAUJAS FUNKCIONALUMAS: Dinamiškai parenkame agentus pagal kategoriją
    if use_dynamic_agents:
        try:
            print(f"\n--- Naudojami specializuoti agentai kategorijai: {category_result['main_category_name']} ---")
            dynamic_agents = get_dynamic_crew_for_category(category_result["main_category"])
            
            if dynamic_agents and len(dynamic_agents) >= 3:
                # Naudojame specializuotus agentus vietoj įprastų
                prompt_engineering_crew = Crew(
                    agents=dynamic_agents[:3],  # Imame pirmus tris specializuotus agentus
                    tasks=[analysis_task, critique_task, refinement_task],
                    process=Process.sequential,
                    verbose=config.VERBOSE,
                    max_iterations=config.MAX_ITERATIONS
                )
            else:
                raise ValueError("Nepakankamas specializuotų agentų skaičius")
        except Exception as e:
            print(f"Nepavyko sukurti specializuotų agentų: {e}")
            print("--- Naudojami standartiniai agentai ---")
            use_dynamic_agents = False

    # Jei nenaudojame dinaminių agentų, naudojame standartinius
    if not use_dynamic_agents:
        prompt_engineering_crew = Crew(
          agents=[prompt_analyst, prompt_critic, prompt_refiner],
          tasks=[analysis_task, critique_task, refinement_task],
          process=Process.sequential,
          verbose=config.VERBOSE,
          max_iterations=config.MAX_ITERATIONS
        )

    try:
        final_prompt_en = prompt_engineering_crew.kickoff()
    except Exception as e:
        print(f"Klaida vykdant užklausos optimizavimą: {e}")
        final_prompt_en = f"Nepavyko optimizuoti užklausos. Klaida: {e}. Originali užklausa: {user_prompt}"
    
    print("\n\n" + "="*50)
    print("|| Initial User Prompt:")
    print("="*50)
    print(user_prompt)

    print("\n\n" + "="*50)
    print("|| Final Optimized Prompt (in English):")
    print("="*50)
    print(final_prompt_en)
    print("="*50)

    # NAUJAS FUNKCIONALUMAS: Analizuojame prompt'o kokybę
    try:
        from prompt_metrics import evaluate_prompt, print_evaluation_result
        evaluation_result = evaluate_prompt(final_prompt_en)
        print_evaluation_result(evaluation_result)
    except Exception as e:
        print(f"Nepavyko atlikti prompt'o kokybės vertinimo: {e}")

    if original_lang != 'en':
        while True:
            choice = input(f"\nAr išversti galutinę užklausą į pradinę kalbą ({original_lang})? (y/n): ").lower()
            if choice in ['y', 'yes']:
                print("--- Verčiama... Tai gali užtrukti minutėlę... ---")
                try:
                    # PATAISYMAS: Naudojame jau importuotus objektus, ne lokalius
                    translator_agent = Agent(
                        role="Professional Translator",
                        goal=f"Translate the English text into {original_lang}",
                        backstory="You are an expert translator with deep knowledge of both languages",
                        verbose=False
                    )
                    
                    translation_task = Task(
                        description=f"Translate this text into {original_lang}:\n\n{final_prompt_en}",
                        expected_output="The translated text with no additional comments",
                        agent=translator_agent
                    )
                    
                    translator_crew = Crew(
                        agents=[translator_agent],
                        tasks=[translation_task],
                        verbose=False
                    )
                    
                    translated_prompt = translator_crew.kickoff()
                    
                    print("\n\n" + "="*50)
                    print(f"|| Išversta Užklausa ({original_lang}):")
                    print("="*50)
                    print(translated_prompt)
                    print("="*50)
                except Exception as e:
                    print(f"Klaida verčiant tekstą: {e}")
                break
            elif choice in ['n', 'no']:
                print("Vertimas atšauktas.")
                break
            else:
                print("Neteisingas pasirinkimas. Įveskite 'y' arba 'n'.")