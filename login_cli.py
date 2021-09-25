import fire
import welcome
import string
import display
import dataQuery


# Test if the Password is valid.
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
    users = dataQuery.getDataList("accounts.txt")
    result = dataQuery.ifCredentialsCorrect(username, password, users)
    if result == True:
        print('You are logged in!')
        return True
    else:
        print("Invalid credentials")
        return False


# def getUsers() has been Moved to dataQuery.py




def signup(username, password, firstname, lastname):
    users = dataQuery.getDataList("accounts.txt")

    if dataQuery.ifUsernameExist(username, users) == True:
        print("Username already exists")
        return False

    if ifPasswordValid(password) == False:
        return False

    if len(users) >= 5:
        print("Too many users")
        return False
    
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
