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
                    "language": "English",
                    'profile': {
                        'title': '',
                        'major': '',
                        'university': '',
                        'about': '',
                        'experience': [],
                        'education': []
                    }
                }
            },
            "jobs": list(),
            "current_login": "admin",
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
    username, firstname, lastname = 'sample', 'sample', 'sample'
    password1, password2 = 'invalidpassword', 'validpa5S$!'
    assert config.create_user(username, password2, firstname, lastname) == True
    assert config.create_user(username, password1, firstname, lastname) == False

def test_create_posting_week2():
    config = init_testing()
    author, title, desc = 'sample', 'sample', 'sample'
    employer, location, salary = 'sample', 'sample', 'unpaid'
    config.create_posting(author, title, desc, employer, location, salary)
    assert len(config.config['jobs']) == 1
    assert config.config['jobs'][0]['salary'] == 'unpaid'

def test_save_lang_week3():
    config = init_testing()
    username1, lang1 = 'admin', 'Spanish'
    config.save_lang(username1, lang1)
    # Check whether the structure was saved into json.
    assert config.config['accounts'][username1]['language'] == lang1

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
