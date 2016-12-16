from flask import Blueprint, render_template

from am.models import db
from .forms import EnemyForm
from am.tags.models import Tag

mod = Blueprint("enemies", __name__, url_prefix="/enemies")


@mod.route("/create", methods=["GET", "POST"])
def create_enemy():
    form = EnemyForm()
    form.e_type.choices = [(q.id, q.name) for q in db.session.query(Tag).filter(Tag.category == "Enemy Type").all()]

    if form.validate_on_submit():
        pass

    return render_template("enemies/enemy_create.html", title="Create an Enemy", form=form)

