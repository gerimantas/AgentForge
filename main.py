#!/usr/bin/env python3
"""
AgentForge - Entry Point
========================

Pagrindinis AgentForge sistemos paleidimo taškas.
Po struktūros pertvarkymo šis failas importuoja main() funkciją iš agentforge paketo.
"""

if __name__ == "__main__":
    from agentforge.ui.cli.main_menu import main
    main()
