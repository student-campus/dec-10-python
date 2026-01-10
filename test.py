import mysql.connector as my

mydb = my.connect(
  host="localhost",
  user="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
