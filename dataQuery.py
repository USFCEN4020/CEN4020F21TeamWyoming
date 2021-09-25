



# Get the dataset from a apecific file
# str is the file name (with the extention)
def getDataList(str):
    dataList = []
    filename = str
    file = open(filename, 'r')
    lines = file.readlines()
    
    for line in lines:
        dataElement = line.replace('\n', '').split(' ')
        dataList.append(dataElement)
        
    file.close()
    return dataList

# Check if the full name is existed in the dataset
def ifNameExist(firstname, lastname, dataList):
    for user in dataList:
        if firstname == user[2] and lastname == user[3]:
                    return True
    return False

# Check if the username and password are in accordance with the dataset
def ifCredentialsCorrect(username, password, dataList):
    for user in dataList:
        if username == user[0] and password == user[1]:
                    return True
    return False

# check if the username is existed in the dataset
def ifUsernameExist(username, dataList):
    for user in dataList:
        if username == user[0]:
                    return True
    return False
