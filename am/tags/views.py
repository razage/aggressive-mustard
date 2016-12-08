from flask import Blueprint, render_template

from am import db
from .models import Tag

mod = Blueprint('tags', __name__, url_prefix="/tags")


@mod.route("/")
def tag_index():
    tags = db.session.query(Tag).order_by(Tag.name).all()
    return render_template("tags/index.html", title="Tag Index", tags=tags)
