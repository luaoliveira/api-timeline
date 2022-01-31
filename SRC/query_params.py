from marshmallow import Schema, fields, pprint, post_load, ValidationError, validates
import BD.queries as queries
import sys

sys.path.append("..")

class Parameters():

    def __init__(self, args):

        self.startDate = args.get("startDate")
        self.endDate = args.get('endDate')
        self.Type = args.get('Type',)
        self.Grouping = args.get('Grouping')
        self.asin = args.get('asin')
        self.brand = args.get('brand')
        self.source = args.get('source')
        self.stars = args.get('stars')


class ParametersSchema(Schema):

    startDate = fields.Date('%Y-%m-%d', required = False, allow_none = True)
    endDate = fields.Date(format='%Y-%m-%d', required = False, allow_none = True)
    Type = fields.String(required = False, allow_none = True)
    Grouping = fields.String(required = False, allow_none = True)
    asin = fields.String(required = False, allow_none = True)
    brand = fields.String(required = False, allow_none = True)
    source = fields.String(required = False, allow_none = True)
    stars = fields.Integer(required = False, allow_none = True)

    @post_load
    def create_parameters(self, data, **kwargs):

        return Parameters(data)

    @validates('Type')
    def validate_Type(self, Type):

        Type_values = ['cumulative', 'usual']
        if ((not Type in Type_values) & (Type != None)):

            raise ValidationError()

    @validates('Grouping')
    def validate_Grouping(self, Grouping):

        Groups = ['weekly', 'bi-weekly', 'monthly']
        if not((Grouping in Groups) & (Grouping != None)):
            
            raise ValidationError("Not a valid grouping argument")

    @validates('asin')
    def validade_asin(self, asin):

        if ((not asin in queries.all_asins()) & (asin != None)):

            raise ValidationError("Asin not valid")

    @validates('brand')
    def validate_brand(self, brand):

        if ((not brand in queries.all_brands()) & (brand != None)):

            raise ValidationError("Brand not valid")

    @validates('source')
    def validate_source(self, source):

        if ((not source in queries.all_sources()) & (source != None)):

            raise ValidationError("Source not valid")

    @validates('stars')
    def validate_stars(self, stars):

        if ((stars > 5) | (stars <1) and (stars != None)):

            raise ValidationError("Stars must be in range 1-5")