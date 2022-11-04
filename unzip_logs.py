import argparse
import settings
import py7zr
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Busca recursivamente arquivos .logjez no diretorio informado e descompacta o arquivo dentro do diretorio de saida."
    )
    parser.add_argument(
        "--inputdir",
        "-i",
        help="Diretório raiz para busca",
        default=settings.INPUT_PATH,
    )
    parser.add_argument(
        "--outputdir",
        "-o",
        help="Arquivo de saída",
        default=settings.OUTPUT_LOGS_PATH,
    )
    args = parser.parse_args()

    print("Buscando arquivos de log no diretório informado")
    print("Diretório raiz:", args.inputdir)

    for root, dirs, files in os.walk(args.inputdir):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".logjez"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(
                    args.outputdir,
                    os.path.basename(root) + "__" + os.path.splitext(file)[0] + ".txt",
                )

                print("Descomprimindo arquivo:", input_file, "->", output_file)

                archive = py7zr.SevenZipFile(input_file, mode="r")
                archive.extractall(path="/tmp")
                archive.close()
                os.replace(
                    os.path.join("/tmp/logd.dat"),
                    output_file,
                )
