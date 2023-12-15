from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import connection_db

def product_management(t):
    if t == 'Aggiungi':
        print('Apro una nuova finestra per aggiungere il prodotto')
    elif t == 'Modifica':
        print('modifico il prodotto selezionato')
    else:
        print('elimino il prodotto selezionato')


sql = 'SELECT * FROM products'
connection_db.cursor.execute(sql)
results = connection_db.cursor.fetchall()

root= Tk()
root.title('Tabella prodotti')
root.geometry("1000x400")

colonne=('id','nome_prodotto', 'codice_prodotto', 'quantità', 'prezzo', 'azione')
tabella=ttk.Treeview(root, columns=colonne, show='headings')

#headings tabella
tabella.heading('id', text='ID')
tabella.heading('nome_prodotto', text='NOME PRODOTTO')
tabella.heading('codice_prodotto', text='CODICE PRODOTTO')
tabella.heading('quantità', text='QUANTITÀ')
tabella.heading('prezzo', text='PREZZO')
tabella.heading('azione', text='AZIONE')

# Quando il widget è più piccolo della cella, viene utilizzato appiccicoso per indicare a quali lati e angoli della cella si attacca il widget. La direzione è definita dalle direzioni della bussola: N, E, S, W, NE, NW, SE e SW e zero.
scrollbar=ttk.Scrollbar(root, orient=VERTICAL, command=tabella.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
tabella.configure(yscrollcommand=scrollbar.set)

addButton = Button(root, text="Aggiungi", command=lambda t= 'Aggiungi': product_management(t)).grid(row=4, column=0) 
editButton = Button(root, text="Modifica", command=lambda t= 'Modifica': product_management(t)).grid(row=5, column=0)
removeButton = Button(root, text="Rimuovi", command=lambda t= 'Rimuovi': product_management(t)).grid(row=6, column=0) 

#corpo tabella
righe=[]
for product in results:
    righe.append((product[0],product[1], product[2],product[3],product[4]))

for riga in righe:
    tabella.insert('', END, values=riga)
    tabella.grid(row=0, column=0, sticky='nsew')

root.mainloop()