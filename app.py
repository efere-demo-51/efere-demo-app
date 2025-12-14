from flask import Flask 
from flask_sqlalchemy import SQLAlchemy from config import Config import os
db = SQLAlchemy()
def create_app():  app = Flask(__name__, instance_relative_config=True)    app.config.from_object(Config)  try: os.makedirs(app.instance_path, exist_ok=True). except Exception:  pass    db.init_app(app)  return app
