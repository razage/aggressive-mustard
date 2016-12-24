from am import ma
from .models import Item, Weapon
from am.tags.schemas import TagSchema


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item
        fields = ("id", "name", "rank", "tags", "timing", "target", "range", "price", "description")

    tags = ma.Nested(TagSchema, many=True)


class WeaponSchema(ma.ModelSchema):
    class Meta:
        model = Weapon
        fields = (
            "id", "name", "rank", "equipment_slot", "weapon_type", "tags", "attack", "magic", "accuracy", "initiative",
            "range", "price", "description"
        )

    equipment_slot = ma.Nested(TagSchema)
    weapon_type = ma.Nested(TagSchema)
    tags = ma.Nested(TagSchema, many=True)
