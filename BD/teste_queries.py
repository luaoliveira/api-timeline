from flask import Flask, request
import sqlite3
from datetime import datetime
import json 

database = sqlite3.connect('data.db')
cursor = database.cursor()

cursor.execute("SELECT DISTINCT brand FROM sales ORDER BY brand")
print(cursor.fetchall())