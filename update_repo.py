# /AgentForge/update_repo.py

"""
Scenarijus, skirtas automatizuotam GitHub repozitorijos atnaujinimui.

Šis scenarijus atlieka tris pagrindines Git komandas:
1. `git add .` - prideda visus pakeistus failus.
2. `git commit -m "Jūsų komentaras"` - įamžina pakeitimus su pateiktu komentaru.
3. `git push` - nusiunčia pakeitimus į nuotolinę repozitoriją.

Kaip naudoti:
1. Iš terminalo: python update_repo.py "Čia rašomas jūsų komentaras"
2. Paleidus be argumento: python update_repo.py
   (scenarijus paprašys įvesti komentarą interaktyviai)
"""

import sys
import subprocess

def run_command(command):
    """Vykdo komandą terminale ir grąžina rezultatą bei klaidą."""
    # `subprocess.run` yra modernus ir saugus būdas vykdyti komandas.
    # `capture_output=True` sugauna viską, ką komanda spausdina.
    # `text=True` paverčia išvestį į tekstą.
    # `check=True` automatiškai išmes klaidą, jei komanda nepavyks.
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
        print(result.stdout) # Spausdiname sėkmingą išvestį
        return True
    except subprocess.CalledProcessError as e:
        # Jei komanda nepavyko, spausdiname klaidos pranešimą.
        print("!!! KOMANDOS VYKDYMO KLAIDA !!!")
        print(f"Komanda: {' '.join(e.cmd)}")
        print(f"Grąžos kodas: {e.returncode}")
        print(f"Standartinė išvestis (stdout):\n{e.stdout}")
        print(f"Klaidos išvestis (stderr):\n{e.stderr}")
        return False
    except FileNotFoundError:
        print("!!! KLAIDA: `git` komanda nerasta. Įsitikinkite, kad Git yra įdiegtas ir pasiekiamas sistemos PATH.")
        return False


def main():
    """Pagrindinė scenarijaus funkcija."""
    # 1. Gauname 'commit' komentarą.
    # Patikriname, ar komentaras buvo pateiktas kaip argumentas komandinėje eilutėje.
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        # Jei argumento nėra, paprašome vartotojo įvesti komentarą.
        commit_message = input("Įveskite 'commit' komentarą: ")

    # Patikriname, ar komentaras není tuščias.
    if not commit_message:
        print("Klaida: 'commit' komentaras negali būti tuščias. Atnaujinimas atšauktas.")
        return # Nutraukiame scenarijaus vykdymą

    print("=============================================")
    print("  Pradedamas GitHub repozitorijos atnaujinimas ")
    print("=============================================\n")


    # 2. Vykdome Git komandas žingsnis po žingsnio.
    print("--- 1/3: Pridedami failai (git add .) ---")
    if not run_command(["git", "add", "."]):
        return # Sustojame, jei įvyko klaida

    print(f"\n--- 2/3: Įamžinami pakeitimai (git commit) ---")
    # Formuojame 'commit' komandą su gautu komentaru.
    if not run_command(["git", "commit", "-m", commit_message]):
        return # Sustojame, jei įvyko klaida

    print("\n--- 3/3: Siunčiama į nuotolinę repozitoriją (git push) ---")
    if not run_command(["git", "push"]):
        return # Sustojame, jei įvyko klaida
    
    print("\n✅ Repozitorija sėkmingai atnaujinta!")


if __name__ == "__main__":
    main()