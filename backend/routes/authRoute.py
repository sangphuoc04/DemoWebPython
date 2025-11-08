from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from backend.models.userModel import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if all required fields are present
    if not all(key in data for key in ["username", "email", "password"]):
        return jsonify({"message": "Missing required fields"}), 400
    
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Validate email format
    if not email or '@' not in email:
        return jsonify({"message": "Invalid email format"}), 400

    # Check if email already exists
    if User.objects(email=email).first():
        return jsonify({"message": "Email already registered"}), 400
    
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"message": f"Registration failed: {str(e)}"}), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        # Check if all required fields are present
        if not all(key in data for key in ["email", "password"]):
            return jsonify({"message": "Missing email or password"}), 400
        
        email = data.get("email")
        password = data.get("password")

        # Find user by email
        user = User.objects(email=email).first()
        
        # Check if user exists and password is correct
        if user and user.check_password(password):
            access_token = create_access_token(identity=str(user.id))
            return jsonify({
                "message": "Login successful",
                "access_token": access_token,
                "user": {
                    "email": user.email,
                    "username": user.username
                }
            }), 200
        return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": f"Login failed: {str(e)}"}), 500

@auth.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"username": user.username, "email": user.email}), 200