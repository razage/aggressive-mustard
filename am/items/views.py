from flask import Blueprint

from am import db

mod = Blueprint("items", __name__, url_prefix="/items")


@mod.route("/create/weapon", methods=["GET", "POST"])
def create_weapon():
    pass
