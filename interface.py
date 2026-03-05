import tkinter as ttk

root = ttk.Tk()

ttk.Label(root, text="Project Smart").grid(row = 0, column = 0)
ttk.Label(root, text="Project Smart").grid(row = 0, column = 0)

entry1 = ttk.Entry(root)
entry2 = ttk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()


