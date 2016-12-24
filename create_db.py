from collections import OrderedDict
from json import load
from os.path import join
from pathlib import Path

from sqlalchemy.orm.exc import NoResultFound

from am import app, db
from am.classes.models import AlternateName, Class
from am.enemies.models import Ability, Enemy, LootDrop
from am.items.models import Item, Weapon
from am.races.models import Race
from am.tags.models import Tag

db.create_all()
db.session.commit()

exports = OrderedDict([
    ("tags", Path(join(app.config['BASEDIR'], "initial_data", "tags.json"))),
    ("items", Path(join(app.config['BASEDIR'], "initial_data", "items.json"))),
    ("weapons", Path(join(app.config['BASEDIR'], "initial_data", "weapons.json"))),
    ("classes", Path(join(app.config['BASEDIR'], "initial_data", "classes.json"))),
    ("races", Path(join(app.config['BASEDIR'], "initial_data", "races.json"))),
    ("servers", Path(join(app.config['BASEDIR'], "initial_data", "servers.json"))),
    ("enemies", Path(join(app.config['BASEDIR'], "initial_data", "enemies.json")))
])

for f in exports.items():
    if f[0] == "tags" and f[1].is_file():
        tags = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for t in tags.items():
            _data = t[1]
            _tag = Tag(t[0], _data['category'], _data['description'])
            db.session.add(_tag)
        db.session.commit()

    elif f[0] == "items" and f[1].is_file():
        items = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for i in items.items():
            _data = i[1]
            _item = Item(i[0], _data['rank'], _data['timing'], _data['target'], _data['range'], _data['check'],
                         _data['price'], _data['description'])

            if _data['tags'] is not None:
                for tag in _data['tags']:
                    _item.tags.append(Tag.query.filter(Tag.name == tag).one())

            db.session.add(_item)
            db.session.commit()

    elif f[0] == "weapons" and f[1].is_file():
        weapons = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for w in weapons.items():
            _data = w[1]
            _weapon = Weapon(w[0], _data['rank'], _data['attack'], _data['magic'], _data['accuracy'],
                             _data['initiative'], _data['range'], _data['price'], _data['description'])

            if _data['tags'] is not None:
                for tag in _data['tags']:
                    _weapon.tags.append(Tag.query.filter(Tag.name == tag).one())

            db.session.add(_weapon)
            db.session.commit()

    elif f[0] == "classes" and f[1].is_file():
        classes = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for c in classes.items():
            _stats = c[1]
            _class = Class(c[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'],
                           _stats['hp_mod'])
            db.session.add(_class)
            db.session.commit()

            if "altnames" in _stats:
                for n in _stats['altnames'].items():
                    _class.alternate_names.append(AlternateName(n[1], n[0]))
                    db.session.commit()

    elif f[0] == "races" and f[1].is_file():
        races = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for r in races.items():
            _stats = r[1]
            _race = Race(r[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'], _stats['fate'],
                         _stats['bonus_points'])
            db.session.add(_race)
            db.session.commit()

    elif f[0] == "enemies" and f[1].is_file():
        enemies = load(open(str(f[1])), object_pairs_hook=OrderedDict)

        for e in enemies.items():
            _stats = e[1]
            if _stats:
                enemy = Enemy(e[0], _stats['STR'], _stats['DEX'], _stats['POW'], _stats['INT'], _stats['HP'],
                              _stats['rank'], _stats['initiative'], _stats['speed'], _stats['evasion'],
                              _stats['phys_def'], _stats['resistance'], _stats['mag_def'], _stats['id_diff'],
                              _stats['hate_multi'], _stats['fate_points'])

                enemy.enemy_type = Tag.query.filter(Tag.name == _stats['type']).one()

                if _stats['tags'] is not None:
                    for tag in _stats['tags']:
                        enemy.tags.append(Tag.query.filter(Tag.name == tag).one())

                for ability in _stats['abilities'].items():
                    _data = ability[1]
                    try:
                        a = db.session.query(Ability).filter(Ability.name == ability[0]).one()
                    except NoResultFound:
                        a = Ability(ability[0], _data['timing'], _data['check'], _data['target'], _data['range'],
                                    _data['limit'], _data['description'])

                        if _data['attack_type'] is not None:
                            a.attack_type = Tag.query.filter(Tag.name == _data['attack_type']).one()

                    enemy.abilities.append(a)

                if 'loot' in _stats:
                    for loot in _stats['loot'].items():
                        _data = loot[1]
                        l = LootDrop(loot[0], _data['quantity'], _data['gold'])

                        if _data['table'] == "items":
                            l.item = Item.query.filter(Item.name == _data['item']).one()
                        elif _data['table'] == "weapons":
                            l.weapon = Weapon.query.filter(Weapon.name == _data['item']).one()

                        enemy.loot.append(l)

                db.session.add(enemy)
                db.session.commit()

            else:
                continue
