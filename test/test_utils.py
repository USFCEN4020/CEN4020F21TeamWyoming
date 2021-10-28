import os
import json
import pytest

import sys
from sys import platform as _platform
path = '../src'
if _platform.startswith('win'):
    path = '..\\src'
sys.path.append(path)
os.chdir(path)
import utils

def init_testing():
    """Initialize dummy config json for testing purposes."""
    test_path = '../test/testConfig.json'
    if _platform.startswith('win'):
        test_path = '..\\test\\testConfig.json'
    with open(test_path, 'w', encoding='utf-8') as f:
        init_data = {
            "accounts": {
                "admin": {
                    "password": "admin",
                    "firstname": "admin",
                    "lastname": "admin",
                    "membership": "pro",
                    "language": "English",
                    'profile': {
                        'title': '',
                        'major': '',
                        'university': '',
                        'about': '',
                        'experience': [],
                        'education': []
                    },
                    "friends": [],
                    "friend_requests": [],
                    "applications": [],
                    "saved_jobs": []
                },
                "test": {
                    "password": "tesT123!",
                    "firstname": "first",
                    "lastname": "LaSt",
                    "membership": "",
                    "language": "English",
                    "profile": {
                        "title": "I a\b\b\bThis a test profile",
                        "major": "Testing",
                        "university": "University of Testing",
                        "about": "Hello I am a test profile",
                        "experience": [],
                        "education": []
                    },
                    "friends": [
                        "new",
                        "admin"
                    ],
                    "friend_requests": [],
                    "applications": {},
                    "saved_jobs": []
                }
            },
            "jobs": list(),
            "current_login": "admin",
            "current_login_membership": "pro",
            "guest_control": {
                "admin": ["InCollege Email"]
            }
        }
        json.dump(init_data, f, ensure_ascii=False, indent=2)
    return utils.InCollegeConfig('../test/testConfig.json')

def test_utils_login_week1():
    config = init_testing()
    username, password = 'admin', 'admin'
    assert config.login_valid(username, password) == True

def test_full_name_exists_week1():
    config = init_testing()
    first, last = 'admin', 'admin'
    assert config.full_name_exists(first, last) == True

def test_password_valid_week1():
    config = init_testing()
    assert config.password_valid('ab') == False
    assert config.password_valid('ab3') == False
    assert config.password_valid('ab3!') == False
    assert config.password_valid('ab3!A') == False
    assert config.password_valid('validPasS4!') == True

def test_create_user_week1():
    config = init_testing()
    username, firstname, lastname, membership = 'sample', 'sample', 'sample', 'sample'
    password1, password2 = 'invalidpassword', 'validpa5S$!'
    assert config.create_user(username, password2, firstname, lastname, membership) == True
    assert config.create_user(username, password1, firstname, lastname, membership) == False

def test_create_posting_week2():
    config = init_testing()
    author, title, desc = 'admin', 'sample', 'sample'
    employer, location, salary = 'sample', 'sample', 'unpaid'
    config.create_posting(author, title, desc, employer, location, salary)
    assert len(config['jobs']) == 1
    assert config['jobs'][0]['salary'] == 'unpaid'

def test_save_lang_week3():
    config = init_testing()
    username1, lang1 = 'admin', 'Spanish'
    config.save_lang(username1, lang1)
    # Check whether the structure was saved into json.
    assert config['accounts'][username1]['language'] == lang1

def test_show_lang_week3(capsys):
    config = init_testing()
    username = 'admin'
    config.show_lang(username)
    captured = capsys.readouterr()
    # Checking correctly outputted languages.
    assert captured.out.split()[-1] == 'English'

def test_save_guest_control_week3():
    config = init_testing()
    username, control_setting_list = 'admin', ['InCollege Email', 'SMS']
    config.save_guest_control(username, control_setting_list)
    # Checking update in the json file.
    assert config.config['guest_control'][username] == control_setting_list

def test_show_guest_control_week3(capsys):
    config = init_testing()
    username = 'admin'
    config.show_guest_control(username)
    captured = capsys.readouterr()
    # Checking proper output.
    assert 'InCollege Email: ON' in captured.out 
    
def test_save_profile_week4():
    config = init_testing()
    username = 'admin'
    profile = {
                'title': 'admin',
                'major': 'CS',
                'university': 'USF',
                'about': 'It\'s me',
                'experience': [{'e1': '1111'},
                               {'e2': '2222'},
                               {'e3': '3333'}
                               ],
                'education': [{'GED': 'home1'},
                              {'Bachelor Degree': 'home2'},
                              {'Master Degree': 'home3'}
                              ]
                }
    config.save_profile(username, profile)
    assert config.config['accounts'][username]['profile'] == profile

def test_edit_profile_week4(capsys):
    config = init_testing()
    username = 'admin'
    config.display_profile(username)
    captured = capsys.readouterr()
    assert 'admin admin'
    'title: admin'
    'major: CS'
    'university: USF'
    'about: It\'s me'
    'experience:'
    'e1: 1111'
    'e2: 2222'
    'e3: 3333'
    'education:'
    'GED: home1'
    'Bachelor Degree: home2'
    'Master Degree: home3' in captured.out

def test_save_friends_week5():
    config = init_testing()
    username = 'admin'
    friend_list = ['test']
    config.save_friends(username, friend_list)
    assert config.config['accounts'][username]['friends'] == friend_list

def test_send_friend_request_week5():
    config = init_testing()
    target_user = 'admin'
    sender = 'test'
    config.send_friend_request(target_user, sender)
    assert 'test' in config.config['accounts'][target_user]['friend_requests']

def test_accept_friend_request_week5():
    config = init_testing()
    config.send_friend_request('admin', 'test')
    user = 'admin'
    accepted_username = 'test'
    config.accept_friend_request(user, accepted_username)
    assert accepted_username in config.config['accounts'][user]['friends']
    assert accepted_username not in config.config['accounts'][user]['friend_requests']
    assert user in config.config['accounts'][accepted_username]['friends']

def test_decline_friend_request_week5():
    config = init_testing()
    config.send_friend_request('admin', 'test')
    user = 'admin'
    declined_username = 'test'
    config.decline_friend_request(user, declined_username)
    assert declined_username not in config.config['accounts'][user]['friend_requests']

def test_submit_application_week6():
    config = init_testing() # TODO: add sample jobs.
    author, title, desc = 'admin', 'sample', 'sample'
    employer, location, salary = 'sample', 'sample', 'unpaid'
    config.create_posting(author, title, desc, employer, location, salary)
    job_id = config.config['jobs'][0]['id']
    config.submit_application('test', job_id, 'grad date', 'start date', 'txt')
    assert job_id in config.config['accounts']['test']['applications']

def test_withdraw_application_week6():
    config = init_testing() # TODO: add sample jobs.
    author, title, desc = 'admin', 'sample', 'sample'
    employer, location, salary = 'sample', 'sample', 'unpaid'
    config.create_posting(author, title, desc, employer, location, salary)
    job_id = config.config['jobs'][0]['id']
    config.submit_application('test', job_id, 'grad date', 'start date', 'txt')
    config.withdraw_application('test', job_id)
    assert job_id not in config.config['accounts']['test']['applications']

def test_get_list_jobs_week6():
    config = init_testing() # TODO: add sample jobs.
    author, title, desc = 'admin', 'sample', 'sample'
    employer, location, salary = 'sample', 'sample', 'unpaid'
    config.create_posting(author, title, desc, employer, location, salary)
    job_id = config.config['jobs'][0]['id']
    user = config.config['accounts']['test']
    jobs = config.get_list_jobs(user)
    assert jobs == [f'{job_id} | {title} | {location}']


