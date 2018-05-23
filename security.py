from models.user import UserModel

def authenticate(username, password):
    user = UserModel.findByUsername(username)
    if user and user.password == password:
        return user
    return None

def identity(payload):
    user_id = payload['identity']
    return UserModel.findById(user_id)
