import tkinter as tk
from tkinter import messagebox

# Input Validation for the user input


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# When the calculate button is clicked


def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operator = operator_var.get()

    if not is_valid_number(num1):
        messagebox.showerror("Invalid Input", "Operant 1 is not valid")
        return

    if operator not in ['+', '-', '*', '/']:
        messagebox.showerror("Invalid Operator",
                             "Please select a valid operator (+, -, *, /).")
        return

    if not is_valid_number(num2):
        messagebox.showerror("Invalid Input", "Operand 2 is not valid.")
        return

    num1 = float(num1)
    num2 = float(num2)

    if operator == '/' and num2 == 0:
        messagebox.showerror("Math Error", "Can not divide by zero.")
        return

# Calculations the operator will perform
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    result_label.config(text=f"Result: {num1} {operator} {num2} = {result}")

# When Clear button is clicked


def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operator_var.set('')
    result_label.config(text="Result:")


# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x300")

# First number
tk.Label(window, text="Enter first number:").pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

# Operator
tk.Label(window, text="Choose operator (+, -, *, /):").pack()
operator_var = tk.StringVar()
operator_menu = tk.OptionMenu(window, operator_var, '+', '-', '*', '/')
operator_menu.pack()

# Second number
tk.Label(window, text="Enter second number:").pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Buttons for operations
tk.Button(window, text="Calculate", command=calculate).pack(pady=5)
tk.Button(window, text="Clear", command=clear_fields).pack()

# Display result to the user
result_label = tk.Label(window, text="Result:")
result_label.pack(pady=10)

# "End" button to close window
tk.Button(window, text="End", command=window.quit).pack()

# Run the app
window.mainloop()
