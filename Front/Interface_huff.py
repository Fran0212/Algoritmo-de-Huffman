# Biblioteca necessaria para a construcao da interface.
from tkinter import *

# faço a importacao do codigo para executar os comandos na interface.
from Back.back_huff import *

# importa as funcoes necessarias para o front do projeto
from Front.front_huff import *

# Inicializacao da tela principal.
Tela_principal = Tk()

# Formatacao do título que aparece no canto superior esquerdo da tela.
Tela_principal.title("Algoritmo de Huffman")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('340x254+200+200')

# Para evitar que minha janela se redimensione
Tela_principal.resizable(False, False)

Tela_principal["bg"] = "white"

# Mudando o Ã­cone da tela
Tela_principal.iconbitmap('imagem/icon.ico')

# Variavel que armazenarÃ¡ a imagem projetada na tela inicial.
img_principal = PhotoImage(file='imagem/tree.png')
img_logo = PhotoImage(file='imagem/logo.png')


# Colocacao da inagem da tela
label_image = Label(Tela_principal, image=img_principal, bg="white").place(x=25, y=30)
label_logo = Label(Tela_principal, image=img_logo, bg="white").place(x=0, y=166)

# Importacao da imagem
img_compactar = PhotoImage(file='imagem/img2.png')
img_descompactar = PhotoImage(file='imagem/pimenta.png')

# botoes responsaveis pela execucao do codigo.
botao_compactar = Button(Tela_principal, text="compactar",image=img_compactar, bg= "white", command=compactar).place(x=220, y=50)
botao_descompactar = Button(Tela_principal, text="descompactar",image=img_descompactar, command=descompactar).place(x=220, y=120)

# Pedir o arquivo 

# Comando necessario para manter a tela "rodando", e tbm responsavel pelo fechamento.
Tela_principal.mainloop()