from marshmallow import Schema, fields, pre_load, post_dump

class ElementShema(Schema):
    position = fields.Integer()
    name = fields.Str()
    weight = fields.Float()
    symbol = fields.Str()
    image = fields.Str()
