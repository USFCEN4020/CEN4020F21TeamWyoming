from re import search
from login_cli import login
from login_cli import getUsers
from login_cli import signup
from login_cli import ifPasswordValid
from login_cli import ifNameValid
import display
import textDepot


class UI:
    def __init__(self):
        self.loggedIn = False
        self.name = ""

    def loginUI(self):
        if self.loggedIn == False:
            display.story(textDepot.storyList)
            display.menu(["Sign in",
                       "Sign up",
                       "Quit",
                       "Watch the video"])
        else:
            display.menu(["Sign in",
                       "Sign up",
                       "Quit"])

        inpt = input("Go to: ")
        if inpt == "1":
            if self.loggedIn == True:
                return self.mainUI()
            username_inpt = input("username: ")
            password_inpt = input("password: ")

            if login(username_inpt, password_inpt) == True:
                self.name = username_inpt
                return self.mainUI()
            else:
                return self.loginUI()
                         
        elif inpt == "2":
            username_inpt = input("username: ")
            password_inpt = input("password: ")
            firstname_inpt = input("firstname: ")
            lastname_inpt = input("lastname: ")
            
            if ifNameValid(username_inpt) == False:
                return self.loginUI()
            if ifPasswordValid(password_inpt) == False:
                return self.loginUI()
            loginRes = signup(username_inpt, password_inpt, firstname_inpt, lastname_inpt)
            if loginRes == True:
                return self.mainUI()
            else:
                return self.loginUI()
                    
        elif inpt == "3":
            return
        elif inpt == "4" and self.loggedIn == False:
            return self.videoUI()
        else:
            print("Invalid entry, please try again.\n")
            return self.loginUI()


        
    def mainUI(self):
        self.loggedIn = True
        display.menu(["Search a job",
                       "Find someone",
                       "Learn a new skill",
                       "Log out"])


        inpt = input("Go to: ")
        if inpt == "1":
            return self.jobSearchUI()
        elif inpt == "2":
            print("Under construction\n")
            return self.mainUI()
        elif inpt == "3":
            return self.skillUI()
        elif inpt == "4":
            return self.loginUI()
        else:
            print("Invalid entry, please try again.\n")
            return self.mainUI()


    def skillUI(self):
        display.menu(["Programming",
                      "Theory of Composition",
                      "Sky Dive",
                      "Short Swing Trading",
                      "Time Management",
                      "I'm perfect enough",])
        
        inpt = input("\nGo to: ")
        x = search("^[1-5]$", inpt)

        if x != None:
            print("Under construction\n")
            return self.skillUI()
        elif inpt == "6":
            return self.mainUI()
        else:
            print("Invalid entry, please try again.\n")
            return self.skillUI()

            
    def videoUI(self):
        display.video()
        display.menu(["Go back"])
        inpt = input("Go to: ")
        
        while inpt != "1":
            print("invalid option")
            inpt = input("Go to: ")
        return self.loginUI()


    def jobSearchUI(self):
        display.menu(["Post a job", "Go back"])

        inpt = input("Go to: ")
        
        if inpt == "1":
            f = open('jobDepot.txt', 'a')

            poster = self.name
            
            title = input("title: ")

            description = input("description: ")

            employer = input("employer: ")

            location = input("location: ")

            salary = input("salary: ")

            f.write(poster + " " + title + " " + description
                    + " " + employer + " " + location
                    + " " + salary + "\n")
            f.close()
            return self.mainUI()
        
        elif inpt == "2":
            return self.mainUI()
        else:
            print("invalid option")
            return self.jobSearchUI()
    
