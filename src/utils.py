import json
import string

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
        for account in self.config['accounts']:
            if self.config['accounts'][account]['firstname'] == first and \
                self.config['accounts'][account]['lastname'] == last:
                return True
        return False
    
    def login_valid(self, username: str, password: str) -> bool:
        """Check whether login/password combination is valid."""
        if username in self.config['accounts'] and \
            self.config['accounts'][username]['password'] == password:
            print('SUCCESS, {}. You are logged in.'.format(username))
            return True
        else:
            print('ERROR. Invalid credentials. Please try again')
            return False

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
            print('ERROR. Password needs to contain at least 1 capital letter.')
        if not digit_flag:
            print('ERROR. Password needs to contain at least 1 digit.')
        if not special_flag:
            print('ERROR. Password needs to contain at least 1 special character')
        if not len_flag:
            print('ERROR. Password needs to be between 8 and 12 characters long')
        return all([cap_flag, digit_flag, special_flag, len_flag])

    def create_user(
        self, username: str, password: str, firstname: str, lastname: str
    ) -> bool:
        """Validate user information and create new entry in the config."""
        num_users_flag = len(self.config['accounts']) >= 5
        password_flag = not self.password_valid(password)
        username_flag = self.username_exists(username)
        if num_users_flag: 
            print('ERROR: Too many users in the system. Try again later.')
        if username_flag:
            print('ERROR. Current username already has an account.')
        if any([num_users_flag, password_flag, username_flag]):
            return False
        else:
            print('SUCCESS, {}. New account has been created'.format(username))
            # Add a new account to config.
            self.config['accounts'][username] = {
                'password': password,
                'firstname': firstname,
                'lastname': lastname
            }
            # Write new config to json file.
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)

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
        self.config['jobs'].append({
            'author': author,
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary
        })
        num_jobs_flag = len(self.config['jobs']) >= 5
        if num_jobs_flag:
            print('ERROR: Too many jobs in the system. Try again later.')
            return False
        else:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            return True
            

    def save_login(self, username: str) -> None:
        """Update current logged in user and write changes to json file."""
        self.config['current_login'] = username
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
