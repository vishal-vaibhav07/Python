import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",  # Replace <your_port> with the actual port
    user="root",
    password="Badal123",
)

mycursor=mydb.cursor()
