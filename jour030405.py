import mysql.connector

# Paramètres de connexion à la base de données
config = {
    'user': 'root',
    'password': 'Diourbel2002@',
    'host': 'localhost',
    'database': 'store'
}

# Connexion à la base de données
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
