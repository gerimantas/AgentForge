# /AgentForge/main.py

"""
Pagrindinis AgentForge projekto paleidimo failas (Orkestratorius).

Šis scenarijus veikia kaip valdymo centras, leidžiantis vartotojui
pasirinkti, kurią operaciją atlikti:
1. Atnaujinti vidinę žinių bazę (Palaikymo Ciklas).
2. Optimizuoti konkrečią vartotojo užklausą (Vykdymo Ciklas).
3. Paleisti sistemos testus.
4. Valdyti kategorijų ir agentų sistemą.
"""

# Importuojame funkcijas iš mūsų ciklų modulių
from maintenance_cycle import run_maintenance_cycle
from execution_cycle import run_execution_cycle
import traceback

def display_menu():
    """Spausdina vartotojo meniu."""
    print("\n" + "="*50)
    print("== AgentForge Valdymo Meniu ==")
    print("="*50)
    print("1. Vykdyti Palaikymo Ciklą (atnaujinti žinių bazę)")
    print("2. Vykdyti Užklausos Optimizavimą (pagrindinė funkcija)")
    print("3. Paleisti sistemos testus")
    print("4. Kategorijų ir agentų valdymo sistema") # Naujas meniu punktas
    print("0. Išeiti")
    print("="*50)

def display_category_menu():
    """Spausdina kategorijų valdymo submeniu."""
    print("\n" + "="*50)
    print("== Kategorijų ir Agentų Valdymo Sistema ==")
    print("="*50)
    print("1. Peržiūrėti visas kategorijas")
    print("2. Testuoti užklausos kategorizavimą")
    print("3. Peržiūrėti agentų įgūdžius")
    print("4. Testuoti dinaminių agentų parinkimą")
    print("0. Grįžti į pagrindinį meniu")
    print("="*50)

def run_category_system():
    """Vykdo kategorijų valdymo submeniu."""
    while True:
        try:
            display_category_menu()
            choice = input("Pasirinkite veiksmą (Įveskite skaičių): ")

            if choice == '1':
                # Peržiūrėti visas kategorijas
                from categories import list_all_categories
                print("\n=== Visos kategorijos ir subkategorijos ===")
                print(list_all_categories())
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '2':
                # Testuoti užklausos kategorizavimą
                test_prompt = input("\nĮveskite tekstą kategorizavimui: ")
                if test_prompt:
                    from category_classifier import get_query_category, print_classification_result
                    result = get_query_category(test_prompt)
                    print_classification_result(result)
                else:
                    print("Klaida: Tekstas negali būti tuščias.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '3':
                # Peržiūrėti agentų įgūdžius
                from agent_skills import load_agent_skills
                skills = load_agent_skills()
                print("\n=== Agentų įgūdžiai ===")
                for agent_id, agent_data in skills["agents"].items():
                    print(f"\n{agent_data['name']} ({agent_id}):")
                    print(f"  Aprašymas: {agent_data['description']}")
                    print("  Įgūdžiai:")
                    for category, level in agent_data['skills'].items():
                        print(f"    - {category}: {level}/5")
                    print("  Specializacijos: " + ", ".join(agent_data['specialties']))
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '4':
                # Testuoti dinaminių agentų parinkimą
                test_category = input("\nĮveskite kategoriją (information_retrieval, creative_content, analysis, development): ")
                if test_category:
                    from dynamic_agents import get_dynamic_crew_for_category, print_dynamic_agents_info
                    agents = get_dynamic_crew_for_category(test_category)
                    print_dynamic_agents_info(agents)
                else:
                    print("Klaida: Kategorija negali būti tuščia.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '0':
                # Grįžti į pagrindinį meniu
                return
            else:
                print("Klaida: Neteisingas pasirinkimas. Bandykite dar kartą.")
        except Exception as e:
            print(f"Įvyko netikėta klaida: {e}")
            print("===== Klaidos detalės: =====")
            traceback.print_exc()
            print("===========================")
            input("\nSpauskite ENTER, kad tęstumėte...")

def main():
    """Pagrindinė programos funkcija su begaliniu meniu ciklu."""
    while True:
        try:
            display_menu()
            choice = input("Pasirinkite veiksmą (Įveskite skaičių): ")

            if choice == '1':
                run_maintenance_cycle()
            elif choice == '2':
                user_prompt = input("Įveskite užklausą (prompt), kurią norite optimizuoti: ")
                if user_prompt:
                    try:
                        run_execution_cycle(user_prompt)
                    except Exception as e:
                        print(f"Klaida vykdant užklausos optimizavimą: {e}")
                        print("===== Klaidos detalės: =====")
                        traceback.print_exc()
                        print("===========================")
                else:
                    print("Klaida: Užklausa negali būti tuščia.")
            elif choice == '3':
                # Paleidžiame testavimo modulį
                print("Paleidžiami sistemos testai...")
                from test_system import run_tests, clean_old_logs
                
                # Išvalyti senus žurnalus prieš testų paleidimą
                clean_old_logs()
                
                # Paleisti testus - jie patys paklaus apie išsaugojimą kai bus įvykdyti
                success = run_tests()
                
                if success:
                    print("\nVisi testai sėkmingai įvykdyti!")
                else:
                    print("\nKai kurie testai nepavyko. Rezultatai išsaugoti test_results/test_results.log faile.")
            elif choice == '4':
                # Kategorijų ir agentų valdymo sistema
                run_category_system()
            elif choice == '0':
                print("Programa baigia darbą. Iki greito!")
                break
            else:
                print("Klaida: Neteisingas pasirinkimas. Bandykite dar kartą.")
        except Exception as e:
            print(f"Įvyko netikėta klaida: {e}")
            print("===== Klaidos detalės: =====")
            traceback.print_exc()
            print("===========================")
            print("Programa tęsia darbą...")

if __name__ == "__main__":
    main()