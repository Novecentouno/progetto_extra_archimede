from tkinter import *
from tkinter import ttk

warehouse_window = Tk()
warehouse_window.title('Gestione Magazzino')
warehouse_window.geometry("600x400")

nb = ttk.Notebook(warehouse_window)
nb.pack(pady=10, fill=BOTH, expand=True)

# Frame 1 and 2
frame1 = ttk.Frame(nb, width=500, height=300)
frame2 = ttk.Frame(nb, width=500, height=300)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

label1 = Label(frame1, text = "Gestione Prodotti")
label1.pack()

label2 = Label(frame2, text = "Gestione Ordini")
label2.pack()

nb.add(frame1, text = "Prodotti")
nb.add(frame2, text = "Ordini")


warehouse_window.mainloop()