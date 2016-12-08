from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("index.html", title="Home")


from am.tags.views import mod as tag_mod

app.register_blueprint(tag_mod)
