from flask import abort, Blueprint, render_template, request

from am import db
from .models import Tag

mod = Blueprint('tags', __name__, url_prefix="/tags")


@mod.route("/")
def tag_index():
    tags = db.session.query(Tag).order_by(Tag.name).all()
    return render_template("tags/index.html", title="Tag Index", tags=tags)


@mod.route("/query")
def tags_category_filtered():
    from .schemas import TagSchema

    if request.args.get("category"):
        tags = Tag.query.filter(Tag.category == request.args.get("category")).with_entities(Tag.id, Tag.name).all()
        tags_schema = TagSchema(many=True)
        return tags_schema.jsonify(tags)
    else:
        abort(400)
