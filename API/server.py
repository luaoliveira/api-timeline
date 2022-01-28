from crypt import methods
from datetime import datetime
from distutils.log import debug
from flask import Flask, request
import pandas as pd
import json

info = [
    
            {
                "Parameters": {

                    "startDate": "Initial date to show the visualization",
                    "endDate": " Final date to show in the visualization",
                    "Type": "cumulative or usual",
                    "Grouping": "weekly, bi-weekly or monthly"
                },
                "Attributes" : {

                    "asin": "1",
                    "brand": "2",
                    "id":"3",
                    "source":"4",
                    "stars": "5"
                }
            }
    
        ]

app = Flask(__name__)

@app.route("/api/info")
def get_info():

    return {'info': info}


#@app.route("/api/timeline/startDate=<startDate>&endDate=<endDate>&Type=<Type>&Grouping=<Grouping>&attr=<attr>")
@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    
    startDate = request.args.get("startDate")
    endDate = request.args.get('endDate')
    Type = request.args.get('Type',)
    Grouping = request.args.get('Grouping')
    attr1 = request.args.get('attr1')
    attr2 = request.args.get('attr2')
    attr3 = request.args.get('attr3')
    attr4 = request.args.get('attr4')

    #return_data(startDate, endDate, Type, Grouping, attr)


if __name__ == "__main__" :
    app.run(debug = True)