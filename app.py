from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "stefano"
api = Api(app)

@app.before_first_request # Prima della prima richiesta fa questo: crea tutte le tabelle con sqlAlchemy
def create_tables():
    db.create_all()


# JWT crea un nuovo endpoint /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# Se name = main vuol dire che è stato runnato questo file,
# così si evita di startare app se il file viene importato altrove
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port = 5000, debug = True)
