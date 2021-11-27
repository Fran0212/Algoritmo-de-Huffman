import configparser
# config parser é uma biblioteca responsável por fazer arquivos de configuração
# será usada para criar uma espécie de banco de
# dados com os dados dos arquivos de entrada

from copy import deepcopy
# deep copy sera usado na função concat
# para que eu altere um dicionário sem que as alterações sejam passadas adiante

from bitstring import Bits
# Bits será usado nas funções "codifica" e "atribui"
# pois nós precisamos manipular bits ao invés de strings

cp = configparser.ConfigParser()


def frequencias(entrada: str) -> dict:
    """Obtem as frequencias de cada letra

    Args:
        entrada (str): um texto inteiro

    Returns:
        letras_freqs (dict): um dicionário que contem cada item
        e suas frequencias
    """
    entrada = entrada
    letras_freqs = {}
    # key = list(dici.keys())

    # esse for vai iterar a string de entrada
    for x in range(len(entrada)):
        # freqs vai receber a incidencia de cada letra no texto
        freqs = entrada.count(entrada[x])

        # o dicionário recebe a chave correspondente a cada letra da entrada
        # e cada key recebe um valor referente à frequencia de cada letra
        letras_freqs[entrada[x]] = freqs

    # letras_freqs[key[0]] = dici[key[0]]

    return letras_freqs


def ordem_freqs(dicio: dict) -> dict:
    """Ordena o dicionário de acordo com a frequencia de cada chave no texto

    Args:
        dicio (dict): um dicionário contendo cada letra
        e sua respectiva frequencia no texto

    Returns:
        dicio_ordem (dict): um dicionário ordenado de acordo com a key (sorted)
        , de argumento x, que representa a tupla de item do dicionário
        , e retona o indice 1 de cada tupla (ou seja x[1])
    """

    # arr_ordem representa a lista de tuplas
    arr_ordem = sorted(dicio.items(), key=lambda x: x[1])
    # dicio_ordem é um dict vazio que vai receber os itens armazenados na tupla
    dicio_ordem = {}

    # esse laço vai iterar sobre os indicies de cada tupla.
    for i in range(len(arr_ordem)):
        # ja esse vai iterar sobre a tupla referente ao indice i(arr_ordem[i])
        for j in arr_ordem[i]:
            # aqui dicio_ordem recebe uma chave referente ao indice 0
            # e essa por sua vez recebe um valor referente ao indice 1
            dicio_ordem[arr_ordem[i][0]] = arr_ordem[i][1]

    # nesse for foi usado o mesmo raciocinio de iteração de matrizes
    # , pois, em tese, essas são estruturas de dados
    # com estruturas de dado dentro, logo uma lista de tuplas é
    # , de certa forma, uma matriz

    return dicio_ordem


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
        dici_copy[new_key] = dici_copy[chaves[0]] + dici_copy[chaves[1]]

        # ordenação de dici_copy
        # para que ele esteja sempre na ordem crescente
        # e as váriaveis nunca sejam confundidas
        dici_copy = ordem_freqs(dici_copy)

        # retida de dici_copy as duas chaves concatenadas
        # dessa forma, a gente evita que as chaves não concatenadas
        # fiquem sempre na frente das somadas
        for j in range(2):
            dici_copy.pop(chaves[j])

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
    keys_alone = obtem_keys_alone(keys)

    # atribui Bits de 0,1 do menor ao maior de acordo com os nós e folhas
    dici = atrubui_bits(dici, keys)

    # verifica se a letra está dentro do nó
    # e atribui à chave o código pertencente aos nós até chegar na folha
    for k in range(len(keys_alone)):
        cod = Bits(0)
        for l in range(len(keys)):
            if keys_alone[k] in keys[l]:
                cod += dici[keys[l]]
        dici_cods[keys_alone[k]] = cod

    return dici_cods


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


def obtem_keys_alone(keys: list, keys_alone: list=[]) -> list:
    """função responsável por retornas as chaves que são apenas letras

    Args:
        keys (list): listas com todas as chaves do meu dicionário
        keys_alone (list, opicional): recebe essas chaves só com uma letra.
        Padrão to [].

    Returns:
        keys_alone (list): lista com as chaves unicas (keys_alone)
    """
    for g in range(len(keys)):
        if len(keys[g]) == 1:
            keys_alone.append(keys[g])

    return keys_alone


def atribui(dici: dict, arquivo: str) -> Bits:
    """é uma função responsável por atribuir à uma variável com um bit vazio
    os códigos das letras nas suas respectivas
    posições em relação ao texto original

    Args:
        dici (dict): dicionário com as chaves e seus respectivos códigos
        arquivo (str): string original para a compactação

    Returns:
        cont_arquivo_comp (bits): a bitstring do arquivo original
    """
    chaves = list(dici.keys())
    cont_arquivo_comp = Bits(0)
    for i in range(len(arquivo)):
        if arquivo[i] in chaves:
            indice = chaves.index(arquivo[i])
            cont_arquivo_comp += dici[chaves[indice]]

    return cont_arquivo_comp


def salva_desc(nome: str, arq: str, tipo_formato: str):
    """reponsável por salvar os dados dos aquivos originais

    Args:
        nome (str): diretório do arquivo
        arq (str): conteúdo do arquivo
    Returns:
        save (ini): salva os dados dos arquivos originais
    """

    dados_arqs = cp
    dados_arqs.read("save.ini", encoding="utf-8")

    nome_banco_dados = nome.lower()

    dados_arqs[nome_banco_dados] = {"nome": arq.lower(), "tipo_formato": tipo_formato}

    with open("save.ini", "x", encoding="utf-8") as save_comps:
        return dados_arqs.write(save_comps)


def compac(arq: str, arquivo_loc: str) -> Bits:
    """
    Responsável por agrupar todas as funções e fazer a compactação de fato

    Args:
        arq (str): conteúdo a ser compactado
        arquivo_loc (str): reponsável por indicar o local do arquivo

    Returns:
        arquivo (mbdk):  arquivo compactado
    """

    freq = frequencias(arq)
    ord = ordem_freqs(freq)
    conc = concat(ord)
    codif = codifica(conc)
    cripto = atribui(codif, arq)

    with open(arquivo_loc, "wb") as comp:
        return cripto.tofile(comp)


def desc(nome: str, form: str, i: int = 1):
    """Descompacta o arquivo

    Args:
        form (str): formato do arquivo original
        nome (str): nome da chave para gravar o arquivo
        dici (str): armazenamento das chaves
        i (int, optional): contador de arquivos existentes. padrão para 0.
    """
    cp.read('save.ini', encoding="utf-8")

    # essa parte é um módulo a parte para o programa rodar no linux
    # pois no windows a função open cria um arquivo diretamente no diretório
    # no qual eu coloquei o nome do arquivo
    nome2 = nome.replace(".huff", "({}){}".format(i, form))
    lista_nome2 = nome2.split("/")
    nome_arquivo = lista_nome2[-1]

    try:
        with open(nome_arquivo, "x", encoding = "UTF-8") as des:
            return des.write(cp[nome].get("nome"))

    except FileExistsError:
        return desc(nome2, form, i+1)


def semi_compac(nome_arquivo: str):
    """faz parte dos proocessos para a compatação do arquivo

    Args:
        nome_arquivo (str): nome do arquivo a ser aberto

    Returns:
        semi_hd: responsável por guardar os dados do arquivo original
    """

    tipo_formato = ".txt"

    with open(nome_arquivo, "r") as conteudo_arq:
        conteudo_arq = conteudo_arq.read()

    nome_arquivo = nome_arquivo.replace(tipo_formato, ".huff")

    compac(conteudo_arq, nome_arquivo)

    # armazena os dados do arquivo original de acordo com a função salva_desc
    semi_hd = salva_desc(nome_arquivo, conteudo_arq, tipo_formato)

    return semi_hd


def erro_import(arq_nome: str, action: str):
    """verifica se o arquivo importado
    para a compactação do arquivo tem uma extensão aceita

    Args:
        arq_nome (str): nome do arquivo
        action (str): ação a ser tomada pelo programa

    Raises:
        ImportError: erro se o arquivo não for aceito pelo programa
    """
    if action == "c":
        if ".txt" not in arq_nome:
            raise ImportError
    elif action == "x":
        if ".huff" not in arq_nome:
            raise ImportError