from flask import Flask
import settings
from apps.user.view import user_blueprint


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings)
    
    app.register_blueprint(user_blueprint)
    print(app.url_map)
    
    return app