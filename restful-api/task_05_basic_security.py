from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'T0p_s3cret@2024BR'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Example hashed passwords (replace these with actual hashed passwords)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)["password"], password):
        return username

@app.route('/')
def index():
    return "Welcome to the API! Use /login to get a JWT token."

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": current_user}), 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Insufficient permissions"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)
