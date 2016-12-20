from am import db
from am.models import BaseModel

item_tags = db.Table("item tags", db.Column("item_id", db.Integer, db.ForeignKey("items.id")),
                     db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))
weapon_tags = db.Table("weapon tags", db.Column("weapon_id", db.Integer, db.ForeignKey("weapons.id")),
                       db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))


class ItemBase(BaseModel):
    __abstract__ = True
    name = db.Column(db.String(32), unique=True)
    rank = db.Column(db.Integer, default=1)
    price = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)


class Item(ItemBase):
    __tablename__ = "items"
    timing = db.Column(db.String(32), nullable=True)
    target = db.Column(db.String(32), nullable=True)
    range = db.Column(db.String(32), nullable=True)
    check = db.Column(db.String(32), nullable=True)

    tags = db.relationship("Tag", secondary=item_tags)

    def __init__(self, name, rank=1, timing=None, target=None, range=None, check=None, price=0, description=None):
        self.name = name
        self.rank = rank
        self.timing = timing
        self.target = target
        self.range = range
        self.check = check
        self.price = price
        self.description = description


class Weapon(ItemBase):
    __tablename__ = "weapons"
    slot_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    attack = db.Column(db.Integer, default=0)
    magic = db.Column(db.Integer, default=0)
    accuracy = db.Column(db.Integer, default=0)
    initiative = db.Column(db.Integer, default=0)
    range = db.Column(db.String(16))

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
