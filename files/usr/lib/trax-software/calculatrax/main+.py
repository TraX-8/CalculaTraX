# CalculaTraX
# Copyright (c) 2026 TraX Software
# Licensed under the MIT License


import tkinter
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from time import sleep
state = True
import calculator.operations, calculator.interface
a = ""
b = ""
operation = ""

def center_window(win, width=None, height=None):
    win.update_idletasks()

    if width is None:
        width = win.winfo_reqwidth()
    if height is None:
        height = win.winfo_reqheight()

    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()

    x = (sw - width) // 2
    y = (sh - height) // 2

    win.geometry(f"{width}x{height}+{x}+{y}")



script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "splash.jpg")

splash = tk.Tk()
splash.overrideredirect(True)
splash.title("CalculaTraX")
splash.configure(background="blue")
splash.resizable(False, False)

if os.path.exists(image_path):
    pil_img = Image.open(image_path)

    # Maximum scale of thumbnail
    pil_img.thumbnail((800, 400), Image.Resampling.LANCZOS)

    img = ImageTk.PhotoImage(pil_img)

    label = tk.Label(splash, image=img, bg="blue")
    label.image = img
    label.pack()

    center_window(
        splash,
        pil_img.width,
        pil_img.height
    )

else:
    label = tk.Label(splash, text="Image introuvable", bg="blue")
    label.pack(expand=True)

    center_window(splash, 400, 200)


splash.after(1500, splash.destroy)
try:
    splash.mainloop()
except tk.TclError:
    pass

root = tk.Tk()
root.withdraw()
root.title("CalculaTraX")

def ttk_message(title="Dialog",
                message="Dialog",
                kind="info",
                width=400,
                height=140):

    symbols = {
        "info": "💡",
        "warning": "⚠️",
        "error": "🚫",
        "joy": "😂",
        "sad": "😭",
        "bruh": "💀🥀",
        "bye": "👋"
    }

    win = tk.Toplevel()
    win.title(title)
    win.resizable(False, False)

    frame = ttk.Frame(win, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(
        frame,
        text=symbols.get(kind, "💡"),
        font=("Noto Color Emoji", 28)
    ).grid(row=0, column=0, sticky="n", padx=(0, 12))
    ttk.Label(
        frame,
        text=message,
        wraplength=width - 120,
        justify="left"
    ).grid(row=0, column=1, sticky="nsew")

    btn = ttk.Button(frame, text="OK", command=win.destroy)
    btn.grid(row=1, column=0, columnspan=2, pady=(12, 0))

    frame.columnconfigure(1, weight=1)

    center_window(win, width, height)

    btn.focus_set()
    win.bind("<Return>", lambda e: win.destroy())
    win.bind("<Escape>", lambda e: win.destroy())

    win.grab_set()
    win.wait_window()



import tkinter as tk
from tkinter import ttk

def ttk_dialog(title="Input",
               message="Enter a value:",
               kind="question",
               width=400,
               height=150,
               default=""):

    symbols = {
        "info": "💡",
        "warning": "⚠️",
        "error": "🚫",
        "joy": "😂",
        "sad": "😭",
        "bruh": "💀🥀",
        "question": "❓"
    }

    result = None

    def validate():
        nonlocal result
        result = entry.get()
        win.destroy()

    def cancel():
        win.destroy()

    win = tk.Toplevel()
    win.title(title)
    win.resizable(False, False)

    frame = ttk.Frame(win, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(
        frame,
        text=symbols.get(kind, "🚫"),
        font=("Noto Color Emoji", 28)
    ).grid(row=0, column=0, rowspan=2, padx=(0, 12), sticky="n")

    ttk.Label(
        frame,
        text=message,
        wraplength=width - 120,
        justify="left"
    ).grid(row=0, column=1, sticky="w")

    entry = ttk.Entry(frame)
    entry.grid(row=1, column=1, sticky="ew", pady=(8, 0))
    entry.insert(0, default)

    frame.rowconfigure(1, weight=1)

    buttons = ttk.Frame(frame)
    buttons.grid(row=2, column=0, columnspan=2, pady=(12, 0))

    ttk.Button(buttons, text="OK", command=validate).pack(side="left", padx=5)
    ttk.Button(buttons, text="Cancel", command=cancel).pack(side="left", padx=5)

    frame.columnconfigure(1, weight=1)

    center_window(win, width, height)

    entry.focus_set()

    win.bind("<Return>", lambda e: validate())
    win.bind("<Escape>", lambda e: cancel())

    win.grab_set()
    win.wait_window()

    return result


def ask_operation():
    """Asks the operation to the user"""
    while True:
        op = ttk_dialog("CalculaTraX", "Enter the operation.")
        if op in ["+", "*", "/", "-", "**"]:
            return op
        ttk_message("Error", f"'{op}' isn't a valid operation sign.")


calculator.interface.appboot("CalculaTraX +", "2026, v1.3 BETA", "TraX")


def close_main_window():
    try:
        if root.winfo_exists():
            root.destroy()
    except:
        pass

ttk_message("Welcome", "CalculaTraX has initialized successfully.")


while state==True:
    while a == "":
        a = ttk_dialog("CalculaTraX", 'Enter the first number (or "quit"): ')
        try :
            a.lower()
        except :
            a = ""

        if a.lower() == "quit":
            ttk_message("Goodbye", "Shutting down.", "bye")
            try:
                state = False
                root.destroy()
            except:
                pass
            quit()
        try:
            int(a)
            a = int(a)
        except:
            ttk_message("CalculaTraX", "Value must be an integer.", "error")
            a = ""

    operation = ask_operation()

    while b == "":
        b = ttk_dialog("CalculaTraX", "Enter the second number: ")
        try:
            int(b)
            b = int(b)
        except:
            ttk_message("CalculaTraX", "Value must be an integer.", "error")
            b = ""
        if operation == "/" and b == 0:
            ttk_message("CalculaTraX", "Error, division by zero.", "error")
            b = ""


    match operation :
        case "+":
            result = calculator.operations.sum(a, b)
            operation_text = "sum"
        case "*":
            result = calculator.operations.multiply(a, b)
            operation_text = "multiplication"
        case "/":
            result = calculator.operations.divide(a, b)
            operation_text = "division"
        case "-":
            result = calculator.operations.subtract(a, b)
            operation_text = "subtraction"
        case "**":
            result = calculator.operations.exponent(a, b)
            operation_text = "power"
        case _ :
            ttk_message("Fatal Error", "Wrong operation sign error : this should not happen. Contact a developer of the app.", "bruh")
            raise SystemExit(1)

    if result == "Err : div by 0":
        ttk_message("Fatal Error", "Division by zero error : this should not happen. Contact a developer of the app.", "bruh")
        print("Error : division by zero. This shouldn't happen.")
        raise SystemExit(1)

    try:
        ttk_message("CalculaTraX", f"The {operation_text} of {a} and {b} is: {result}")
    except:
        ttk_message("A problem has occured, the result can't be shown.", "error")
    
    if state == True:
        a = ""
        b = ""
    else:
        break
close_main_window()
ttk_message("Goodbye", "Shutting down.", "bye")
