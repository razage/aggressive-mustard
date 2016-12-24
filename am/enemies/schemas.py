from am import ma
from .models import Ability, Enemy, LootDrop
from am.items.schemas import ItemSchema, WeaponSchema
from am.tags.schemas import TagSchema


class AbilitySchema(ma.ModelSchema):
    class Meta:
        table = Ability
        fields = ("id", "name", "attack_type", "timing", "check", "target", "range", "limit", "description")

    attack_type = ma.Nested(TagSchema)


class LootDropSchema(ma.ModelSchema):
    class Meta:
        table = LootDrop
        fields = ("roll", "item", "weapon", "quantity", "gold")

    item = ma.Nested(ItemSchema)
    weapon = ma.Nested(WeaponSchema)


class EnemySchema(ma.ModelSchema):
    class Meta:
        table = Enemy
        fields = (
            "id", "name", "enemy_type", "tags", "rank", "STR", "DEX", "POW", "INT", "HP", "initiative", "speed",
            "evasion", "phys_def", "resistance", "mag_def", "id_diff", "hate_multi", "fate_points", "abilities", "loot"
        )

    enemy_type = ma.Nested(TagSchema)
    tags = ma.Nested(TagSchema, many=True)
    abilities = ma.Nested(AbilitySchema, many=True)
    loot = ma.Nested(LootDropSchema, many=True)
