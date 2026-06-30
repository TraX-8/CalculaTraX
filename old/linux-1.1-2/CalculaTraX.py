from time import *
def fin():
    print("Merci d'avoir utilisé la CalculaTraX !")
    quit()
print("Bienvenue dans la CalculaTraX !")
def calcul():
    premier_nombre = input("Entrez le premier nombre de l'opération (ou entrez 'quit' pour quitter): ")
    if premier_nombre == "quit":
        fin()
    operation = input("Entrez l'opération (+, -, *, /,²,**) : ")
    if operation == "²":
        try:
            premier_nombre = float(premier_nombre)
        except:
            print(f"{premier_nombre} n'est pas un nombre valide.")
            return
        resultat = premier_nombre * premier_nombre
        calcul_possible = True
    else:
        deuxieme_nombre = input("Entrez le deuxième nombre de l'opération : ")
        try:
            premier_nombre = float(premier_nombre)
            deuxieme_nombre = float(deuxieme_nombre)
        except:
            print(f"{premier_nombre} ou {deuxieme_nombre} n'est pas un nombre valide.")
            return
        if operation == "+":
            resultat = premier_nombre + deuxieme_nombre
            calcul_possible = True
        elif operation == "-":
            resultat = premier_nombre - deuxieme_nombre
            calcul_possible = True
        elif operation == "*":
            resultat = premier_nombre * deuxieme_nombre
            calcul_possible = True
        elif operation == "**":
            resultat = premier_nombre ** deuxieme_nombre
            calcul_possible = True
        elif operation == "quit":
            fin()
        elif operation == "/":
            if deuxieme_nombre != 0:
                resultat = premier_nombre / deuxieme_nombre
                calcul_possible = True
            else:
                resultat = "Division par zéro"
                calcul_possible = False
        else:
            resultat = "Opération invalide."
            calcul_possible = False
    if calcul_possible == True:
        print("Le résultat de l'opération est :", resultat)
    else:
        print(f"Erreur : {resultat}")
def nvcalc():
    sleep(1.5)
    état = input("Voulez-vous faire un autre calcul ? (oui/non) : ")
    if état == "oui" or état == "":
        calcul()
        nvcalc()
    elif état == "non":
        fin()
    else:
        print("Réponse invalide, veuillez répondre par 'oui' ou 'non'.")
        nvcalc()
def calcul_exec():
    calcul()
    nvcalc()
calcul_exec()

