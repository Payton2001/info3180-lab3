from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
app.secret_key = 'Som3$ec5etK*y'
from app import views