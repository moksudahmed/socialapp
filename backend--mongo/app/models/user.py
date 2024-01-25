from app import mongo

class User:
    def __init__(self, username, password, name, email, profile_picture):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.profile_picture = profile_picture

    def save(self):
        users = mongo.db.users
        user_id = users.insert_one({
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'email': self.email,
            'profile_picture': self.profile_picture,
        })
        return str(user_id.inserted_id)
