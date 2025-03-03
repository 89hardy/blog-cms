from flask import Flask
from flask_login import LoginManager
from config.config import Config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    login_manager.init_app(app)
    
    # Initialize config
    config_class.init_app()
    
    # Register blueprints
    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from app.routes.posts import posts as posts_blueprint
    app.register_blueprint(posts_blueprint)
    
    from app.routes.media import media as media_blueprint
    app.register_blueprint(media_blueprint)
    
    return app 