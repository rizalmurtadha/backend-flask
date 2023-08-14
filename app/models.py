from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    brand = db.Column(db.String(30), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Item {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'stock': self.stock,
            'status': self.status,
            # ... add more attributes as needed
        }