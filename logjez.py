import glob, os
import random, string
import shutil
import py7zr
import tempfile
from urna_info import get_urna_info
from zipfile import ZipFile


def get_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def search_logjez(dict_writer, last_file, folder_path=None, zip_path=None):
    if zip_path:
        print("Buscando arquivos .logjez no arquivo zip")
        print("Arquivo:", zip_path)

        zip_file = ZipFile(zip_path)

        dir_logjez = [f for f in zip_file.namelist() if f.endswith(".logjez")]
    else:
        print("Buscando arquivos .logjez no diretório informado")
        print("Diretório dos logs:", folder_path)

        os.chdir(folder_path)
        dir_logjez = glob.glob("*.logjez")

    qtd_total = len(dir_logjez)
    print("Quantidade total:", qtd_total)

    dir_logjez = [f for f in dir_logjez if f > last_file]
    dir_logjez.sort()
    qtd_faltantes = len(dir_logjez)
    qtd_processada = qtd_total - qtd_faltantes
    print("Quantidade processada recuperada:", qtd_processada)

    if qtd_faltantes:
        print("Quantidade a processar:", qtd_faltantes)
        qtd_erro = 0

        for file in dir_logjez:
            output_path = os.path.join(tempfile.gettempdir(), get_random_string(20))

            if zip_path:
                # zip_file.open vai descompactar o arquivo .logjez diretamente do .zip para a memoria
                f = zip_file.open(file)
            else:
                # se o arquivo .logjez vier de uma pasta, somente passar o nome do arquivo
                f = file

            logjez_file = py7zr.SevenZipFile(f, mode="r")
            logjez_file.extractall(path=output_path)
            logjez_file.close()

            log_file = os.path.join(output_path, "logd.dat")
            if os.path.exists(log_file):
                qtd_processada += 1
                info = get_urna_info(log_file)
                if zip_path:
                    info["Diretório"] = os.path.split(os.path.splitext(zip_path)[0])[-1]
                else:
                    info["Diretório"] = os.path.split(folder_path)[-1]
                info["Arquivo"] = file
                dict_writer.writerow(info)
                shutil.rmtree(output_path)
            else:
                qtd_erro += 1
                print(file, ":", log_file, "nao encontrado")

        print("Quantidade processada:", qtd_processada)
        if qtd_erro:
            print("Quantidade erros:", qtd_erro)

    print("Processamento do diretório completo.")
