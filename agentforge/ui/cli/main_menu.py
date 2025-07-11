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
from ...workflows.maintenance import run_maintenance_cycle
from ...workflows.execution import run_execution_cycle
import traceback

def display_menu():
    """Spausdina vartotojo meniu."""
    print("\n" + "="*50)
    print("== AgentForge Valdymo Meniu ==")
    print("="*50)
    print("1. Vykdyti Palaikymo Ciklą (atnaujinti žinių bazę)")
    print("2. Vykdyti Užklausos Optimizavimą (pagrindinė funkcija)")
    print("3. Paleisti sistemos testus")
    print("4. Kategorijų ir agentų valdymo sistema")
    print("5. Prompt'ų šablonų valdymo sistema") # Naujas meniu punktas
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

def display_templates_menu():
    """Spausdina šablonų valdymo submeniu."""
    print("\n" + "="*50)
    print("== Prompt'ų Šablonų Valdymo Sistema ==")
    print("="*50)
    print("1. Peržiūrėti visus šablonus")
    print("2. Ieškoti šablonų")
    print("3. Peržiūrėti šabloną")
    print("4. Sukurti naują šabloną")
    print("5. Ištrinti šabloną")
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
                from ...categories.manager import list_all_categories
                print("\n=== Visos kategorijos ir subkategorijos ===")
                print(list_all_categories())
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '2':
                # Testuoti užklausos kategorizavimą
                test_prompt = input("\nĮveskite tekstą kategorizavimui: ")
                if test_prompt:
                    from ...categories.classifier import get_query_category, print_classification_result
                    result = get_query_category(test_prompt)
                    print_classification_result(result)
                else:
                    print("Klaida: Tekstas negali būti tuščias.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '3':
                # Peržiūrėti agentų įgūdžius
                from ...agents.skills import load_agent_skills
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
                    from ...agents.dynamic_selection import get_dynamic_crew_for_category
                    # print_dynamic_agents_info function not implemented, adding basic output
                    agents = get_dynamic_crew_for_category(test_category)
                    print(f"\n=== Dynamically selected agents for category '{test_category}' ===")
                    for agent in agents:
                        print(f"- {agent}")
                    print("=====================================")
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

def run_templates_system():
    """Vykdo šablonų valdymo submeniu."""
    while True:
        try:
            display_templates_menu()
            choice = input("Pasirinkite veiksmą (Įveskite skaičių): ")

            if choice == '1':
                # Peržiūrėti visus šablonus
                from ...templates.manager import list_templates, format_template_list
                
                # Filtravimo pasirinkimai
                print("\n=== Filtravimo parinktys ===")
                print("1. Visi šablonai")
                print("2. Filtruoti pagal kategoriją")
                print("3. Filtruoti pagal žymę (tag)")
                filter_choice = input("Pasirinkite filtravimą (1-3): ")
                
                if filter_choice == '2':
                    from ...templates.manager import get_template_categories
                    categories = get_template_categories()
                    print("\nGalimos kategorijos:", ", ".join(categories))
                    category = input("Įveskite kategoriją: ")
                    templates = list_templates(category=category)
                elif filter_choice == '3':
                    from ...templates.manager import get_template_tags
                    tags = get_template_tags()
                    print("\nGalimos žymės:", ", ".join(tags))
                    tag = input("Įveskite žymę: ")
                    templates = list_templates(tag=tag)
                else:
                    templates = list_templates()
                
                print("\n=== Prompt'ų šablonai ===")
                print(format_template_list(templates))
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '2':
                # Ieškoti šablonų
                from ...templates.manager import search_templates, format_template_list
                search_query = input("\nĮveskite paieškos žodžius: ")
                if search_query:
                    templates = search_templates(search_query)
                    print("\n=== Paieškos rezultatai ===")
                    print(format_template_list(templates))
                else:
                    print("Klaida: Paieškos užklausa negali būti tuščia.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '3':
                # Peržiūrėti šabloną
                from ...templates.manager import load_template
                template_id = input("\nĮveskite šablono ID: ")
                if template_id:
                    template = load_template(template_id)
                    if template:
                        print("\n=== Šablono informacija ===")
                        print(f"Pavadinimas: {template['name']}")
                        print(f"Aprašymas: {template['description']}")
                        print(f"Kategorija: {template['category']}")
                        print(f"Žymės: {', '.join(template['tags'])}")
                        print(f"Sukurtas: {template['created']}")
                        print("\nOriginali užklausa:")
                        print("-" * 40)
                        print(template['original_prompt'])
                        print("-" * 40)
                        print("\nOptimizuota užklausa:")
                        print("-" * 40)
                        print(template['optimized_prompt'])
                        print("-" * 40)
                        
                        # Galimybė naudoti šabloną
                        use_choice = input("\nAr norite naudoti šį šabloną užklausos optimizavimui? (y/n): ")
                        if use_choice.lower() in ['y', 'yes', 'taip']:
                            user_input = input("\nĮveskite parametrus, kuriuos norite pakeisti šablone (palikite tuščią, jei norite naudoti originalą): ")
                            from ...workflows.execution import run_execution_cycle
                            prompt_to_use = template['optimized_prompt']
                            if user_input:
                                # Čia galima būtų pridėti parametrų pakeitimo logiką
                                prompt_to_use = prompt_to_use.replace("[PARAMETER]", user_input)
                            run_execution_cycle(prompt_to_use)
                    else:
                        print(f"Klaida: Šablonas su ID '{template_id}' nerastas.")
                else:
                    print("Klaida: ID negali būti tuščias.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '4':
                # Sukurti naują šabloną
                from ...templates.manager import save_template
                print("\n=== Naujo šablono kūrimas ===")
                name = input("Įveskite šablono pavadinimą: ")
                description = input("Įveskite šablono aprašymą: ")
                category = input("Įveskite kategoriją: ")
                tags_input = input("Įveskite žymes (atskirtas kableliais): ")
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                original_prompt = input("Įveskite originalią užklausą: ")
                optimized_prompt = input("Įveskite optimizuotą užklausą: ")
                
                if name and description and category and original_prompt and optimized_prompt:
                    template_data = {
                        "name": name,
                        "description": description,
                        "category": category,
                        "original_prompt": original_prompt,
                        "optimized_prompt": optimized_prompt,
                        "tags": tags
                    }
                    template_id = save_template(template_data)
                    print(f"\nŠablonas sukurtas sėkmingai! ID: {template_id}")
                else:
                    print("Klaida: Visi laukai, išskyrus žymes, yra privalomi.")
                input("\nSpauskite ENTER, kad tęstumėte...")

            elif choice == '5':
                # Ištrinti šabloną
                from ...templates.manager import delete_template
                template_id = input("\nĮveskite trinamojo šablono ID: ")
                if template_id:
                    confirm = input(f"Ar tikrai norite ištrinti šabloną {template_id}? (y/n): ")
                    if confirm.lower() in ['y', 'yes', 'taip']:
                        success = delete_template(template_id)
                        if success:
                            print(f"Šablonas {template_id} sėkmingai ištrintas.")
                        else:
                            print(f"Klaida: Šablonas su ID '{template_id}' nerastas.")
                else:
                    print("Klaida: ID negali būti tuščias.")
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
                try:
                    import sys
                    sys.path.append('.')
                    from tests.integration.test_full_workflow import run_tests
                    
                    # Paleidžiame testus
                    success = run_tests()
                    
                    if success:
                        print("\n✅ Visi testai praeiti sėkmingai!")
                    else:
                        print("\n❌ Kai kurie testai nepraėjo.")
                except Exception as e:
                    print(f"Klaida paleidžiant testus: {e}")
                    print("Testų sistema bus patobulinta ateityje.")
            elif choice == '4':
                # Kategorijų ir agentų valdymo sistema
                run_category_system()
            elif choice == '5':
                # Prompt'ų šablonų valdymo sistema
                run_templates_system()
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