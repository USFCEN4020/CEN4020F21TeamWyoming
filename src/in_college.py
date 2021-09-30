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
        choices=['Log in', 'Sign up to join friends', 'Go back']
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
            'Useful Links',
            'InCollege Important Links',
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
        choices=[
            'Sign in',
            'Sign up',
            'Go back',
            'Watch a video',
            'Useful Links',
            'InCollege Important Links'
        ]
    )])

def print_ulinks_screen() -> dict:
    return menu.prompt([menu.List(
        'ulinks_target',
        message='[LINKS] Which useful link would you like to browse?',
        choices=[
            'General',
            'Browse InCollege',
            'Business Solutions',
            'Directories',
            'Go back'
        ]
    )])

def print_general_screen() -> dict:
    return menu.prompt([menu.List(
        'general_target',
        message='[LINKS] Which general link would you like to choose?',
        choices=[
            'Sign up',
            'Help Center',
            'About',
            'Press',
            'Blog',
            'Careers',
            'Developers',
            'Go back'
        ]
    )])

def print_ilinks_screen() -> dict:
    return menu.prompt([menu.List(
        'ilinks_target',
        message='[LINKS] Which InCollege  link would you like to browse?',
        choices=[
            'Copyright Notice',
            'About',
            'Accessibility',
            'User Agreement',
            'Privacy Policy',
            'Cookie Policy',
            'Copyright Policy',
            'Brand Policy',
            'Guest Controls',
            'Languages',
            'Go back'
        ]
    )])

def print_privacy_screen() -> dict:
    return menu.prompt([menu.List(
        'privacy_target',
        message='[PRIVACY] Which privacy option would you like to choose?',
        choices=[
            'Guest Control',
            'Go back'
        ]
    )])

def print_guest_screen() -> dict:
    return menu.prompt([menu.Checkbox(
        'guest_target',
        message='[PRIVACY] Which guest control would you like to toggle?',
        choices=[
            'InCollege Email',
            'SMS',
            'Targeted Advertising features'
        ]
    )])

def print_language_screen() -> dict:
    return menu.prompt([menu.List(
        'language_target',
        message='[LANG] Which language would you like to choose?',
        choices=[
            'English',
            'Spanish'
        ]
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
    inputs, logged_in_user = None, config.config['current_login']
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
                if config.config['current_login'] != '':
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
                if config.create_posting(logged_in_user, *info):
                    print('✅ New posting for {} has been created!'.format(list(info)[0]))
                if list(info)[-1].lower() == 'updaid': # Easter egg.
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
            elif inputs['main_target'] == 'Useful Links':
                inputs = print_ulinks_screen()
            elif inputs['main_target'] == 'InCollege Important Links':
                inputs = print_ilinks_screen()
            elif inputs['main_target'] == 'Log out':
                config.save_login('')  # reset login "cookie".
                inputs = print_login_screen()

        if 'login_target' in inputs:
            if inputs['login_target'] == 'Sign in':
                if config.config['current_login'] != '':
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
            elif inputs['login_target'] == 'Watch a video':
                print('⚠️🚨 Playing video 🎥. Under construction. 🚨⚠️')
                inputs = print_login_screen()
            elif inputs['login_target'] == 'Useful Links':
                inputs = print_ulinks_screen()
            elif inputs['login_target'] == 'InCollege Important Links':
                inputs = print_ilinks_screen()
        if 'ulinks_target' in inputs:
            if inputs['ulinks_target'] == 'General':
                inputs = print_general_screen()
            elif inputs['ulinks_target'] == 'Browse InCollege':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_ulinks_screen()
            elif inputs['ulinks_target'] == 'Business Solutions':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_ulinks_screen()
            elif inputs['ulinks_target'] == 'Directories':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_ulinks_screen()
            elif inputs['ulinks_target'] == 'Go back':
                if config.config['current_login'] != '':
                    inputs = print_main_screen()
                else:
                    inputs = print_login_screen()

        if 'general_target' in inputs:
            if inputs['general_target'] == 'Sign up':
                inputs = print_login_screen()
                # if config.config['current_login'] != '':
                #     print('🔑 You were already logged in.')
                #     inputs = print_main_screen()
                # else:
                #     login, password = ask_for_login().values();
                #     print()
                #     if config.login_valid(login, password):
                #         print('🔑 You are logged in. Welcome {}'.format(login))
                #         config.save_login(login)
                #         inputs = print_main_screen()
                #     else:
                #         print('❌ Invalid credentials. Try again later.')
                #         inputs = print_general_screen()
            elif inputs['general_target'] == 'Help Center':
                print('🎓 We\'re here to help')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'About':
                print('🎓 In College: Welcome to In College, '
                      'the world\'s largest college student '
                      'network with many users in many countries '
                      'and territories worldwide')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'Press':
                print('🎓 In College Pressroom: '
                      'Stay on top of the latest news, updates, and reports')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'Blog':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'Careers':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'Developers':
                print('⚠️🚨 Under construction. 🚨⚠️')
                inputs = print_general_screen()
            elif inputs['general_target'] == 'Go back':
                inputs = print_ulinks_screen()

        if 'ilinks_target' in inputs:
            if inputs['ilinks_target'] == 'Copyright Notice':
                print('Copyright @ 1980-2021, InCollege Inc. None Rights Reserved.')
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'About':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Accessibility':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'User Agreement':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Privacy Policy':
                print()
                inputs = print_privacy_screen()
            elif inputs['ilinks_target'] == 'Cookie Policy':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Copyright Policy':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Brand Policy':
                print()
                inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Guest Controls':
                if config.config['current_login'] != '':
                    inputs = print_guest_screen()
                else:
                    print('Please sign in to see the hidden content')
                    inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Languages':
                if config.config['current_login'] != '':
                    inputs = print_language_screen()
                else:
                    print('Please sign in to see the hidden content')
                    inputs = print_ilinks_screen()
            elif inputs['ilinks_target'] == 'Go back':
                if config.config['current_login'] != '':
                    inputs = print_main_screen()
                else:
                    inputs = print_login_screen()

        if 'privacy_target' in inputs:
            if inputs['privacy_target'] == 'Guest Control':
                if config.config['current_login'] != '':
                    inputs = print_guest_screen()
                else:
                    print('Please sign in to see the hidden content')
                    inputs = print_privacy_screen()
            elif inputs['privacy_target'] == 'Go back':
                inputs = print_ilinks_screen()

        if 'guest_target' in inputs:
            config.save_guest_control(config.config['current_login'], inputs['guest_target'])
            print()
            config.show_guest_control(config.config['current_login'])
            inputs = print_ilinks_screen()

        if 'language_target' in inputs:
            config.save_lang(config.config['current_login'], inputs['language_target'])
            config.show_lang(config.config['current_login'])
            inputs = print_ilinks_screen()


if __name__ == '__main__':
    user_loop()
