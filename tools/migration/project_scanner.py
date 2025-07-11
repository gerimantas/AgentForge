# /AgentForge/tools/migration/project_scanner.py

"""
Projekto struktūros nuskaitymo ir analizės įrankis.
Sukuria detalizuotą projekto failų struktūros ataskaitas.
"""

import os
import datetime
from pathlib import Path
from typing import List, Dict, Set


class ProjectScanner:
    """Projekto struktūros analizės klasė."""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.ignore_patterns = {
            '__pycache__',
            '.git',
            '.venv',
            'venv',
            '.env',
            'node_modules',
            '.pytest_cache',
            '.coverage',
            'dist',
            'build',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.DS_Store',
            'Thumbs.db'
        }
        
    def should_ignore(self, path: Path) -> bool:
        """Tikrina ar failą/aplanką reikia ignoruoti."""
        for pattern in self.ignore_patterns:
            if pattern in str(path):
                return True
            if pattern.startswith('*') and str(path).endswith(pattern[1:]):
                return True
        return False
    
    def scan_directory(self, directory: Path, prefix: str = "", max_depth: int = 10) -> List[str]:
        """Rekursyviai nuskaito direktorijos struktūrą."""
        if max_depth <= 0:
            return []
            
        structure = []
        
        try:
            # Gauti visus failus ir aplankus
            items = list(directory.iterdir())
            # Rūšiuoti: pirma aplankai, paskui failai
            items.sort(key=lambda x: (x.is_file(), x.name.lower()))
            
            for i, item in enumerate(items):
                if self.should_ignore(item):
                    continue
                    
                # Nustatyti ar tai paskutinis elementas
                is_last = i == len(items) - 1
                current_prefix = "└── " if is_last else "├── "
                next_prefix = "    " if is_last else "│   "
                
                if item.is_dir():
                    # Aplankas
                    structure.append(f"{prefix}{current_prefix}{item.name}/")
                    # Rekursyviai nuskaityti subaplankus
                    sub_structure = self.scan_directory(
                        item, 
                        prefix + next_prefix, 
                        max_depth - 1
                    )
                    structure.extend(sub_structure)
                else:
                    # Failas
                    file_info = self.get_file_info(item)
                    structure.append(f"{prefix}{current_prefix}{item.name}{file_info}")
                    
        except PermissionError:
            structure.append(f"{prefix}[Prieiga uždrausta]")
            
        return structure
    
    def get_file_info(self, file_path: Path) -> str:
        """Gauna papildomą informaciją apie failą."""
        try:
            stat = file_path.stat()
            size = stat.st_size
            
            # Formato konvertavimas
            if size < 1024:
                size_str = f" ({size} B)"
            elif size < 1024 * 1024:
                size_str = f" ({size / 1024:.1f} KB)"
            else:
                size_str = f" ({size / (1024 * 1024):.1f} MB)"
                
            # Failų tipų analizė
            extension = file_path.suffix.lower()
            if extension == '.py':
                lines = self.count_lines(file_path)
                return f"{size_str} - Python modulis ({lines} eilutės)"
            elif extension == '.yaml' or extension == '.yml':
                return f"{size_str} - YAML konfigūracija"
            elif extension == '.json':
                return f"{size_str} - JSON duomenys"
            elif extension == '.md':
                return f"{size_str} - Markdown dokumentacija"
            elif extension == '.txt':
                return f"{size_str} - Tekstinis failas"
            elif extension == '.log':
                return f"{size_str} - Log failas"
            else:
                return size_str
                
        except (OSError, PermissionError):
            return " [Nepavyko nuskaityti]"
    
    def count_lines(self, file_path: Path) -> int:
        """Suskaičiuoja eilučių skaičių Python faile."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return sum(1 for _ in f)
        except:
            return 0
    
    def analyze_python_files(self) -> Dict[str, Dict]:
        """Analizuoja Python failus projekte."""
        python_files = {}
        
        for py_file in self.project_root.rglob("*.py"):
            if self.should_ignore(py_file):
                continue
                
            relative_path = py_file.relative_to(self.project_root)
            
            try:
                with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                analysis = {
                    'lines': len(content.splitlines()),
                    'imports': self.extract_imports(content),
                    'classes': self.extract_classes(content),
                    'functions': self.extract_functions(content),
                    'size_bytes': py_file.stat().st_size
                }
                
                python_files[str(relative_path)] = analysis
                
            except Exception as e:
                python_files[str(relative_path)] = {'error': str(e)}
                
        return python_files
    
    def extract_imports(self, content: str) -> List[str]:
        """Ištraukia import statements."""
        imports = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                imports.append(line)
        return imports
    
    def extract_classes(self, content: str) -> List[str]:
        """Ištraukia klasių pavadinimus."""
        classes = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('class ') and ':' in line:
                class_name = line.split('class ')[1].split('(')[0].split(':')[0].strip()
                classes.append(class_name)
        return classes
    
    def extract_functions(self, content: str) -> List[str]:
        """Ištraukia funkcijų pavadinimus."""
        functions = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('def ') and ':' in line:
                func_name = line.split('def ')[1].split('(')[0].strip()
                functions.append(func_name)
        return functions
    
    def generate_migration_map(self) -> Dict[str, str]:
        """Sukuria migracijos žemėlapį iš dabartinės į naują struktūrą."""
        migration_map = {}
        
        # Baziniai Python failai
        base_files = {
            'config.py': 'agentforge/core/config.py',
            'custom_tools.py': 'agentforge/utils/file_operations.py',
            'agents.py': 'agentforge/agents/__init__.py',
            'agent_skills.py': 'agentforge/agents/skills.py',
            'dynamic_agents.py': 'agentforge/agents/dynamic_selection.py',
            'categories.py': 'agentforge/categories/manager.py',
            'category_classifier.py': 'agentforge/categories/classifier.py',
            'maintenance_cycle.py': 'agentforge/workflows/maintenance.py',
            'execution_cycle.py': 'agentforge/workflows/execution.py',
            'tasks_maintenance.py': 'agentforge/workflows/tasks/maintenance_tasks.py',
            'tasks_execution.py': 'agentforge/workflows/tasks/execution_tasks.py',
            'prompt_templates.py': 'agentforge/templates/manager.py',
            'prompt_metrics.py': 'agentforge/analysis/metrics.py',
            'test_system.py': 'tests/integration/test_full_workflow.py',
            'main.py': 'agentforge/ui/cli/main_menu.py'
        }
        
        # YAML ir duomenų failai
        data_files = {
            'categories.yaml': 'data/config/categories.yaml',
            'agent_skills.yaml': 'data/config/agent_skills.yaml',
            'ziniu_baze.yaml': 'data/knowledge_base/ziniu_baze.yaml',
            'kanonine_sistema.yaml': 'data/knowledge_base/kanonine_sistema.yaml',
            'source_registry.yaml': 'data/knowledge_base/source_registry.yaml'
        }
        
        # Aplankai
        directory_mappings = {
            'templates/': 'data/templates/',
            'test_results/': 'data/results/',
            '__pycache__/': '[DELETE]'
        }
        
        # Sujungti visus mapping'us
        migration_map.update(base_files)
        migration_map.update(data_files)
        migration_map.update(directory_mappings)
        
        return migration_map
    
    def save_current_structure(self, output_file: str):
        """Išsaugo dabartinę projekto struktūrą į failą."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Nuskaityti struktūrą
        structure = self.scan_directory(self.project_root)
        
        # Analizuoti Python failus
        python_analysis = self.analyze_python_files()
        
        # Sukurti migracijos žemėlapį
        migration_map = self.generate_migration_map()
        
        # Sukurti ataskaitos turinį
        report_content = f"""
# AgentForge Projekto Struktūros Ataskaita
Sukurta: {timestamp}

## 📁 Dabartinė failų struktūra

AgentForge/
"""
        
        # Pridėti struktūros medį
        for line in structure:
            report_content += line + "\n"
        
        report_content += f"""

## 📊 Python failų analizė

Iš viso Python failų: {len(python_analysis)}

"""
        
        # Detalus Python failų aprašymas
        for file_path, analysis in python_analysis.items():
            if 'error' in analysis:
                report_content += f"### {file_path}\n❌ Klaida: {analysis['error']}\n\n"
                continue
                
            report_content += f"""### {file_path}
- **Eilutės:** {analysis['lines']}
- **Dydis:** {analysis['size_bytes']} baitų
- **Klasės:** {', '.join(analysis['classes']) if analysis['classes'] else 'Nėra'}
- **Funkcijos:** {len(analysis['functions'])} vnt.
- **Import'ai:** {len(analysis['imports'])} vnt.

**Pagrindiniai import'ai:**
"""
            for imp in analysis['imports'][:5]:  # Pirmi 5 import'ai
                report_content += f"  - {imp}\n"
            if len(analysis['imports']) > 5:
                report_content += f"  - ... ir dar {len(analysis['imports']) - 5}\n"
            report_content += "\n"
        
        report_content += f"""

## 🔄 Siūlomas migracijos žemėlapis

Dabartinis failas → Nauja vieta:

"""
        
        for old_path, new_path in migration_map.items():
            if new_path == '[DELETE]':
                report_content += f"❌ {old_path} → [IŠTRINTI]\n"
            else:
                report_content += f"📦 {old_path} → {new_path}\n"
        
        report_content += f"""

## 📈 Statistika

- **Python failų:** {len([f for f in python_analysis.keys() if f.endswith('.py')])}
- **YAML failų:** {len([f for f in migration_map.keys() if f.endswith('.yaml') or f.endswith('.yml')])}
- **Iš viso perkeltinų failų:** {len([v for v in migration_map.values() if v != '[DELETE]'])}
- **Ištrintinų failų/aplankų:** {len([v for v in migration_map.values() if v == '[DELETE]'])}

## 🎯 Siūloma nauja struktūra

Žr. development_plan.md sekciją "🎯 Galutinė optimizuota struktūra"

---
Ataskaita sugeneruota automatiškai naudojant ProjectScanner įrankį.
"""
        
        # Išsaugoti į failą
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        print(f"✅ Projekto struktūros ataskaita išsaugota: {output_file}")
        print(f"📊 Analizuota {len(python_analysis)} Python failų")
        print(f"🔄 Sukurtas {len(migration_map)} failų migracijos žemėlapis")


def main():
    """Pagrindinis skriptas."""
    project_root = Path(__file__).parent.parent.parent  # AgentForge root
    
    # Sukurti output direktoriją
    output_dir = project_root / "tools" / "migration" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sukurti scanner objektą
    scanner = ProjectScanner(str(project_root))
    
    # Sugeneruoti ataskaitą
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"current_structure_{timestamp}.txt"
    
    print("🔍 Analizuojama projekto struktūra...")
    scanner.save_current_structure(str(output_file))
    
    print(f"\n📁 Ataskaita išsaugota: {output_file}")
    print("\n🎯 Rekomenduojami tolimesni žingsniai:")
    print("1. Peržiūrėkite sukurtą ataskaitą")
    print("2. Patvirtinkite migracijos žemėlapį")
    print("3. Paleiskite phase_migrator.py Phase 0 pradžiai")


if __name__ == "__main__":
    main()
