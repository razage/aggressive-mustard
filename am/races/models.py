from am import db
from am.models import Attributes, BaseModel


class Race(BaseModel, Attributes):
    __tablename__ = "races"
    name = db.Column(db.String(32), unique=True)
    fate = db.Column(db.Integer, default=0)
    bonus_points = db.Column(db.Integer, default=5)

    def __init__(self, name, STR, DEX, POW, INT, HP, fate, bonus_points=5):
        self.name = name
        self.STR = STR
        self.DEX = DEX
        self.POW = POW
        self.INT = INT
        self.HP = HP
        self.fate = fate
        self.bonus_points = bonus_points