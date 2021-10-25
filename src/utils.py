import json
import string
from random import randint

class InCollegeConfig:
    """
    This is a configuration class that stores all necessary text
    and user information that is used for user interface, communication,
    and content.
    """
    def __init__(self, filename='config.json'):
        """Initialize config by reading json from a given file."""
        self.filename = filename
        self.config = json.load(open(filename, 'r'))
    
    def full_name_exists(self, first: str, last: str) -> bool:
        """Check whether given first and last names exist."""
        return any([self.config['accounts'][account]['firstname'] == first and \
                self.config['accounts'][account]['lastname'] == last for \
                account in self.config['accounts']])
    
    def login_valid(self, username: str, password: str) -> bool:
        """Check whether login/password combination is valid."""
        return username in self.config['accounts'] and \
                self.config['accounts'][username]['password'] == password

    def username_exists(self, username: str) -> bool:
        """Check whether given username exists."""
        return username in self.config['accounts']

    def password_valid(self, password: str) -> bool:
        """Validate password based on provided guidelines."""
        cap_flag = any([char.isupper() for char in password])
        digit_flag = any([char.isdigit() for char in password])
        special_flag = any([char in string.punctuation for char in password])
        len_flag = 8 <= len(password) <= 12
        if not cap_flag:
            print('❌ Password needs to contain at least 1 capital letter.')
        if not digit_flag:
            print('❌ Password needs to contain at least 1 digit.')
        if not special_flag:
            print('❌ Password needs to contain at least 1 special character')
        if not len_flag:
            print('❌ Password needs to be between 8 and 12 characters long')
        return all([cap_flag, digit_flag, special_flag, len_flag])

    def create_user(
        self, username: str, password: str, firstname: str, lastname: str
    ) -> bool:
        """Validate user information and create new entry in the config."""
        num_users_flag = len(self.config['accounts']) >= 10
        password_flag = not self.password_valid(password)
        username_flag = self.username_exists(username)
        if num_users_flag: 
            print('❌ Too many users in the system. Try again later.')
        if username_flag:
            print('❌ Current username already has an account.')
        if any([num_users_flag, password_flag, username_flag]):
            return False
        else:
            self.config['accounts'][username] = {
                'password': password,
                'firstname': firstname,
                'lastname': lastname,
                'language': 'English',
                'profile': {
                    'title': '',
                    'major': '', 
                    'university': '', 
                    'about': '', 
                    'experience': [], 
                    'education': []
                },
                'friends': [],
                'friend_requests': [],
                'applications': [],
                'saved_jobs': []
            }
            # Write new config to json file.
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            return True

    def create_posting(
        self, 
        author: str, 
        title: str, 
        description: str, 
        employer: str, 
        location: str, 
        salary: str
    ) -> bool:
        """Create a job posting and update the json config file."""
        # Inefficient, but creates a new id by storing all previous in a set.
        ids = set()
        for job in self.config['jobs']:
            ids.add(job['id'])
        # Generate new id while it clashes with existing ones.
        new_id = randint(1, 100)
        while new_id in ids:
            new_id = randint(1, 100)
        fullname = self.config['accounts'][author]['firstname'] + ' ' + \
                self.config['accounts'][author]['firstname']
        self.config['jobs'].append({
            'author': fullname,
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'id': str(new_id)
        })

        if len(self.config['jobs']) >= 10:
            print('ERROR: Too many jobs in the system. Try again later.')
            return False
        else:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            return True

    def delete_posting(self, job_id: str):
        # Remove job from available postings.
        for job in self.config['jobs']:
            if job['id'] == job_id:
                self.config['jobs'].remove(job)
        # Remove job from user's application lists.
        for user in self.config['accounts']:
            if job_id in self.config['accounts'][user]['applications']:
                self.config['accounts'][user]['applications'].remove(job_id)
        # Save updated config.
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
        # Print success message.
        print(f'✅ Success! Posting {job_id} and associated apps were removed.')

    def unsave_posting(self, job_id: str):
        user = self.config['accounts'][self.config['current_login']]
        user['saved_jobs'].remove(job_id)
        print(f'✅ Success! Posting {job_id} has been removed from saved.')
        
    def save_login(self, username: str) -> None:
        """Update current logged in user and write changes to json file."""
        self.config['current_login'] = username
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def save_guest_control(self, username: str, control_setting_list: dict) -> None:
        """Update current guest control setting in user's privacy setting and write changes to json file."""
        self.config['guest_control'].update({username: control_setting_list})
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def show_guest_control(self, username: str) -> None:
        """Display the current guest control setting of the current user."""
        guest_control_list = ['InCollege Email', 'SMS', 'Targeted Advertising features']
        print('Your current guest control setting: ')
        # Equivalent to the commented section below
        list(map((lambda x: print(x + ': ' + 'ON')
                  if x in self.config['guest_control'][username]
                  else print(x + ': ' + 'OFF')), guest_control_list))

        # status = lambda x: print(x + ': ' + 'ON')\
        #     if x in self.config['guest_control'][username]\
        #     else print(x + ': ' + 'OFF')
        # for key in guest_control_list:
        #     status(key)

    def save_lang(self, username: str, lang: str) -> None:
        """Update current lang setting in user and write changes to json file."""
        self.config['accounts'][username]['language'] = lang
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def show_lang(self, username: str) -> None:
        """Display the lang setting for the current user."""
        print('Your current language setting: ')
        print(self.config['accounts'][username]['language'])

    def save_profile(self, username: str , profile: dict) -> None:
        """Update profile of user and write changes to json file."""
        self.config['accounts'][username]['profile'] = profile
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def display_profile(self, username: str) -> None:
        '''Displays a user profile'''
        if self.username_exists(username):
            user = self.config['accounts'][username]
            profile = user['profile']
            firstname = user['firstname']
            lastname = user['lastname']
            print('{} {}'.format(firstname, lastname))
            for k, v in profile.items(): #loops through all keys in profile
                if k != 'experience' and k != 'education':
                    print('{}: {}'.format(k, v))
                else:
                    print('{}:'.format(k))
                    for entry in v: #loops elements in the experience and education arrays
                        for entry_k, entry_v in entry.items(): #loops through all kes in a entry, which are an experience or education entry
                            print('   {}: {}'.format(entry_k, entry_v))
                        print('')
                        
        else:
            print('User {} does not exist.'.format(username))

    def display_all_jobs(self) -> None:
        """Display job information based on requested job id."""
        # The job is guaranteed to exist, since it's retrieved from config.
        for job in self.config['jobs']:
            self.display_job(job['id'])
            print('\n')


    def display_job(self, job_id: str) -> None:
        """Display job information based on requested job id."""
        # The job is guaranteed to exist, since it's retrieved from config.
        for job in self.config['jobs']:
            if job['id'] == job_id:
                if job_id in self.config['accounts'][self.config['current_login']]['applications']:
                    print('YOU HAVE APPLIED FOR THIS JOB')
                print('Job information is displayed below:')
                print(f'✍️  Posted by: {job["author"]}')
                print(f'🧑 Role: {job["title"]}')
                print(f'📝 Description: {job["description"]}')
                print(f'🕴️  Employer: {job["employer"]}')
                print(f'🏙️  Location: {job["location"]}')
                print(f'💰 Salary: {job["salary"]}')

                
    def submit_application(self, user: str, job_id: str, grad_date: str, start_date: str, brief: str) -> None:
        """Apply for a job by adding the id into user's application list."""
        print(f'✅ Success! You have applied to the job {job_id}! 🎉')
        if job_id in self.config['accounts'][user]['applications']:
            print('You have applied this job.\n')
            return
        # application = {job_id : [grad_date, start_date, brief]}
        # self.config['accounts'][user]['applications'].append(application)
        self.config['accounts'][user]['applications'].append(job_id)
        self.config['accounts'][user]['applications'].append([grad_date, start_date, brief])
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def withdraw_application(self, user: str, job_id: str) -> None:
        """Withdraw application by removing it from user's application list."""
        print(f'✅ Success. The application {job_id} was withdrawn.')
        index = self.config['accounts'][user]['applications'].index(job_id)
        self.config['accounts'][user]['applications'].pop(index + 1)
        self.config['accounts'][user]['applications'].pop(index)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def save_application(self, user: str, job_id: str) -> None:
        print(f'✅ Success. The application {job_id} was saved.')
        if job_id not in self.config['accounts'][user]['saved_jobs']:
            self.config['accounts'][user]['saved_jobs'].append(job_id)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def get_list_jobs(
            self, user: dict, my_apps=False, my_posts=False, saved=False
    ) -> list:
        """Return a list of jobs to be displayed in the menu based on user."""
        jobs = list()
        if my_apps:
            for app in user['applications']:
                for job in self.config['jobs']:
                    if job['id'] in app:
                        jobs.append(' '.join([
                            str(job['id']),
                            job['title'],
                            job['location']
                        ]))
        elif saved:
            for job in self.config['jobs']:
                if job['id'] in user['saved_jobs']:
                    jobs.append(' '.join([
                        job['id'],
                        job['title'],
                        job['location']
                    ]))
        elif my_posts:
            for job in self.config['jobs']:
                if job['author'] == user['firstname'] + ' ' + user['lastname']:
                    jobs.append(' '.join([
                        job['id'],
                        job['title'],
                        job['location']
                    ]))
        else: # TODO: merge these four branches together (@alisnichenko).
            for job in self.config['jobs']:
                # Filter list based on author and existing user applications.
                if job['author'] != user['firstname'] + ' ' + user['lastname'] and \
                        job['id'] not in user['applications']:
                    # Display in the format id_title_location.
                    jobs.append(' '.join([
                        str(job['id']), 
                        job['title'], 
                        job['location']
                    ]))
        return jobs

    def search_student(self, key: str, value: str):
        '''Returns an array of all the account usernames found based on a key and value.\n\nvalid keys = {"lastname", "major", "university"}\n\nreturns -1 if the key is invalid'''
        valid_keys = ["lastname", "major", "university"]
        accounts = self.config['accounts']
        accountsFound = []
    
        if key in valid_keys:
            for username, data in accounts.items():
                if username == self.config['current_login'] or self.config['current_login'] in self.config['accounts'][username]['friends']:
                    continue
                if key == 'lastname' and data[key] == value:
                    accountsFound.append(username)
                elif (key == 'major' or key == 'university') and data['profile'][key] == value:
                    accountsFound.append(username)
        return accountsFound

    def display_friends(self, username: str):
        user = self.config['accounts'][username]
        if len(user['friends']) == 0:
            print('None')
        else:
            for friend_username in user['friends']:
                self.display_profile(friend_username)
                print(' ')

    def save_friends(self, username: str, friendList: list) -> None:
        """Update friends list and write to json"""
        self.config['accounts'][username]['friends'] = friendList
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def send_friend_request(self, target_user: str, sender: str) -> None:
        """Update friend_requests list and write to json"""
        self.config['accounts'][target_user]['friend_requests'].append(sender)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def accept_friend_request(self, user: str, acceptedUsername: str) -> None:
        self.config['accounts'][user]['friends'].append(acceptedUsername)
        self.config['accounts'][user]['friend_requests'].remove(acceptedUsername)

        self.config['accounts'][acceptedUsername]['friends'].append(user)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def decline_friend_request(self, user: str, declinedUsername: str) -> None:
        self.config['accounts'][user]['friend_requests'].remove(declinedUsername)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    
