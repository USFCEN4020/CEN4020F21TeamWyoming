import fire
import welcome
import string
import display
#from history import loginRecordAppend
#from history import loginRecordQuery
#from history import makeDict

# Test if the username is valid.
# Added by Wenchao 9/19/2021 23:00
def ifNameValid(username):
    users = getUsers()
    # First, we will check if the username is unique
    for user in users:
        _username = user[0]
        if _username == username:
            print("User name existed!\n")
            return False
    return True

# Test if the Password is valid.
# Added by Wenchao 9/19/2021 23:00
def ifPasswordValid(Password):
    charList = list(Password)
    capNum = 0
    length = len(Password)
    digitNum = 0
    sepecialNum = 0
    for char in charList:
        if char in string.digits:
            digitNum += 1
        elif char in string.ascii_uppercase:
            capNum += 1
        elif char in string.punctuation:
            sepecialNum += 1
        else:
            pass
    if length <= 12 and length >= 8 and capNum >=1 and digitNum >=1 and sepecialNum >=1:
        return True
    else:
        print("Invalid Password!\n")
        print("Password need to be:\n")
        print("8 <= length <= 12\n")
        print("Have at least 1 cap letter\n")
        print("Have at least 1 digit\n")
        print("Have at least 1 non-alpha character\n")
        return False
    


# We want to get all of the current users and then see if the given username and password match
def login(username, password):
    users = getUsers()
    for user in users:
        _username = user[0]
        _password = user[1]
        if _username == username and _password == password:

            print('You are logged in!')
            return True
    print("Invalid credentials")
    return False

def getUsers():
    users = []
    file = open('accounts.txt', 'r')
    # Get each line from the file and extract the user data
    lines = file.readlines()
    for line in lines:
        user = line.replace('\n', '').split(' ')
        # We are appending an array with the user data i.e. ['johndoe123', 'mypassword123']
        users.append(user)
        
    file.close()
    return users

# Appends the user to the accounts.txt as a new line
# If there are more than 5 users, then no account may be created
def signup(username, password, firstname, lastname):
    users = getUsers()
    # First, we will check if the username is unique
    for user in users:
        _username = user[0]
        if _username == username:
            print("Username already exists")
            return False

    # Next, check if there are too many accounts
    if len(users) >= 5:
        print("Too many users")
        return False
    else:
        file = open('accounts.txt', 'a')
        file.write(username + ' ' + password + ' ' + firstname + ' ' + lastname + '\n' )
        file.close()

        print ("Account created!")
        return True

if __name__ == '__main__':
    # Generic welcome message for the cli
    welcome.message()
    # Fire turns our app into a cli. See the docs here https://stackabuse.com/generating-command-line-interfaces-cli-with-fire-in-python/
    fire.Fire()
