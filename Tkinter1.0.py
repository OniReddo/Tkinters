import tkinter
from tkinter import *

root = Tk()
root.geometry('1280x720+700+100')

# Classe frame
title = Frame(root)
title.grid()
# borderwidth=20, relief='groove'

caption = Frame(root)
caption.grid()

button = Frame(root, bg='gray')
caption.grid()

# Grade da tela
for row in range(13):
    root.grid_rowconfigure(row, weight=1)
for column in range(7):
    root.grid_columnconfigure(column, weight=1)


# class do layout
class Layout():
    # função titulo,| nome da var, texto da var, cordenadas y, x |
    def titulo(var, text, y, x):
        var = Label(title, text=text, fg='red')
        var.grid(row=y, column=x)

    # função caption,| nome da var, texto da var, cordenadas y, x |
    def caption(var, text, y, x):
        var = Label(caption, text=text, fg='black')
        var.grid(row=y, column=x)

    # provavelmente nada e vai sair daqui
    def button():
        pass


class Command():
    def screen_one():
        # Limpa e cria a primeira tela
        Layout.titulo('login', 'Login', 0, 0)
        Layout.titulo('nome', 'Nome', 1, 0)
        Layout.titulo('senha', 'Senha', 2, 0)

    def screen_two():
        # Limpa e cria a segunda tela
        Command.clear()
        Layout.titulo('dados_pessoais', 'Dados Pessoais', 0, 0)

    def clear():
        for widget in root.winfo_children():
            widget.destroy()

    def join():
        # chama uma função que limpa tela, e ja cria outra
        pass

    def exit():
        pass

    def grvr_dds():
        pass


# Area para rodar codigo
Command.screen_one()

root.mainloop()