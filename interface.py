import tkinter as tk
from tkinter import ttk

from CSVcreationFile import carica_dati, salva_dati
from Models.DataAnalyser import DataAnalyzer
from simulazione import genera_misurazioni_industriali

# Styles
BG        = "#1e1e2e"
PANEL     = "#2a2a3d"
ACCENT    = "#7c5cbf"
ACCENT_HV = "#9b7de0"
TEXT      = "#e0e0f0"
SUBTEXT   = "#a0a0c0"
ENTRY_BG  = "#2f2f45"
FONT_TITLE  = ("Segoe UI", 20, "bold")
FONT_SUB    = ("Segoe UI", 9)
FONT_LABEL  = ("Segoe UI", 11)
FONT_BTN    = ("Segoe UI", 10, "bold")
FONT_RESULT = ("Consolas", 11)

root = tk.Tk()
root.title("Project Smart")
root.configure(bg=BG)
root.resizable(False, False)

dati_correnti: list[float] = []
analisi_corrente: dict = {}


style = ttk.Style(root)
style.theme_use("clam")
style.configure("Accent.TButton",
                background=ACCENT, foreground=TEXT,
                font=FONT_BTN, padding=(14, 8),
                relief="flat", borderwidth=0)
style.map("Accent.TButton",
          background=[("active", ACCENT_HV)],
          relief=[("active", "flat")])


header = tk.Frame(root, bg=PANEL, pady=18)
header.pack(fill="x")

tk.Label(header, text="Project Smart", font=FONT_TITLE,
         bg=PANEL, fg=TEXT).pack()
tk.Label(header, text="Realizzato da Daniel, Hedijan, Nikolai, Zaim",
         font=FONT_SUB, bg=PANEL, fg=SUBTEXT).pack(pady=(2, 0))

tk.Frame(root, height=2, bg=ACCENT).pack(fill="x")

# Body
body = tk.Frame(root, bg=BG, padx=30, pady=24)
body.pack(fill="both")

# Input
input_frame = tk.Frame(body, bg=BG)
input_frame.pack(fill="x", pady=(0, 18))

tk.Label(input_frame, text="Numero di valori:", font=FONT_LABEL,
         bg=BG, fg=TEXT).pack(side="left", padx=(0, 12))

entry1 = tk.Entry(input_frame, font=FONT_LABEL,
                  bg=ENTRY_BG, fg=TEXT, insertbackground=TEXT,
                  relief="flat", bd=6, width=12)
entry1.pack(side="left")

# Buttons
btn_frame = tk.Frame(body, bg=BG)
btn_frame.pack(pady=(0, 22))

# Risultati
tk.Frame(root, height=1, bg=PANEL).pack(fill="x")

result_outer = tk.Frame(root, bg=PANEL, padx=30, pady=18)
result_outer.pack(fill="both")

tk.Label(result_outer, text="Risultati", font=FONT_LABEL,
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")

result_box = tk.Frame(result_outer, bg=ENTRY_BG, pady=10, padx=14)
result_box.pack(fill="x", pady=(6, 0))

result_text = tk.StringVar(value="Nessun dato caricato.")
tk.Label(result_box, textvariable=result_text, font=FONT_RESULT,
         bg=ENTRY_BG, fg=TEXT, anchor="w", justify="left", wraplength=460).pack(fill="x")

status_text = tk.StringVar(value="Pronto")
tk.Label(result_outer, textvariable=status_text, font=FONT_SUB,
         bg=PANEL, fg=SUBTEXT).pack(anchor="w", pady=(8, 0))


def aggiorna_output() -> None:
    """Aggiorna il box risultati con dati e analisi correnti."""
    if not dati_correnti:
        result_text.set("Nessun dato disponibile.")
        return

    valori_preview = ", ".join(str(int(v)) if float(v).is_integer() else f"{v:.2f}" for v in dati_correnti[:20])
    if len(dati_correnti) > 20:
        valori_preview += ", ..."

    righe = [f"Dati ({len(dati_correnti)}): {valori_preview}"]
    if analisi_corrente:
        righe.extend(
            [
                f"Media: {analisi_corrente.get('media', 0)}",
                f"Minimo: {analisi_corrente.get('minimo', 0)}",
                f"Massimo: {analisi_corrente.get('massimo', 0)}",
                f"Deviazione std: {analisi_corrente.get('deviazione_standard', 0)}",
            ]
        )
    result_text.set("\n".join(righe))


def genera_dati_click() -> None:
    """Genera nuovi dati tramite il modulo di simulazione."""
    global dati_correnti, analisi_corrente

    testo = entry1.get().strip()
    try:
        quantita = int(testo)
        if quantita <= 0:
            raise ValueError
    except ValueError:
        status_text.set("Inserisci un numero intero positivo.")
        return

    valori, stati = genera_misurazioni_industriali(quantita)
    dati_correnti = [float(v) for v in valori]
    analisi_corrente = {}

    fuori_range = sum(1 for stato in stati if stato != "OK")
    status_text.set(f"Generati {quantita} valori ({fuori_range} fuori range).")
    aggiorna_output()


def analizza_dati_click() -> None:
    """Analizza i dati correnti con la classe OOP DataAnalyzer."""
    global analisi_corrente

    if not dati_correnti:
        status_text.set("Genera o carica prima dei dati.")
        return

    analizzatore = DataAnalyzer(dati_correnti)
    analisi_corrente = analizzatore.riepilogo()
    status_text.set("Analisi completata con successo.")
    aggiorna_output()


def salva_dati_click() -> None:
    """Salva dati e analisi in file CSV."""
    if not dati_correnti:
        status_text.set("Nessun dato da salvare.")
        return

    if not analisi_corrente:
        analizza_dati_click()

    if salva_dati(dati_correnti, analisi_corrente):
        status_text.set("Salvataggio completato: dati.csv e analisi.csv")
    else:
        status_text.set("Errore durante il salvataggio.")


ttk.Button(btn_frame, text="Genera Dati", style="Accent.TButton", command=genera_dati_click).pack(side="left", padx=8)
ttk.Button(btn_frame, text="Analizza Dati", style="Accent.TButton", command=analizza_dati_click).pack(side="left", padx=8)
ttk.Button(btn_frame, text="Salva Dati", style="Accent.TButton", command=salva_dati_click).pack(side="left", padx=8)


def carica_all_avvio() -> None:
    """Carica eventuali dati salvati all'avvio dell'app."""
    global dati_correnti, analisi_corrente
    dati, analisi = carica_dati()
    dati_correnti = dati
    analisi_corrente = analisi
    if dati_correnti:
        status_text.set(f"Caricati {len(dati_correnti)} valori da file.")
    else:
        status_text.set("Nessun file trovato: inizia generando nuovi dati.")
    aggiorna_output()


carica_all_avvio()

# Footer
tk.Frame(root, height=2, bg=ACCENT).pack(fill="x")
tk.Label(root, text="Project Smart © 2025", font=FONT_SUB,
         bg=BG, fg=SUBTEXT).pack(pady=8)

root.mainloop()


