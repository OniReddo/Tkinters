import tkinter as tk
from tkinter import ttk


# Parte do Banco

class Person:
    def __init__(self, name, cpf, age, phonenumber):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.phonenumber = phonenumber


class Client(Person):
    Users = []

    def __init__(self, accountnumber, password, balance):
        super().__init__()
        self.accountnumber = accountnumber
        self.password = password
        self.balance = balance
        self.history = []

    def deposit(self, amount):

        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        elif amount > self.balance:
            return False
        else:
            self.balance += amount
            return True

    def withdrawal(self, amount):

        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        elif amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def transfer(self, amount, subject):
        if amount not in '1234568790.':
            return False
        elif amount <= 0:
            return False
        elif amount > self.balance:
            return False
        else:
            subject.balance += amount
            self.balance -= amount
            return True

    def history(self, type, amount, who):
        if type == 1:
            self.history.append(f'Deposit of {amount}')
        if type == 2:
            self.history.append(f'Withdrawal of {amount}')
        if type == 3:
            self.history.append(f'Transfer of {amount} to acount{who}')

# Ui/Hus stuff

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('720x1000+610+0')
        self.title('Bank App')
        self.resizable(False,False)

class LoginScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('1')

class UserLoggedScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('2')

class CreditsScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('3')

class DepositScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('4')

class WithdrawalScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('5')

class TransferScreen(ttk.Frame):
    def __init__(self, root, Render = False):
        super().__init__(root)
        if Render:
            print('6')


if __name__ == '__main__':
    app = App()
    app.mainloop()