import random

def border():
     print("\n******************************************\n")

# printout the menu list with sequence numbers
# strList is the string list of all options
def menu(strList):
    border()    
    i = 1
    for str in strList:
        print(i, ". " + str + '\n')
        i += 1    
    border()

# randomly chose a story from the string list to print
def story(strList):
    border()
    
    random.seed()
    i = random.randint(0, len(strList) - 1)
    print(strList[i])
        
    border()


# "play a video"
def video():
     border()
     print("Video is now playing")
     border()
