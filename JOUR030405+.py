import tkinter as tk
from tkinter import messagebox

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")
        self.create_widgets()

    def create_widgets(self):
        self.product_listbox = tk.Listbox(self.root, width=50, height=20)
        self.product_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Ajouter Produit", command=self.add_product)
        self.add_button.grid(row=1, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Supprimer Produit", command=self.delete_product)
        self.delete_button.grid(row=2, column=0, padx=10, pady=5)

        self.edit_button = tk.Button(self.root, text="Modifier Produit", command=self.edit_product)
        self.edit_button.grid(row=3, column=0, padx=10, pady=5)

        self.refresh_button = tk.Button(self.root, text="Actualiser", command=self.refresh_product_list)
        self.refresh_button.grid(row=4, column=0, padx=10, pady=5)

    def refresh_product_list(self):
        # Efface la liste actuelle et récupère les produits de la base de données
        self.product_listbox.delete(0, tk.END)
        cursor.execute("SELECT name FROM product")
        products = cursor.fetchall()
        for product in products:
            self.product_listbox.insert(tk.END, product[0])

    def add_product(self):
        # Implémentez la logique pour ajouter un produit dans la base de données
        pass

    def delete_product(self):
        # Implémentez la logique pour supprimer un produit de la base de données
        pass

    def edit_product(self):
        # Implémentez la logique pour modifier un produit dans la base de données
        pass

# Crée une instance de l'application Tkinter
root = tk.Tk()
app = StockManagementApp(root)
root.mainloop()
