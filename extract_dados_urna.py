import settings
import os
import csv
import argparse

ATRIBUTOS_BUSCA = [
    "Município",
    "Zona Eleitoral",
    "Local de Votação",
    "Seção Eleitoral",
    "Versão da aplicação",
    "Turno da UE",
    "Identificação do Modelo de Urna",
    "Fase da UE",
    "Serial de votação da MV",
]

HEADERS = ["Arquivo"] + ATRIBUTOS_BUSCA


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

    info["Arquivo"] = file
    return info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extrai dados da urna a partir de arquivos no diretorio (./data/outputs/logs)."
    )
    parser.add_argument(
        "--inputdir",
        "-i",
        help="Diretório de entrada (logs)",
        default=settings.OUTPUT_LOGS_PATH,
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Arquivo de saída",
        default="dados_urnas.csv",
    )
    args = parser.parse_args()

    # preenche extensao se necessario
    if not args.output.endswith(".csv"):
        args.output += ".csv"

    # caso nao tenha sido informado o diretorio de saida, utilizar o diretorio de saida de dados padrao
    if os.path.split(args.output)[0] == "":
        args.output = os.path.join(settings.OUTPUT_DATA_PATH, args.output)

    print("Extraindo dados dos arquivos de log")
    print("Diretório de entrada (logs):", args.inputdir)

    with open(args.output, "w") as f:
        w = csv.DictWriter(f, HEADERS)
        w.writeheader()

        for file in os.listdir(args.inputdir):
            try:
                info = get_urna_info(os.path.join(args.inputdir, file))
                print("Lendo arquivo de log:", os.path.join(args.inputdir, file))
                w.writerow(info)
            except IsADirectoryError:
                print(f"Ignorando: {file} é um diretório.")
                continue

    print("Arquivo de saída:", args.output)
