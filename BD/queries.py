from flask import Flask, request
import sqlite3
from datetime import datetime
import json 

database = sqlite3.connect('data.db')
cursor = database.cursor()

def get_data(startDate, endDate=None, Type=None, Grouping=None, attr1=None, attr2=None, attr3=None, attr4=None):

    options_type = {
        'weekly': '%W',
        'monthly': '%m',
        'bi-weekly': '%W'
    }

    Type=options_type[Type]

    attributes = [attr1,attr2,attr3,attr4]
    
    # Generates list of attributes to be retrieved from database
    colunas =""
    for i in range(len(attributes)):
        
        if attributes[i] is not None:
            colunas+=attributes[i]
            colunas+=","


    #cursor.execute("SELECT "+colunas+", COUNT(*) AS nRecords FROM sales WHERE date(timestamp) \
                    #BETWEEN date('"+startDate+"') AND date('2020-04-01') \
                    #GROUP by strftime("+Type+", timestamp)")

    cursor.execute("SELECT date(timestamp),"+colunas+" COUNT(*) AS nRecords FROM sales WHERE date(timestamp) \
                    BETWEEN date('"+startDate+"', 'weekday 2') AND date('2020-04-01') \
                    GROUP by strftime('"+Type+"', timestamp)")

    print(cursor.fetchall())

get_data('2020-01-01', Type='weekly')