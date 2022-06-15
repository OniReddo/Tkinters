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

    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def transfer(self):
        pass

    def history(self):
        pass

    





# Ui/Hus stuff


if __name__ == '__main__':
    pass
