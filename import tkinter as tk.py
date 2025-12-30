import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.resizable(False, False)


tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=10)


tk.Label(root, text="Enter Temperature:").pack()
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)


tk.Label(root, text="Select Unit:").pack()
unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(
    root,
    textvariable=unit_var,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    state="readonly"
)
unit_dropdown.pack(pady=5)
unit_dropdown.current(0)


tk.Button(
    root,
    text="Convert",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    command=convert_temperature
).pack(pady=10)


result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue").pack(pady=10)


root.mainloop()
