from tkinter import  *
import pymysql
from tkinter import messagebox
from tkinter import ttk

class usuario():
    def fazerLogin(self):
        print('Vem aqui de boa')

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        Label(self.root, text='Faça o seu login').grid(row=0, column=0, columnspan=2)
        Label(self.root, text='Usuário').grid(row=1, column=0)
        self.usuario = Entry(self.root).grid(row=1, column=1, padx=5, pady=5)
        Label(self.root, text='Senha').grid(row=2, column=0)
        self.senha = Entry(self.root, show='*').grid(row=2, column=1, padx=5, pady=5)
        Button(self.root, text='Login', bg='green3', width=13, command=self.fazerLogin).grid(row=5, column=0, padx=5, pady=5)
        Button(self.root, text='Lembrar senha', width=13).grid(row=5, column=1, padx=3, pady=3)
        self.root.mainloop()


usuario()