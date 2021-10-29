import json
import string
import re
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

    def __getitem__(self, key):
        """Allow calling self['thing'] instead of self.config['thing']."""
        return self.config[key]

    def __setitem__(self, key, value):
        """Allow setting self['thing'] = val instead of self.config[..."""
        self.config[key] = value

    def save_config(self) -> None:
        """Write current config to file with utf-8 indentation."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
            f.write('\n')  # linux convention.

    def full_name_exists(self, first: str, last: str) -> bool:
        """Check whether given first and last names exist."""
        return any([self['accounts'][account]['firstname'] == first and \
                    self['accounts'][account]['lastname'] == last for \
                    account in self['accounts']])

    def login_valid(self, username: str, password: str) -> bool:
        """Check whether login/password combination is valid."""
        return username in self['accounts'] and \
               self['accounts'][username]['password'] == password

    def username_exists(self, username: str) -> bool:
        """Check whether given username exists."""
        return username in self['accounts']

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
            self, username: str, password: str, firstname: str, lastname: str, membership: str
    ) -> bool:
        """Validate user information and create new entry in the config."""
        num_users_flag = len(self['accounts']) >= 10
        password_flag = not self.password_valid(password)
        username_flag = self.username_exists(username)
        if num_users_flag:
            print('❌ Too many users in the system. Try again later.')
        if username_flag:
            print('❌ Current username already has an account.')
        if any([num_users_flag, password_flag, username_flag]):
            return False
        else:
            self['accounts'][username] = {
                'password': password,
                'firstname': firstname,
                'lastname': lastname,
                'membership': '',
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
                'applications': [],  # is this a dict or list the config.json shows dict yet here it's a list
                'saved_jobs': [],
                'inbox': []
            }

            if membership.strip().lower() == 'pro':
                self['accounts'][username]['membership'] = 'pro'
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
        for job in self['jobs']:
            ids.add(job['id'])
        # Generate new id while it clashes with existing ones.
        new_id = randint(1, 100)
        while new_id in ids:
            new_id = randint(1, 100)
        fullname = self['accounts'][author]['firstname'] + ' ' + \
                   self['accounts'][author]['firstname']
        self['jobs'].append({
            'author': fullname,
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'id': str(new_id)
        })

        if len(self['jobs']) >= 10:
            print('ERROR: Too many jobs in the system. Try again later.')
            return False
        else:
            self.save_config()
            return True

    def delete_posting(self, job_id: str):
        # Remove job from available postings.
        for job in self['jobs']:
            if job['id'] == job_id:
                self['jobs'].remove(job)
        # Remove job from user's application lists.
        for user in self['accounts']:
            if job_id in self['accounts'][user]['applications']:
                del self['accounts'][user]['applications'][job_id]
        # Save updated config.
        self.save_config()
        # Print success message.
        print(f'✅ Success! Posting {job_id} and associated apps were removed.')

    def unsave_posting(self, job_id: str):
        user = self['accounts'][self['current_login']]
        user['saved_jobs'].remove(job_id)
        print(f'✅ Success! Posting {job_id} has been removed from saved.')

    def save_login(self, username: str) -> None:
        """Update current logged in user and write changes to json file."""
        self['current_login'] = username
        if username != '':
            self['current_login_membership'] = self['accounts'][username]['membership']
        else:
            self['current_login_membership'] = ''
        self.save_config()

    def save_guest_control(self, username: str, control_setting_list: dict) -> None:
        """Update current guest control setting in user's privacy setting."""
        self['guest_control'].update({username: control_setting_list})
        self.save_config()

    def show_guest_control(self, username: str) -> None:
        """Display the current guest control setting of the current user."""
        guest_control_list = ['InCollege Email', 'SMS', 'Targeted Advertising features']
        print('Your current guest control setting: ')
        # Equivalent to the commented section below
        list(map((lambda x: print(x + ': ' + 'ON')
        if x in self['guest_control'][username]
        else print(x + ': ' + 'OFF')), guest_control_list))

    def save_lang(self, username: str, lang: str) -> None:
        """Update current lang setting in user and write changes to json file."""
        self['accounts'][username]['language'] = lang
        self.save_config()

    def show_lang(self, username: str) -> None:
        """Display the lang setting for the current user."""
        print('Your current language setting: ')
        print(self['accounts'][username]['language'])

    def save_profile(self, username: str, profile: dict) -> None:
        """Update profile of user and write changes to json file."""
        self['accounts'][username]['profile'] = profile
        self.save_config()

    def display_profile(self, username: str) -> None:
        '''Displays a user profile'''
        if self.username_exists(username):
            user = self['accounts'][username]
            profile = user['profile']
            firstname = user['firstname']
            lastname = user['lastname']
            print('{} {}'.format(firstname, lastname))
            # For all keys within the profile.
            for k, v in profile.items():
                if k != 'experience' and k != 'education':
                    print(f'{k}: {v}')
                else:
                    print(f'{k}:')
                    # For every element in the education/experience section.
                    for entry in v:
                        # For each entry in the section of element/education.
                        for entry_k, entry_v in entry.items():
                            print(f'   {entry_k}: {entry_v}')
                        print('')
        else:
            print(f'❌ Error. User {username} does not exist.')

    def display_job(self, job_id: str) -> None:
        """Display job information based on requested job id."""
        # The job is guaranteed to exist, since it's retrieved from config.
        for job in self['jobs']:
            if job['id'] == job_id:
                print('Job information is displayed below:')
                print(f'✍️  Posted by: {job["author"]}')
                print(f'🧑 Role: {job["title"]}')
                print(f'📝 Description: {job["description"]}')
                print(f'🕴️  Employer: {job["employer"]}')
                print(f'🏙️  Location: {job["location"]}')
                print(f'💰 Salary: {job["salary"]}')

    def submit_application(
            self,
            user: str,
            job_id: str,
            grad_date: str,
            start_date: str,
            brief: str
    ) -> None:
        """Apply for a job by adding the id into user's application list."""
        print(f'✅ Success! You have applied to the job {job_id}! 🎉')
        if job_id in self['accounts'][user]['applications']:
            print('❌ Error. You have applied this job.')
            return
        self['accounts'][user]['applications'][job_id] = {
            'grad_date': grad_date,
            'start_date': start_date,
            'app_text': brief
        }
        self.save_config()

    def withdraw_application(self, user: str, job_id: str) -> None:
        """Withdraw application by removing it from user's application list."""
        print(f'✅ Success. The application {job_id} was withdrawn.')
        del self['accounts'][user]['applications'][job_id]
        self.save_config()

    def save_application(self, user: str, job_id: str) -> None:
        print(f'✅ Success. The application {job_id} was saved.')
        if job_id not in self['accounts'][user]['saved_jobs']:
            self['accounts'][user]['saved_jobs'].append(job_id)
        self.save_config()

    def get_list_jobs(
            self,
            user: dict,
            browse=False,
            my_apps=False,
            my_posts=False,
            saved=False
    ) -> list:
        """Return a list of jobs to be displayed in the menu based on user."""
        jobs = list()
        # Create a list of flags to filter the jobs with.
        fullname = user['firstname'] + ' ' + user['lastname']
        all_jobs = not my_apps and not my_posts and not saved and not browse
        for job in self['jobs']:
            in_applications = job['id'] in user['applications']
            in_saved = job['id'] in user['saved_jobs']
            is_author = fullname == job['author']
            if (browse and not in_applications and not is_author or
                    my_apps and in_applications or
                    my_posts and is_author or
                    saved and in_saved or
                    all_jobs):
                # FIlter job based on the flag provided.
                ind = '✅ ' if all_jobs and in_applications else ''
                ind += '🔖 ' if all_jobs and in_saved else ''
                job_line = [job['id'], ind + job['title'], job['location']]
                jobs.append(' | '.join(job_line))
        return jobs

    def search_student(self, key: str, val: str):
        """Returns an array of all the account usernames that match key/val."""
        valid_keys = ["lastname", "major", "university"]
        accounts, matches = self['accounts'], []
        if key in valid_keys:
            for user, data in accounts.items():
                is_login = user == self['current_login']
                is_fr = self['current_login'] in accounts[user]['friends']
                if (key == 'lastname' and data[key] == val or
                    ((key == 'major' or key == 'university') and
                     data['profile'][key] == val)) and not (is_login or is_fr):
                    matches.append(user)
        return matches

    def display_friends(self, username: str):
        user = self['accounts'][username]
        if len(user['friends']) == 0:
            print('None')
        else:
            for friend_username in user['friends']:
                self.display_profile(friend_username)
                print(' ')

    def save_friends(self, username: str, friendList: list) -> None:
        """Update friends list and write to json"""
        self['accounts'][username]['friends'] = friendList
        self.save_config()

    def send_friend_request(self, target_user: str, sender: str) -> None:
        """Update friend_requests list and write to json"""
        self['accounts'][target_user]['friend_requests'].append(sender)
        self.save_config()

    def accept_friend_request(self, user: str, accepted_username: str) -> None:
        self['accounts'][user]['friends'].append(accepted_username)
        self['accounts'][user]['friend_requests'].remove(accepted_username)

        self['accounts'][accepted_username]['friends'].append(user)
        self.save_config()

    def decline_friend_request(self, user: str, declined_username: str) -> None:
        self['accounts'][user]['friend_requests'].remove(declined_username)
        self.save_config()

    def send_message(self, recipient: str, message: str) -> None:
        email = {self['current_login']: message}
        if recipient == '':
            print('\nPlease not to leave the recipient and the message blank.\n')
        elif recipient == self['current_login']:
            print('\nYou need a friend.\n')
        elif recipient in self['accounts']:
            if self['current_login_membership'] != 'pro' and recipient.strip() not in \
                    self['accounts'][self['current_login']]['friends']:
                print('\nStandard user can not send message to whom are not your friend.\n')
            else:
                self['accounts'][recipient]['inbox'].append(email)
                print('\nYour message has been sent.\n')
        else:
            print('\nThe recipient does not exist.\n')

        self.save_config()

    def reply_message(self, email: dict) -> None:
        matcher = re.search("(.*): (.*)", email)
        sender = matcher.group(1)
        message = matcher.group(2)
        reply = input('Reply: \n')
        self.send_message(sender, reply)
        self.save_config()

    def delete_message(self, email: dict) -> None:
        matcher = re.search("(.*): (.*)", email)
        sender = matcher.group(1)
        message = matcher.group(2)
        counter = 0
        for element in self['accounts'][self['current_login']]['inbox']:
            if sender in element and element[sender] == message:
                self['accounts'][self['current_login']]['inbox'].pop(counter)
            counter += 1
        self.save_config()

