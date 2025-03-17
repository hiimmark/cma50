from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import query_db, execute_db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = query_db('SELECT * FROM users WHERE email = ?', [email], one=True)
    
    if not user or not check_password_hash(user['password'], password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    session['user_id'] = user['id']
    session['user_name'] = user['name']
    return redirect(url_for('blog.index'))

@auth.route('/signup')
def signup():
    return render_template('register.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = query_db('SELECT * FROM users WHERE email = ?', [email], one=True)
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    execute_db('INSERT INTO users (email, password, name) VALUES (?, ?, ?)', (email, hashed_password, name))
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('blog.index'))
