from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required
from models import User, db
# from user import username_taken, email_taken, valid_username

routes_blueprint = Blueprint('routes',__name__)
####### HOME
@routes_blueprint.route('/')
def index():
    return render_template('/index.html')

# @routes_blueprint.route('/action_login', methods=['POST'])
# def action_login():
# 	username = request.form['user_name']
# 	password = request.form['password_hash']
# 	user = User.query.filter(User.user_name == username).first()
# 	if user and user.check_password(password):
# 		login_user(user)
# 	else:
# 		errors = []
# 		errors.append("Username or password is incorrect!")
# 		return render_template("login.html", errors=errors)
# 	return redirect("/")


# @login_required
# @routes_blueprint.route('/action_logout')
# def action_logout():
# 	#todo
# 	logout_user()
# 	return redirect("/")

# @routes_blueprint.route('/action_createaccount', methods=['POST'])
# def action_createaccount():
# 	username = request.form['user_name']
# 	password = request.form['password_hash']
# 	email = request.form['email']
# 	errors = []
# 	retry = False
# 	if username_taken(username):
# 		errors.append("Username is already taken!")
# 		retry=True
# 	if email_taken(email):
# 		errors.append("An account already exists with this email!")
# 		retry = True
# 	if not valid_username(user):
# 		errors.append("Username is not valid!")
# 		retry = True
# 	# if not valid_password(password):
# 	# 	errors.append("Password is not valid!")
# 	# 	retry = True
# 	if retry:
# 		return render_template("login.html", errors=errors)
# 	user = User(email, username, password)
# 	if user.user_name == "admin":
# 		user.admin = True
# 	db.session.add(user)
# 	db.session.commit()
# 	login_user(user)
# 	return redirect("/")



######## NAVIGATION BAR
@routes_blueprint.route('/day_view')
def day_view():
    return render_template('day_view.html')

@routes_blueprint.route('/night_view')
def night_view():
    return render_template('night_view.html')

@routes_blueprint.route('/faq')
def faq():
    return render_template('/faq.html')

@routes_blueprint.route('/user')
def user():
    return render_template('/user.html')

@routes_blueprint.route('/reports')
def reports():
    return render_template('/reports.html')

######### TASKS
@routes_blueprint.route('/new_task')
def new_task():
    return render_template('new_task.html')

@routes_blueprint.route('/edit_task')
def edit_task():
    return render_template('/edit_task.html')