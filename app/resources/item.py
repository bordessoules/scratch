from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.services.item_service import ItemService

class ItemResource(Resource):
    @jwt_required()
    def get(self, item_id):
        return ItemService.get_item(item_id)

    @jwt_required()
    def put(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('labels', type=str, action='append', required=True)
        parser.add_argument('images', type=str, action='append', required=True)
        args = parser.parse_args()
        return ItemService.update_item(item_id, args)

    @jwt_required()
    def delete(self, item_id):
        return ItemService.delete_item(item_id)

class ItemListResource(Resource):
    @jwt_required()
    def get(self):
        return ItemService.get_all_items()

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('labels', type=str, action='append', required=True)
        parser.add_argument('images', type=str, action='append', required=True)
        args = parser.parse_args()
        return ItemService.create_item(args)