from tkinter import *
import tkinter

root = Tk()
root.geometry(('1280x720'))
root.config(bg='lightblue')
root.grid()


def validate():
    return False

vdcm = root.register(validate())


ntry1 = tkinter.Entry(validate='key', validatecommand=vdcm)
ntry1.grid(row=1, column=1, sticky=NSEW)

root.mainloop()


def format_CPF(event = None):
    text = CPFR.get().replace(".","").replace("-","")[:11]
    new_text = ""



    for index in range(len(text)):

        if text[index] in "0123456789":
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]

    CPFR.delete (0,'end')
    CPFR.insert (0, new_text)


CPFR.bind("<KeyRelease>",format_CPF)