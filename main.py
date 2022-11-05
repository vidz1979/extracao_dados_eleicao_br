import argparse
import os
import csv
from settings import OUTPUT_PATH, HEADERS
from logjez import search_logjez
from urna_info import ATRIBUTOS_BUSCA


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Busca arquivos .logjez e gera arquivo de informações da urna eletrônica.Especifique um diretório ou um arquivo zip contendo arquivos .logjez."
    )
    parser.add_argument(
        "--folder",
        "-f",
        help="Diretório contendo .logjez",
    )
    parser.add_argument(
        "--zip",
        "-z",
        help="Arquivo zip contendo .logjez",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Arquivo de saída. Utiliza por padrão o nome do diretório.",
    )
    args = parser.parse_args()

    if not args.folder and not args.zip:
        print("Informe o diretório ou arquivo zip.")
        exit()

    if args.folder and args.zip:
        print("Informe somente o diretório ou somente o arquivo zip.")
        exit()

    if not args.output:
        zip_name = os.path.splitext(args.zip)[0]
        args.output = os.path.split(args.folder or zip_name)[-1]

    # preenche extensao se necessario
    if not args.output.endswith(".csv"):
        args.output += ".csv"

    # caso nao tenha sido informado o diretorio de saida, utilizar o diretorio de saida de dados padrao
    if os.path.split(args.output)[0] == "":
        args.output = os.path.join(OUTPUT_PATH, args.output)

    if os.path.exists(args.output):
        with open(args.output, "rb") as f:
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b"\n":
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode('latin-1')
            last_file = last_line.split(",")[1]

        output_file = open(args.output, "a", newline="")
        dict_writer = csv.DictWriter(output_file, HEADERS)
    else:
        last_file = ""
        output_file = open(args.output, "w", newline="")
        dict_writer = csv.DictWriter(output_file, HEADERS)
        dict_writer.writeheader()

    if args.folder:
        search_logjez(dict_writer, last_file, folder_path=args.folder)
    else:
        search_logjez(dict_writer, last_file, zip_path=args.zip)
