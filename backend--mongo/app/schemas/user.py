from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta:
        fields = ('_id', 'username', 'password', 'name', 'email', 'profile_picture')
