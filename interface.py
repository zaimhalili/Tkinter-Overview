import tkinter as tk
from tkinter import ttk

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

for label in ("Genera Dati", "Analizza Dati", "Salva Dati"):
    ttk.Button(btn_frame, text=label, style="Accent.TButton").pack(
        side="left", padx=8)

# Risultati
tk.Frame(root, height=1, bg=PANEL).pack(fill="x")

result_outer = tk.Frame(root, bg=PANEL, padx=30, pady=18)
result_outer.pack(fill="both")

tk.Label(result_outer, text="Risultati", font=FONT_LABEL,
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")

data = "123, 3, 2"
result_box = tk.Frame(result_outer, bg=ENTRY_BG, pady=10, padx=14)
result_box.pack(fill="x", pady=(6, 0))

tk.Label(result_box, text=data, font=FONT_RESULT,
         bg=ENTRY_BG, fg=TEXT, anchor="w",
         justify="left", wraplength=400).pack(fill="x")

# Footer
tk.Frame(root, height=2, bg=ACCENT).pack(fill="x")
tk.Label(root, text="Project Smart © 2025", font=FONT_SUB,
         bg=BG, fg=SUBTEXT).pack(pady=8)

root.mainloop()


