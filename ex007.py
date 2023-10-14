# desenvolva um programa que leia as duas notas de um aluno . Calcule e mostre sua media.

from tkinter import *



    #
    #print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}'.format(n1, n2, media))
    
    

janela = Tk() # aqui é a janela o tkinter
janela.title('Cadatros') # titulo 
janela.geometry('500x300+200+200')# aqui determino onde a janela ficará posicionada ao executar o programa
janela.configure(background='#dde') # cor de fundo



def media():
      entrada1 = int(text1.get())
      entrada2 = int(text2.get())
      m = entrada1 + entrada2
      media = Label(janela, text=f'A media é: {m}').grid(row= 3, column=1)
      


l1 = Label(janela,text='Primeira nota ',
      background='#dde',
      foreground='#009',
      font='black',
      anchor=W).grid(row=0) 
text1 = Entry(janela) # aqui cria uma caixa vazia para digitar o nome
text1.grid(row=0, column=1)

l2 = Label(janela,text='Segunda nota ',
      background='#dde',
      foreground='#009',
      font='black', 
      anchor=W).grid(row=1)
text2 = Entry(janela)
text2.grid(row=1, column=1)




media = Button(janela,text='Media',
       
       command=media).grid(row=3) # command é o camando do botão gravar que aparece na tela, place é a posição da caixa com o nome.


janela.mainloop()