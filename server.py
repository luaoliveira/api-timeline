from datetime import datetime
from xml.dom import ValidationErr
from flask import Flask, request
import pandas as pd
import json
from marshmallow import Schema, fields, pprint, post_load, ValidationError
import BD.queries as queries
import SRC.query_params as query_params

Type = ['cumulative', 'usual']
Grouping = ['weekly', 'bi-weekly', 'monthly']

info = [
            {
                "Parameters" : {

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
        prs = schema.load(request.args)
        return queries.get_data(startDate=prs.startDate, endDate=prs.endDate, Type=prs.Type, grp=prs.Grouping, att1=prs.asin, att2=prs.brand, att3=prs.source, att4=prs.stars)

    except ValidationErr as err:
        
        return print(err)
    
if __name__ == "__main__":

    app.run(debug = True)



