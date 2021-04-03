from app.app import db

association_table = db.Table('association', db.Model.metadata,
                            db.Column('items_id', db.Integer, db.ForeignKey('items.id'), primary_key = True),
                            db.Column('stores_id', db.Integer, db.ForeignKey('stores.id'), primary_key = True)
                            )

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items_id = db.relationship('ItemModel', lazy='dynamic', secondary=association_table)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
