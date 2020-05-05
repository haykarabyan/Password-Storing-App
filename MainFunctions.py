import json
from hashlib import sha256
from random import randint
from datetime import date


def fill_the_file(file_name):
    empty = False
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
            empty = True
    if empty:
        with open(file_name, 'w') as f:
            f.write("[]")


def get_user_input(text):
    t = input(text)
    if t == 'exit':
        return None
    else:
        return t


def answerIsYes(answer):
    if answer.lower() == 'yes' or answer.lower() == 'y':
        return True
    return False


def answerIsNo(answer):
    if answer.lower() == "no" or answer.lower() == 'n':
        return True
    return False


def answerIsChange(answer):
    if answer.lower() == "change":
        return True
    return False


def answerIsInteractive(answer):
    if answer.lower() == "interactive":
        return True
    return False


def readFile(file_name):
    with open(file_name) as f:
        data = f.read()
        data = json.loads(data)
        return data


def writeFile(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)


def StorePassword(file):
    user_account = get_user_input("Enter your account ")
    user_password = get_user_input("Enter your password ")

    if not user_password or not user_account:
        return

    Password = {user_account: user_password}
    data = readFile(file)
    exists = False
    for d in data:
        if d.get(user_account):
            exists = True
            if exists:
                update_pass = get_user_input("Password for this account already exists, do you want to update it? ")
                if not update_pass:
                    return -1
                if answerIsYes(update_pass):
                    d[user_account] = user_password
                    print("Password successfully updated")
                else:
                    print("Password not updated, going back to the main menu.")
    if not exists:
        data.append(Password)
        print("___Password successfully stored___")

    data = json.dumps(data)
    writeFile(file, data)


def ReadPassword(file):
    data = readFile(file)
    interactive_printing = get_user_input("Do you want interactive listing of all of your passwords? ")
    if not interactive_printing:
        return -1
    if answerIsYes(interactive_printing):
        print_with_table(data)
        print("Total number of passwords is", len(data))
        return
    user_account = get_user_input("Enter the account ")
    if not user_account:
        return -1

    for d in data:
        if d.get(user_account):
            print(d[user_account])
            return
    print("Not found")


def authenticate():
    password = get_user_input("Enter your password ")
    if not password:
        return -1
    if password:
        hash = convert_to_sha256(password)
        with open("hash_password.txt") as f:
            original_hash = f.read()
        if original_hash == hash:
            return True


def update_authentication_password():
    new_password = get_user_input("Enter your new password ")
    new_password_hash = convert_to_sha256(new_password)
    if not new_password_hash or not new_password:
        return -1
    with open("hash_password.txt", "w") as f:
        f.write(new_password_hash)


def convert_to_sha256(plain_text):
    hash = sha256(bytes(plain_text, 'utf-8'))
    hash = hash.hexdigest()
    return hash


def print_with_table(password_list):
    for password in password_list:
        for account in password.keys():
            print('|', account, password[account], '|')



def number_is_even(n):
    if n % 2 == 0:
        return True
    return False


def game_mode(file):
    data = readFile("data.json")
    score_records = readFile("score_records.json")
    view_results = get_user_input("If you want to play, type yes, if you want to view the results, type no ")
    if not view_results:
        return -1
    if answerIsNo(view_results):
        print_with_table(score_records)
        print("Total number of records is", len(score_records))
    else:
        score = 0
        already_asked = []

        amount_of_passwords = len(data)
        number_of_questions = amount_of_passwords // 2
        for i in range(number_of_questions):
            n = 0
            not_found = True
            while not_found:
                n = randint(0, amount_of_passwords - 1)
                if data[n] not in already_asked:
                    already_asked.append(data[n])
                    not_found = False

            question_account = data[n]
            print(get_key(question_account))
            guess = get_user_input("Enter the password you remember for this account ")
            if not guess:
                return -1
            if guess == question_account[get_key(question_account)]:
                print("!!!!!CORRECT!!!!!")
                score += 1
            else:
                print("!!!!!WRONG!!!!!")
        print("Your final score is", score)
        data = readFile("score_records.json")
        data.append({str(date.today()): score})
        data = json.dumps(data)
        writeFile("score_records.json", data)


def get_key(dict):
    for key in dict.keys():
        return key
# print them with a list
# make a password guessing game
