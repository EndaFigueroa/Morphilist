
from flask import render_template
from flask_login import LoginManager
from models import db, User
from __init__ import create_app
app = create_app()

app.config['SITE_NAME'] = 'Morphilist'
app.config['SITE_DESCRIPTION'] = 'a sleep-driven to-do list'
app.config['FLASK_DEBUG'] = 1


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mophi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(userid):
# 	return User.query.get(userid)

with app.app_context():
	db.create_all() # TODO this may be redundant
	

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

