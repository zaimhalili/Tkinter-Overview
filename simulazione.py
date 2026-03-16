"""
random.py
Esperto Simulazione Logica - Funzioni per simulazioni casuali e logiche.
"""

from random import randint, choice, random as random_float, sample
from typing import List, Tuple


def genera_sequenza_casuale(lunghezza: int, min_val: int = 1, max_val: int = 100) -> List[int]:
    """
    Genera una sequenza di numeri casuali tra min_val e max_val.
    
    Args:
        lunghezza: numero di elementi da generare
        min_val: valore minimo (default 1)
        max_val: valore massimo (default 100)
    
    Returns:
        Lista di numeri interi casuali
    """
    return [randint(min_val, max_val) for _ in range(lunghezza)]


def simula_monete(lanci: int) -> Tuple[int, int]:
    """
    Simula il lancio di una moneta.
    
    Args:
        lanci: numero di lanci da simulare
    
    Returns:
        Tupla con (numero_teste, numero_croci)
    """
    teste = sum(1 for _ in range(lanci) if random_float() < 0.5)
    croci = lanci - teste
    return teste, croci


def simula_dadi(lanci: int, facce: int = 6) -> List[int]:
    """
    Simula il lancio di uno o più dadi.
    
    Args:
        lanci: numero di lanci da simulare
        facce: numero di facce del dado (default 6)
    
    Returns:
        Lista con i risultati dei lanci
    """
    return [randint(1, facce) for _ in range(lanci)]


def simula_probabilita(probabilita_successo: float, prove: int) -> Tuple[int, float]:
    """
    Simula un evento con una determinata probabilità di successo.
    
    Args:
        probabilita_successo: probabilità di successo (0.0 - 1.0)
        prove: numero di prove da simulare
    
    Returns:
        Tupla con (numero_successi, percentuale_successi)
    """
    successi = sum(1 for _ in range(prove) if random_float() < probabilita_successo)
    percentuale = (successi / prove * 100) if prove > 0 else 0
    return successi, round(percentuale, 2)


def simula_montecarlo_pi(iterazioni: int) -> float:
    """
    Stima il valore di Pi usando il metodo Monte Carlo.
    
    Args:
        iterazioni: numero di punti casuali da generare
    
    Returns:
        Stima approssimativa di Pi
    """
    dentro_cerchio = 0
    
    for _ in range(iterazioni):
        x = random_float()
        y = random_float()
        distanza = (x**2 + y**2) ** 0.5
        
        if distanza <= 1:
            dentro_cerchio += 1
    
    pi_stimato = (dentro_cerchio / iterazioni) * 4
    return round(pi_stimato, 4)


def simula_campionamento_casuale(popolazione: List[int], dimensione_campione: int) -> List[int]:
    """
    Estrae un campione casuale da una popolazione.
    
    Args:
        popolazione: lista della popolazione
        dimensione_campione: dimensione del campione da estrarre
    
    Returns:
        Campione casuale
    """
    if dimensione_campione > len(popolazione):
        return popolazione
    
    return sample(popolazione, dimensione_campione)


def analizza_distribuzione_casuale(dati: List[int]) -> dict:
    """
    Analizza la distribuzione di dati casuali.
    
    Args:
        dati: lista di numeri
    
    Returns:
        Dizionario con statistiche sulla distribuzione
    """
    if not dati:
        return {}
    
    return {
        "campione_size": len(dati),
        "minimo": min(dati),
        "massimo": max(dati),
        "media": round(sum(dati) / len(dati), 2),
        "range": max(dati) - min(dati),
        "primo_quartile": sorted(dati)[len(dati) // 4],
        "mediana": sorted(dati)[len(dati) // 2],
        "terzo_quartile": sorted(dati)[3 * len(dati) // 4],
    }


def genera_numeri_unici(quantita: int, min_val: int, max_val: int) -> List[int]:
    """
    Genera numeri casuali unici (senza ripetizioni).
    
    Args:
        quantita: quanti numeri generare
        min_val: valore minimo
        max_val: valore massimo
    
    Returns:
        Lista di numeri unici
    """
    if quantita > (max_val - min_val + 1):
        return list(range(min_val, max_val + 1))
    
    return sample(range(min_val, max_val + 1), quantita)


def simula_passeggiata_casuale(passi: int, dimensione_passo: int = 1) -> Tuple[int, float]:
    """
    Simula una passeggiata casuale su una linea.
    
    Args:
        passi: numero di passi da simulare
        dimensione_passo: dimensione di ogni passo
    
    Returns:
        Tupla con (posizione_finale, distanza_media_da_origine)
    """
    posizione = 0
    distanze = []
    
    for _ in range(passi):
        direzione = choice([-1, 1])
        posizione += direzione * dimensione_passo
        distanze.append(abs(posizione))
    
    distanza_media = sum(distanze) / len(distanze) if distanze else 0
    return posizione, round(distanza_media, 2)
