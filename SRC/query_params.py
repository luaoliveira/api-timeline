from xml.dom import ValidationErr
from marshmallow import Schema, fields, pprint, post_load, ValidationError, validates
import BD.queries
import sys

sys.path.append("..")

class Parameters():

    def __init__(self, request):

        self.startDate = request.args.get("startDate")
        self.endDate = request.args.get('endDate')
        self.Type = request.args.get('Type',)
        self.Grouping = request.args.get('Grouping')
        self.attr1 = request.args.get('asin')
        self.attr2 = request.args.get('brand')
        self.attr3 = request.args.get('source')
        self.attr4 = request.args.get('stars')


class ParametersSchema(Schema):

    startDate = fields.Date('%Y-%m-%d')
    endDate = fields.Date(format='%Y-%m-%d')
    Type = fields.String()
    Grouping = fields.String()
    attr1 = fields.String()
    attr2 = fields.String()
    attr3 = fields.String()
    attr4 = fields.Integer()

    @validates('Type')
    def validate_Type(self, Type):

        Type_values = ['cumulative', 'usual']

        if not Type in Type_values:

            return ValidationError()

    @validates('Grouping')
    def validate_Grouping(self, Grouping):

        Groups = ['weekly', 'bi-weekly', 'monthly']

        if not Grouping in Groups:
            
            return ValidationError()

    @validates('attr1')
    def validade_attr1(self, attr1):

        if not attr1 in queries.all_asins():

            return ValidationError()

    @validates('attr2')
    def validate_attr2(self, attr2):

        if not attr2 in queries.all_brands():

            return ValidationError()

    @validates('attr3')
    def validate_attr3(self, attr3):

        if not attr3 in queries.all_sources():

            return ValidationError()

    @validates('attr4')
    def validate_attr4(self, attr4):

        if ((attr4 > 5) | (attr4 <1)):

            return ValidationError()