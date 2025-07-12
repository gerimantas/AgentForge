"""
AgentForge CLI Main Menu
=======================

Pagrindinis AgentForge CLI sąsajos meniu.
"""

import sys
import os
from typing import Optional
from agentforge.workflows.execution import run_execution_cycle, test_execution_cycle
from agentforge.workflows.maintenance import run_maintenance_cycle, test_maintenance_cycle
from agentforge.categories.manager import load_categories, list_all_categories
from agentforge.categories.classifier import get_query_category, print_classification_result
from agentforge.analysis.metrics import evaluate_prompt
from agentforge.templates.manager import list_templates, save_template

def print_main_menu():
    """Išspausdina pagrindinį meniu."""
    print("\\n" + "="*60)
    print("🚀 AgentForge - AI Prompt Optimization System")
    print("="*60)
    print("1. 🔄 Vykdymo ciklas (Prompt Optimization)")
    print("2. 🔧 Palaikymo ciklas (Knowledge Base Maintenance)")
    print("3. 🧪 Sistemos testai (System Tests)")
    print("4. 📊 Kategorijų valdymas (Category Management)")
    print("5. 📝 Šablonų valdymas (Template Management)")
    print("6. 📈 Sistemos statistika (System Statistics)")
    print("0. 🚪 Išeiti (Exit)")
    print("="*60)

def handle_execution_cycle():
    """Tvarko vykdymo ciklo paleidimą."""
    print("\\n🔄 VYKDYMO CIKLAS")
    print("-" * 40)
    
    while True:
        query = input("\\nĮveskite užklausą optimizacijai (arba 'back' grįžti): ").strip()
        
        if query.lower() in ['back', 'b', 'atgal']:
            break
        
        if not query:
            print("❌ Užklausa negali būti tuščia!")
            continue
        
        print(f"\\n📝 Optimizuojamas prompt'as: {query}")
        
        # Vykdyti optimizacijos ciklą
        result = run_execution_cycle(query, verbose=True)
        
        if result:
            print(f"\\n✅ Optimizacijos rezultatas:")
            print("-" * 40)
            print(result)
        else:
            print("\\n❌ Optimizacija nepavyko!")
        
        # Klausti ar tęsti
        continue_choice = input("\\nAr norite optimizuoti kitą prompt'ą? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes', 'taip', 't']:
            break

def handle_maintenance_cycle():
    """Tvarko palaikymo ciklo paleidimą."""
    print("\\n🔧 PALAIKYMO CIKLAS")
    print("-" * 40)
    
    confirm = input("Ar tikrai norite paleisti palaikymo ciklą? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes', 'taip', 't']:
        print("\\n🚀 Paleidžiamas palaikymo ciklas...")
        result = run_maintenance_cycle(verbose=True)
        
        if result:
            print(f"\\n✅ Palaikymo ciklas baigtas sėkmingai!")
        else:
            print("\\n❌ Palaikymo ciklas nepavyko!")
    else:
        print("\\n⏸️ Palaikymo ciklas atšauktas.")

def handle_system_tests():
    """Tvarko sistemos testų paleidimą."""
    print("\\n🧪 SISTEMOS TESTAI")
    print("-" * 40)
    print("1. 🔄 Testuoti vykdymo ciklą")
    print("2. 🔧 Testuoti palaikymo ciklą")
    print("3. 📊 Testuoti kategorijų sistemą")
    print("4. 🔍 Pilnas sistemos testas")
    print("0. ⬅️ Grįžti")
    
    while True:
        choice = input("\\nPasirinkite testą (0-4): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            print("\\n🔄 Testuojamas vykdymo ciklas...")
            success = test_execution_cycle()
            print(f"Testas {'sėkmingas' if success else 'nepavyko'}!")
        elif choice == '2':
            print("\\n🔧 Testuojamas palaikymo ciklas...")
            success = test_maintenance_cycle()
            print(f"Testas {'sėkmingas' if success else 'nepavyko'}!")
        elif choice == '3':
            print("\\n📊 Testuojama kategorijų sistema...")
            test_categories()
        elif choice == '4':
            print("\\n🔍 Pilnas sistemos testas...")
            run_full_system_test()
        else:
            print("❌ Neteisingas pasirinkimas!")

def handle_category_management():
    """Tvarko kategorijų valdymą."""
    print("\\n📊 KATEGORIJŲ VALDYMAS")
    print("-" * 40)
    print("1. 📋 Peržiūrėti kategorijas")
    print("2. 🔍 Klasifikuoti užklausą")
    print("3. 📈 Kategorijų statistika")
    print("0. ⬅️ Grįžti")
    
    while True:
        choice = input("\\nPasirinkite veiksmą (0-3): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            print("\\n📋 Sistemos kategorijos:")
            list_all_categories()
        elif choice == '2':
            query = input("\\nĮveskite užklausą klasifikacijai: ").strip()
            if query:
                result = get_query_category(query)
                print_classification_result(result)
            else:
                print("❌ Užklausa negali būti tuščia!")
        elif choice == '3':
            print("\\n📈 Kategorijų statistika:")
            show_category_statistics()
        else:
            print("❌ Neteisingas pasirinkimas!")

def handle_template_management():
    """Tvarko šablonų valdymą."""
    print("\\n📝 ŠABLONŲ VALDYMAS")
    print("-" * 40)
    print("1. 📋 Peržiūrėti šablonus")
    print("2. ➕ Pridėti šabloną")
    print("3. ✏️ Redaguoti šabloną")
    print("4. 🗑️ Šalinti šabloną")
    print("0. ⬅️ Grįžti")
    
    while True:
        choice = input("\\nPasirinkite veiksmą (0-4): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            print("\\n📋 Sistemos šablonai:")
            show_templates()
        elif choice == '2':
            add_template()
        elif choice == '3':
            edit_template()
        elif choice == '4':
            delete_template()
        else:
            print("❌ Neteisingas pasirinkimas!")

def handle_system_statistics():
    """Tvarko sistemos statistikos rodymą."""
    print("\\n📈 SISTEMOS STATISTIKA")
    print("-" * 40)
    
    try:
        # Rodyti bendras statistikas
        print("📊 Bendros statistikos:")
        print(f"• Kategorijų skaičius: {get_categories_count()}")
        print(f"• Šablonų skaičius: {get_templates_count()}")
        print(f"• Žinių bazės įrašų: {get_knowledge_base_count()}")
        print(f"• Šaltinių registro įrašų: {get_sources_count()}")
        
        # Rodyti sistemos būsenos informaciją
        print("\\n🔧 Sistemos būsena:")
        print(f"• API raktai: {'✅ Konfigūruoti' if check_api_keys() else '❌ Nėra'}")
        print(f"• Žinių bazė: {'✅ Prieinama' if check_knowledge_base() else '❌ Nepasiekiama'}")
        print(f"• Šaltinių registras: {'✅ Prieinama' if check_sources_registry() else '❌ Nepasiekiama'}")
        
    except Exception as e:
        print(f"❌ Klaida gaunant statistikas: {e}")

def main():
    """Pagrindinė CLI meniu funkcija."""
    try:
        print("\\n🚀 AgentForge CLI paleidimas...")
        
        # Patikrinti sistemos būseną
        if not check_system_health():
            print("\\n⚠️ Sistemos būsenos problemos. Tęsiama su ribotumo funkcionalumu.")
        
        while True:
            print_main_menu()
            
            choice = input("\\nPasirinkite veiksmą (0-6): ").strip()
            
            if choice == '0':
                print("\\n👋 Iki pasimatymo!")
                break
            elif choice == '1':
                handle_execution_cycle()
            elif choice == '2':
                handle_maintenance_cycle()
            elif choice == '3':
                handle_system_tests()
            elif choice == '4':
                handle_category_management()
            elif choice == '5':
                handle_template_management()
            elif choice == '6':
                handle_system_statistics()
            else:
                print("❌ Neteisingas pasirinkimas! Pasirinkite 0-6.")
                
    except KeyboardInterrupt:
        print("\\n\\n⚠️ Programa nutraukta vartotojo.")
        sys.exit(0)
    except Exception as e:
        print(f"\\n❌ Kritinė klaida: {e}")
        sys.exit(1)

# Pagalbinės funkcijos
def test_categories():
    """Testuoja kategorijų sistemą."""
    try:
        categories = load_categories()
        print(f"✅ Kategorijos įkeltos: {len(categories.get('categories', {}))} kategorijos")
        
        # Testuoti klasifikaciją
        test_queries = [
            "Kaip sukurti gerą prompt'ą?",
            "Analizuok šiuos duomenis",
            "Parašyk pasaką apie robotą"
        ]
        
        for query in test_queries:
            result = get_query_category(query)
            print(f"📝 '{query}' -> {result.get('main_category', 'Nežinoma')}")
            
    except Exception as e:
        print(f"❌ Kategorijų testas nepavyko: {e}")

def run_full_system_test():
    """Vykdo pilną sistemos testą."""
    print("\\n🔍 Pilno sistemos testo pradžia...")
    
    tests = [
        ("Konfigūracijos testas", test_configuration),
        ("Kategorijų testas", test_categories),
        ("Vykdymo ciklo testas", test_execution_cycle),
        ("Palaikymo ciklo testas", test_maintenance_cycle),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"\\n🧪 {test_name}...")
            if test_func():
                print(f"✅ {test_name} praeitas")
                passed += 1
            else:
                print(f"❌ {test_name} nepavyko")
                failed += 1
        except Exception as e:
            print(f"❌ {test_name} klaida: {e}")
            failed += 1
    
    print(f"\\n📊 Testų rezultatai: {passed} sėkmingų, {failed} nesėkmingų")
    return failed == 0

def test_configuration():
    """Testuoja konfigūracijos failus."""
    try:
        from agentforge.core.config import validate_api_keys
        validate_api_keys()
        return True
    except Exception as e:
        print(f"Konfigūracijos klaida: {e}")
        return False

def check_system_health():
    """Tikrina sistemos būseną."""
    try:
        # Tikrinti pagrindinius komponentus
        health_checks = [
            check_api_keys(),
            check_knowledge_base(),
            check_sources_registry()
        ]
        
        return all(health_checks)
    except Exception:
        return False

def check_api_keys():
    """Tikrina API raktų konfigūraciją."""
    try:
        from agentforge.core.config import OPENAI_API_KEY, SERPER_API_KEY
        return OPENAI_API_KEY is not None and SERPER_API_KEY is not None
    except Exception:
        return False

def check_knowledge_base():
    """Tikrina žinių bazės prieinamumą."""
    try:
        from agentforge.utils.file_operations import load_knowledge_base
        kb = load_knowledge_base()
        return isinstance(kb, list)
    except Exception:
        return False

def check_sources_registry():
    """Tikrina šaltinių registro prieinamumą."""
    try:
        from agentforge.utils.file_operations import load_source_registry
        sr = load_source_registry()
        return isinstance(sr, dict)
    except Exception:
        return False

def get_categories_count():
    """Grąžina kategorijų skaičių."""
    try:
        categories = load_categories()
        return len(categories.get('categories', {}))
    except Exception:
        return 0

def get_templates_count():
    """Grąžina šablonų skaičių."""
    try:
        templates = list_templates()
        return len(templates)
    except Exception:
        return 0

def get_knowledge_base_count():
    """Grąžina žinių bazės įrašų skaičių."""
    try:
        from agentforge.utils.file_operations import load_knowledge_base
        kb = load_knowledge_base()
        return len(kb)
    except Exception:
        return 0

def get_sources_count():
    """Grąžina šaltinių registro įrašų skaičių."""
    try:
        from agentforge.utils.file_operations import load_source_registry
        sr = load_source_registry()
        return len(sr.get('sources', []))
    except Exception:
        return 0

def show_category_statistics():
    """Rodo kategorijų statistikas."""
    try:
        categories = load_categories()
        cats = categories.get('categories', {})
        
        print(f"\\n📊 Kategorijų statistika:")
        for category, data in cats.items():
            print(f"• {category}: {data.get('description', 'Nėra aprašymo')}")
            
    except Exception as e:
        print(f"❌ Nepavyko gauti kategorijų statistikos: {e}")

def show_templates():
    """Rodo šablonų sąrašą."""
    try:
        templates = list_templates()
        
        print(f"\\n📝 Šablonų sąrašas:")
        for template_data in templates:
            print(f"• {template_data.get('id', 'Nėra ID')}: {template_data.get('name', 'Nėra pavadinimo')}")
            
    except Exception as e:
        print(f"❌ Nepavyko gauti šablonų sąrašo: {e}")

def add_template():
    """Prideda naują šabloną."""
    print("\\n➕ Pridėjimas šablono (ne implementuota)")

def edit_template():
    """Redaguoja šabloną."""
    print("\\n✏️ Redagavimas šablono (ne implementuota)")

def delete_template():
    """Šalina šabloną."""
    print("\\n🗑️ Šalinimas šablono (ne implementuota)")

if __name__ == "__main__":
    main()
