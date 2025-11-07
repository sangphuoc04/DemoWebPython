from flask import Flask
from mongoengine import connect

connect(
    db="PythonDemoWeb",
    host="mongodb://localhost:27017/PythonDemoWeb"
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
 

    from backend.routes.HelloRoute import hello
    app.register_blueprint(hello)
    from backend.routes.aboutRoute import about
    app.register_blueprint(about)
    from backend.routes.userRoute import user
    app.register_blueprint(user)

    return app