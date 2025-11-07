from flask import Blueprint, request, jsonify
from backend.services.showUser import showUser

user = Blueprint('user', __name__)

@user.route('/getusers', methods=['GET'])
def get_all_users():
    users = showUser.get_all_users()
    return jsonify(users)

@user.route('/addusers', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password_hash = data.get("password_hash")
    result = showUser().create_user(username, email, password_hash)
    return jsonify(result)