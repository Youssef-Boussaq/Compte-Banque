from compte import Compte
from compteCaurrant import compteCourant
from compteEpargne import compteEpargne
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import os

gui = Tk()

gui.geometry("700x500")

gui.configure(bg='#eee')  # Set window color to blue

gui.title("Banque J'oshef")

# Initialize Sequential account number
account_number = 0

# Load the last account number from the JSON file
if os.path.exists('comptes.json'):
    with open('comptes.json', 'r') as f:
        lines = f.readlines()
        if lines:
            last_account = json.loads(lines[-1])
            account_number = last_account["Numéro de compte"]

# Create a StringVar to hold the account number
account_number_var = StringVar()

# Create a label with the account number
account_number_label = Label(gui, textvariable=account_number_var)
account_number_label.grid(row=0, column=0)

Label(gui, text="Propriétaire").grid(row=1, column=0)
pro = Entry(gui)
pro.grid(row=1, column=1)

Label(gui, text="Solde").grid(row=2, column=0)
sold = Entry(gui)
sold.grid(row=2, column=1)
Label(gui, text="Ero").grid(row=2, column=2)

def ckeked(*args):
    if selected.get() == 'Epargne':
        entret.config(state=DISABLED)
        mda.config(state=NORMAL)
    else:
        mda.config(state=DISABLED)
        entret.config(state=NORMAL)

Label(gui, text="Type de compte").grid(row=4, column=0)
selected = StringVar()
selected.trace('w', ckeked)

# Create radio buttons
r1 = Radiobutton(gui, text='Epargne', value='Epargne', variable=selected)
r2 = Radiobutton(gui, text='Courant', value='Courant', variable=selected)

r1.grid(row=4, column=1)
r2.grid(row=4, column=2)

Label(gui, text="Intérêt").grid(row=5, column=0)
entret = Entry(gui)
entret.grid(row=5, column=1)

Label(gui, text="MDA").grid(row=6, column=0)
mda = Entry(gui)
mda.grid(row=6, column=1)

# Create Treeview
tree = ttk.Treeview(gui)
tree["columns"]=("one","two","three","four","five")
tree.column("#0", width=100)
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column("five", width=100)
tree.heading("#0",text="Numéro de compte")
tree.heading("one", text="Propriétaire")
tree.heading("two", text="Type de compte")
tree.heading("three", text="MDA")
tree.heading("four", text="Intérêt")
tree.grid(row=8, column=0, columnspan=4)

# Function to print account details
def create_account():
    global account_number
    account_number += 1
    account_number_var.set("Numéro de compte: " + str(account_number))
    print("Numéro de compte: ", account_number)
    print("Propriétaire: ", pro.get())
    print("Solde: ", sold.get())
    print("Type de compte: ", selected.get())
    print("Intérêt: ", entret.get())
    print("MDA: ", mda.get())
    tree.insert('', 'end', text=str(account_number), values=(pro.get(), selected.get(), mda.get(), entret.get()))
    
    # Save account details to JSON file
    account_details = {
        "Numéro de compte": account_number,
        "Propriétaire": pro.get(),
        "Solde": sold.get(),
        "Type de compte": selected.get(),
        "Intérêt": entret.get(),
        "MDA": mda.get()
    }
    with open('comptes.json', 'a') as f:
        json.dump(account_details, f)
        f.write('\n')

# Create account button
create_button = Button(gui, text="Créer un compte", command=create_account)
create_button.grid(row=7, column=0)

gui.mainloop()
