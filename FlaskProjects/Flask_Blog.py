from datetime import datetime
from enum import unique
from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '3320f813d85f022ca5114eeee6997837'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy = True)

    def __repr__(self):
        return f"User'{self.username}','{self.email}','{self.image_file}'"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


posts = [
    {
        "author":"Akash Kumar",
        "title":"Blog Post1",
        "content":"First Post Content",
        "date_posted": "April 20, 2018"
    },
    {
        "author":"Jane Doe",
        "title":"Blog Post2",
        "content":"Second Post Content",
        "date_posted": "April 21, 2018"
    }
]

@app.route("/")
@app.route("/Home")
def Home():
    return render_template('Home.html',posts = posts)


@app.route("/About")
def About():
    return render_template('About.html', title = "About")


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Home'))
    return render_template('register.html', title = 'Registration', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'test':
            flash(f'You have been logged in !', 'success')
            return redirect(url_for('Home'))
        else:
            flash(f'Please check your email and password', 'danger')
    return render_template('login.html', title = 'Login',form = form)


if __name__ == '__main__':
    app.run(debug=True)