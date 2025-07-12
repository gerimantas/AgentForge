#!/usr/bin/env python3
"""
AgentForge GUI Main Application
==============================

Pagrindinis GUI aplikacijos failas, integruojantis su AgentForge sistema.
Naudoja standartinį tkinter moderniam dizainui ir integruojasi su esamais workflow.
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root))


class AgentForgeGUI:
    """
    Pagrindinė AgentForge GUI klasė.
    Integruojasi su esamais AgentForge workflow ir konfigūracija.
    """
    
    def __init__(self):
        """Inicializuoti GUI aplikaciją."""
        # Sukurti pagrindinį langą
        self.root = tk.Tk()
        self.setup_main_window()
        self.setup_styles()
        self.create_interface()
        
    def setup_main_window(self):
        """Nustatyti pagrindinį langą."""
        self.root.title("AgentForge - AI Prompt Optimization System")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)
        
        # Centruoti langą ekrane
        self.center_window()
        
    def center_window(self):
        """Centruoti langą ekrane."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def setup_styles(self):
        """Nustatyti UI stilius."""
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modernus stilius
        
        # Konfigūruoti stilius
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'))
        self.style.configure('Subtitle.TLabel', font=('Arial', 12))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        self.style.configure('Action.TButton', font=('Arial', 11, 'bold'), padding=10)
        
    def create_interface(self):
        """Sukurti vartotojo sąsają."""
        # Pagrindinis konteineris
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Antraštė
        self.create_header(main_frame)
        
        # Pagrindinė meniu zona
        self.create_menu_section(main_frame)
        
        # Būsenos juosta
        self.create_status_bar(main_frame)
        
    def create_header(self, parent):
        """Sukurti antraštės sekciją."""
        header_frame = ttk.LabelFrame(parent, text="", padding="10")
        header_frame.pack(fill="x", pady=(0, 20))
        
        title_label = ttk.Label(
            header_frame,
            text="🤖 AgentForge",
            style='Title.TLabel'
        )
        title_label.pack()
        
        subtitle_label = ttk.Label(
            header_frame,
            text="AI Prompt Optimization System",
            style='Subtitle.TLabel'
        )
        subtitle_label.pack(pady=(5, 0))
        
    def create_menu_section(self, parent):
        """Sukurti meniu sekciją."""
        menu_frame = ttk.LabelFrame(parent, text="Pasirinkite operaciją", padding="15")
        menu_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Meniu mygtukai (atitinka CLI funkcionalumą)
        buttons = [
            ("🔄 Palaikymo Ciklas", "Atnaujinti žinių bazę", self.run_maintenance_cycle),
            ("⚡ Vykdymo Ciklas", "Optimizuoti užklausą", self.run_execution_cycle),
            ("🧪 Sistemos Testai", "Paleisti testus", self.run_tests),
            ("📊 Kategorijų Valdymas", "Valdyti kategorijas ir agentus", self.manage_categories),
            ("📝 Šablonų Valdymas", "Valdyti prompt šablonus", self.manage_templates),
        ]
        
        for i, (title, description, command) in enumerate(buttons):
            self.create_menu_button(menu_frame, title, description, command, i)
            
    def create_menu_button(self, parent, title, description, command, row):
        """Sukurti meniu mygtuką."""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill="x", pady=5)
        
        # Pagrindinis mygtukas
        button = ttk.Button(
            button_frame,
            text=title,
            style='Action.TButton',
            command=command,
            width=25
        )
        button.pack(side="left", padx=(0, 10))
        
        # Aprašymas
        desc_label = ttk.Label(
            button_frame,
            text=description,
            font=('Arial', 10)
        )
        desc_label.pack(side="left", anchor="w")
        
    def create_status_bar(self, parent):
        """Sukurti būsenos juostą."""
        status_frame = ttk.LabelFrame(parent, text="Būsena", padding="5")
        status_frame.pack(fill="x")
        
        self.status_var = tk.StringVar(value="✅ Paruošta veikimui")
        self.status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            font=('Arial', 9)
        )
        self.status_label.pack(anchor="w")
        
    def update_status(self, message):
        """Atnaujinti būsenos pranešimą."""
        self.status_var.set(message)
        self.root.update_idletasks()
        
    # Workflow integracijos metodai
    def run_maintenance_cycle(self):
        """Paleisti palaikymo ciklą."""
        self.update_status("🔄 Paleidžiamas palaikymo ciklas...")
        messagebox.showinfo("Palaikymo Ciklas", "Žinių bazės atnaujinimas bus implementuotas Stage 2 metu.\\n\\n✅ GUI sąsaja veikia teisingai!")
        self.update_status("✅ Paruošta veikimui")
            
    def run_execution_cycle(self):
        """Paleisti vykdymo ciklą."""
        # Gauti vartotojo užklausą
        query = simpledialog.askstring(
            "Vykdymo Ciklas",
            "Įveskite užklausą optimizavimui:",
            parent=self.root
        )
        
        if not query:
            return
            
        self.update_status("⚡ Apdorojama užklausa...")
        
        # Simuliuoti apdorojimą
        self.root.after(1000, lambda: self.finish_execution_cycle(query))
            
    def finish_execution_cycle(self, query):
        """Baigti vykdymo ciklą."""
        self.update_status("✅ Užklausa apdorota")
        
        # Parodyti rezultatą
        result_text = f"Įvestis: {query}\\n\\nRezultatas: Užklausos optimizavimas bus implementuotas Stage 2 metu.\\n\\n✅ GUI sąsaja veikia teisingai!"
        messagebox.showinfo("Vykdymo Ciklas - Rezultatas", result_text)
        self.update_status("✅ Paruošta veikimui")
            
    def run_tests(self):
        """Paleisti sistemos testus."""
        self.update_status("🧪 Paleidžiami testai...")
        messagebox.showinfo("Testai", "Testų sistema bus implementuota Stage 3 metu.\\n\\n✅ GUI sąsaja veikia teisingai!")
        self.update_status("✅ Paruošta veikimui")
        
    def manage_categories(self):
        """Valdyti kategorijas ir agentus."""
        self.update_status("📊 Atidaromas kategorijų valdymas...")
        messagebox.showinfo("Kategorijos", "Kategorijų valdymas bus implementuotas Stage 4 metu.\\n\\n✅ GUI sąsaja veikia teisingai!")
        self.update_status("✅ Paruošta veikimui")
        
    def manage_templates(self):
        """Valdyti šablonus."""
        self.update_status("📝 Atidaromas šablonų valdymas...")
        messagebox.showinfo("Šablonai", "Šablonų valdymas bus implementuotas Stage 4 metu.\\n\\n✅ GUI sąsaja veikia teisingai!")
        self.update_status("✅ Paruošta veikimui")
        
    def run(self):
        """Paleisti GUI aplikaciją."""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\\n👋 GUI uždaromas...")
        except Exception as e:
            print(f"❌ GUI klaida: {e}")


def main():
    """Pagrindinė funkcija GUI paleidimui."""
    try:
        app = AgentForgeGUI()
        app.run()
    except Exception as e:
        print(f"❌ Nepavyko paleisti GUI: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
