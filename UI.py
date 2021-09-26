import re 
import login_cli
import display
import textDepot
import dataQuery


class UI:
    # loggedIn is used to remember if the user is logged in
    # name is to record the name of who posts a job
    def __init__(self):
        self.loggedIn = False
        self.name = ""

    def loginUI(self):
        if self.loggedIn == False:
            display.story(textDepot.storyList)
            display.menu(["Sign in",
                       "Sign up",
                       "Go back",
                       "Watch the video"])
        else:
            display.menu(["Sign in",
                       "Sign up",
                       "Go back"])

        inpt = input("Go to: ")
        
        if inpt == "1":
            if self.loggedIn == True:
                return self.mainUI()
            
            username_inpt = input("username: ")
            password_inpt = input("password: ")

            if login_cli.login(username_inpt, password_inpt) == True:
                self.name = username_inpt
                return self.mainUI()
            else:
                return self.loginUI()
                         
        elif inpt == "2":
            
            username_inpt = input("username: ")
            password_inpt = input("password: ")
            firstname_inpt = input("firstname: ")
            lastname_inpt = input("lastname: ")

            if login_cli.signup(username_inpt, password_inpt, firstname_inpt, lastname_inpt) == True:
                return self.mainUI()
            else:
                return self.loginUI()
                             
        elif inpt == "3":
            return self.welcomeUI()
        
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
            print("Please enter the first and last name of your friend below\n")
            firstname = input("first name: ")
            lastname = input("last name: ")
            users = dataQuery.getDataList("accounts.txt")
            
            if dataQuery.ifNameExist(firstname, lastname, users) == True:
                print("He/she is a part of the InCollege system!\n")
                return self.mainUI()
            
            else:
                print("He/she is not yet a part of the InCollege system yet")
                return self.mainUI()
                   
        elif inpt == "3":
            return self.skillUI()
        
        elif inpt == "4":
            return self.welcomeUI()
        
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
        x = re.search("^[1-5]$", inpt)

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
        display.menu(["Internship",
                      "Go back"])

        inpt = input("Go to: ")
        
        if inpt == "1":
            return self.internshipUI()
        
        elif inpt == "2":
            return self.mainUI()
        
        else:
            print("invalid option")
            return self.jobSearchUI()


    def internshipUI(self):
        display.menu(["Post a job",
                      "Go back"])
        
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
            return self.jobSearchUI()
        
        elif inpt == "2":
            return self.jobSearchUI()
        
        else:
            print("invalid option")
            return self.internshipUI()
        
    

    def welcomeUI(self):
        display.menu(["Connect to friends",
                      "Skip",
                      "Quit"])
        
        inpt = input("Go to: ")
        
        if inpt == "1":
            print("Please enter the first and last name of your friend below\n")
            firstname = input("first name: ")
            lastname = input("last name: ")
            users = dataQuery.getDataList("accounts.txt")
            
            if dataQuery.ifNameExist(firstname, lastname, users) == True:
                print("He/she is a part of the InCollege system!\n")
                return self.connectUI()
            
            else:
                print("He/she is not yet a part of the InCollege system yet")
                return self.welcomeUI()

        elif inpt == "2":
            return self.loginUI()

        elif inpt == "3":
            return
        
        else:
            print("invalid option")
            return self.welcomeUI()



    def connectUI(self):
        display.menu(["Log in",
                      "Sign up to join friends",
                      "Go back"])

        inpt = input("Go to: ")
        
        if inpt == "1":
            
            if self.loggedIn == True:
                return self.mainUI()
            
            username_inpt = input("username: ")
            password_inpt = input("password: ")

            if login_cli.login(username_inpt, password_inpt) == True:
                self.name = username_inpt
                return self.mainUI()
            
            else:
                return self.connectUI()
                         
        elif inpt == "2":
            username_inpt = input("username: ")
            password_inpt = input("password: ")
            firstname_inpt = input("firstname: ")
            lastname_inpt = input("lastname: ")

            if login_cli.signup(username_inpt, password_inpt, firstname_inpt, lastname_inpt) == True:
                return self.mainUI()
            
            else:
                return self.connectUI()
                    
        elif inpt == "3":
            return self.welcomeUI()

        else:
            print("Invalid entry, please try again.\n")
            return self.connectUI()
