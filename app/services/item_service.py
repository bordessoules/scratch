from app import db
from app.models.item import Item
from app.utils.image_handler import save_image

class ItemService:
    @staticmethod
    def get_item(item_id):
        item = Item.query.get_or_404(item_id)
        return {'id': item.id, 'description': item.description, 'labels': item.labels, 'images': item.images}

    @staticmethod
    def get_all_items():
        items = Item.query.all()
        return [{'id': item.id, 'description': item.description, 'labels': item.labels, 'images': item.images} for item in items]

    @staticmethod
    def create_item(data):
        images = [save_image(image) for image in data['images']]
        new_item = Item(description=data['description'], labels=data['labels'], images=images)
        db.session.add(new_item)
        db.session.commit()
        return {'id': new_item.id, 'description': new_item.description, 'labels': new_item.labels, 'images': new_item.images}, 201

    @staticmethod
    def update_item(item_id, data):
        item = Item.query.get_or_404(item_id)
        item.description = data['description']
        item.labels = data['labels']
        item.images = [save_image(image) for image in data['images']]
        db.session.commit()
        return {'id': item.id, 'description': item.description, 'labels': item.labels, 'images': item.images}

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return '', 204