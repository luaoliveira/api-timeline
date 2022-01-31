from crypt import methods
from datetime import datetime
from distutils.log import debug
from xml.dom import ValidationErr
from flask import Flask, request
import pandas as pd
import json
import BD.queries as queries
import SRC.query_params as query_params

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
    
    try:

        schema = query_params.ParametersSchema()
        prs = query_params.Parameters(request)
        return queries.get_data(startDate=prs.startDate, endDate=prs.endDate, Type=prs.Type, grp=prs.Grouping, att1=prs.attr1, att2=prs.attr2, att3=prs.attr3, att4=prs.attr4)

    except ValidationErr as err:
        
        return err
    
if __name__ == "__main__" :
    app.run(debug = True)



