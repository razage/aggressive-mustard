from am import ma
from .models import Tag


class TagSchema(ma.ModelSchema):
    class Meta:
        model = Tag
        fields = ("id", "name", "category")
