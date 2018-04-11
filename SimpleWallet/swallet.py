from time import ctime
from sys import exit
import json
import io

"""
Кровью и потом выдавил из себя этот шедевр.
Впринципе, он делает все как надо.
не исключено что где то вылетит ошибка.
"""


def current_time(date: str):
    date = date.split()
    return "{}-{}-{}  {}".format(date[2], date[1], date[4], date[3])


class Person:

    users = dict()
    current_user = 0
    data = dict()

    def __init__(self, name, id):
        self._name = name
        self._id = id
        self.wallets = []
        Person.users[self] = {'obj': tuple((self._name, self._id))}

    def __str__(self):
        return "{} - {}".format(self._id, self._name)

    @staticmethod
    def gen_id():
        """Generate id-number"""
        id = 1
        obj = iter(sorted(Person.users, key=lambda x: x._id))
        try:
            while True:
                if id == int(next(obj)._id):
                    id += 1
                else: return str(id)
        except StopIteration: return str(id)

    @staticmethod
    def print_users():
        """Print users from list"""
        for pers in sorted(Person.users, key=lambda x: x._id):
            print('{} - {}'.format(pers._id, pers._name))

    @staticmethod
    def choose_user(id_or_name):
        """Choose user from list 'users'."""
        for pers in Person.users:
            if id_or_name in Person.users[pers]['obj']:
                Person.current_user = pers
                print("Current user: {} - {}".format(pers._id, pers._name))
                break
        else:
            print("There is no user with id or name: {}".format(id_or_name))

    @staticmethod
    def delete_user(id_or_name):
        """Delete user from list 'users'."""
        for pers in Person.users:
            try:
                if id_or_name in Person.users[Person.current_user]['obj']:
                    print("You can't delete active user\n"
                          "Choose another user.")
                    break
            except KeyError: print('', end='')
            if id_or_name in Person.users[pers]['obj']:
                print("Deleted user: {} - {}".format(pers._id, pers._name))
                Person.users.pop(pers)
                break
        else:
            print("There is no user with id or name: {}".format(id_or_name))

    @staticmethod
    def save_data():
        """Convert {users} to format which supported"""
        for pers in Person.users:
            Person.data['{}:{}'.format(pers._id, pers._name)] = {'obj': (pers._name, pers._id),
                                                                 'wallets': dict()}
            for w in pers.wallets:
                Person.data['{}:{}'.format(pers._id, pers._name)]['wallets'][w._name] = w.transactions

    def add_wallet(self, name):
        """Add new wallet"""
        self.wallets.append(Wallet(name))

class Wallet:

    wallets = []

    def __init__(self, name):
        self._name = name
        Wallet.wallets.append(self)
        self._transactions = []
        self._ballance = 0

    def __str__(self):
        return '{} - {}'.format(self._name, self._ballance)

    def calc_ballance(self):
        """
        Take info from _transactions add calculate ballance from element[0] of tuples.
        """
        res = 0
        for i in self._transactions:
            res += i[0]
        return res

    def add_transaction(self, value):
        """
        Add transactions to list.
        """
        self._transactions = list(self._transactions)
        if type(value) == list:
            self._transactions.extend(value)
        else:
            self._transactions.append([int(value), current_time(ctime())])
        self._ballance = self.calc_ballance()

    @property
    def name(self):
        return self._name

    @property
    def transactions(self):
        return self._transactions

    def print_transactions(self):
        for t, count in zip(reversed(self._transactions), range(10)):
            print('\t{} \t {} '.format(t[1], t[0]))


def whelp():
    print("""
    - `h` або `?`          - вивести список команд з прикладами
    -  +p[name]            - додати людину
    -  lp                  - вивести список людей з їх порядковими номерами
    -  lpa                 - Вивести людину яку активовано
    -  -p[id or name]      - видалити людину з вказаним номером
    -  sp[id or name]      - вибрати людину з вказаним номером (подальші транзакції будуть записуватися від відповідного імені)
    -  +w[name of wallet]  - додати гаманець
    -  lw                  - вивести список гаманців з номерами і залишками
    -  -w 1`               - видалити вказаний гаманець разом з усіма прив'язаними транзакціями
    -  t[name][value]`     - додати транзакцію з суммою [value] у гаманець [name] і показати залишок
    -  last[name]          - вивести останні 10 транзакцій з сумами і датами по відповідному гаманцю, а також залишок по ньому
    -  last                - аналогічно, але для всіх гаманців один за одним
    -  q                   - вихід з програми""")


def main():
    """This is main function"""
    load_data()
    while True:
        users_input = input(">>> ").split()
        if users_input[0] == 'q' or users_input == 'exit':
            save_to_file()
            exit()
        elif users_input[0] == 'sd':
            save_to_file()
        elif users_input[0] == 'h' or users_input == '?':
            whelp()
            continue
        elif users_input[0] == '+p':
            try: Person(users_input[1], Person.gen_id())
            except IndexError: print("Enter name!!!")
        elif users_input[0] == 'lp':
            Person.print_users()
            continue
        elif users_input[0] == 'lpa':
            print('Current user: {}'.format(str(Person.current_user)))
            continue
        elif users_input[0] == '-p':
            try:
                Person.delete_user(users_input[1])
            except IndexError: print("Enter ID or Name!!!")
            continue
        elif users_input[0] == 'sp':
            try:
                Person.choose_user(users_input[1])
            except IndexError: print("Enter ID or Name!!!")
            continue
        elif users_input[0] == '+w':
            if Person.current_user == 0:
                print('Please, choose an user!!!')
            else:
                Person.current_user.add_wallet(users_input[1])
                print('New wallet: {}({})'.format(users_input[1], Person.current_user))
        elif users_input[0] == 'lw':
            if Person.current_user == 0:
                print('Please, choose an user!!!')
            else:
                for w in Person.current_user.wallets:
                    print(str(w))
            continue
        elif users_input[0] == 't':
            for w in Wallet.wallets:
                if users_input[1] == w._name:
                    w.add_transaction(int(users_input[2]))
                    print(w)
        elif users_input[0] == "--pw":
            for w in Wallet.wallets:
                print(w, w.transactions)
            continue
        elif users_input[0] == 'last':
            if len(users_input) == 1:
                for w in Wallet.wallets:
                    print(w.name.center(50, ' '))
                    w.print_transactions()
                    print('='*50)
                    print()
                continue
            else:
                for w in Wallet.wallets:
                    if w.name == users_input[1]:
                        w.print_transactions()
                        break
                else: print("There is not a wallet with id: {}".format(users_input[1]))
                continue
        elif users_input[0] == '-w':
            if Person.current_user == 0:
                print('Please, choose an user!!!')
            else:
                for w in Person.current_user.wallets:
                    if w.name == users_input[1]:
                        Person.current_user.wallets.remove(w)
                        Wallet.wallets.remove(w)
                        break
                else:
                    print("There is not a wallet with id: {}".format(users_input[1]))
        save_to_file()


def load_data():
    """Load data from file and convert data => objects.
    If the file doesn't exist - function create new empty file"""
    try:
        data = json.load(open('transactions.json', 'r+'))
        for k, v in data.items():
            p = Person(v['obj'][0], v['obj'][1])
            for w, t in v['wallets'].items():
                try:
                    w = Wallet(w)
                    w.add_transaction(t)
                    p.wallets.append(w)
                except IndexError: p.add_wallet(w)
    except FileNotFoundError: print('New file created')
    except io.UnsupportedOperation: pass
    except json.JSONDecodeError: pass


def save_to_file():
    """Save dictionary to the file"""
    Person.save_data()
    json.dump(Person.data, open('transactions.json', 'w'), indent=10)
    print('Data saved')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()

