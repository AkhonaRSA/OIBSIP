import tkinter as tk
from tkinter import messagebox, Button, Entry, Label, IntVar, Checkbutton
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(pass_length.get())
        if length <= 0:
            messagebox.showerror("Error!!!", "Password length must be greater than 0")
            return

        # Determine which character types to include
        letters = var_letters.get()
        digits = var_digits.get()
        symbols = var_symbols.get()


        characters = ""
        if  letters:
            characters += string.ascii_letters
        if  digits:
            characters += string.digits
        if  symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return


        password = "".join(random.choice(characters) for _ in range(length))

        entry_password.config(state='normal') 
        entry_password.delete(0, 'end')
        entry_password.insert(0, password)
        entry_password.config(state='readonly') 

        #clipboard
        pyperclip.copy(password)
        messagebox.showinfo("Clipboard", "Password copied to clipboard.")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length")

root = tk.Tk()
root.title("Password Generator")

Label(root, text="Password Length:").pack()
pass_length = Entry(root)
pass_length.pack()

var_letters = IntVar()
var_digits = IntVar()
var_symbols = IntVar()

Checkbutton(root, text="Include Letters", variable=var_letters).pack()
Checkbutton(root, text="Include Digits", variable=var_digits).pack()
Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

Button(root, text="Generate Password", command=generate_password).pack()

#generated password
Label(root, text="Your Generated Password Below:").pack()
entry_password = Entry(root, state='readonly')
entry_password.pack()

root.mainloop()
