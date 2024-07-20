from app import db
from sqlalchemy.dialects.postgresql import ARRAY

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    labels = db.Column(ARRAY(db.String), nullable=False)
    images = db.Column(ARRAY(db.String), nullable=False)

    def __repr__(self):
        return f'<Item {self.id}>'