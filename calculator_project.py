import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def apply_sqrt():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(math.sqrt(float(current))))

def apply_sin():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(math.sin(math.radians(float(current)))))

def apply_cos():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(math.cos(math.radians(float(current)))))

def apply_tan():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(math.tan(math.radians(float(current)))))

# Main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x600")


entry = tk.Entry(window, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=20)
button_params = {'font': ('Arial', 14), 'padx': 20, 'pady': 20,}

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'C', '⌫',
    'sin', 'cos', 'tan', 'sqrt'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        window, text=button,
        command=lambda b=button: button_click(b) if b not in {'=', 'sin', 'cos', 'tan', 'sqrt', 'C', '⌫'} else evaluate() if b == '=' else apply_sqrt() if b == 'sqrt' else apply_sin() if b == 'sin' else apply_cos() if b == 'cos' else apply_tan() if b == 'tan' else clear_entry() if b == 'C' else backspace(),
        **button_params
    ).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Main loop
window.mainloop()