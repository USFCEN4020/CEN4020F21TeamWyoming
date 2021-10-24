from random import randrange as rand
from typing import List
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
            'Friends',
            'Profile',
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
        choices=[
            'Post a job', 
            'Apply for a job',
            'Show my applications',
            'Show my postings',
            'Show my saved jobs',
            'Go back'
        ]
    )])

def print_profile_screen() -> dict:
    return menu.prompt([menu.List(
        'profile_target',
        message='profile screen',
        choices=[
            'View profile',
            'Edit profile title',
            'Edit profile major',
            'Edit profile university',
            'Edit profile about',
            'Edit profile experience',
            'Edit profile education',
            'Go Back'
        ]
    )])

def print_friend_screen() -> dict:
    return menu.prompt([menu.List(
        'friend_target',
        message='Friend screen',
        choices = [
            'Show my Network',
            'Search for Someone',
            'View Friend Requests',
            'Go Back'
        ]
    )])

def print_job_list_screen():
    # Get current login to not display already applied jobs.
    user = config.config['accounts'][config.config['current_login']]
    return menu.prompt([menu.List(
        'posting_target',
        message='Choose a job that you want to learn more about',
        # Get list of proper jobs and make them menu choices.
        choices=config.get_list_jobs(user) + ['Go Back']
    )])

def print_postings_list_screen():
    user = config.config['accounts'][config.config['current_login']]
    return menu.prompt([menu.List(
        'my_posting_target',
        message='Choose your posting for more information',
        choices=config.get_list_jobs(user, my_posts=True) + ['Go Back']
    )])
    
def print_application_list_screen():
    user = config.config['accounts'][config.config['current_login']]
    return menu.prompt([menu.List(
        'my_application_target',
        message='Choose your application',
        choices=config.get_list_jobs(user, my_apps=True) + ['Go Back']
    )])

def print_saved_list_screen():
    user = config.config['accounts'][config.config['current_login']]
    return menu.prompt([menu.List(
        'saved_list_target',
        message='Choose from your saved posts',
        choices=config.get_list_jobs(user, saved=True) + ['Go Back']
    )])

def print_unsave_posting_screen(job_id: str):
    return menu.prompt([menu.List(
        'unsave_posting_target',
        message='What would you like to do with your posting',
        choices=['Delete this saved posting: ' + job_id, 'Go Back']
    )])

def print_delete_posting_screen(job_id: str):
    return menu.prompt([menu.List(
        'delete_posting_target',
        message='What would you like to do with your posting',
        choices=['Delete this posting: ' + job_id, 'Go Back']
    )])

def print_application_screen(job_id: str):
    return menu.prompt([menu.List(
        'application_target',
        message='What would you like to do',
        choices=[
            'Apply for this job: ' + job_id, 
            'Save this job: ' + job_id, 
            'Go Back'
        ]
    )])

def print_withdrawal_screen(job_id: str):
    return menu.prompt([menu.List(
        'withdraw_target',
        message='What would you like to do',
        choices=['Withdraw from this job: ' + job_id, 'Go Back']
    )])

def print_friend_list_screen(key) -> dict:
    user = config.config['accounts'][config.config['current_login']]
    listOfChoices = []
    if key == 'friends':           #Handles friend list
        listOfAccounts = user[key]
        
        if len(listOfAccounts) == 0:
            listOfChoices.append('No Connections')
        else:    
            for account in listOfAccounts:
                listOfChoices.append(f'View profile of {account}')
                listOfChoices.append(f'Disconnect from {account}')
    elif key == 'friend_requests':  #This secition handles pending friend requests
        listOfRequests = user[key]
        if len(listOfRequests) == 0:
            listOfChoices.append('No Requests')
        else:
            for account in listOfRequests:
                listOfChoices.append(f'Accept friend request of {account}')
                listOfChoices.append(f'Decline friend request of {account}')

    else:                            #Handles searching for someone to add to friend list
        inputs = menu.prompt([
            menu.Text('key', 'Search by: lastname, university, or major'),
            menu.Text('value', 'Enter search parameter')
        ])

        key = inputs['key']
        value = inputs['value']
        print(f'{key}   {value}')

        results = config.search_student(inputs['key'], inputs['value'])
        if len(results) == 0:
            listOfChoices.append('No results')
        else:
            for account in results:
                listOfChoices.append(f'Request to connect with {account}')
    listOfChoices.append('Go Back')

    return menu.prompt([menu.List(
        'friend_list_target',
        message='to be changed',
        choices = listOfChoices
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

def edit_profile(editSelection) -> None:
    ''' Edit selection is the part of the profile to be edited that was selected in print_profile_screen() '''
    profile = config.config['accounts'][config.config['current_login']]['profile']
    if editSelection != 'education' and editSelection != 'experience':
        input = menu.prompt([
            menu.Text('edit', 'Enter a new {}'.format(editSelection))
        ])
        edit = input['edit']
        if editSelection == 'major' or editSelection == 'university':
            edit = edit.title()
        profile[editSelection] = edit
        config.save_profile(config.config['current_login'], profile)
    elif editSelection == 'experience':
        if len(profile[editSelection]) < 3:
            input = menu.prompt([
                menu.Text('title', 'Enter title for experience'),
                menu.Text('employer', 'Enter employer'),
                menu.Text('date_started', 'Enter date started'),
                menu.Text('date_ended', 'Enter date ended'),
                menu.Text('location', 'Enter the location'),
                menu.Text('description', 'Enter a description')
            ])
            profile[editSelection].append(input)
            config.save_profile(config.config['current_login'], profile)
        else:
            print('Maximum Experiences')
    elif editSelection == 'education':
        input = menu.prompt([
            menu.Text('name', 'Enter the school name'),
            menu.Text('degree', 'Enter your degree'),
            menu.Text('years', 'Enter your years attended')
        ])
        profile[editSelection].append(input)
        config.save_profile(config.config['current_login'], profile)

def edit_friends_list(currentUser, currentFriendList, friendUsername, friendFriendList) -> None:
    currentFriendList.remove(friendUsername)
    config.save_friends(currentUser, currentFriendList)

    friendFriendList.remove(currentUser)
    config.save_friends(friendUsername, friendFriendList)

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
        if 'my_application_target' in inputs:
            if inputs['my_application_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['my_application_target'].split()[0]
                config.display_job(job_id)
                inputs = print_withdrawal_screen(job_id)
        if 'withdraw_target' in inputs:
            if inputs['withdraw_target'] != 'Go Back':
                user = config.config['current_login']
                job_id = inputs['withdraw_target'].split()[-1]
                config.withdraw_application(user, job_id)
            inputs = print_application_list_screen()
        if 'application_target' in inputs:
            if inputs['application_target'] != 'Go Back':
                user = config.config['current_login']
                # Grab the job id listed in the string from choices.
                job_id = inputs['application_target'].split()[-1]
                # Apply for a job by adding it to the list of user apps.
                if inputs['application_target'].split()[0] == 'Apply':
                    config.submit_application(user, job_id)
                else:
                    config.save_application(user, job_id)
            # Go back in any case.
            inputs = print_job_list_screen()
        if 'posting_target' in inputs:
            if inputs['posting_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['posting_target'].split()[0]
                config.display_job(job_id)
                inputs = print_application_screen(job_id)
        if 'delete_posting_target' in inputs:
            if inputs['delete_posting_target'] != 'Go Back':
                user = config.config['current_login']
                job_id = inputs['delete_posting_target'].split()[-1]
                config.delete_posting(job_id)
            inputs = print_postings_list_screen()
        if 'my_posting_target' in inputs:
            if inputs['my_posting_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['my_posting_target'].split()[0]
                config.display_job(job_id)
                inputs = print_delete_posting_screen(job_id)
        if 'unsave_posting_target' in inputs:
            if inputs['unsave_posting_target'] != 'Go Back':
                user = config.config['current_login']
                job_id = inputs['unsave_posting_target'].split()[-1]
                config.unsave_posting(job_id)
            inputs = print_saved_list_screen()
        if 'saved_list_target' in inputs:
            if inputs['saved_list_target'] == 'Go Back':
                inputs = print_internship_screen()
            else:
                job_id = inputs['saved_list_target'].split()[0]
                config.display_job(job_id)
                inputs = print_unsave_posting_screen(job_id)
        if 'internship_target' in inputs:
            if inputs['internship_target'] == 'Post a job':
                info = ask_job_posting().values(); print()
                if config.create_posting(logged_in_user, *info):
                    print('✅ New posting for {} has been created!'.format(list(info)[0]))
                if list(info)[-1].lower() == 'unpaid': # Easter egg.
                    print('🤨 Unpaid position? We aren\'t into charity business here.')
                inputs = print_internship_screen()
            elif inputs['internship_target'] == 'Apply for a job':
                inputs = print_job_list_screen()
            elif inputs['internship_target'] == 'Show my applications':
                inputs = print_application_list_screen()
            elif inputs['internship_target'] == 'Show my postings':
                inputs = print_postings_list_screen()
            elif inputs['internship_target'] == 'Show my saved jobs':
                inputs = print_saved_list_screen()
            else:
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
            elif inputs['main_target'] == 'Friends':
                inputs = print_friend_screen()
            elif inputs['main_target'] == 'Profile':
                inputs = print_profile_screen()
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
            config.show_guest_control(config.config['current_login'])
            inputs = print_ilinks_screen()

        if 'language_target' in inputs:
            config.save_lang(config.config['current_login'], inputs['language_target'])
            config.show_lang(config.config['current_login'])
            inputs = print_ilinks_screen()

        if 'profile_target' in inputs:
            if inputs['profile_target'] == 'View profile':
                config.display_profile(config.config['current_login'])
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile title':
                edit_profile('title')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile major':
                edit_profile('major')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile university':
                edit_profile('university')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile about':
                edit_profile('about')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile experience':
                edit_profile('experience')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Edit profile education':
                edit_profile('education')
                inputs = print_profile_screen()
            elif inputs['profile_target'] == 'Go Back':
                inputs = print_main_screen()

        if 'friend_target' in inputs:
            if inputs ['friend_target'] == 'Show my Network':
                inputs = print_friend_list_screen('friends')
            elif inputs ['friend_target'] == 'Search for Someone':
                
                inputs = print_friend_list_screen('search')
            elif inputs['friend_target'] == 'View Friend Requests':
                inputs = print_friend_list_screen('friend_requests')
            elif inputs['friend_target'] == 'Go Back':
                inputs = print_main_screen()

        if 'friend_list_target' in inputs:
            if inputs['friend_list_target'][0] == 'N':
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0] == 'V':
                config.display_profile(inputs['friend_list_target'][16:])
                inputs = print_friend_list_screen('friends')
            elif inputs['friend_list_target'][0:2] == 'Di': #Remove from friend list
                currentUser = config.config['current_login']
                currentUserFriendList = config.config['accounts'][currentUser]['friends']
                friendUsername = inputs['friend_list_target'][16:]
                friendFriendList = config.config['accounts'][friendUsername]['friends']

                edit_friends_list(currentUser, currentUserFriendList, friendUsername, friendFriendList)
                inputs = print_friend_list_screen('friends')
            elif inputs['friend_list_target'][0] == 'A':
                config.accept_friend_request(config.config['current_login'], inputs['friend_list_target'][25:])
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0:2] == 'De':
                config.decline_friend_request(config.config['current_login'], inputs['friend_list_target'][26:])
                inputs = print_friend_screen()
            elif inputs['friend_list_target'][0] == 'R':
                user = config.config['current_login']
                config.send_friend_request(inputs['friend_list_target'][24:], user)
                inputs = print_friend_screen()
            elif inputs['friend_list_target'] == 'Go Back':
                inputs = print_friend_screen()
                
if __name__ == '__main__':
    user_loop()
