import math


class DataAnalyzer:
    def __init__(self):
        self.dati = []

    def genera_dati(self, quantita):
        self.dati = []

        for i in range(quantita):
            numero = (i + 1) * 2
            self.dati.append(numero)

        return self.dati

    def media(self):
        if len(self.dati) == 0:
            return 0

        somma = sum(self.dati)
        return somma / len(self.dati)

    def massimo(self):
        if len(self.dati) == 0:
            return 0

        return max(self.dati)

    def minimo(self):
        if len(self.dati) == 0:
            return 0

        return min(self.dati)

    def deviazione_standard(self):
        if len(self.dati) == 0:
            return 0

        m = self.media()
        somma_scarti = 0

        for numero in self.dati:
            somma_scarti += (numero - m) ** 2

        varianza = somma_scarti / len(self.dati)
        return math.sqrt(varianza)

    def salva_su_file(self, nome_file="dati_salvati.txt"):
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write("Dati generati:\n")
            file.write(str(self.dati) + "\n\n")
            file.write("Media: " + str(self.media()) + "\n")
            file.write("Massimo: " + str(self.massimo()) + "\n")
            file.write("Minimo: " + str(self.minimo()) + "\n")
            file.write("Deviazione standard: " + str(round(self.deviazione_standard(), 2)) + "\n")