from am import db
from am.models import BaseModel


class Tag(BaseModel):
    __tablename__ = "tags"
    name = db.Column(db.String(32))
    category = db.Column(db.String(32), default="General")
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, category="General", description=None):
        self.name = name
        self.category = category
        self.description = description
