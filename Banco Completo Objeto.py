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
        self.resizable(False, False)

        self.curr_screen = None

    def screen_one(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = LoginScreen(self,True)

    def screen_two(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = UserLoggedScreen(self,True)

    def screen_three(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = CreditsScreen(self,True)
    def screen_four(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = DepositScreen(self,True)
    def screen_five(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = WithdrawalScreen(self,True)
    def screen_six(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.curr_screen = TransferScreen(self,True)

class LoginScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(self,text='Tela 1')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_two)
            bttn.pack()

class UserLoggedScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(root,text='Tela 2')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_three)
            bttn.pack()

class CreditsScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(root,text='Tela 3')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_four)
            bttn.pack()

class DepositScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(root,text='Tela 4')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_five)
            bttn.pack()

class WithdrawalScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(root,text='Tela 5')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_six)
            bttn.pack()

class TransferScreen(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            self.pack()
            lbl = ttk.Label(root,text='Tela 6')
            lbl.pack()
            bttn = ttk.Button(self,text='Mudar tela', command= app.screen_one)
            bttn.pack()

if __name__ == '__main__':
    app = App()
    app.screen_one()
    app.mainloop()
