from flask import Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello_world():
    from backend.services.Hello import say_hello
    return say_hello()

@hello.route('/myname')
def my_name():
    from backend.services.Hello import myName
    return myName()