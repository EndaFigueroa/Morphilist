from flask import Flask
from morphilist.mophroutes import routes_blueprint

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # I think more blueprints might be used to break routes up into things like
    # post_routes
    # subforum_routes
    # etc
    app.register_blueprint(routes_blueprint)
    # Set globals
    from morphilist.models import db
    db.init_app(app)
    
    with app.app_context():
        # Add some routes
        db.create_all()
        return app

