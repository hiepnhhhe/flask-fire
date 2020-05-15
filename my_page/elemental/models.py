from ..database import Column, Model, SurrogatePK


class PeriodicElement(SurrogatePK, Model):
    position = Column(db.Integer)
    name = Column(db.String(30))
    weight = Column(db.Float)
    symbol = Column(db.String(30))
    image = Column(db.String(100))

    def __repr__(self):
        return f"Element('{self.position}', '{self.name}', '{self.weigth}', '{self.symbol}')"
