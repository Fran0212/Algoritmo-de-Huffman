
# Biblioteca necess�ria para a construção da interface.
from tkinter import *

# fa�o a importa��o do codigo para executar os comandos na interface.
from Back.back_huff import *

# importa as fun��es necess�rias para o front do projeto
from Front.front_huff import *

# Inicialização da tela principal.
Tela_principal = Tk()

# Formata��o do t�tulo que aparece no canto superior esquerdo da tela.
Tela_principal.title("Algoritmo de Huffman")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('400x350')

# Variavel que armazenará a imagem projetada na tela inicial.
img_principal = PhotoImage(file='imagem/arvoreOfc-removebg-preview.png')

# Colocação da inagem da tela
label_image = Label(Tela_principal, image=img_principal).pack()

# Importação da imagem
img_compactar = PhotoImage(file='imagem/imagemDescompactar-removebg-preview.png')

# bot�es responsaveis pela execu��o do codigo.
botão_compactar = Button(Tela_principal, text="compactar", image= img_compactar, command=reconstruir )
botão_descompactar = Button(Tela_principal, text="descompactar", command=compactar)
botão_reconstruir = Button(Tela_principal, text="reconstruir", command=descompactar)

# Colocando a localização do botão na tela.
botão_compactar.place(x=280, y=260)
botão_descompactar.place(x=280, y=180)
botão_reconstruir.place(x=280, y=220)


# Comando necess�rio para manter a tela "rodando", e tbm responsavel pelo fechamento.
Tela_principal.mainloop()