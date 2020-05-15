class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    long_description = fields.Str()