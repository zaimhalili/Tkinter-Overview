"""Modulo OOP per analisi dati numerici."""

import math
from typing import Iterable


class DataAnalyzer:
    """Incapsula una lista di valori numerici e fornisce metodi statistici."""

    def __init__(self, valori: Iterable[float] | None = None):
        """Inizializza l'analizzatore con una sequenza opzionale di valori."""
        self.valori: list[float] = [float(v) for v in valori] if valori else []

    def set_valori(self, valori: Iterable[float]) -> None:
        """Sostituisce i valori interni convertendoli in float."""
        self.valori = [float(v) for v in valori]

    def conteggio(self) -> int:
        """Restituisce il numero di valori presenti."""
        return len(self.valori)

    def media(self) -> float:
        """Restituisce la media aritmetica o 0.0 se la lista è vuota."""
        if not self.valori:
            return 0.0
        return sum(self.valori) / len(self.valori)

    def massimo(self) -> float:
        """Restituisce il massimo o 0.0 se la lista è vuota."""
        if not self.valori:
            return 0.0
        return max(self.valori)

    def minimo(self) -> float:
        """Restituisce il minimo o 0.0 se la lista è vuota."""
        if not self.valori:
            return 0.0
        return min(self.valori)

    def deviazione_standard(self) -> float:
        """Restituisce la deviazione standard della popolazione o 0.0."""
        if not self.valori:
            return 0.0
        media_valori = self.media()
        varianza = sum((numero - media_valori) ** 2 for numero in self.valori) / len(self.valori)
        return math.sqrt(varianza)

    def riepilogo(self) -> dict:
        """Restituisce un dizionario con le principali statistiche."""
        return {
            "conteggio": self.conteggio(),
            "minimo": round(self.minimo(), 2),
            "massimo": round(self.massimo(), 2),
            "media": round(self.media(), 2),
            "deviazione_standard": round(self.deviazione_standard(), 2),
        }