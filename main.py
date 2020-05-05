from MainFunctions import *

def main():
    file_name = 'data.json'
    fill_the_file(file_name)
    action = None
    authenticated = False
    while not authenticated:
        authenticated = False
        while not authenticated:
            if authenticate():
                authenticated = True
            else:
                print("Incorrect password, please try again")
    while True:
        print("Do you want to store password? If YES, type y, if you want to get one of your passwords, type n")
        print("If you want to change your password for this app, type change")
        stores = get_user_input("If you want to try our game mode type interactive ")
        if not stores:
            break
        if answerIsYes(stores):
            action = StorePassword
            print("Storing")
        elif answerIsNo(stores):
            action = ReadPassword
        elif answerIsChange(stores):
            update_authentication_password()
        elif answerIsInteractive(stores):
            action = game_mode
        else:
            print("Invalid input, going back to the main menu ")

        if action:
            x = action(file_name)
            if x == -1:
                break
    print("You closed our app")
    print("Thank you for using our app")

main()