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

def display_menu():
    """Spausdina vartotojo meniu."""
    print("\n" + "="*50)
    print("== AgentForge Valdymo Meniu ==")
    print("="*50)
    print("1. Vykdyti Palaikymo Ciklą (atnaujinti žinių bazę)")
    print("2. Vykdyti Užklausos Optimizavimą (pagrindinė funkcija)")
    print("0. Išeiti")
    print("="*50)

def main():
    """Pagrindinė programos funkcija su begaliniu meniu ciklu."""
    while True:
        display_menu()
        choice = input("Pasirinkite veiksmą (Įveskite skaičių): ")

        if choice == '1':
            run_maintenance_cycle()
        elif choice == '2':
            user_prompt = input("Įveskite užklausą (prompt), kurią norite optimizuoti: ")
            if user_prompt:
                run_execution_cycle(user_prompt)
            else:
                print("Klaida: Užklausa negali būti tuščia.")
        elif choice == '0':
            print("Programa baigia darbą. Iki greito!")
            break
        else:
            print("Klaida: Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main()