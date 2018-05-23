from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    # Guarda nel payload e controlla se i parametri esistono
    # Abilita solamente i parametri elencati
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item need a store id"
    )

    @jwt_required() # Ogni volta che si chiamano questi viene controllato se l'utente ha un token
    def get(self, name):
        item = ItemModel.findByName(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404




    def post(self, name):
        # Error approach
        if ItemModel.findByName(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # Bad request

        data = Item.parser.parse_args()

        #data = request.get_json(silent = True)
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201 # 201 --> 200 for create




    def delete(self, name):
        item = ItemModel.findByName(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}




    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.findByName(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()




class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
        # map:
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all())) }
