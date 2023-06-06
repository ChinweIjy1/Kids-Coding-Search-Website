from flask import Flask
from flask_login import LoginManager
from .views import bp

app = Flask(__name__)
app.secret_key = 'secret_key'
app.register_blueprint(bp)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(email):
    return User(email)
