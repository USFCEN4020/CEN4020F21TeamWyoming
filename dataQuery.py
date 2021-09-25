




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


def ifNameExist(firstname, lastname, dataList):
    for user in dataList:
        if firstname == user[2] and lastname == user[3]:
                    return True
    return False


def ifCredentialsCorrect(username, password, dataList):
    for user in dataList:
        if username == user[0] and password == user[1]:
                    return True
    return False

def ifUsernameExist(username, dataList):
    for user in dataList:
        if username == user[0]:
                    return True
    return False
