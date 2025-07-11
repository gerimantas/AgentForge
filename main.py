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
        
        # Bandyti importuoti agentforge modulius
        from agentforge.ui.cli.main_menu import main as menu_main
        print("✓ AgentForge moduliai importuoti sėkmingai")
        
        # Paleisti pagrindinį meniu
        menu_main()
        
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

if __name__ == "__main__":
    main()
