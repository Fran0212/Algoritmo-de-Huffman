
# Biblioteca necess�ria para a construção da interface.
import tkinter.colorchooser
from tkinter import *

# fa�o a importação do codigo para executar os comandos na interface.
from Back.back_huff import *

# importa as fun��es necessárias para o front do projeto
from Front.front_huff import *

# Inicialização da tela principal.
Tela_principal = Tk()

# Formata��o do t�tulo que aparece no canto superior esquerdo da tela.
Tela_principal.title("Algoritmo de Huffman")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('340x254+200+200')

# Para evitar que minha janela se redimensione
Tela_principal.resizable(False, False)

Tela_principal["bg"] = "white"

# Mudando o ícone da tela
Tela_principal.iconbitmap('imagem/icon.ico')

# Variavel que armazenará a imagem projetada na tela inicial.
img_principal = PhotoImage(file='imagem/tree.png')
img_logo = PhotoImage(file='imagem/logo.png')


# Colocação da inagem da tela
label_image = Label(Tela_principal, image=img_principal, bg="white").place(x=25, y=30)
label_logo = Label(Tela_principal, image=img_logo, bg="white").place(x=0, y=166)

# Importação da imagem
img_compactar = PhotoImage(file='imagem/img2.png')
img_descompactar = PhotoImage(file='imagem/pimenta.png')

# bot�es responsaveis pela execu��o do codigo.
botão_compactar = Button(Tela_principal, text="compactar",image=img_compactar, bg= "white", command=reconstruir).place(x=220, y=50)
botão_descompactar = Button(Tela_principal, text="descompactar",image=img_descompactar, command=compactar).place(x=220, y=120)


# Comando necess�rio para manter a tela "rodando", e tbm responsavel pelo fechamento.
Tela_principal.mainloop()