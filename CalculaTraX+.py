from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox

calcul_possible = 0
état = True

CalculaTraX = tk.Tk()
CalculaTraX.withdraw()  # Masquer la fenêtre principale
messagebox.showinfo("Bienvenue", "Bienvenue dans la CalculaTraX !")

while état == True:
    operation = simpledialog.askstring("CalculaTraX", "Entrez l'opération (+, -, *, /, ²,**, ou 'quit' pour quitter) :")
    if operation is None or operation == "quit":
        break
    if operation == "²":
        premier_nombre = simpledialog.askstring("CalculaTraX", "Entrez le nombre à mettre au carré :")
        if premier_nombre is None:
            break
        try:
            premier_nombre = float(premier_nombre)
        except:
            messagebox.showerror("Erreur", f"'{premier_nombre}' n'est pas un nombre valide.")
            continue
        resultat = premier_nombre * premier_nombre
        calcul_possible = True
    elif operation == "**":
        premier_nombre = simpledialog.askstring("CalculaTraX", "Entrez la base :")
        if premier_nombre is None:
            break
        deuxieme_nombre = simpledialog.askstring("CalculaTraX", "Entrez l'exposant :")
        if deuxieme_nombre is None:
            break
        try:
            premier_nombre = float(premier_nombre)
            deuxieme_nombre = float(deuxieme_nombre)
        except:
            messagebox.showerror("Erreur", f"'{premier_nombre}' ou '{deuxieme_nombre}' n'est pas un nombre valide.")
            continue
        resultat = premier_nombre ** deuxieme_nombre
        calcul_possible = True
    else:
        premier_nombre = simpledialog.askstring("CalculaTraX", "Entrez le premier nombre de l'opération :")
        if premier_nombre is None:
            break
        deuxieme_nombre = simpledialog.askstring("CalculaTraX", "Entrez le deuxième nombre de l'opération :")
        if deuxieme_nombre is None:
            break
        try:
            premier_nombre = float(premier_nombre)
            deuxieme_nombre = float(deuxieme_nombre)
        except:
            messagebox.showerror("Erreur", f"'{premier_nombre}' ou '{deuxieme_nombre}' n'est pas un nombre valide.")
            continue
        if operation == "+":
            resultat = premier_nombre + deuxieme_nombre
            calcul_possible = True
        elif operation == "-":
            resultat = premier_nombre - deuxieme_nombre
            calcul_possible = True
        elif operation == "*":
            resultat = premier_nombre * deuxieme_nombre
            calcul_possible = True
        elif operation == "/":
            if deuxieme_nombre != 0:
                resultat = premier_nombre / deuxieme_nombre
                calcul_possible = True
            else:
                resultat = "Division par zéro"
                calcul_possible = False
        else:
            resultat = "Opération invalide"
            calcul_possible = False

    if calcul_possible == True:
        messagebox.showinfo("Résultat", f"Le résultat de l'opération est : {resultat}")
    else:
        messagebox.showerror("Erreur", f"Erreur : {resultat}")

    while True:
        reponse = simpledialog.askstring("CalculaTraX", "Voulez-vous faire un autre calcul ? (oui/non) :")
        if reponse is None or reponse.lower() == "non":
            état = False
            break
        elif reponse.lower() == "oui":
            état = True
            break
        else:
            messagebox.showerror("Erreur", "Réponse invalide, veuillez répondre par 'oui' ou 'non'.")

messagebox.showinfo("Au revoir", "Merci d'avoir utilisé la CalculaTraX !")
CalculaTraX.destroy()