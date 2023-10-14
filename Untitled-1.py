from tkinter import *
import os

c=os.path.dirname(_file_)
nomeArquivo=c+'\\nomes.txt'

def impDados():
    print('Nome.....:%s' % vnome.get())
    print('Telefone.....:%s' % vtelefone.get())
    print('Nª/Apartamento.....:%s' % vapart.get())

def gravar():
    arquivo = open(nomeArquivo,'a')
    arquivo.write('Nome.....:%s' % vnome.get())
    arquivo.write('Telefone.....:%s' % vtelefone.get())
    arquivo.write('Nª/Apartamento.....:%s' % vapart.get())
    arquivo.write('\n\n')

janela = Tk()

janela.title('Cadastro')
janela.geometry('500x300')
janela.configure(background="#dde")

Label(janela,text='Nome',background='#dde',foreground='#099',anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(janela)
vnome.place(x=10,y=30,width=200,height=20)

Label(janela,text='Telefone',background='#dde',foreground='#099',anchor=W).place(x=10,y=60,width=100,height=20)
vtelefone= Entry(janela)
vtelefone.place(x=10,y=80,width=200,height=20)

Label(janela,text='N/Apartamento',background='#dde',foreground='#099',anchor=W).place(x=10,y=110,width=100,height=20)
vapart= Entry(janela)
vapart.place(x=10,y=130,width=200,height=20)

Button(janela,text='Imprimir',command=impDados).place(x=10,y=150,width=100,height=30)
Button(janela,text='Gravar',comand=gravar).place(x=10,y=160,width=100,height=30)


janela.mainloop()