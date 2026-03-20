"""Funzioni di persistenza dati su file CSV."""

import csv

FILE_DATI = "dati.csv"
FILE_ANALISI = "analisi.csv"


def salva_dati(dati: list[float], analisi: dict) -> bool:
    """Salva i dati grezzi e il riepilogo statistico in due file CSV."""
    try:
        with open(FILE_DATI, "w", newline="", encoding="utf-8") as file_dati:
            writer = csv.writer(file_dati)
            writer.writerow(["valore"])
            for valore in dati:
                writer.writerow([float(valore)])

        with open(FILE_ANALISI, "w", newline="", encoding="utf-8") as file_analisi:
            writer = csv.writer(file_analisi)
            writer.writerow(["chiave", "valore"])
            for chiave, valore in analisi.items():
                writer.writerow([chiave, valore])

        return True
    except OSError as errore:
        print(f"[ERRORE salvataggio] {errore}")
        return False


def carica_dati() -> tuple[list[float], dict]:
    """
    Carica i file CSV e ricostruisce dati e statistiche.
    Include anche un parsing con split() come fallback su vecchi formati testuali.
    """
    dati: list[float] = []
    analisi: dict = {}

    try:
        with open(FILE_DATI, "r", newline="", encoding="utf-8") as file_dati:
            reader = csv.DictReader(file_dati)
            for riga in reader:
                valore_testo = str(riga.get("valore", "")).strip()
                if valore_testo:
                    dati.append(float(valore_testo))
    except FileNotFoundError:
        pass
    except OSError as errore:
        print(f"[ERRORE caricamento dati] {errore}")
    except ValueError:
        try:
            with open(FILE_DATI, "r", encoding="utf-8") as file_dati:
                contenuto = file_dati.read().strip()
                if contenuto:
                    parti = contenuto.split(",")
                    dati = [float(parte.strip()) for parte in parti if parte.strip()]
        except (OSError, ValueError) as errore:
            print(f"[ERRORE parsing dati] {errore}")

    try:
        with open(FILE_ANALISI, "r", newline="", encoding="utf-8") as file_analisi:
            reader = csv.DictReader(file_analisi)
            for riga in reader:
                chiave = str(riga.get("chiave", "")).strip()
                valore = str(riga.get("valore", "")).strip()
                if not chiave:
                    continue
                try:
                    valore_convertito = int(valore) if valore.isdigit() else float(valore)
                except ValueError:
                    valore_convertito = valore
                analisi[chiave] = valore_convertito
    except FileNotFoundError:
        pass
    except OSError as errore:
        print(f"[ERRORE caricamento analisi] {errore}")

    return dati, analisi
