import sqlite3 
import pandas as pd
from datetime import datetime

df = pd.read_csv("/home/luana/Documentos/Simporter/SRC/data.csv", sep=';')
df['timestamp'] = df['timestamp'].apply(lambda x: str(datetime.fromtimestamp(x)))
df.sort_index(inplace=True)

database = sqlite3.connect('data.db')

cursor = database.cursor()

cursor.execute("CREATE TABLE sales(asin text, \
                brand text,id text,source text, \
                stars integer,timestamp text)")

for index, row in df.iterrows():

    asin = row['asin']
    brand = row['brand']
    id = row['id']
    source = row['source']
    stars = row['stars']
    timestamp = row['timestamp']

    cursor.execute("INSERT INTO sales VALUES(?,?,?,?,?,?)", 
                    (asin,brand, id, source, stars, timestamp))
                    
    database.commit()