import authentication
from tkinter import *
from functools import partial
from tkinter import messagebox

def close(): 
    tkWindow.destroy() 
    
def validateLogin(username, password):
    check = authentication.authentication_function(username, password)
    if check == True:
        messagebox.showinfo(icon = 'info', title='Info', message='Autorizzazione concessa')
        close()
        tkWindow_products = Tk()
        tkWindow_products.geometry('600x900')  
        tkWindow_products.title('Gestione prodotti')
        
    else:
        messagebox.showerror(icon = "warning", title='Attenzione!', message='Non hai accesso a questo servizio')

# Window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Accesso al magazzino')

# Username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# Password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

# Login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

if __name__ == '__main__':
    tkWindow.mainloop()