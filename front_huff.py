# Biblioteca necessária para a construção da interface.
from tkinter import *

# faço a importação do codigo para executar os comandos na interface.
from Defs_huff import *

# Inicialização da tela principal.
Tela_principal = Tk()

# Formatação do título que aparece no canto superior esquerdo da tela.
Tela_principal.title("Algoritmo de Huffman")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('600x338')

# Variavel que armazenará a imagem projetada na tela inicial.
img_principal = PhotoImage(file='imagem/ALGORITMO DE HUFFMAN(2).png')

#
label_image = Label(Tela_principal, image=img_principal).pack()

# botões responsaveis pela execução do código.
botão_compactar = Button(Tela_principal, text = "compactar", command=)
botão_descompactar = Button(Tela_principal, text = "descompactar", command=)
botão_reconstruir = Button(Tela_principal, text = "reconstruir", command=)

# Pedir o arquivo 

# Comando necessário para manter a tela "rodando", e tbm responsavel pelo fechamento.
Tela_principal.mainloop()