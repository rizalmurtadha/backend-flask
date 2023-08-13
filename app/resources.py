from flask_restful import Resource, Api, reqparse, request
from app.models import Item
from app import app, db
from flask import jsonify

api = Api(app)

class CreateItemResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('brand', type=str)
        parser.add_argument('stock', type=int)
        parser.add_argument('status', type=str)
        args = parser.parse_args()

        # Check if an item with the same name already exists
        existing_item = Item.query.filter_by(name=args['name']).first()
        if existing_item:
            return {'message': 'Item with this name already exists'}, 409
        new_item = Item(name=args['name'], brand=args['brand'], stock=args['stock'], status=args['status'])
        db.session.add(new_item)
        db.session.commit()
        return {'message': 'Item created', 'id': new_item.id}, 201

    

class ItemDetailResource(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return {'id': item.id, 'name': item.name, 'brand': item.brand, 'stock': item.stock, 'status': item.status}
        return {'message': 'Item not found'}, 404

    def put(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('brand', type=str, required=True)
        parser.add_argument('stock', type=int, required=True)
        parser.add_argument('status', type=str, required=True)
        args = parser.parse_args()

        item = Item.query.get(item_id)
        
        if item:
            item.name = args['name']
            item.brand = args['brand']
            item.stock = args['stock']
            item.status = args['status']
            db.session.commit()
            return {'message': 'Item updated successfully'}, 200
        else:
            return {'message': 'Item not found'}, 404

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted successfully'}, 200
        return {'message': 'Item not found'}, 404

class ItemPaginationResource(Resource):
    def get(self):
        # return jsonify({"message": "Pagination"})
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        items = Item.query.paginate(page=page, per_page=per_page)

        items_list = [item.serialize() for item in items.items]

        response = {
            'items': items_list,
            'total_items': items.total,
            'current_page': items.page,
            'items_per_page': per_page
        }
        return jsonify(response)
        # return response


api.add_resource(CreateItemResource, '/items/create')
api.add_resource(ItemDetailResource, '/items/<int:item_id>')
api.add_resource(ItemPaginationResource, '/items')