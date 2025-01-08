from flask import Flask
from models import db, User
from api_routes import create_user, get_users, update_user, delete_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes
@app.route('/users', methods=['POST'])
def add_user():
    return create_user()

@app.route('/users', methods=['GET'])
def list_users():
    return get_users()

@app.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    return update_user(user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    return delete_user(user_id)

if __name__ == '__main__':
    print("Server is start")
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)

