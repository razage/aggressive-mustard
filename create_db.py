from json import load
from os.path import join
from pathlib import Path

from am import app, db
from am.models import Attributes, BaseModel
from am.classes.models import AlternateName, Class
from am.items.models import Weapon
from am.races.models import Race
from am.tags.models import Tag

db.create_all()
db.session.commit()

exports = {
    "classes": Path(join(app.config['BASEDIR'], "initial_data", "classes.json")),
    "races": Path(join(app.config['BASEDIR'], "initial_data", "races.json")),
    "servers": Path(join(app.config['BASEDIR'], "initial_data", "servers.json")),
    "tags": Path(join(app.config['BASEDIR'], "initial_data", "tags.json"))
}

for f in exports.items():
    if f[0] == "classes" and f[1].is_file():
        classes = load(open(str(f[1])))

        for c in classes.items():
            _stats = c[1]
            _class = Class(c[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'], _stats['hp_mod'])
            db.session.add(_class)
            db.session.commit()

            if "altnames" in _stats:
                for n in _stats['altnames'].items():
                    _class.alternate_names.append(AlternateName(n[1], n[0]))
                    db.session.commit()

    elif f[0] == "races" and f[1].is_file():
        races = load(open(str(f[1])))

        for r in races.items():
            _stats = r[1]
            _race = Race(r[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'], _stats['fate'], _stats['bonus_points'])
            db.session.add(_race)
            db.session.commit()

    elif f[0] == "tags" and f[1].is_file():
        tags = load(open(str(f[1])))

        for t in tags.items():
            _data = t[1]
            _tag = Tag(t[0], _data['category'], _data['description'])
            db.session.add(_tag)
            db.session.commit()
