import csv

def export_csv():
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    with open('products.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Nom', 'Description', 'Prix', 'Quantité', 'ID_Catégorie']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow({'ID': product[0], 'Nom': product[1], 'Description': product[2], 
                             'Prix': product[3], 'Quantité': product[4], 'ID_Catégorie': product[5]})
def filter_category():
    selected_category = category_combobox.get()
    cursor.execute("SELECT * FROM product WHERE id_category = %s", (selected_category,))
    products = cursor.fetchall()
    product_listbox.delete(0, tk.END)
    for product in products:
        product_listbox.insert(tk.END, product[1])  # Affiche le nom du produit seulement

import matplotlib.pyplot as plt

def plot_product_quantity_by_category():
    cursor.execute("SELECT category.name, SUM(product.quantity) FROM product JOIN category ON product.id_category = category.id GROUP BY category.id")
    category_data = cursor.fetchall()
    categories = [data[0] for data in category_data]
    quantities = [data[1] for data in category_data]

    plt.bar(categories, quantities)
    plt.xlabel('Catégorie')
    plt.ylabel('Quantité')
    plt.title('Quantité de produits par catégorie')
    plt.show()
