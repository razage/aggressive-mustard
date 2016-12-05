from am import db
from am.models import Attributes, BaseModel


class Class(BaseModel, Attributes):
    __tablename__ = "classes"
    name = db.Column(db.String(32), unique=True)
    hp_mod = db.Column(db.Integer, default=0)
    alternate_names = db.relationship("AlternateName")

    def __init__(self, name, STR, DEX, POW, INT, HP, hp_mod):
        self.name = name
        self.STR = STR
        self.DEX = DEX
        self.POW = POW
        self.INT = INT
        self.HP = HP
        self.hp_mod = hp_mod


class AlternateName(BaseModel):
    __tablename__ = "alternate names"
    parent_class = db.Column(db.Integer, db.ForeignKey('classes.id'))
    name = db.Column(db.String(32))
    server = db.Column(db.String(24))

    def __init__(self, name, server):
        self.name = name
        self.server = server
