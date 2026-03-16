"""
dati_manager.py
Funzioni per generare, analizzare, salvare e caricare i dati.
"""

import random

FILE_DATI    = "dati.txt"
FILE_ANALISI = "analisi.txt"


def genera_dati(n: int) -> list[int]:
    """Genera n numeri interi casuali tra 1 e 1000."""
    return [random.randint(1, 1000) for _ in range(n)]


def analizza_dati(dati: list[int]) -> dict:
    """
    Calcola le statistiche sui dati.
    Restituisce un dizionario con: conteggio, minimo, massimo, somma, media.
    """
    if not dati:
        return {}
    return {
        "conteggio": len(dati),
        "minimo":    min(dati),
        "massimo":   max(dati),
        "somma":     sum(dati),
        "media":     round(sum(dati) / len(dati), 2),
    }


def salva_dati(dati: list[int], analisi: dict) -> bool:
    """
    Salva i dati grezzi e le statistiche su file di testo.

    dati.txt    →  numeri separati da virgola su una riga  (es. 12,430,77)
    analisi.txt →  una coppia chiave=valore per riga       (es. media=512.4)
    """
    try:
        with open(FILE_DATI, "w", encoding="utf-8") as f:
            f.write(",".join(str(n) for n in dati))

        with open(FILE_ANALISI, "w", encoding="utf-8") as f:
            for chiave, valore in analisi.items():
                f.write(f"{chiave}={valore}\n")

        return True

    except OSError as e:
        print(f"[ERRORE salvataggio] {e}")
        return False


def carica_dati() -> tuple[list[int], dict]:
    """
    Legge i file e ricostruisce dati e dizionario statistiche.
    Usa split() per separare i valori dalle stringhe lette dal file.
    """
    dati: list[int] = []
    analisi: dict   = {}

    # ── dati grezzi ──────────────────────────────────────
    try:
        with open(FILE_DATI, "r", encoding="utf-8") as f:
            riga = f.read().strip()
            if riga:
                # "12,430,77" → ["12", "430", "77"]
                dati = [int(p) for p in riga.split(",") if p.strip().isdigit()]
    except FileNotFoundError:
        pass
    except (OSError, ValueError) as e:
        print(f"[ERRORE caricamento dati] {e}")

    # ── analisi ──────────────────────────────────────────
    try:
        with open(FILE_ANALISI, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if "=" in riga:
                    # "media=512.4" → chiave="media", valore="512.4"
                    chiave, valore = riga.split("=", 1)
                    try:
                        valore_conv = int(valore) if "." not in valore else float(valore)
                    except ValueError:
                        valore_conv = valore
                    analisi[chiave.strip()] = valore_conv
    except FileNotFoundError:
        pass
    except OSError as e:
        print(f"[ERRORE caricamento analisi] {e}")

    return dati, analisi
