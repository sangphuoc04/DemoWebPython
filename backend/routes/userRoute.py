from flask import Blueprint, jsonify
from backend.services.showUser import showUser


user = Blueprint('user', __name__)

@user.route('/getusers', methods=['GET'])
def get_all_users():
    users = showUser.get_all_users()
    return jsonify(users)

@user.route('/getuser/<user_id>', methods=['GET'])
def get_one_user(user_id):
    user = showUser.get_one_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@user.route('/updateuser/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = showUser.update_user(user_id)
    return jsonify(user)

@user.route('/deleteuser/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = showUser.delete_user(user_id)
    return jsonify(result)