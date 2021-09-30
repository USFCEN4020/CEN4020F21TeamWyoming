import os
import json
import pytest
import utils
import sys
from sys import platform as _platform

if _platform.startswith('linux'):
    sys.path.append('../src')
    os.chdir('../src')
elif _platform == 'darwin':
    sys.path.append('../src')
    os.chdir('../src')
elif _platform.startswith('win'):
    sys.path.append('..\\src')
    os.chdir('..\\src')
else:
    sys.path.append('../src')
    os.chdir('../src')



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
                        "lastname": "admin"
                    }
                },
                "jobs": list()
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