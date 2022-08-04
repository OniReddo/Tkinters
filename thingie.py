import tkinter as tk
from tkinter import ttk
import tkinter.font as font


class Methods:
    @staticmethod
    def gridding(subject, row, column):
        for rows in range(row):
            print(rows)
            subject.grid_rowconfigure(rows, weight=1)
        for columns in range(column):
            print(columns)
            subject.grid_columnconfigure(columns, weight=1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.length = 1280
        self.height = 720

        self.geometry(f'{self.length}x{self.height}')

        self.curr_screen = None

        Methods.gridding(self, 1, 1)
        self.count = 1

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def screen1(self, render=False):
        self.clear()
        self.curr_screen = Screen1(self, render)

    def screen2(self, render=False):
        self.clear()
        self.curr_screen = Screen2(self, render)


class Screen1(ttk.Frame):
    def __init__(self, root, render):
        super().__init__(root)
        if render:
            self.root = root
            Methods.gridding(self, 1, 1)
            self.grid(row=0, column=0, stick=tk.NSEW)

            self.frame = tk.Frame(self, bg='lightblue')
            self.frame.grid(row=0, column=0, sticky=tk.NSEW)
            Methods.gridding(self.frame, 3, 3)

            f = font.Font(size=35)

            self.label = ttk.Label(self.frame, text=self.root.count, background='lightblue', foreground='white')
            self.label['font'] = f
            self.label.grid(row=0, column=1, sticky=tk.NSEW)

            self.button = ttk.Button(self.frame, command=self.back)
            self.button.grid(row=1, column=1, sticky=tk.NSEW)

            self.after(1000, self.back)

    def back(self):
        self.root.count += 1
        self.root.screen2(True)


class Screen2(ttk.Frame):
    def __init__(self, root, render):
        super().__init__(root)
        if render:
            self.root = root

            Methods.gridding(self, 1, 1)
            self.grid(row=0, column=0, sticky=tk.NSEW)

            self.frame = tk.Frame(self, bg='pink')
            self.frame.grid(row=0, column=0, sticky=tk.NSEW)
            Methods.gridding(self.frame, 3, 3)

            f = font.Font(size=35)

            self.label = ttk.Label(self.frame, text=self.root.count, background='pink', foreground='white')
            self.label['font'] = f
            self.label.grid(row=0, column=1, sticky=tk.NSEW)

            self.button = ttk.Button(self.frame, command=self.back)
            self.button.grid(row=1, column=1, sticky=tk.NSEW)

            self.after(1000, self.back)

    def back(self):
        self.root.count += 1
        self.root.screen1(True)


if __name__ == '__main__':
    app = App()
    app.screen1(True)
    app.mainloop()
