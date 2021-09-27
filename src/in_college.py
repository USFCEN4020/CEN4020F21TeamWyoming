from random import randrange as rand
import inquirer as menu 
import utils

logged_in_user = "" # global variable for current login.
config = utils.InCollegeConfig() # global config.

def print_welcome_screen() -> dict:
    """Print welcome selections for the user."""
    return menu.prompt([menu.List(
        'welcome_target',
        message='Welcome! Where would you like to go?',
        choices=['Connect to friends', 'Skip', 'Quit']
    )])

def print_connect_screen() -> dict:
    """Print connect screen selections for the user."""
    return menu.prompt([menu.List(
        'connect_target',
        message='[CONNECT] Where would you like to go from here?',
        choices=['Log in', 'Sign up to join friends', 'Go back'],
    )])

def print_main_screen() -> dict:
    """Print main screen selections to the user."""
    return menu.prompt([menu.List(
        'main_target',
        message='[HOME] Where would you like to go next?',
        choices=[
            'Search for a job',
            'Find someone',
            'Learn a new skill',
            'Log out'
        ]
    )])

def print_login_screen() -> dict:
    """Print login screen selections to the user."""
    if logged_in_user == '':
        print('-----\n🎓 Here is one of the success stories by one of the users 🎓')
        story = config.config['stories'][rand(len(config.config['stories']))]
        print('"{}"'.format(story))
        print('🎓 Join us to get a job, find some friends, and some more! 🎓\n-----\n')
    return menu.prompt([menu.List(
        'login_target',
        message='[LOGIN] What would you like to do?',
        choices=['Sign in', 'Sign up', 'Go back', 'Watch a video']
    )])

def print_skill_screen() -> dict:
    return menu.prompt([menu.List(
        'skill_target',
        message='[SKILLS] What would you like to learn?',
        choices=[
            'Programming in C#',
            'Theory of composition',
            'Sky dive',
            'Short swing trading',
            'Time management',
            'I am perfect enough',
            'Go back'
        ]
    )])

def print_job_screen() -> dict:
    return menu.prompt([menu.List(
        'job_target',
        message='[JOBS] What would you like to do?',
        choices=['Internships', 'Go back']
    )])

def print_internship_screen() -> dict:
    return menu.prompt([menu.List(
        'internship_target',
        message='[INTERNSHIPS] What would you like?',
        choices=['Post a job', 'Go back']
    )])

def ask_for_login() -> dict:
    return menu.prompt([
        menu.Text('login_username', 'Enter your username'),
        menu.Text('login_password',  'Enter your password')
    ])

def ask_for_signup():
    return menu.prompt([
        menu.Text('signup_username', 'Enter your new username'),
        menu.Text('signup_password', 'Enter your new password (strong)'),
        menu.Text('signup_firstname', 'Enter your first name'),
        menu.Text('signup_lastname', 'Enter your last name')
    ])

def ask_for_fullname() -> dict:
    return menu.prompt([
        menu.Text('friend_first', 'Enter your friend\'s first name'),
        menu.Text('friend_last', 'Enter your friend\'s last name')
    ])

def ask_job_posting() -> dict:
    return menu.prompt([
        menu.Text('job_title', 'Enter job title'),
        menu.Text('job_description', 'Enter job description'),
        menu.Text('job_employer', 'Enter company name'),
        menu.Text('job_location', 'Enter location (city, state)'),
        menu.Text('job_salary', 'Enter salary (format: $/month)')
    ])

def user_loop() -> None:
    """Main driver for the user interaction."""
    print('-#- 🎓 WELCOME TO THE IN COLLEGE CLI! 🎓 -#-\n')
    inputs, logged_in_user = None, config.config['currentLogin']
    while True: # endless user loop.
        # If inputs are empty, it's the welcome screen.
        if inputs is None:
            inputs = print_welcome_screen()
        # Use *_target notation to understand where we are in the state.
        if 'welcome_target' in inputs:
            if inputs['welcome_target'] == 'Connect to friends':
                # Find their friend by prompting for full name.
                first, last = ask_for_fullname().values(); print()
                if config.full_name_exists(first, last):
                    print('🎉 {0} is InCollege! Hooray!'.format(first))
                    inputs = print_connect_screen()
                else:
                    print('🎓 They are not part of our system. Invite them!')
                    inputs = print_welcome_screen()
            elif inputs['welcome_target'] == 'Skip':
                inputs = print_login_screen()
            else:
                print('-#- 🎓 THANKS FOR USING IN COLLEGE CLI! 🎓 -#-')
                break
        if 'connect_target' in inputs:
            if inputs['connect_target'] == 'Log in':
                if config.config['currentLogin'] != '':
                    print('🔑 You were already logged in.')
                    inputs = print_main_screen()
                else:
                    login, password = ask_for_login().values(); print()
                    if config.login_valid(login, password):
                        print('🔑 You are logged in. Welcome {}'.format(login))
                        config.save_login(login)
                        inputs = print_main_screen()
                    else:
                        inputs = print_connect_screen()
            elif inputs['connect_target'] == 'Sign up to join friends':
                login, passwd, first, last = ask_for_signup().values(); print();
                if config.create_user(login, passwd, first, last):
                    print('✅ User with login {} has been added'.format(login))
                    inputs = print_main_screen()
                else: # Error was detected.
                    inputs = print_connect_screen()
            else:
                inputs = print_welcome_screen()
        if 'internship_target' in inputs:
            if inputs['internship_target'] == 'Post a job':
                info = ask_job_posting().values(); print()
                config.create_posting(logged_in_user, *info)
                print('✅ New posting for {} has been created!'.format(info[1]))
                if info[-1].lower() == 'updaid': # Easter egg.
                    print('🤨 Unpaid position? We aren\'t into charity business here.')
            inputs = print_job_screen()
        if 'job_target' in inputs:
            if inputs['job_target'] == 'Internships':
                inputs = print_internship_screen()
            else: # Go back was selected.
                inputs = print_main_screen()
        if 'skill_target' in inputs:
            if inputs['skill_target'] == 'Go back':
                inputs = print_main_screen()
            else:
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_main_screen()
        if 'main_target' in inputs:
            if inputs['main_target'] == 'Search for a job':
                inputs = print_job_screen()
            elif inputs['main_target'] == 'Find someone':
                first, last = ask_for_fullname().values(); print()
                if config.full_name_exists(first, last):
                    print('🎉 {0} is InCollege! Hooray!'.format(first))
                else:
                    print('🎓 They are not part of our system. Invite them!')
                inputs = print_main_screen()
            elif inputs['main_target'] == 'Learn a new skill':
                inputs = print_skill_screen()
            else:
                inputs = print_login_screen()
                config.save_login('') # reset login "cookie".
        if 'login_target' in inputs:
            if inputs['login_target'] == 'Sign in':
                if config.config['currentLogin'] != '':
                    print('🔑 You were already logged in.')
                    inputs = print_main_screen()
                else:
                    login, password = ask_for_login().values(); print()
                    if config.login_valid(login, password):
                        print('🔑 You are logged in. Welcome {}'.format(login))
                        config.save_login(login)
                        inputs = print_main_screen()
                    else:
                        print('❌ Invalid credentials. Try again later.')
                        inputs = print_login_screen()
            elif inputs['login_target'] == 'Sign up':
                login, passwd, first, last = ask_for_signup().values(); print();
                if config.create_user(login, passwd, first, last):
                    print('✅ User with login {} has been added'.format(login))
                    config.save_login(login)
                    inputs = print_main_screen()
                else: # Error was detected.
                    inputs = print_login_screen()
            elif inputs['login_target'] == 'Go back': # Reuse code.
                inputs = print_welcome_screen()
            else:
                print('⚠️🚨 Playing video 🎥. Under construction. 🚨⚠️')
                inputs = print_login_screen()

if __name__ == '__main__':
    user_loop()
