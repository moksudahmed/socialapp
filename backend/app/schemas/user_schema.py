# app/schemas/user_schema.py
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=4, max=50))
    email = fields.Email(required=True)  # Add the email field with Email validation
    password = fields.Str(required=True, validate=validate.Length(min=6, max=255))
