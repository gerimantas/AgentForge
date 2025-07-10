# /AgentForge/main.py

"""
Pagrindinis AgentForge projekto paleidimo failas (Orkestratorius).

Šis scenarijus veikia kaip valdymo centras, leidžiantis vartotojui
pasirinkti, kurią operaciją atlikti:
1. Atnaujinti vidinę žinių bazę (Palaikymo Ciklas).
2. Optimizuoti konkrečią vartotojo užklausą (Vykdymo Ciklas).
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
    print("3. Paleisti sistemos testus") # Pridėta nauja meniu opcija
    print("0. Išeiti")
    print("="*50)

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