from os.path import abspath, dirname, join
from pathlib import Path

BASEDIR = abspath(dirname(__file__))
DB = Path(join(BASEDIR, "database.db"))

WTF_CSRF_ENABLED = True
SECRET_KEY = "not the real key"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
