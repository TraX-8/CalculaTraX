#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

app_name = "CalculaTraX"

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(app_name)
        self.geometry("300x400")
        self.resizable(False, False)
        self.configure(bg="#000000")

        self.expression = ""

        # Écran (lecture seule)
        self.display = tk.Entry(
            self,
            font=("Adwaita", 20),
            bd=10,
            relief="flat",
            justify="right",
            bg="#0A0A0A",
            fg="#d65302",
            readonlybackground="#0d1c66",
            state="readonly"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        self.create_buttons()

        # Active le clavier
        self.focus_set()
        self.bind("<Key>", self.on_key_press)

    # ------------------------
    # Création des boutons
    # ------------------------
    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "x"],
            ["1", "2", "3", "-"],
            ["0", ".", "**", "+"],
            ["²", "C", "=", "Quit"]
        ]

        for row_values in buttons:
            row = tk.Frame(self, bg="#1e1e1e")
            row.pack(expand=True, fill="both")

            for btn_text in row_values:
                btn = tk.Button(
                    row,
                    text=btn_text,
                    font=("Arial", 18),
                    bd=0,
                    fg="#d65302",
                    bg="#0d1c66",
                    activebackground="#041540",
                    command=lambda val=btn_text: self.on_button_click(val)
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    # ------------------------
    # Gestion boutons souris
    # ------------------------
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""

        elif char == "=":
            self.calculate()
            return

        elif char == "²":
            try:
                value = float(self.expression)
                self.expression = str(value ** 2)
            except:
                self.display_error("Entrée invalide")
                return

        elif char == "Quit":
            self.quit()

        else:
            if char == "x":
                char = "*"
            self.expression += str(char)

        self.update_display()

    # ------------------------
    # Gestion clavier
    # ------------------------
    def on_key_press(self, event):
        touche = event.char

        # Pavé numérique
        if event.keysym.startswith("KP_"):
            val = event.keysym.replace("KP_", "")

            mapping = {
                "Add": "+",
                "Subtract": "-",
                "Multiply": "*",
                "Divide": "/",
                "Decimal": ".",
            }

            if val in "0123456789":
                self.expression += val
            elif val in mapping:
                self.expression += mapping[val]

            self.update_display()
            return

        # Touches normales
        if touche in "0123456789+-*/.x":
            if touche == "x":
                touche = "*"
            self.expression += touche

        elif touche == "^":  # puissance rapide
            self.expression += "**"

        elif event.keysym == "Return" or event.keycode == 104:
            self.calculate()
            return

        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]

        elif event.keysym == "Escape":
            self.expression = ""

        self.update_display()

    # ------------------------
    # Calcul
    # ------------------------
    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_error("Division par zéro")
            return
        except:
            self.display_error("Erreur de calcul")
            return

        self.update_display()

    # ------------------------
    # Mise à jour écran
    # ------------------------
    def update_display(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state="readonly")

    # ------------------------
    # Gestion erreurs
    # ------------------------
    def display_error(self, message):
        messagebox.showerror("Erreur", message)
        self.expression = ""
        self.update_display()


# ------------------------
# Lancement de l'application
# ------------------------
if __name__ == "__main__":
    app = Calculator()
    messagebox.showinfo("Bienvenue", f"Bienvenue dans {app_name} !")
    app.mainloop()

