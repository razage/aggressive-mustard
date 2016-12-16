from am import db
from am.models import Attributes, BaseModel

enemy_tags = db.Table("enemy tags", db.Column("enemy_id", db.Integer, db.ForeignKey("enemies.id")),
                      db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))


class Enemy(BaseModel, Attributes):
    __tablename__ = "enemies"
    name = db.Column(db.String(32), unique=True)
    type_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    rank = db.Column(db.Integer, default=1)
    initiative = db.Column(db.Integer)
    speed = db.Column(db.Integer, default=2)
    evasion = db.Column(db.String(16))
    phys_def = db.Column(db.Integer)
    resistance = db.Column(db.String(16))
    mag_def = db.Column(db.Integer)
    id_diff = db.Column(db.Integer)
    hate_multi = db.Column(db.Integer, default=2)
    fate_points = db.Column(db.Integer, default=0)

    enemy_type = db.relationship("Tag", backref="enemies_of_type", foreign_keys=type_id)
    tags = db.relationship("Tag", secondary=enemy_tags)

    def __init__(self, name, STR, DEX, POW, INT, HP, rank, initiative, speed, evasion, phys_def, resistance, mag_def,
                 id_diff, hate_multi=2, fate_points=0):
        self.name = name
        self.STR = STR
        self.DEX = DEX
        self.POW = POW
        self.INT = INT
        self.HP = HP
        self.rank = rank
        self.initiative = initiative
        self.speed = speed
        self.evasion = evasion
        self.phys_def = phys_def
        self.resistance = resistance
        self.mag_def = mag_def
        self.id_diff = id_diff
        self.hate_multi = hate_multi
        self.fate_points = fate_points
