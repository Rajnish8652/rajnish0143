from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from PythonProjects.routes import home
    from PythonProjects.models import db
    # Sceret key
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///demo'
    app.config['SECRET_KEY'] = 'any secret'
    db.init_app(app)  
    app.register_blueprint(home)
    
    return app
    