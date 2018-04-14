from configparser import ConfigParser
import getpass
import hashlib
import sys

parser = ConfigParser()
parser.read('configs.ini')

def choice():
    action = input('1: Login\n'
                   '2: Sign up\n'
                   '>>> ')
    return int(action)


def new_user():
    first = getpass.getpass()
    second = getpass.getpass()
    if first == second:
        password = hashlib.sha1()
        password.update(first.encode('utf-8'))
        return {'password': password.hexdigest()}
    else:
        print('Passwords are different')
        return 0


def new_data_input(login):
    if login in parser:
        print("User '{}' alredy exist".format(login))
    else:
        user = new_user()
        if user:
            parser[login] = user
            with open('configs.ini', 'w') as file:
                parser.write(file)
                print()
        else:
            return 0


def check_pass(password: str, hashcode: str):
    p = hashlib.sha1()
    p.update(password.encode('utf-8'))
    hash = (p.hexdigest())
    if hash == hashcode:
        print("Access granted")
        return True
    else:
        print("Access denied")
        return False


def main():
    pars_list = [i for i in parser]
    if len(pars_list) == 1:
        print('Create a new user')
        new_data_input(input("Login: "))
    while True:
        choice_num = choice()
        if choice_num == 2:
            new_data_input(input("Login: "))
        elif choice_num == 1:
            login = input("Login: ")
            if login in parser:
                if check_pass(getpass.getpass(), parser.get(login, 'password')):
                    pass
                else:
                    sys.exit()


if __name__ == '__main__':
    main()

