from . import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class Attributes(db.Model):
    __abstract__ = True
    STR = db.Column(db.Integer, default=0)
    DEX = db.Column(db.Integer, default=0)
    POW = db.Column(db.Integer, default=0)
    INT = db.Column(db.Integer, default=0)
    HP = db.Column(db.Integer, default=0)
