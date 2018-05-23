import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    # Guarda nel payload e controlla se i parametri esistono
    # Abilita solamente i parametri elencati
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.findByUsername(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data) #(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User create successfully"}, 201
