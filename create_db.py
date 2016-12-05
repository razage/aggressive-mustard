from json import load
from os.path import join
from pathlib import Path

from am import app, db
from am.models import Attributes, BaseModel
from am.classes.models import AlternateName, Class

db.create_all()
db.session.commit()

export = Path(join(app.config['BASEDIR'], "data.json"))

if export.is_file():
    data = load(open(str(export)))

    for c in data['classes'].items():
        _stats = c[1]
        _class = Class(c[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'], _stats['hp_mod'])

        db.session.add(_class)
        db.session.commit()

        if "altnames" in _stats:
            for n in _stats['altnames'].items():
                _class.alternate_names.append(AlternateName(n[1], n[0]))
            db.session.commit()
