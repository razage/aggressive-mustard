from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class EnemyForm(FlaskForm):
    name = StringField("Monster Name", [DataRequired(), Length(1, 32)])
    tags = TextAreaField("Monster Tags", [Optional()])
    e_type = SelectField("Monster Type", coerce=int, validators=[DataRequired()])
    strength = IntegerField("Strength", [DataRequired()])
    dexterity = IntegerField("Dexterity", [DataRequired()])
    power = IntegerField("Power", [DataRequired()])
    intelligence = IntegerField("Intelligence", [DataRequired()])
    health_points = IntegerField("Health Points", [DataRequired()])
    rank = IntegerField("Monster Rank", [DataRequired()])
    initiative = IntegerField("Initiative", [DataRequired()])
    speed = IntegerField("Movement Speed", [DataRequired()])
    evasion = StringField("Evasion", [DataRequired(), Length(1, 16)])
    phys_def = IntegerField("Physical Defense", [DataRequired()])
    resistance = StringField("Resistance", [DataRequired(), Length(1, 16)])
    mag_def = IntegerField("Magic Defense", [DataRequired()])
    id_diff = IntegerField("Identification Difficulty", default=0, validators=[Optional()])
    hate_multi = IntegerField("Hate Multiplier", default=2, validators=[DataRequired()])
    fate_points = IntegerField("Fate Points", default=0, validators=[Optional()])
