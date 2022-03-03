from flask import render_template,url_for, flash, redirect
from Flask_Blog import app
from Flask_Blog.forms import RegistrationForm, LoginForm
from Flask_Blog.models import User, Post




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