from am import app
from am.models import BaseModel


class Tag(BaseModel):
    __tablename__ = "tags"
    name = db.Column(db.String(32))
    category = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, category=0, description=None):
        self.name = name
        self.category = category
        self.description = description

    @property
    def category_name(self):
        return app.config['TAGCATEGORIES'][self.category]
