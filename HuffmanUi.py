# arquivo que contém as funções de compactação
from Defs_huff import *

# biblioteca pela interface
from tkinter import filedialog as dlg

# biblioteca usada pra printar as mensagens coloridas
from termcolor import cprint

# importa o erro para o tratamento
from configparser import NoSectionError

# laço que roda o programa
while True:
    # laço que recebe a ação que vai orientar o resto do código
    while True:
        print("Digite c para COMPACTAR, x para DESCOMPACTAR,\
r para RECONSTRUIR ou q para SAIR:", end=" ")
        action = str(input()).lower()
        if action == "x" or action == "c" or action == "r":
            break
        elif action == "q":
            exit(0)
        else:
            cprint("Ué!? não entendi, djabeisso?", "red")
            continue

    print("Selecione o arquivo desejado na janela:")

    # vai tentar importar um arquivo, se não for compatível
    # com o código ele da um "ImportError"
    try:
        arquivo_loc = dlg.askopenfilename()
        erro_import(arquivo_loc, action)
    except ImportError:
        if action == "c":
            cprint('Extensão inválida, selecione um arquivo ".txt"', "red")
        if action == "x":
            cprint('Extensão inválida, selecione um arquivo ".huff"', "red")
        continue

    if action == "c":
        try:
            semi_compac(arquivo_loc)
        except:
            cprint("Ops, algo deu errado!", "red")
        else:
            cprint("Arquivo compactado com sucesso!", "green")

    if action == "x":

        cp.read('save.ini', encoding="utf-8")

        try:
            nome_section = arquivo_loc.lower()
            formate = cp[nome_section].get("tipo_formato")
            desc(nome_section, formate)

        except NoSectionError:
            print("Ops, algo deu errado!", "red")
        else:
            cprint("Arquivo descompactado com sucesso!", "green")

    if action == "r":

        cp.read('save.ini', encoding="utf-8")

        try:
            nome_section = arquivo_loc.lower()
            formate = cp[nome_section].get("tipo_formato")
            desc(nome_section, formate)

        except NoSectionError:
            print("Ops, algo deu errado!", "red")
        else:
            cprint("Arquivo reconstruido com sucesso!", "green")
