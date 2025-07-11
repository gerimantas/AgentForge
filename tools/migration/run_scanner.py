# /AgentForge/tools/migration/run_scanner.py

"""
Projekto struktūros analizės paleidimo skriptas.
Naudokite šį skriptą dabartinės struktūros analizei.
"""

import sys
import os
from pathlib import Path

# Pridėti projects root į Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tools.migration.project_scanner import ProjectScanner
import datetime


def run_analysis():
    """Paleidžia projekto struktūros analizę."""
    print("🔍 AgentForge Projekto Struktūros Analizė")
    print("=" * 50)
    
    # Sukurti scanner
    scanner = ProjectScanner(str(project_root))
    
    # Sukurti output direktoriją jei nėra
    output_dir = project_root / "tools" / "migration" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sukurti ataskaitos failą
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"project_structure_analysis_{timestamp}.txt"
    
    print(f"📁 Projekto root: {project_root}")
    print(f"💾 Ataskaita bus išsaugota: {output_file}")
    print("\n🔄 Analizuojama...")
    
    try:
        # Vykdyti analizę
        scanner.save_current_structure(str(output_file))
        
        print("\n✅ Analizė baigta sėkmingai!")
        print(f"📄 Ataskaita: {output_file}")
        
        # Rodyti trumpą santrauką
        print("\n📊 Trumpa santrauka:")
        
        # Suskaičiuoti Python failus
        python_files = list(project_root.rglob("*.py"))
        python_files = [f for f in python_files if not any(ignore in str(f) for ignore in scanner.ignore_patterns)]
        
        yaml_files = list(project_root.rglob("*.yaml")) + list(project_root.rglob("*.yml"))
        
        print(f"   🐍 Python failų: {len(python_files)}")
        print(f"   📝 YAML failų: {len(yaml_files)}")
        print(f"   📁 Pagrindinis katalogas: {len(list(project_root.iterdir()))} elementų")
        
        print("\n🎯 Tolimesni žingsniai:")
        print("   1. Peržiūrėkite sukurtą ataskaitos failą")
        print("   2. Patvirtinkite migracijos žemėlapį")
        print("   3. Sukurkite backup prieš migracijos pradžią")
        print("   4. Pradėkite Phase 0 (pasiruošimas)")
        
    except Exception as e:
        print(f"\n❌ Klaida vykdant analizę: {e}")
        print(f"   Detalūs duomenys: {type(e).__name__}")
        return False
        
    return True


if __name__ == "__main__":
    success = run_analysis()
    
    if success:
        print("\n🎉 Skriptas baigtas sėkmingai!")
        sys.exit(0)
    else:
        print("\n💥 Skriptas baigtas su klaidomis!")
        sys.exit(1)
