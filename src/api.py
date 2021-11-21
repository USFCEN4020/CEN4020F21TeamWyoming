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
        password = user_data["password"]
        firstname = user_data["firstName"]
        lastname = user_data["lastName"]
        membership = user_data["membership"]
        content = username + '\n' + firstname + ' ' + lastname + '\n' + password + '\n' + membership + '\n'
        config.append_file('studentAccounts.txt', content)
        return username + ": In Queue\n"




if __name__ == '__main__':
    app.run(debug=True)
