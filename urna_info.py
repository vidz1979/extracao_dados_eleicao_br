from settings import ATRIBUTOS_BUSCA


def get_urna_info(file):
    info = {}
    cont = 0
    with open(file, "r", encoding="ISO-8859-1") as fp:
        exit = False
        for l_no, line in enumerate(fp):
            cont += 1
            for atributo in ATRIBUTOS_BUSCA:
                if atributo in line:
                    # busca 5a coluna do log (mensagem)
                    msg = line.split("\t")[4]
                    info[atributo] = msg.split(": ")[1]
                    if atributo == "Serial de votação da MV":
                        info[atributo] = info[atributo].split(" ")[0]

                    # se encontrou todos os atributos, para de procurar no arquivo
                    # TODO verificar se os atributos podem sofrer alteração ao longo arquivo, se sim deixar buscar em todo arquivo
                    if len(info.keys()) == len(ATRIBUTOS_BUSCA):
                        exit = True

                    # nao busca mais atributos na mesma linha
                    break
            if exit:
                break

    return info
