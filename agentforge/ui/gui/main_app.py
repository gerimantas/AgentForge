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
        
        # Patvirtinimo dialogas
        confirm = messagebox.askyesno(
            "Palaikymo Ciklas",
            "Ar tikrai norite paleisti palaikymo ciklą?\\n\\nŠis procesas gali užtrukti kelias minutes.",
            parent=self.root
        )
        
        if not confirm:
            self.update_status("✅ Paruošta veikimui")
            return
            
        # Paliesti palaikymo ciklą atskirame thread'e
        import threading
        thread = threading.Thread(target=self._run_maintenance_cycle_thread)
        thread.daemon = True
        thread.start()
            
    def _run_maintenance_cycle_thread(self):
        """Palaikymo ciklo thread'as."""
        try:
            # Importuoti palaikymo ciklo funkcijas
            from agentforge.workflows.maintenance import run_maintenance_cycle
            
            # Paleisti palaikymo ciklą
            result = run_maintenance_cycle(verbose=False)
            
            # Atnaujinti GUI rezultatu
            self.root.after(0, lambda: self._maintenance_cycle_complete(result))
            
        except Exception as e:
            # Pranešti apie klaidą
            self.root.after(0, lambda: self._maintenance_cycle_error(str(e)))
            
    def _maintenance_cycle_complete(self, result):
        """Palaikymo ciklo baigimas."""
        self.update_status("✅ Palaikymo ciklas baigtas")
        
        if result:
            messagebox.showinfo(
                "Palaikymo Ciklas - Baigta",
                f"Palaikymo ciklas sėkmingai baigtas!\\n\\nRezultatas: {result[:200]}...",
                parent=self.root
            )
        else:
            messagebox.showwarning(
                "Palaikymo Ciklas - Klaida",
                "Palaikymo ciklas nepavyko. Patikrinkite konfigūraciją.",
                parent=self.root
            )
            
        self.update_status("✅ Paruošta veikimui")
        
    def _maintenance_cycle_error(self, error_msg):
        """Palaikymo ciklo klaida."""
        self.update_status("❌ Palaikymo ciklas nepavyko")
        messagebox.showerror(
            "Palaikymo Ciklas - Klaida",
            f"Palaikymo ciklas nepavyko dėl klaidos:\\n\\n{error_msg}",
            parent=self.root
        )
        self.update_status("✅ Paruošta veikimui")
            
    def run_execution_cycle(self):
        """Paleisti vykdymo ciklą."""
        # Gauti vartotojo užklausą
        query = simpledialog.askstring(
            "Vykdymo Ciklas",
            "Įveskite užklausą optimizavimui:",
            parent=self.root
        )
        
        if not query or not query.strip():
            return
            
        self.update_status("⚡ Optimizuojama užklausa...")
        
        # Paleisti vykdymo ciklą atskirame thread'e
        import threading
        thread = threading.Thread(target=self._run_execution_cycle_thread, args=(query.strip(),))
        thread.daemon = True
        thread.start()
            
    def _run_execution_cycle_thread(self, query):
        """Vykdymo ciklo thread'as."""
        try:
            # Importuoti vykdymo ciklo funkcijas
            from agentforge.workflows.execution import run_execution_cycle
            
            # Paleisti vykdymo ciklą
            result = run_execution_cycle(query, verbose=False)
            
            # Atnaujinti GUI rezultatu
            self.root.after(0, lambda: self._execution_cycle_complete(query, result))
            
        except Exception as e:
            # Pranešti apie klaidą
            self.root.after(0, lambda: self._execution_cycle_error(query, str(e)))
            
    def _execution_cycle_complete(self, query, result):
        """Vykdymo ciklo baigimas."""
        self.update_status("✅ Užklausa optimizuota")
        
        if result:
            # Parodyti rezultatą dialogo lange
            self.show_result_dialog("Vykdymo Ciklas - Rezultatas", query, result)
        else:
            messagebox.showwarning(
                "Vykdymo Ciklas - Klaida",
                "Užklausos optimizavimas nepavyko. Patikrinkite konfigūraciją.",
                parent=self.root
            )
            
        self.update_status("✅ Paruošta veikimui")
        
    def _execution_cycle_error(self, query, error_msg):
        """Vykdymo ciklo klaida."""
        self.update_status("❌ Optimizavimas nepavyko")
        messagebox.showerror(
            "Vykdymo Ciklas - Klaida",
            f"Užklausos optimizavimas nepavyko dėl klaidos:\\n\\n{error_msg}",
            parent=self.root
        )
        self.update_status("✅ Paruošta veikimui")
        
    def show_result_dialog(self, title, query, result):
        """Parodyti rezultatų dialogą."""
        # Sukurti rezultatų langą
        result_window = tk.Toplevel(self.root)
        result_window.title(title)
        result_window.geometry("600x400")
        result_window.transient(self.root)
        result_window.grab_set()
        
        # Centruoti langą
        result_window.update_idletasks()
        x = (result_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (result_window.winfo_screenheight() // 2) - (400 // 2)
        result_window.geometry(f"600x400+{x}+{y}")
        
        # Sukurti turinį
        main_frame = ttk.Frame(result_window, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Užklausos etiketė
        ttk.Label(main_frame, text="Pradinė užklausa:", font=("Arial", 10, "bold")).pack(anchor="w")
        query_text = tk.Text(main_frame, height=3, wrap=tk.WORD)
        query_text.pack(fill="x", pady=(5, 15))
        query_text.insert("1.0", query)
        query_text.config(state="disabled")
        
        # Rezultato etiketė
        ttk.Label(main_frame, text="Optimizuotas rezultatas:", font=("Arial", 10, "bold")).pack(anchor="w")
        result_text = tk.Text(main_frame, wrap=tk.WORD)
        result_text.pack(fill="both", expand=True, pady=(5, 15))
        result_text.insert("1.0", str(result))
        result_text.config(state="disabled")
        
        # Mygtukai
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x")
        
        ttk.Button(
            button_frame,
            text="Kopijuoti į iškarpinę",
            command=lambda: self.copy_to_clipboard(str(result))
        ).pack(side="left", padx=(0, 10))
        
        ttk.Button(
            button_frame,
            text="Uždaryti",
            command=result_window.destroy
        ).pack(side="right")
        
    def copy_to_clipboard(self, text):
        """Kopijuoti tekstą į iškarpinę."""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Kopijuota", "Tekstas nukopijuotas į iškarpinę!", parent=self.root)
            
    def run_tests(self):
        """Paleisti sistemos testus."""
        self.update_status("🧪 Paleidžiami testai...")
        
        # Patvirtinimo dialogas
        confirm = messagebox.askyesno(
            "Sistemos Testai",
            "Ar norite paleisti sistemos testus?\\n\\nŠis procesas gali užtrukti.",
            parent=self.root
        )
        
        if not confirm:
            self.update_status("✅ Paruošta veikimui")
            return
            
        # Paleisti testus atskirame thread'e
        import threading
        thread = threading.Thread(target=self._run_tests_thread)
        thread.daemon = True
        thread.start()
        
    def _run_tests_thread(self):
        """Testų thread'as."""
        try:
            # Importuoti testų funkcijas
            from agentforge.workflows.execution import test_execution_cycle
            from agentforge.workflows.maintenance import test_maintenance_cycle
            
            # Paleisti testus
            exec_result = test_execution_cycle()
            maint_result = test_maintenance_cycle()
            
            # Atnaujinti GUI rezultatu
            self.root.after(0, lambda: self._tests_complete(exec_result, maint_result))
            
        except Exception as e:
            # Pranešti apie klaidą
            self.root.after(0, lambda: self._tests_error(str(e)))
            
    def _tests_complete(self, exec_result, maint_result):
        """Testų baigimas."""
        self.update_status("✅ Testai baigti")
        
        message = f"Testų rezultatai:\\n\\n"
        message += f"• Vykdymo ciklas: {'✅ Praeitas' if exec_result else '❌ Nepavyko'}\\n"
        message += f"• Palaikymo ciklas: {'✅ Praeitas' if maint_result else '❌ Nepavyko'}\\n\\n"
        
        if exec_result and maint_result:
            message += "Visi testai praėjo sėkmingai!"
            messagebox.showinfo("Testai - Rezultatai", message, parent=self.root)
        else:
            message += "Kai kurie testai nepavyko. Patikrinkite konfigūraciją."
            messagebox.showwarning("Testai - Rezultatai", message, parent=self.root)
            
        self.update_status("✅ Paruošta veikimui")
        
    def _tests_error(self, error_msg):
        """Testų klaida."""
        self.update_status("❌ Testai nepavyko")
        messagebox.showerror(
            "Testai - Klaida",
            f"Testų paleidimas nepavyko dėl klaidos:\\n\\n{error_msg}",
            parent=self.root
        )
        self.update_status("✅ Paruošta veikimui")
        
    def manage_categories(self):
        """Valdyti kategorijas ir agentus."""
        self.update_status("📊 Atidaromas kategorijų valdymas...")
        
        # Paleisti kategorijų valdymo langą
        import threading
        thread = threading.Thread(target=self._manage_categories_thread)
        thread.daemon = True
        thread.start()
        
    def _manage_categories_thread(self):
        """Kategorijų valdymo thread'as."""
        try:
            # Importuoti kategorijų funkcijas
            from agentforge.categories.manager import load_categories
            from agentforge.categories.classifier import get_query_category
            
            # Įkelti kategorijas
            categories = load_categories()
            
            # Atnaujinti GUI rezultatu
            self.root.after(0, lambda: self._show_categories_dialog(categories))
            
        except Exception as e:
            # Pranešti apie klaidą
            self.root.after(0, lambda: self._categories_error(str(e)))
            
    def _show_categories_dialog(self, categories):
        """Parodyti kategorijų valdymo dialogą."""
        self.update_status("📊 Kategorijų valdymas atidarytas")
        
        # Sukurti kategorijų langą
        cat_window = tk.Toplevel(self.root)
        cat_window.title("Kategorijų Valdymas")
        cat_window.geometry("500x300")
        cat_window.transient(self.root)
        cat_window.grab_set()
        
        # Centruoti langą
        cat_window.update_idletasks()
        x = (cat_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (cat_window.winfo_screenheight() // 2) - (300 // 2)
        cat_window.geometry(f"500x300+{x}+{y}")
        
        # Sukurti turinį
        main_frame = ttk.Frame(cat_window, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        ttk.Label(main_frame, text="Sistemos kategorijos:", font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Kategorijų sąrašas
        categories_text = tk.Text(main_frame, wrap=tk.WORD)
        categories_text.pack(fill="both", expand=True, pady=(10, 20))
        
        # Įrašyti kategorijas
        cats = categories.get('categories', {})
        for cat_name, cat_data in cats.items():
            categories_text.insert(tk.END, f"• {cat_name}\\n")
            if 'description' in cat_data:
                categories_text.insert(tk.END, f"  {cat_data['description']}\\n\\n")
        
        categories_text.config(state="disabled")
        
        # Uždarymo mygtukas
        ttk.Button(
            main_frame,
            text="Uždaryti",
            command=cat_window.destroy
        ).pack(anchor="e")
        
        self.update_status("✅ Paruošta veikimui")
        
    def _categories_error(self, error_msg):
        """Kategorijų valdymo klaida."""
        self.update_status("❌ Kategorijų valdymas nepavyko")
        messagebox.showerror(
            "Kategorijų Valdymas - Klaida",
            f"Kategorijų valdymo atidarymas nepavyko dėl klaidos:\\n\\n{error_msg}",
            parent=self.root
        )
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
