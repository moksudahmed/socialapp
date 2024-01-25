from marshmallow import Schema, fields

class JobPostingSchema(Schema):
    class Meta:
        fields = ('_id', 'title', 'description', 'user_id', 'images')
