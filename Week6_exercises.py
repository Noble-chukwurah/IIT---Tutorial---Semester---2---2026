
import tkinter as tk
from tkinter import ttk

def compute():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        operation = operation_box.get()

        if operation == "+":
            result = num1 + num2 + num3
        elif operation == "-":
            result = num1 - num2 - num3
        elif operation == "×":
            result = num1 * num2 * num3
        elif operation == "÷":
            if num2 == 0 or num3 == 0:
                result_label.config(text="Error: Cannot divide by zero")
                return
            result = num1 / num2 / num3
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers")


root = tk.Tk()
root.title("Mini Calculator (3 Inputs)")


tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number 3:").grid(row=2, column=0, padx=5, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)


tk.Label(root, text="Operation:").grid(row=3, column=0, padx=5, pady=5)
operation_box = ttk.Combobox(root, values=["+", "-", "×", "÷"])
operation_box.grid(row=3, column=1, padx=5, pady=5)
operation_box.current(0)


compute_button = tk.Button(root, text="Compute", command=compute)
compute_button.grid(row=4, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
