import mysql.connector

#connessione al database
warehouse_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'im231310',
    database = 'warehouse_db'
)

cursor = warehouse_db.cursor()
