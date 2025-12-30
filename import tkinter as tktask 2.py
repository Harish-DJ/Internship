import tkinter as tk
import random
from tkinter import messagebox
secret = random.randint(1, 100)
attempts = 0
def check():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < secret:
            result.set("Too Low ⬇️")
        elif guess > secret:
            result.set("Too High ⬆️")
        else:
            messagebox.showinfo(
                "You Won!",
                f"Correct number: {secret}\nAttempts: {attempts}"
            )
            restart()
    except:
        messagebox.showerror("Error", "Enter a valid number")
def restart():
    global secret, attempts
    secret = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result.set("New game started 🎯")
root = tk.Tk()
root.title("Guessing Game")
root.geometry("350x280")
root.resizable(False, False)
tk.Label(root, text="Number Guessing Game", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Guess a number between 1 and 100").pack()
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=8)
tk.Button(root, text="Check Guess", command=check, bg="#4CAF50", fg="white").pack(pady=10)
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue").pack(pady=10)
tk.Button(root, text="Restart Game", command=restart).pack()
root.mainloop()
