import json


stores = input("Do you want to store password? If YES, type y, if NO, type n ")
if stores == "y":
    file = open("data.json", "w")
    password = input("Enter your password ")
    account = input("Enter for what account is it ")
    pass_dict = {"password" : password, "account" : account}
    pass_dict_json= json.dumps(pass_dict)
    file.write(pass_dict_json)


if stores == "n":
    file = open("data.json", "r")
    print("You want to get one of your passwords ")
    #print(file.read())
    data_string = file.read()
    account = input("Enter the account ")
    pass_dict = json.loads(data_string)
    print(pass_dict["password"])


