#!/usr/bin/env python3
"""
AgentForge - Entry Point
========================

Pagrindinis AgentForge sistemos paleidimo taškas.
Po struktūros pertvarkymo šis failas importuoja main() funkciją iš agentforge paketo.
"""

import sys
import os

# Pridėti project root į Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def main():
    """Pagrindinis paleidimo taškas."""
    try:
        print("AgentForge paleidimas...")
        print(f"Python executable: {sys.executable}")
        print(f"Project root: {project_root}")
        
        # Patikrinti ar .env failas egzistuoja
        env_path = os.path.join(project_root, '.env')
        if os.path.exists(env_path):
            print("✓ .env failas rastas")
        else:
            print("⚠ .env failas nerastas")
        
        # Pasirinkti sąsają: CLI arba GUI
        print("\n" + "="*50)
        print("== AgentForge Sąsajos Pasirinkimas ==")
        print("="*50)
        print("1. CLI (Komandinė eilutė) - tradicinė sąsaja")
        print("2. GUI (Grafinė sąsaja) - moderni vizualinė sąsaja")
        print("0. Išeiti")
        print("="*50)
        
        while True:
            choice = input("\nPasirinkite sąsają (1/2/0): ").strip()
            
            if choice == "1":
                # CLI režimas
                try:
                    from agentforge.ui.cli.main_menu import main as menu_main
                    print("✓ Paleidžiamas CLI režimas...")
                    menu_main()
                except ImportError as e:
                    print(f"❌ CLI importavimo klaida: {e}")
                    print("CLI moduliai nerasimą. Pabandykite GUI režimą (pasirinkimas 2).")
                    continue
                break
            elif choice == "2":
                # GUI režimas
                print("✓ Paleidžiamas GUI režimas...")
                launch_gui()
                break
            elif choice == "0":
                print("Iki pasimatymo!")
                sys.exit(0)
            else:
                print("❌ Neteisingas pasirinkimas. Įveskite 1, 2 arba 0.")
        
    except ImportError as e:
        print(f"❌ Importavimo klaida: {e}")
        print("\nTikrinio:")
        print("1. Ar virtual environment aktyvuotas?")
        print("2. Ar instaliuotos visos priklausomybės?")
        print("3. Paleiskite: pip install -r requirements.txt")
        print("4. Arba naudokite: scripts\\setup\\setup_env.bat")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Bendrinė klaida: {e}")
        print("Paleiskite debug režimą per VS Code arba patikrinkite log'us")
        sys.exit(1)

def launch_gui():
    """Paleisti GUI sąsają."""
    try:
        # Import GUI application
        from agentforge.ui.gui.main_app import AgentForgeGUI
        
        print("🚀 Paleidžiama AgentForge GUI sąsaja...")
        app = AgentForgeGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ GUI importavimo klaida: {e}")
        print("GUI sąsaja dar nebaigta implementuoti.")
        print("Naudokite CLI režimą (pasirinkimas 1).")
        return False
    except Exception as e:
        print(f"❌ GUI paleidimo klaida: {e}")
        return False

if __name__ == "__main__":
    main()
