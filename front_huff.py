# Biblioteca necess�ria para a constru��o da interface.
from tkinter import *

# fa�o a importa��o do codigo para executar os comandos na interface.
from Defs_huff import *

# Inicializa��o da tela principal.
Tela_principal = Tk()

# Formata��o do t�tulo que aparece no canto superior esquerdo da tela.
Tela_principal.title("Algoritmo de Huffman")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('600x338')

# Variavel que armazenar� a imagem projetada na tela inicial.
img_principal = PhotoImage(file='imagem/ALGORITMO DE HUFFMAN(2).png')

#
label_image = Label(Tela_principal, image=img_principal).pack()

# bot�es responsaveis pela execu��o do c�digo.
bot�o_compactar = Button(Tela_principal, text = "compactar", command=)
bot�o_descompactar = Button(Tela_principal, text = "descompactar", command=)
bot�o_reconstruir = Button(Tela_principal, text = "reconstruir", command=)

# Pedir o arquivo 

# Comando necess�rio para manter a tela "rodando", e tbm responsavel pelo fechamento.
Tela_principal.mainloop()