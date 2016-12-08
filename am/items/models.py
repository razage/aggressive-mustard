from am import db
from am.models import BaseModel

weapon_tags = db.Table("weapon tags", db.Column("weapon_id", db.Integer, db.ForeignKey("weapons.id")),
                       db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))


class Weapon(BaseModel):
    __tablename__ = "weapons"
    name = db.Column(db.String(32), unique=True)
    rank = db.Column(db.Integer, default=0, nullable=True)
    slot_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    attack = db.Column(db.Integer, default=0)
    magic = db.Column(db.Integer, default=0)
    accuracy = db.Column(db.Integer, default=0)
    initiative = db.Column(db.Integer, default=0)
    range = db.Column(db.String(16))
    price = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)

    equipment_slot = db.relationship("Tag", backref="items_in_slot", foreign_keys=slot_id)
    weapon_type = db.relationship("Tag", backref="items_in_type", foreign_keys=type_id)
    tags = db.relationship("Tag", secondary=weapon_tags)

    def __init__(self, name, rank, attack, magic, accuracy, initiative, range, price, description):
        self.name = name
        self.rank = rank
        self.attack = attack
        self.magic = magic
        self.accuracy = accuracy
        self.initiative = initiative
        self.range = range
        self.price = price
        self.description = description
