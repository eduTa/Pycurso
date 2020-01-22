from tkinter import  *
import pymysql
from tkinter import messagebox
from tkinter import ttk

class usuario():
    def fazerLogin(self):
        logado = False
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='cursopythonum',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        except:
            print('Erro ao conectar com o banco de dados')

        usu = self.usuario.get()
        senha = self.senha.get()
        try:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM usuario LEFT JOIN admin on admin.idusuario = usuario.id')
                usuarios = cursor.fetchall()
        except:
            print('Houve outro erro escandaloso')
        for dado in usuarios:
            if dado['email'] == usu and dado['senha'] == senha:
                print('O seu usuário tá logado de boa')
                if dado['idusuario']:
                    print('É administrador meu filho')
                    logado = True
                else:
                    print('É usuario comum')
                    logado = True
        if logado == False:
            messagebox.showinfo('Login', 'Senha ou usuário errados')






    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        Label(self.root, text='Faça o seu login').grid(row=0, column=0, columnspan=2)
        Label(self.root, text='Usuário').grid(row=1, column=0)
        self.usuario = Entry(self.root)
        self.usuario.grid(row=1, column=1, padx=5, pady=5)
        Label(self.root, text='Senha').grid(row=2, column=0)
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)
        Button(self.root, text='Login', bg='green3', width=13, command=self.fazerLogin).grid(row=5, column=0, padx=5, pady=5)
        Button(self.root, text='Lembrar senha', width=13).grid(row=5, column=1, padx=3, pady=3)
        self.root.mainloop()


usuario()