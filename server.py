from crypt import methods
from datetime import datetime
from distutils.log import debug
from flask import Flask, request
import pandas as pd
import json
import BD.queries as queries


Type = ['cumulative', 'usual']
Grouping = ['weekly', 'bi-weekly', 'monthly']

info = [
    
            {
                "Parameters": {

                    "startDate": "",
                    "endDate": "",
                    "Type": Type,
                    "Grouping": Grouping
                },
                "Attributes" : {

                    "asin": queries.all_asins(),
                    "brand": queries.all_brands(),
                    "source": queries.all_sources(),
                    "stars": queries.all_stars()
                }
            }
    
        ]

app = Flask(__name__)

@app.route("/api/info")
def get_info():

    return {'info': info}

@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    
    startDate = request.args.get("startDate")
    endDate = request.args.get('endDate')
    Type = request.args.get('Type',)
    Grouping = request.args.get('Grouping')
    attr1 = request.args.get('asin')
    attr2 = request.args.get('brand')
    attr3 = request.args.get('source')
    attr4 = request.args.get('stars')

    return queries.get_data(startDate=startDate, endDate=endDate, Type=Type, grp=Grouping, att1=attr1, att2=attr2, att3=attr3, att4=attr4)



if __name__ == "__main__" :
    app.run(debug = True)