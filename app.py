import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_debugtoolbar import DebugToolbarExtension

from config import DevelopementConfig, ProductionConfig

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or ProductionConfig)
# инициализирует расширения
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# toolbar = DebugToolbarExtension(app)