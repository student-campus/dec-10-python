import requests
url = "https://www.onlinekhabar.com/smtm/home/high-52-week"
r= requests.get(url=url)
if r.status_code ==200:
    data = r.json()['response']
   


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    database = "online khabar"
)
terminal = db.cursor()
for i in data:
    information = i['ticker']
    value = i['latest_price']
    high = i['new_high']
    previous_high = i['prev_high']
    
terminal.execute(f'Insert into info (	ticker,	latest price,new high,prev high) values ({information},{value},{high},{previous_high})')
db.commit()
print(db)

    

    