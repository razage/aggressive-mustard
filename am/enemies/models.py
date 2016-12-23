from am import db
from am.models import Attributes, BaseModel

enemy_ability = db.Table("enemy ability", db.Column("enemy_id", db.Integer, db.ForeignKey("enemies.id")),
                         db.Column("ability_id", db.Integer, db.ForeignKey("abilities.id")))
enemy_tags = db.Table("enemy tags", db.Column("enemy_id", db.Integer, db.ForeignKey("enemies.id")),
                      db.Column("tag_id", db.Integer, db.ForeignKey("tags.id")))


class Ability(BaseModel):
    __tablename__ = "abilities"
    name = db.Column(db.String(32), unique=True)
    attack_type_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=True)
    timing = db.Column(db.String(32))
    check = db.Column(db.String(42), nullable=True)
    target = db.Column(db.String(32))
    range = db.Column(db.String(32), nullable=True)
    limit = db.Column(db.String(16), nullable=True)
    description = db.Column(db.Text)

    attack_type = db.relationship("Tag", backref="abilities_with_attack_type", foreign_keys=attack_type_id)

    def __init__(self, name, timing, check, target, range, limit, description):
        self.name = name
        self.timing = timing
        self.check = check
        self.target = target
        self.range = range
        self.limit = limit
        self.description = description


class LootTable(BaseModel):
    __tablename__ = "loot tables"
    enemy_id = db.Column(db.Integer, db.ForeignKey("enemies.id"))
    roll = db.Column(db.String(3), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=True)
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapons.id"), nullable=True)
    quantity = db.Column(db.Integer, default=1)
    gold = db.Column(db.String(16), nullable=True)

    enemy = db.relationship("Enemy", backref="loot")
    item = db.relationship("Item", backref="item_dropped_by")
    weapon = db.relationship("Weapon", backref="weapon_dropped_by")

    def __init__(self, roll=None, quantity=1, gold=None):
        self.roll = roll
        self.quantity = quantity
        self.gold = gold


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
    abilities = db.relationship("Ability", secondary=enemy_ability)

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
