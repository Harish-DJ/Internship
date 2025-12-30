import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import csv

def scrape_products():
    try:
        for row in tree.get_children():
            tree.delete(row)

        url = "https://books.toscrape.com/catalogue/page-1.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        data = []

        for product in products:
            name = product.h3.a["title"]
            price = product.find("p", class_="price_color").text.replace("£", "")
            rating = product.p["class"][1]

            data.append([name, price, rating])
            tree.insert("", tk.END, values=(name, price, rating))

        with open("products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price (£)", "Rating"])
            writer.writerows(data)

        status_label.config(text=f"Scraped {len(data)} products • Saved to products.csv")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("E-commerce Product Scraper")
root.geometry("800x450")
root.resizable(False, False)

tk.Label(
    root,
    text="E-commerce Product Scraper",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Button(
    root,
    text="Scrape Products",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    width=20,
    height=2,
    command=scrape_products
).pack(pady=10)

columns = ("Name", "Price (£)", "Rating")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.heading("Name", text="Product Name")
tree.heading("Price (£)", text="Price (£)")
tree.heading("Rating", text="Rating")

tree.column("Name", width=500)
tree.column("Price (£)", width=120, anchor="center")
tree.column("Rating", width=120, anchor="center")

tree.pack(pady=10)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=770, y=130, height=245)

status_label = tk.Label(
    root,
    text="Click 'Scrape Products' to begin",
    font=("Arial", 10),
    fg="gray"
)
status_label.pack(pady=5)

root.mainloop()
