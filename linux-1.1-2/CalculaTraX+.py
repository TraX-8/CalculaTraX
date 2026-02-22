from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox

calcul_possible = False
état = True

CalculaTraX = tk.Tk()
CalculaTraX.withdraw()  # Masquer la fenêtre principale
messagebox.showinfo("Bienvenue", "Bienvenue dans la CalculaTraX !")

while état:
    premier_nombre = simpledialog.askstring("CalculaTraX", "Entrez le premier nombre (ou 'quit' pour quitter) :")
    if premier_nombre is None or premier_nombre.lower() == "quit":
        break

    try:
        premier_nombre = float(premier_nombre)
    except:
        messagebox.showerror("Erreur", f"'{premier_nombre}' n'est pas un nombre valide.")
        continue

    operation = simpledialog.askstring("CalculaTraX", "Entrez l'opération (+, -, *, /, ², **) :")
    if operation is None or operation == "quit":
        break

    # Cas carré
    if operation == "²":
        resultat = premier_nombre * premier_nombre
        calcul_possible = True

    # Cas puissance
    elif operation == "**":
        deuxieme_nombre = simpledialog.askstring("CalculaTraX", "Entrez l'exposant :")
        if deuxieme_nombre is None:
            break
        try:
            deuxieme_nombre = float(deuxieme_nombre)
        except:
            messagebox.showerror("Erreur", f"'{deuxieme_nombre}' n'est pas un nombre valide.")
            continue
        resultat = premier_nombre ** deuxieme_nombre
        calcul_possible = True

    # Cas + - * /
    elif operation in ["+", "-", "*", "/"]:
        deuxieme_nombre = simpledialog.askstring("CalculaTraX", "Entrez le deuxième nombre :")
        if deuxieme_nombre is None:
            break
        try:
            deuxieme_nombre = float(deuxieme_nombre)
        except:
            messagebox.showerror("Erreur", f"'{deuxieme_nombre}' n'est pas un nombre valide.")
            continue

        if operation == "+":
            resultat = premier_nombre + deuxieme_nombre
        elif operation == "-":
            resultat = premier_nombre - deuxieme_nombre
        elif operation == "*":
            resultat = premier_nombre * deuxieme_nombre
        elif operation == "/":
            if deuxieme_nombre != 0:
                resultat = premier_nombre / deuxieme_nombre
            else:
                resultat = "Division par zéro"
                calcul_possible = False

        calcul_possible = resultat != "Division par zéro"

    else:
        resultat = "Opération invalide"
        calcul_possible = False

    if calcul_possible:
        messagebox.showinfo("Résultat", f"Le résultat de l'opération est : {resultat}")
    else:
        messagebox.showerror("Erreur", f"Erreur : {resultat}")

    while True:
        reponse = simpledialog.askstring("CalculaTraX", "Voulez-vous faire un autre calcul ? (oui/non) :")
        if reponse is None or reponse.lower() == "non":
            état = False
            break
        elif reponse.lower() == "oui":
            break
        else:
            messagebox.showerror("Erreur", "Réponse invalide, veuillez répondre par 'oui' ou 'non'.")

messagebox.showinfo("Au revoir", "Merci d'avoir utilisé la CalculaTraX !")
CalculaTraX.destroy()

