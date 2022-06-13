import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1280x720')
        self.title('App Window')

        self.grid()

        for row in range(3):
            self.grid_rowconfigure(row,weight=1)
        for row in range(3):
            self.grid_columnconfigure(row,weight=1)


        self.frm1 = tk.Frame(self)
        self.frm1.grid(row=1, column=1)

        for row in range(7):
            print(row)
            self.frm1.grid_rowconfigure(row,weight=1)
        for row in range(3):
            self.frm1.grid_columnconfigure(row,weight=1)


        # things
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

        self.bttn1 = tk.Button(self.frm1, text='Entrar', command=self.entrar)
        self.bttn1.grid(row=6, column=0)

    def entrar(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
