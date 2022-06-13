from tkinter import *

root = Tk()
root.geometry('1280x720+300+100')
root.config(bg='lightgray')


# borderwidth=20, relief='groove'

# ==========================================================================

# class do layout
class Layout():
    # função titulo,| nome da var, texto da var, cordenadas y, x |
    @staticmethod
    def titulo(var, frame, text, y, x):
        var = Label(frame, bg='gray', text=text)
        var.grid(row=y, column=x, sticky=NSEW)

    # função caption,| nome da var, texto da var, cordenadas y, x |
    @staticmethod
    def caption(var, frame, text, y, x):
        var = Label(frame, bg='gray', text=text)
        var.grid(row=y, column=x, sticky=NSEW)

    @staticmethod
    def entry(var, frame, y, x, show=''):
        var = Entry(frame, show=show)
        var.grid(row=y, column=x, sticky=NSEW)

    # provavelmente nada e vai sair daqui
    @staticmethod
    def button(var, frame, text, command, y, x):
        var = Button(frame, text=text, command=command)
        var.grid(row=y, column=x, sticky=NSEW)

    @staticmethod
    def chckbttn(var, frame, text, y, x):
        var = Checkbutton(frame, bg='gray', text=text, width=15)
        var.grid(row=y, column=x, sticky=NSEW)


# ==========================================================================
# ========================== Primeira Tela =================================
# ==========================================================================
class Command:
    @staticmethod
    def screen_one():
        # Limpa e cria o layout primeira tela
        Command.clear()

        login = Frame(root, bg='gray', borderwidth=2, relief='groove')
        login.grid(row=1, column=1, sticky=NSEW)

        Layout.titulo('login', login, 'Login', 0, 0)

        Layout.caption('nome', login, 'Nome :', 1, 0)
        Layout.entry('nome_entry', login, 1, 1)

        Layout.caption('senha', login, 'Senha :', 2, 0)
        Layout.entry('senha_entry', login, 2, 1, '*')

        Layout.button('login', login, 'Login', Command.screen_two, 3, 1)

    # ==========================================================================
    # ============================== Segunda Tela   ============================
    # ==========================================================================
    @staticmethod
    def screen_two():
        # Limpa e cria o layout da segunda tela
        Command.clear()

        # Layout Grid
        dados_p = Frame(root, bg='gray', borderwidth=2, relief='groove')
        dados_p.grid(row=0, column=1, sticky=NSEW)

        endereco = Frame(root, bg='gray', borderwidth=2, relief='groove')
        endereco.grid(row=1, column=1, sticky=NSEW)

        extra = Frame(root, bg='gray', borderwidth=2, relief='groove')
        extra.grid(row=2, column=1, sticky=NSEW)

        # ============================== Dados Pessoais ============================
        Layout.titulo('dados_pessoais', dados_p, 'Dados Pessoais', 0, 0)

        Layout.caption('nome', dados_p, 'Nome :', 1, 0)
        Layout.entry('nome_entry', dados_p, 1, 1)

        Layout.caption('cpf', dados_p, 'CPF :', 2, 0)
        Layout.entry('cpf_entry', dados_p, 2, 1)

        Layout.caption('telefone', dados_p, 'Telefone :', 2, 2)
        Layout.entry('', dados_p, 2, 3)

        Layout.caption('data_nasc', dados_p, 'Data Nasc :', 2, 4)
        Layout.entry('data_nasc', dados_p, 2, 5)

        Layout.caption('sexo', dados_p, 'Sexo :', 3, 0)
        Layout.chckbttn('masc', dados_p, 'Masculino', 3, 1)
        Layout.chckbttn('fem', dados_p, 'Feminino', 3, 2)

        # quadradinho de selecionar sexu | AQUI |

        # ============================== Endereço ============================
        Layout.titulo('endereco', endereco, 'Endereço', 0, 0)

        Layout.caption('rua', endereco, 'Rua :', 1, 0)
        Layout.entry('rua', endereco, 1, 1)

        Layout.caption('numero', endereco, 'Nº :', 1, 2)
        Layout.entry('numero', endereco, 1, 3)

        Layout.caption('bairro', endereco, 'Bairro :', 2, 0)
        Layout.entry('bairro', endereco, 2, 1)

        Layout.caption('cidade', endereco, 'Cidade :', 2, 2)
        Layout.entry('cidade', endereco, 2, 3)

        Layout.caption('uf', endereco, 'UF :', 2, 4)
        Layout.entry('uf', endereco, 2, 5)

        Layout.button('gravar', extra, 'Gravar Dados', Command.grvr_dds, 0, 0)
        Layout.button('sair', extra, 'Sair', Command.screen_one, 0, 1)

    # ==========================================================================
    @staticmethod
    def clear():
        for widget in root.winfo_children():
            widget.destroy()

    @staticmethod
    def grvr_dds():
        pass


# Area para rodar codigo
Command.screen_one()

root.mainloop()
