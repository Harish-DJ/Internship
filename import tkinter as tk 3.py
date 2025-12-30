import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def refresh_list():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, c["name"])

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    refresh_list()
    clear_fields()

def select_contact(event):
    try:
        index = listbox.curselection()[0]
        c = contacts[index]
        name_var.set(c["name"])
        phone_var.set(c["phone"])
        email_var.set(c["email"])
    except:
        pass

def update_contact():
    try:
        index = listbox.curselection()[0]
        contacts[index]["name"] = name_var.get()
        contacts[index]["phone"] = phone_var.get()
        contacts[index]["email"] = email_var.get()
        save_contacts()
        refresh_list()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a contact to update")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        contacts.pop(index)
        save_contacts()
        refresh_list()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a contact to delete")

def search_contact():
    keyword = search_var.get().lower()
    listbox.delete(0, tk.END)
    for c in contacts:
        if keyword in c["name"].lower():
            listbox.insert(tk.END, c["name"])

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Management System")
root.geometry("700x400")
root.resizable(False, False)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(root, text="Contact Management System", font=("Arial", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

left = tk.Frame(frame)
left.pack(side="left", padx=20)

right = tk.Frame(frame)
right.pack(side="right", padx=20)

tk.Label(left, text="Search").pack()
tk.Entry(left, textvariable=search_var).pack()
tk.Button(left, text="Search", command=search_contact).pack(pady=5)

listbox = tk.Listbox(left, width=30, height=15)
listbox.pack()
listbox.bind("<<ListboxSelect>>", select_contact)

tk.Label(right, text="Name").pack()
tk.Entry(right, textvariable=name_var, width=30).pack()

tk.Label(right, text="Phone").pack()
tk.Entry(right, textvariable=phone_var, width=30).pack()

tk.Label(right, text="Email").pack()
tk.Entry(right, textvariable=email_var, width=30).pack()

tk.Button(right, text="Add Contact", width=20, command=add_contact, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(right, text="Update Contact", width=20, command=update_contact).pack(pady=5)
tk.Button(right, text="Delete Contact", width=20, command=delete_contact, bg="#f44336", fg="white").pack(pady=5)

refresh_list()
root.mainloop()
