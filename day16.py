# API 
'''import requests
url = "https://www.onlinekhabar.com/smtm/home/high-52-week"
r = requests.get(url= url)     # get or post to hit 
if r. status_code== 200:
    #print(r.text)  # to know which formate in str,json
     data =r.json()['response']
     #print(type(data))
     print(len(data))
     for i in data:
          print(i['ticker'],i['latest_price'],i['new_high'],i['prev_high'])'''
          
import requests
url = "https://www.onlinekhabar.com/smtm/home/fear-and-greed"
r = requests.get(url = url)
if r. status_code ==200:
    #print(r.text)
    data= r.json()['response']
    print(data)
    for i in data:
         z= i.get("value")
         y= i.get('status')
         u= i.get('message')
         print(z)
         print(y)
         print(u)
import mysql.connector
sd = mysql.connector.connect(
     host= "localhost",
     user = "root",
     port = 3306,
     database= "online khabar"
     
)
terminal= sd.cursor()
terminal.execute(
    'INSERT INTO information (value, status, message) VALUES (%s, %s, %s)',
    (z, y, u)
)
sd.commit()
print(sd)
