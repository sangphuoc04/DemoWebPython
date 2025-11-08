from backend.models.userModel import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
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
    
    def create_user(self, username, email, password_hash):
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        new_user.save()
        return {
            "message": "User created successfully",
            "username": new_user.username,
            "email": new_user.email
        }

