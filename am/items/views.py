from flask import Blueprint, redirect, render_template, url_for

from am import db
from .forms import WeaponForm
from .models import Weapon
from am.tags.models import Tag

mod = Blueprint("items", __name__, url_prefix="/items")


@mod.route("/create/weapon", methods=["GET", "POST"])
def create_weapon():
    form = WeaponForm()
    form.weapon_slot.choices = [(q.id, q.name) for q in db.session.query(Tag).filter(Tag.name.like("%Handed")).all()]
    form.weapon_type.choices = [(q.id, q.name) for q in db.session.query(Tag).filter(Tag.category == "Weapon Type").order_by(Tag.name).all()]

    if form.validate_on_submit():
        w = Weapon(form.name.data, form.rank.data, form.attack.data, form.magic.data, form.accuracy.data, form.initiative.data, form.range.data, form.price.data, form.description.data)
        w.equipment_slot = db.session.query(Tag).filter(Tag.id == form.weapon_slot.data).one()
        w.weapon_type = db.session.query(Tag).filter(Tag.id == form.weapon_type.data).one()
        db.session.add(w)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                print("%s: %s" % (getattr(form, field).label.text, error))

    return render_template("items/weapon_create.html", title="Create a Weapon", form=form)
