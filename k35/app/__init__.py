from flask import Flask
from database import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    init_db()
    
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
