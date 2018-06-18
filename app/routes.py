from flask import render_template, flash, redirect, url_for, request
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm, SubscribeForm
from app.models import User, UserEmail
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
#@login_required #remove this to remove login requirement for a page
def index():	
	return render_template('index.html', title='Home', subscribe_form=SubscribeForm())

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
	form = SubscribeForm()
	if form.validate_on_submit():
		email_addr = UserEmail(email_addr=form.email_addr.data)
		db.session.add(email_addr)
		db.session.commit()
		flash('Thank you for subscribing')
		
		return redirect(url_for('index'))
	return render_template('register.html', title='Subscribe', form=form)
	
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = Email(email=form.email.data)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page=request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)
	
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))