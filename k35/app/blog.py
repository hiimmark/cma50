from flask import Blueprint, render_template, redirect, url_for, request, session
from database import query_db, execute_db

# Custom function to get the current user
def get_current_user():
    if 'user_id' in session:
        user = query_db('SELECT * FROM users WHERE id = ?', [session['user_id']], one=True)
        return user
    return None

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
    blogs = query_db('SELECT * FROM blogs')
    current_user = get_current_user() # Add current_user to context
    return render_template('home.html', blogs=blogs, current_user=current_user)

@blog.route('/new_blog')
def new_blog():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    current_user = get_current_user()
    return render_template('new_blog.html', current_user=current_user)

@blog.route('/new_blog', methods=['POST'])
def new_blog_post():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    user_id = session['user_id']
    
    execute_db('INSERT INTO blogs (title, user_id) VALUES (?, ?)', (title, user_id))
    
    return redirect(url_for('blog.index'))

@blog.route('/blog/<int:blog_id>')
def blog_view(blog_id):
    blog = query_db('SELECT * FROM blogs WHERE id = ?', [blog_id], one=True)
    entries = query_db('SELECT * FROM entries WHERE blog_id = ?', [blog_id])
    current_user = get_current_user()
    return render_template('blog_view.html', blog=blog, entries=entries, current_user=current_user)

@blog.route('/blog/<int:blog_id>/new_entry')
def new_entry(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    current_user = get_current_user()
    return render_template('entry.html', blog_id=blog_id, current_user=current_user)

@blog.route('/blog/<int:blog_id>/new_entry', methods=['POST'])
def new_entry_post(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    content = request.form.get('content')
    
    execute_db('INSERT INTO entries (title, content, blog_id) VALUES (?, ?, ?)', (title, content, blog_id))
    
    return redirect(url_for('blog.blog_view', blog_id=blog_id))

@blog.route('/blog/<int:blog_id>/edit/<int:entry_id>')
def edit_entry(blog_id, entry_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    entry = query_db('SELECT * FROM entries WHERE id = ? AND blog_id = ?', (entry_id, blog_id), one=True)
    if entry is None:
        return redirect(url_for('blog.blog_view', blog_id=blog_id))
    
    current_user = get_current_user()
    return render_template('blog_edit.html', entry=entry, current_user=current_user)

@blog.route('/blog/<int:blog_id>/edit/<int:entry_id>', methods=['POST'])
def edit_entry_post(blog_id, entry_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    content = request.form.get('content')
    
    execute_db('UPDATE entries SET title = ?, content = ? WHERE id = ? AND blog_id = ?', (title, content, entry_id, blog_id))
    
    return redirect(url_for('blog.blog_view', blog_id=blog_id))
