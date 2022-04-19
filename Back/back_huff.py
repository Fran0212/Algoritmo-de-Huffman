# Counter será usado na função "frequencia"
from collections import Counter

# config parser é uma biblioteca responsável por fazer arquivos de configuração
# será usada para criar uma espécie de banco de
# dados com os dados dos arquivos de entrada
import configparser

# deep copy sera usado na função concat
# para que eu altere um dicionário sem que as alterações sejam passadas adiante
from copy import deepcopy

# usado em ara odenar os dicionários de forma mais eficiente 
from operator import itemgetter

# Bits será usado nas funções "codifica" e "atribui"
# pois nós precisamos manipular bits ao invés de strings
from bitstring import Bits

cp = configparser.ConfigParser()


def frequencias(conteudo: str) -> dict:
    """Obtem as frequencias do texto do arquivo

    Args:
        conteudo (str): conteúdo do arquivo

    Returns:
        dict: dicionário com as frequências de cada letra
    """

    return dict(Counter(conteudo))


def ordem_freqs(dici: dict) -> dict:
    return dici


def concat(dici: dict) -> dict:
    """Essa função é responsável por concatenar
    as chaves e somar os valores do dicionário que é
    responsável por armazenar as letras e suas repectivias frequências no texto

    Args:
        dici (dict): dicionário que armazena as letras e suas frequencias

    Returns:
        dici (dict): retorna o mesmo argumento, no entanto
                    , atualizado com as novas variaveis e suas frequencias
    """

    # cria uma cópia do dicionário original
    # a qual será iterada, evitando assim perda de dados
    dici_copy = deepcopy(dici)
    # lista das chaves da cópia do dicionário
    chaves = list(dici_copy.keys())

    # laço reponsável por concatenar e somar chaves e valores
    # e adiocioná-las ao dicionário original
    while len(chaves) > 1:
        # new_key é o valor da soma das duas menores chaves do diconário
        new_key = chaves[0] + chaves[1]
        # soma das frequencias da menores e adição de new_key ao dicionário
        dici[new_key] = dici_copy[chaves[0]] + dici_copy[chaves[1]]
        # repete o mesmo processo de cima
        # mas dessa vez, o intuito é adicionar a nova para remover as antigas
        dici_copy[new_key] = dici[new_key]

        # ordenação de dici_copy
        # para que ele esteja sempre na ordem crescente
        # e as váriaveis nunca sejam confundidas
        dici_copy = ordem_freqs(dici_copy)

        # retida de dici_copy as duas chaves concatenadas
        # dessa forma, a gente evita que as chaves não concatenadas
        # fiquem sempre na frente das somadas
        for j in range(2):
            del dici_copy[chaves[j]]

        # atualização da lista de chaves
        # é necessária repetição de código, para que a lista seja atualizada
        chaves = list(dici_copy.keys())

    return ordem_freqs(dici)


def codifica(dici: dict, dici_cods: dict = {}) -> dict:
    """função responsável pela atribuição dos códigos de casa digito do meu arquivo

    Args:
        dici (dict): dicionário que contém as frequencias originais
        dici_cods (dict, optional): dicionário que contém os codigos das letras. Padrão: {}.

    Returns:
        dict: dicionário com os códigos
    """
    # keys recebe a lista de chaves do dicionário com as folhas e nós
    keys = list(dici.keys())

    # chama uma função responsável por obter as chaves que são apenas letras
    keys_alone = obtem_keys_alone(dici)

    # atribui Bits de 0,1 do menor ao maior de acordo com os nós e folhas
    dici = atrubui_bits(dici, keys)

    # atribuição de uma lista com as chaves do dicionário
    list_keys_alone = list(keys_alone.keys())


    # e atribui à chave o código pertencente aos nós até chegar na folha
    for k in range(len(list_keys_alone)):
        # reseta o codigo
        cod = Bits(0)
        for l in range(len(keys)):
            # verifica se a letra está dentro do nó
            if list_keys_alone[k] in keys[l]:
                # concatena um bit ao código
                cod += dici[keys[l]]
        # cada letra recebe seu código
        keys_alone[list_keys_alone[k]] = cod

    return keys_alone


def atrubui_bits(dici: dict, keys: list) -> dict:
    """atribui os bits de 0 e 1 para as chaves e nós do menor ao maior

    Args:
        dici (dict): dicionário original, ou seja, so com as frequencias
        keys (list): lista de chaves do dicionário

    Returns:
        dict: dicionário com 0 e 1, ou seja, a árvore montada
    """


    for i in range(len(keys)):
        if i == len(keys) - 1:
            dici[keys[i]] = Bits(0)
            continue
        if i % 2 == 0:
            dici[keys[i]] = Bits(bin="0b0")
            dici[keys[i+1]] = Bits(bin="0b1")

    return dici


def obtem_keys_alone(dici: dict) -> dict:
    """Obtem as chaves que contém apenas uma letra

    Args:
        dici (dict): dicionário contendo as frequencias de todos os nós e folhas da árvore

    Returns:
        dict: dicionário que contém os nós com letras únicas
    """

    # l é um lambda function que retona:
    # # o item se o seu tamanho for de apenas uma letra
    # # uma tupla contendo (None,None)
    l = lambda x: x if len(x[0]) == 1 else (None,None)

    # keys alone recebe o cast para dicionário do mapemento
    # dos itens do dicionário inserido na função
    # # eu fiz esse cast pois o hashmap só aceita uma chave por item
    # # logo, isso faz com que tudo que não tenha uma uníca letra
    # # seja facilmente retirado com a função del   
    keys_alone = dict(map(l, dici.items()))

    # remoção dos termos, de acordo com o pressuposto
    del keys_alone[None]

    return keys_alone


def atribui(dici: dict, arquivo: str, arquivo_loc) -> Bits:
    """é uma função responsável por atribuir à uma variável com um bit vazio
    os códigos das letras nas suas respectivas
    posições em relação ao texto original

    Args:
        dici (dict): dicionário com as chaves e seus respectivos códigos
        arquivo (str): string original para a compactação

    Returns:
        cont_arquivo_comp (bits): a bitstring do arquivo original
    """


    with open(arquivo_loc, "wb") as comp:
        for i in arquivo:
            # monta o arquivo compactado
            # concatenando os bits de cada letra 
            dici[i].tofile(comp)


def salva_desc(nome: str, arq: str, tipo_formato: str):
    """reponsável por salvar os dados dos aquivos originais

    Args:
        nome (str): diretório do arquivo
        arq (str): conteúdo do arquivo
    Returns:
        save (ini): salva os dados dos arquivos originais
    """

    dados_arqs = cp
    dados_arqs.read("save.ini", encoding= "UTF-8")

    # vê se o arquivo já consta no ini
    if existente(nome):
        # se contar retorna vazio
        return 0
    else:
        # o nome do arquivo é reescrio em caixa baixa
        # nome = nome.lower()

        # salvamento no arquivo ini
        dados_arqs[nome] = {"nome": arq, "tipo_formato": tipo_formato}

        # escreve os dados no ini
        with open("save.ini", "a", encoding="UTF-8") as save_comps:
            return dados_arqs.write(save_comps)


def compac(arq: str, arquivo_loc: str) -> Bits:
    """
    Responsável por agrupar todas as funções e fazer a compactação de fato

    Args:
        arq (str): conteúdo a ser compactado
        arquivo_loc (str): reponsável por indicar o local do arquivo

    Returns:
        arquivo (huff):  arquivo compactado
    """

    # pega as frequencias
    freq = frequencias(arq)
    print(1)
    # ordena-as 
    ord = ordem_freqs(freq)
    print(2)
    # concatena elas
    conc = concat(ord)
    print(3)
    # atribui codificação a cada letra
    codif = codifica(conc)
    print(4)
    # retorna o arquivo final compatado
    atribui(codif, arq, arquivo_loc)
    print(5)


def desc(nome: str, form: str, i: int = 1):
    """Descompacta o arquivo

    Args:
        form (str): formato do arquivo original
        nome (str): nome da chave para gravar o arquivo
        dici (str): armazenamento das chaves
        i (int, optional): contador de arquivos existentes. padrão para 0.
    """
    cp.read('save.ini', encoding="UTF-8")

    # cria o arquivo compactado no mesmo diretório do txt
    nome.replace(".huff", form)
    lista_nome2 = nome.split("/")

    if existente(nome):
        nome_arquivo = lista_nome2[-1].replace(".txt",f"({i}){form}")
    else:
        nome_arquivo = lista_nome2[-1]

    # tenta criar o arquivo
    try:
        with open(nome_arquivo, "x", encoding = "UTF-8") as des:
            return des.write(cp[nome].get("nome"))

    # se der erro ele entra na recursividade
    # passando o formato e i incrementado em um 
    except FileExistsError:
        return desc(nome, form, i+1)


def semi_compac(nome_arquivo: str):
    """faz parte dos processos para a compatação do arquivo

    Args:
        nome_arquivo (str): nome do arquivo a ser aberto

    Returns:
        semi_hd: responsável por guardar os dados do arquivo original
    """

    # abre o arquivo txt
    with open(nome_arquivo, "r") as conteudo_arq:
        conteudo_arq = conteudo_arq.read()

    # troca a extensão txt por huff
    nome_arquivo = nome_arquivo.replace(".txt", ".huff")

    # retorna o arquivo compactado
    compac(conteudo_arq, nome_arquivo)

    # armazena os dados do arquivo original de acordo com a função salva_desc
    semi_hd = salva_desc(nome_arquivo.replace(".huff", ".txt"), conteudo_arq, ".txt")

    return semi_hd


def existente(nome: str) -> bool:
    """verifica a existência de um determinado arquivo no diretório
        para isso, ele ve se o nome do meu arquivo -- diretório -- já se encontra
        no arquivo .ini que a codificação está salva

    Args:
        nome (str): diretório do arquivo

    Returns:
        bool: verdadeiro ou falso
    """

    return nome in cp.sections() 