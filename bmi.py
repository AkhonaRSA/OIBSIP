import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Enter Weight (kg):").pack()
weight_person = tk.Entry(frame)
weight_person.pack()

tk.Label(frame, text="Enter Height (m):").pack()
height_person = tk.Entry(frame)
height_person.pack()

results = []

def calculate_bmi():
    try:
        weight = float(weight_person.get())
        height = float(height_person.get())
        bmi = weight / (height ** 2)
        category = "Underweight" if bmi < 18.5 else "Normal weight" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
        results.append((bmi, category))
        messagebox.showinfo("BMI Result", f"Your BMI: {bmi:.2f}\nCategory: {category}")
        update_listbox()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

    weight_person.delete(0, 'end')
    height_person.delete(0, 'end')

def update_listbox():
    listbox.delete(0, 'end')
    for i, (bmi, category) in enumerate(results, start=1):
        listbox.insert('end', f"BMI: {bmi:.2f} - Category: {category}")

tk.Button(frame, text="Calculate BMI", command=calculate_bmi).pack()

def show_all_results():
    update_listbox()

show_results_btn = tk.Label(root, text="All Results:")
show_results_btn.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
