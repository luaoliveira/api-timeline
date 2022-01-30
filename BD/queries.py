import os
import grp
from flask import Flask, request
import sqlite3
from datetime import datetime
import json 
import pandas as pd

def connect():
    return sqlite3.connect(os.path.join( os.path.dirname(__file__), 'data.db'))
    
def all_brands():

    cursor = connect().cursor()
    cursor.execute("SELECT DISTINCT brand FROM sales ORDER BY brand")
    return [brand[0] for brand in cursor.fetchall()]

def all_asins():

    cursor = connect().cursor()
    cursor.execute("SELECT DISTINCT asin FROM sales ORDER BY asin")
    return [asin[0] for asin in cursor.fetchall()]

def all_sources():

    cursor = connect().cursor()
    cursor.execute("SELECT DISTINCT source FROM sales ORDER BY source")
    return [source[0] for source in cursor.fetchall()]

def all_stars():

    cursor = connect().cursor()
    cursor.execute("SELECT DISTINCT stars FROM sales ORDER BY stars")
    return [stars[0] for stars in cursor.fetchall()]

def get_data(startDate=None, endDate=None, Type=None, grp=None, att1=None, att2=None, att3=None, att4=None):

    database = connect()

    options_type = {
        'weekly': '%W',
        'monthly': '%m',
        'bi-weekly': '%W'
    }

    attrs = {
        'asin': att1,
        'brand':att2,
        'source':att3,
        'stars': att4
    }

    grp_options = {

        'weekly': 'W',
        'bi-weekly': '2W',
        'monthly' : 'M',
    }

    def get_condition():

        condition = "WHERE " if any(attrs.values()) else ""
        rest = ""
        for att, value in attrs.items():
        
            if value != None:

                if (rest):
                    rest+= "AND "
                rest+= att + " = '" + value + "' "

        if startDate != None:

            rest+= "AND date(timestamp) >= '" + startDate + "' "

        if endDate != None:

            rest+= " AND date(timestamp) <= '" + endDate + "' "

        return (condition + rest)

    df = pd.read_sql_query("SELECT * FROM sales " + get_condition() + " ORDER BY date(timestamp)", database)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    if grp != None:
        df = df.resample(grp_options[grp], on='timestamp').count()['stars']
    else:
        df = df.resample('1D', on='timestamp').count()['stars']

    if Type == 'cumulative':

        df = df.cumsum()

    timeline = {
        "timeline": [{'date': key, 'value': value} for key, value in zip(df.index, df)] 
    }

    return timeline

#get_data(att2='Downy', att4 = '3', startDate='2020-01-01', endDate='2020-12-01' , grp = 'weekly')
#get_data(att2='Downy', att4 = '3', grp = 'weekly')
#get_data(grp='bi-weekly')