from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

ranges = [("na", "N/a"), ("close", "Close"), ("1 sq.", "1 Sq."), ("2 sq.", "2 Sq."), ("3 sq.", "3 Sq.")]


class WeaponForm(FlaskForm):
    name = StringField("Weapon Name", [DataRequired()])
    rank = SelectField("Weapon Rank", choices=[(i, i) for i in range(1, 11)], coerce=int, validators=[DataRequired()])
    weapon_slot = SelectField("Weapon Slot", [DataRequired()], coerce=int)
    weapon_type = SelectField("Weapon Type", [DataRequired()], coerce=int)
    attack = IntegerField("Attack", [Optional()])
    magic = IntegerField("Magic", [Optional()])
    accuracy = IntegerField("Accuracy", [Optional()])
    initiative = IntegerField("Initiative", [Optional()])
    range = SelectField("Weapon Range", choices=ranges, validators=[DataRequired()])
    price = IntegerField("Price", [Optional()])
    description = TextAreaField("Description", [Optional()])
