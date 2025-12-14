config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-efere-demo")SQLALCHEMY_TRACK_MODIFICATIONS = FalseSQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","sqlite:///" + os.path.join(basedir, "instance", "app.db"))
