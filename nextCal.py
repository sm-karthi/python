import tkinter as tk
import math

# Track if a calculation was just performed
calculated = False

# Functions for calculator operations
def press(key):
    global calculated
    current_text = entry.get()
    # Clear "Error" or the result if a new number is clicked
    if current_text == "Error" or calculated:
        entry.delete(0, tk.END)
        calculated = False
    entry.insert(tk.END, str(key))

def calculate():
    global calculated
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        calculated = True  # Mark that a calculation was performed
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    global calculated
    entry.delete(0, tk.END)
    calculated = False  # Reset the flag

def backspace():
    global calculated
    current_text = entry.get()
    if current_text != "Error":
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])
    calculated = False  # Reset the flag

def square():
    global calculated
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        calculated = True  # Mark that a calculation was performed
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    global calculated
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        calculated = True  # Mark that a calculation was performed
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Entry field for the calculator
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Button layout
buttons = [
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*', 'x²',
    '1', '2', '3', '-', '←',
    'C', '0', '=', '+'
]

# Create and place buttons
row_val, col_val = 1, 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, font=("Arial", 18), bg="#4caf50", fg="white", command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, font=("Arial", 18), bg="#f44336", fg="white", command=clear)
    elif button == "←":
        btn = tk.Button(root, text=button, font=("Arial", 18), command=backspace)
    elif button == "x²":
        btn = tk.Button(root, text=button, font=("Arial", 18), command=square)
    elif button == "√":
        btn = tk.Button(root, text=button, font=("Arial", 18), command=square_root)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: press(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Configure row and column weights for proper alignment
for i in range(row_val + 1):  # Number of rows used
    root.rowconfigure(i, weight=1)
for i in range(5):  # 5 columns used
    root.columnconfigure(i, weight=1)

# Run the application
root.mainloop()