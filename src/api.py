from flask import Flask, json, jsonify, request

app = Flask(__name__)
import utils

@app.route("/")
def index():
    return 'The InCollege APIs are Launched.'


@app.route('/api/in/users', methods=['GET', 'POST'])
def create_user_route():
    config = utils.InCollegeConfig()
    if request.method == 'POST':
        user_data = request.get_json()
        username = user_data["username"]
        first_name = user_data["firstName"]
        last_name = user_data["lastName"]
        password = user_data["password"]
        membership = user_data["membership"]
        created = config.create_user(username, password, first_name, last_name, membership)
        return jsonify({"created": created})


if __name__ == '__main__':
    app.run(debug=True)
