from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(20), unique=True)
    password_hash = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    admin = db.Column(db.Boolean, default=False)
    days = db.relationship('Day', backref='author')
    nights = db.relationship('Night', backref='author')

    def __init__(self,email,user_name,password_hash):
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password_hash)
    
    # def check_password(self, password_hash):
    #     return check_password_hash(self.password_hash, password_hash)
    
    # class Days(db.Model):
    #     id=db.Column(db.Integer, primary_key=True)
    #     day_user=db.Column(db.Integer, db.ForeignKey('User.id'))
    #     day_date=db.Column(db.Date,nullable=False)
    #     day_caff=db.Column(db.Integer)
    #     day_todo=db.relationship("Todo", backref="Days")

    #     def __init__(self,day_user,day_date,day_caff,day_todo):
    #         self.day_user=day_user
    #         self.day_date=day_date
    #         self.day_caff = day_caff
    #         self.day_todo = day_todo
    
    # class Todo(db.Model):
    #     id=db.Column(db.Integer, primary_key=True)
    #     todo_days = db.Column(db.Integer, db.ForeignKey('Days.id'))
    #     todo_title = db.Column(db.VARCHAR(30),nullable=False)
    #     todo_time = db.Column(db.Time)
    #     todo_date = db.Column(db.Date, nullable=False)
    #     todo_allday = db.Column(db.Boolean, default=False)
    #     todo_pri = db.Column(db.Text, nullable=False)
    #     todo_excer = db.Column(db.Integer, nullable=False)
    #     todo_desc = db.Column(db.VARCHAR(200), nullable=False)
    #     todo_status = db.Column(db.Boolean, default=False)

    #     def __init__(self,todo_days,todo_title,todo_time,todo_date,todo_allday,todo_pri,todo_excer,todo_desc,todo_status):
    #         self.todo_days = todo_days
    #         self.todo_title = todo_title
    #         self.todo_time = todo_time
    #         self.todo_date = todo_date
    #         self.todo_allday = todo_allday
    #         self.todo_pri = todo_pri
    #         self.todo_excer = todo_excer
    #         self.todo_desc = todo_desc
    #         self.todo_status = todo_status
                

