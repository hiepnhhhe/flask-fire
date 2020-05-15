from marshmallow import Schema, fields, pre_load, post_dump

class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()

    @pre_load
    def make_user(self, data, **kwargs):
        data = data['user']
        return data

    @post_dump
    def dump_user(self, data, **kwargs):
        return {'user': data}

    class Meta:
        strict = True

user_schema = UserSchema()
user_schemas = UserSchema(many=True)