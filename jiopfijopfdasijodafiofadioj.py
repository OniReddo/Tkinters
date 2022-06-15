import tkinter as tk
from tkinter import ttk


def switchscreen(screenpos):
    App.clear_screen()


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry('1280x720')
        self.title('App Window')
        self.grid()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()


# Screen 1
class ScreenOne(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            # Root manipulation
            self.frame = ttk.Frame(root)
            self.frame.pack()
            grid_create(self.frame, 3, 3)
    
            # Stuff declatarion
            self.frm1 = tk.Frame(self.frame)
            self.frm1.grid(row=1, column=1)
    
            self.lbl1 = tk.Label(self.frm1, text='Login')
            self.lbl1.grid(row=1, column=0)
    
            self.lbl2 = tk.Label(self.frm1, text='Usuario')
            self.lbl2.grid(row=2, column=0)
    
            self.ntry1 = tk.Entry(self.frm1)
            self.ntry1.grid(row=3, column=0)
    
            self.lbl3 = tk.Label(self.frm1, text='Senha')
            self.lbl3.grid(row=4, column=0)
    
            self.ntry2 = tk.Entry(self.frm1)
            self.ntry2.grid(row=5, column=0)
    
            self.bttn1 = tk.Button(self.frm1, text='Entrar', command=print(''))
            self.bttn1.grid(row=6, column=0)


# Screen 2
class ScreenTwo(ttk.Frame):
    def __init__(self, root, Render=False):
        super().__init__(root)
        if Render:
            # Root manipulation
            self.frame = ttk.Frame(root)
            self.frame.pack()

            # Stuff declaration
            self.frm1 = ttk.Frame(self.frame)
            self.frm1.grid(row=0, column=1)
            self.lbl1 = tk.Label(self.frm1, text='Segunda tela 😃👍')
            self.lbl1.grid(row=0, column=0)


def grid_create(root, row, column):
    for count in range(row):
        root.grid_rowconfigure(count, weight=1)
    for count in range(column):
        root.grid_columnconfigure(count, weight=1)

    def entrar(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
