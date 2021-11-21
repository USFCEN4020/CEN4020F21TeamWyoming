from flask import Flask, json, jsonify, request
app = Flask(__name__)
import utils

@app.route("/")
def index():
    return 'The InCollege API'

#input users
@app.route("/api/in/users", methods=["GET", "POST"])
def create_user_route():
    config = utils.InCollegeConfig()
    if(request.method == "POST"):
        user_data = request.get_json()
        username = user_data["username"]
        first_name = user_data["firstName"]
        last_name = user_data["lastName"]
        password = user_data["password"]
        membership = user_data["membership"]
        created = config.create_user(username, password, first_name, last_name, membership)
        return jsonify({"created": created})

#inputs jobs
@app.route('/api/in/jobs', methods=['POST'])
def create_job_route():
    config = utils.InCollegeConfig()
    data = request.get_json()

    poster = data['poster']
    title = data['title']
    description = data['description']
    employer = data['employer']
    location = data['location']
    salary = data['salary']

    created = config.create_posting(poster, title, description, employer, location, salary)
    return jsonify({'created': created})

#inputs training courses
@app.route('/api/in/training', methods=['POST'])
def create_training_route():
    config = utils.InCollegeConfig()
    data = request.get_json()

    title = data['title']

    created = config.create_course(title)
    return jsonify({'created': created})

#outputs jobs
@app.route('/api/out/jobs', methods=['GET'])
def get_jobs_route():
    jobs = json.load(open('config.json', 'r'))['jobs']
    file = open('MyCollege_jobs.txt', 'w')

    for job in jobs:
        file.write(f"{job['title']}\n")
        file.write(f"{job['description']}\n")
        file.write(f"{job['employer']}\n")
        file.write(f"{job['location']}\n")
        file.write(f"{job['salary']}\n")
        file.write(f"=====\n")

    file.close()
    return jsonify({'outputed': 'jobs'})
        
#outputs profiles
@app.route('/api/out/profiles', methods=['GET'])
def get_profiles_route():
    accounts = json.load(open('config.json', 'r'))['accounts']
    file = open('MyCollege_profiles.txt', 'w')

    for k, account in accounts.items():
        profile = account['profile']
        for k, v in profile.items():
                if k != 'experience' and k != 'education':
                    file.write(f"{v}\n")
                else:
                    file.write(f'{k}:\n')
                    for entry in v:
                        for entry_k, entry_v in entry.items():
                            file.write(f'  {entry_v}\n')
        
        file.write("=====\n")
    file.close()
    return jsonify({'outputed': 'profiles'})

#outputs users
@app.route('/api/out/users', methods=['GET'])
def get_users_route():
    users = json.load(open('config.json', 'r'))['accounts']
    file = open('MyCollege_users.txt', 'w')

    for k, v in users.items():
        file.write(f"{k}\n")
        file.write(f"{v['membership']}\n")
        file.write('=====\n')
    
    file.close()
    return jsonify({'outputed': 'users'})

#outputs training courses
@app.route('/api/out/training', methods=['GET'])
def get_training_route():
    users = json.load(open('config.json', 'r'))['accounts']
    file = open('MyCollege_training.txt', 'w')

    for k,v in users.items():
        file.write(f"{k}\n")
        for training in v['courses']:
            file.write(f"{training}\n")
        file.write('=====\n')
    
    file.close()
    return jsonify({'outputed': 'training'})

#output Applied Jobs
    #MyCollege_appliedJobs.txt
        #Jobs Posting
            #Users applied
            #Why

#output Saved Jobs
    #MyColege_saveJobs.txt
        #user
            #Saved jobs
        #=====

if __name__ == '__main__':
    app.run(debug=True) 