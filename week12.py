# import tkinter as tk
# Exercise 1

# from tkinter import messagebox


# def get_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         return num1, num2
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")
#         return None


# def add():
#     values = get_numbers()
#     if values:
#         num1, num2 = values
#         result_var.set(f"Sum: {num1 + num2}")


# def subtract():
#     values = get_numbers()
#     if values:
#         num1, num2 = values
#         result_var.set(f"Difference: {num1 - num2}")


# def multiply():
#     values = get_numbers()
#     if values:
#         num1, num2 = values
#         result_var.set(f"Product: {num1 * num2}")

# # Main window
# root = tk.Tk()
# root.title("Calculator")
# root.geometry("300x180")

# # Labels and entries
# tk.Label(root, text="First number:").grid(row=0, column=0, padx=10, pady=10)
# entry1 = tk.Entry(root)
# entry1.grid(row=1, column=0)

# tk.Label(root, text="Second number:").grid(row=0, column=2, padx=10, pady=10)
# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=2)

# # Buttons
# tk.Button(root, text="+", width=8, command=add).grid(row=0, column=1, pady=5)
# tk.Button(root, text="-", width=8, command=subtract).grid(row=1, column=1, pady=5)
# tk.Button(root, text="×", width=8, command=multiply).grid(row=2, column=1, pady=5)

# # Result
# result_var = tk.StringVar()
# result_var.set("Result:")

# tk.Label(root, textvariable=result_var,
#          relief="sunken", width=25).grid(row=3, column=0,
#                                          columnspan=3, pady=15)

# root.mainloop()

# Exercise 2
import tkinter as tk
from tkinter import messagebox


def load_oceans():
    try:
        # Read oceans from file
        with open("oceans.txt", "r") as file:
            oceans = [line.strip() for line in file if line.strip()]

        if not oceans:
            messagebox.showerror("Error", "The file is empty.")
            return

      
        oceans.sort()

     
        listbox.delete(0, tk.END)
        for ocean in oceans:
            listbox.insert(tk.END, ocean)

    except FileNotFoundError:
        messagebox.showerror("Error", "oceans.txt was not found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("Oceans")
root.geometry("250x250")


listbox = tk.Listbox(root, width=20, height=10)
listbox.pack(pady=10)


load_button = tk.Button(root, text="Load Oceans", command=load_oceans)
load_button.pack()

root.mainloop()