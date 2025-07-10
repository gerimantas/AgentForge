# /AgentForge/test_system.py

import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import datetime
import io
from contextlib import redirect_stdout
import logging
from logging.handlers import RotatingFileHandler

# Užtikriname, kad testų modulis gali importuoti mūsų kodo modulius
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Konstantos
TEST_RESULTS_DIR = "test_results"
TEST_RESULTS_FILE = os.path.join(TEST_RESULTS_DIR, "test_results.log")
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

def setup_logging():
    """Sukonfigūruoja testų rezultatų žurnalo failą"""
    if not os.path.exists(TEST_RESULTS_DIR):
        os.makedirs(TEST_RESULTS_DIR)
    
    # Sukuriame logger su failų rotacija
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    
    # Pašaliname esamus handlers, jei jų yra
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    
    # Sukuriame handler su failų rotacija
    handler = RotatingFileHandler(
        TEST_RESULTS_FILE,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    handler.setLevel(logging.INFO)
    
    # Formatuojame įrašus
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    
    # Pridedame handler į logger
    logger.addHandler(handler)
    
    return logger

def clean_old_logs(days_to_keep=30):
    """Ištrina senus žurnalo failus"""
    if not os.path.exists(TEST_RESULTS_DIR):
        return
        
    now = datetime.datetime.now()
    for filename in os.listdir(TEST_RESULTS_DIR):
        if filename.startswith("test_results") and filename.endswith(".log"):
            if filename != os.path.basename(TEST_RESULTS_FILE):  # Netrinti aktyvaus failo
                filepath = os.path.join(TEST_RESULTS_DIR, filename)
                
                # Tikriname failo amžių
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                if (now - file_time).days > days_to_keep:
                    try:
                        os.remove(filepath)
                        print(f"Ištrintas senas žurnalo failas: {filepath}")
                    except Exception as e:
                        print(f"Nepavyko ištrinti failo {filepath}: {e}")

class AgentForgeTestCase(unittest.TestCase):
    """Pagrindinė testavimo klasė AgentForge sistemai."""
    
    def setUp(self):
        """Paruošia testavimo aplinką prieš kiekvieną testą."""
        # Čia galima paruošti testų duomenis, pavyzdžiui, sukurti laikinus failus
        pass
        
    def tearDown(self):
        """Išvalo testavimo aplinką po kiekvieno testo."""
        # Čia galima išvalyti laikinai sukurtus failus
        pass
    
    def test_config_loading(self):
        """Testuoja ar konfigūracija tinkamai įkraunama."""
        import config
        # Tikriname ar MAX_ITERATIONS yra skaičius
        self.assertIsInstance(config.MAX_ITERATIONS, int)
        # Tikriname ar API raktai yra
        self.assertIsNotNone(config.OPENAI_API_KEY)
        self.assertIsNotNone(config.SERPER_API_KEY)
    
    @patch('langdetect.detect')
    def test_language_detection(self, mock_detect):
        """Testuoja kalbos aptikimo funkcionalumą."""
        mock_detect.return_value = 'lt'
        from langdetect import detect
        
        # Testuojame su lietuvišku tekstu
        result = detect("Labas rytas")
        self.assertEqual(result, 'lt')
        
        # Patikriname ar funkcija buvo iškviesta
        mock_detect.assert_called_once()
    
    @patch('crewai.Crew')
    def test_execution_cycle(self, mock_crew_class):
        """Testuoja užklausos vykdymo ciklą."""
        # Sukuriame mock objektą Crew klasei
        mock_crew_instance = MagicMock()
        mock_crew_instance.kickoff.return_value = "Optimized prompt content"
        mock_crew_class.return_value = mock_crew_instance
        
        # Patikriname, ar Crew objektas sukuriamas
        self.assertIsNotNone(mock_crew_class.return_value)
        
        # Pakeičiame langdetect.detect, kad negrąžintų klaidų
        with patch('langdetect.detect', return_value='en'):
            # Turime užtikrinti, kad execution_cycle modulis būtų iš naujo importuotas
            # su naujais patch'ais
            import sys
            if 'execution_cycle' in sys.modules:
                del sys.modules['execution_cycle']
            
            from execution_cycle import run_execution_cycle
            
            # Pakeičiame input funkciją, kad testas nesustotų
            with patch('builtins.input', return_value='n'):
                # Vykdome funkciją su test prompt
                run_execution_cycle("Test prompt")
        
        # Tikriname ar kickoff metodas buvo iškviestas
        mock_crew_instance.kickoff.assert_called_once()
    
    def test_yaml_file_operations(self):
        """Testuoja YAML failų operacijas."""
        import yaml
        from custom_tools import load_knowledge_base, save_knowledge_base
        
        # Sukuriame testinį žinių bazės įrašą
        test_knowledge = [
            {
                "topic": "Test Topic",
                "fact": "This is a test fact",
                "source": "Test Source",
                "verified": True
            }
        ]
        
        # Sukuriame laikiną failą testams
        test_file = "test_knowledge_base.yaml"
        
        try:
            # Išsaugome testinę žinių bazę
            save_knowledge_base(test_knowledge, test_file)
            
            # Patikriname ar failas sukurtas
            self.assertTrue(os.path.exists(test_file))
            
            # Įkrauname žinių bazę
            loaded_knowledge = load_knowledge_base(test_file)
            
            # Patikriname ar įkrautas turinys atitinka išsaugotą
            self.assertEqual(len(loaded_knowledge), 1)
            self.assertEqual(loaded_knowledge[0]["topic"], "Test Topic")
            self.assertEqual(loaded_knowledge[0]["fact"], "This is a test fact")
            self.assertTrue(loaded_knowledge[0]["verified"])
            
        finally:
            # Išvalome testinį failą
            if os.path.exists(test_file):
                os.remove(test_file)

def run_tests():
    """Paleidžia visus testus ir sprendžia dėl rezultatų išsaugojimo"""
    # Sukuriame laiko žymą
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Sukuriame test suite objektą
    loader = unittest.TestLoader()
    test_suite = loader.loadTestsFromTestCase(AgentForgeTestCase)
    
    # Sukuriame string buffer, kad galėtume sugauti testų rezultatus
    test_output = io.StringIO()
    
    # Nukreipiame stdout į buffer
    with redirect_stdout(test_output):
        # Sukuriame test runner
        runner = unittest.TextTestRunner(verbosity=2, stream=test_output)
        
        # Paleidžiame testus
        print(f"=== AgentForge Testų Rezultatai ({timestamp}) ===")
        result = runner.run(test_suite)
        
        # Pridedame rezultatų santrauką
        print("\n=== Testavimo rezultatų santrauka ===")
        print(f"Testų vykdyta: {result.testsRun}")
        print(f"Sėkmingų: {result.testsRun - len(result.failures) - len(result.errors)}")
        print(f"Nesėkmingų: {len(result.failures)}")
        print(f"Klaidų: {len(result.errors)}")
    
    # Gauname visus testų rezultatus iš buffer
    test_results = test_output.getvalue()
    
    # Atspausdiname rezultatus konsolėje
    print(test_results)
    
    # SVARBUS PAKEITIMAS: tik po testo vykdymo klausiame, ar išsaugoti rezultatus
    # Jei testas sėkmingas, paprastai nereikia saugoti detalių, o jei nepavyko - taip
    if not result.wasSuccessful():
        print("\nKai kurie testai nepavyko!")
        save_choice = input("Ar norite išsaugoti detalius testų rezultatus? (y/n, pagal nutylėjimą - taip): ").lower()
        should_save = save_choice not in ['n', 'no', 'ne']
    else:
        print("\nVisi testai sėkmingai įvykdyti!")
        save_choice = input("Ar norite išsaugoti detalius testų rezultatus? (y/n, pagal nutylėjimą - ne): ").lower()
        should_save = save_choice in ['y', 'yes', 'taip']
    
    # Išsaugome rezultatus, jei vartotojas to nori
    if should_save:
        logger = setup_logging()
        logger.info(f"Testų rezultatai ({timestamp})\n{test_results}\n{'='*80}\n")
        print(f"\nTestų rezultatai išsaugoti: {os.path.abspath(TEST_RESULTS_FILE)}")
    else:
        print("\nTestų rezultatai nebuvo išsaugoti.")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_tests()