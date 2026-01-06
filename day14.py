import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    database="college"
  )
#print(db)
my_terminal=db.cursor()
#my_terminal.execute('Insert into marks(Name,Address)values("Sita","Janakpur")') # for insertation
#my_terminal.execute('Update marks set Address="India"where Id=3')                 for update
#my_terminal.execute('Delete from marks where ID=3')                               for delete
'''my_terminal.execute ("select * from marks")'''                                #select
my_terminal.execute("select id,name from marks where address='Tinkune'")        
result = my_terminal.fetchall()                                               #fetching
print(result)
#db.commit()
#print(db)
for i in result:
    print(i[1])


''' create database (name)
drop database (name)== deleting 
use database (name )
'''