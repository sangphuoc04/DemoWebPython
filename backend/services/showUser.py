from backend.models.userModel import User
from flask import request
class showUser:
    @staticmethod
    def get_all_users():
        users = User.objects()
        user_list = []
        for user in users:
            user_data = {
                "username": user.username,
                "email": user.email
            }
            user_list.append(user_data)
        return user_list

    @staticmethod
    def get_one_user(user_id):
        user = User.objects(id=user_id).first()
        if user:
            return {
                "username": user.username,
                "email": user.email
            }
        return None
    
    @staticmethod
    def update_user(user_id): 
        data = request.get_json()
        user = User.objects(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        
        if "username" in data:
            user.username = data["username"]
        if "email" in data:
            user.email = data["email"]
        if "password_hash" in data:
            user.password_hash = data["password_hash"]
        
        user.save()
        return {"message": "User updated successfully"}, 200

    @staticmethod
    def delete_user(user_id):
        user = User.objects(id=user_id).first()
        if not user:
            return {"message": "User not found"}, 404
        user.delete()
        return {"message": "User deleted successfully"}, 200