from flask import Blueprint, redirect, render_template, url_for

from am.models import db
from .forms import AbilityForm, EnemyForm
from .models import Ability, Enemy
from am.tags.models import Tag

mod = Blueprint("enemies", __name__, url_prefix="/enemies")


@mod.route("/")
def enemy_index():
    e = Enemy.query.all()
    return render_template("enemies/enemy_index.html", title="Enemy List", enemies=e)


@mod.route("/<int:enemy_id>")
def view_enemy(enemy_id):
    e = Enemy.query.get_or_404(enemy_id)
    return render_template("enemies/enemy_view.html", title=e.name, enemy=e)


@mod.route("/create", methods=["GET", "POST"])
def create_enemy():
    form = EnemyForm()
    form.e_type.choices = [(q.id, q.name) for q in
                           db.session.query(Tag).filter(Tag.category == "Enemy Type").order_by(Tag.name).all()]

    if form.validate_on_submit():
        e = Enemy(form.name.data, form.strength.data, form.dexterity.data, form.power.data, form.intelligence.data,
                  form.health_points.data, form.rank.data, form.initiative.data, form.speed.data, form.evasion.data,
                  form.phys_def.data, form.resistance.data, form.mag_def.data, form.id_diff.data, form.hate_multi.data,
                  form.fate_points.data)
        e.enemy_type = db.session.query(Tag).filter(Tag.id == form.e_type.data).one()

        if form.tags.data != "":
            _tags = form.tags.data.split(",")
            for t in _tags:
                if t[0] == " ":
                    t = t[1:]
                tq = db.session.query(Tag).filter(Tag.name == t).first()

                if t == "" or tq is None:
                    continue
                else:
                    e.tags.append(tq)

        db.session.add(e)
        db.session.commit()

        return redirect(url_for("enemies.view_enemy", enemy_id=e.id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                print("%s: %s" % (getattr(form, field).label.text, error))

    return render_template("enemies/enemy_create.html", title="Create an Enemy", form=form)


@mod.route("/abilities/<int:ability_id>")
def view_ability(ability_id):
    pass


@mod.route("/<int:enemy_id>/abilities/create", methods=["GET", "POST"])
def create_ability(enemy_id):
    e = Enemy.query.get_or_404(enemy_id)

    form = AbilityForm()
    form.attack_type.choices += [(q.id, q.name) for q in
                                 db.session.query(Tag).filter(Tag.category == "Attack Type").order_by(Tag.name).all()]

    if form.validate_on_submit():
        a = Ability(form.name.data, form.timing.data, None, None, None, None, form.description.data)

        if form.attack_type.data == "":
            a.attack_type_id = None
        else:
            a.attack_type_id = form.attack_type.data

        if form.check.data != "":
            a.check = form.check.data

        if form.target.data != "":
            a.target = form.target.data

        if form.range.data != "":
            a.range = form.range.data

        if form.limit_times.data > 0 and form.limit_tf.data != "":
            a.limit = "%s/%s" % (str(form.limit_times.data), form.limit_tf.data)

        e.abilities.append(a)
        db.session.commit()
        return redirect(url_for("enemies.view_enemy", enemy_id=e.id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                print("%s: %s" % (getattr(form, field).label.text, error))

    return render_template("enemies/ability_create.html", title="Create an Ability for %s" % e.name, enemy=e, form=form)
