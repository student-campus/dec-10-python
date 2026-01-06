import mysql.connector
sd = mysql.connector.connect(
    host = "localhost",
    username = "root",
    database = "share",
    port = 3306
)
terminal = sd.cursor()
terminal.execute('CREATE DATABASE if not exists share')
terminal.execute('''CREATE TABLE if not exists data ( name VARCHAR(20))''')
terminal.execute('Insert into data (name) values("Sunita")')
result = terminal.fetchall()
print(result)
#d.commit()
#print(sd)
