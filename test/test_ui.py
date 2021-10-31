import os
import json
import pytest
import sys
import helper
# from StringIO import StringIO
import readchar
from readchar import key
from readchar import readkey
from sys import platform as _platform
from inquirer import events

from io import StringIO

# Setup path assignment.
if _platform.startswith('win'):
    config_path = '..\\test\\config.json'
    path = '..\\src'
else:
    config_path = '../test/config.json'
    path = '../src'
helper.create_config(config_path)
sys.path.append(path)
os.chdir(path)

import utils
import in_college

# Create actual instance of config object.
config = utils.InCollegeConfig(config_path)

def test_connect_friends(monkeypatch, capsys):
    """Example UI test with captured output and simulated keypresses."""
    test_sequence = [
            key.ENTER,      # go to connect friends. 
            *list('admin'), # enter friend's first name.
            key.ENTER,      # record string input.
            *list('admin'), # enter friend's last name.
            key.ENTER,      # record string input.
            key.DOWN,
            key.DOWN,       # scroll to go back.
            key.ENTER,      # go back to previous screen.
            key.DOWN,
            key.DOWN,       # scroll to quit.
            key.ENTER,      # quit.
    ]
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    _ = in_college.user_loop(config)
    # Receive output from the execution.
    captured = capsys.readouterr()
    # Check if the stuff printed out as expected.
    assert '🎉 admin is InCollege! Hooray!' in captured.out 
    # Make sure that the error field is empty.
    assert captured.err == ''

def test_save_posting(monkeypatch):
    """Example UI test with simulated keypresses and json update assert."""
    test_sequence = [
            key.DOWN,       # scroll to skip the welcome screen.
            key.ENTER,      # skip welcome screen.
            key.ENTER,      # sign in into application.
            *list('admin'), # sign in with login admin.
            key.ENTER,
            *list('admin'), # sign in with password admin.
            key.ENTER,
            key.ENTER,      # search for a job.
            key.ENTER,      # internships.
            key.DOWN,       # apply for a job.
            key.ENTER,      # show list of jobs.
            key.ENTER,      # show the first job.
            key.DOWN,       # save posting.
            key.ENTER,      # save this job.
            key.DOWN,
            key.DOWN,
            key.ENTER,      # go back.
            *[key.DOWN] * 5,
            key.ENTER,      # go back.
            key.DOWN,
            key.ENTER,
            *[key.DOWN] * 8,
            key.ENTER,     # logout.
            *[key.DOWN] * 6,
            key.ENTER,     # go back.
            *[key.DOWN] * 2,
            key.ENTER      # quit.
    ]
    monkeypatch.setattr('readchar.readkey', lambda: test_sequence.pop(0))
    _ = in_college.user_loop(config)
    # We saved only one job so far, check length of the saved list.
    assert len(config['accounts']['admin']['saved_jobs']) == 1
    # We store saved jobs as a list of ids, so compare the id of interest.
    assert config['accounts']['admin']['saved_jobs'][0] == '2'

