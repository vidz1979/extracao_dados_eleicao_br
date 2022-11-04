# Extração de dados de eleição do Brasil 🇧🇷

Este pacote de ferramentas busca facilitar a extração de dados que não foram disponibilizados de forma automática pela apuração.

## Download dos arquivos do TSE

Para realizar o download dos arquivos, vá até o site [Dados Abertos do TSE](https://dadosabertos.tse.jus.br/dataset/).

Procure por "arquivos transmitidos para totalização". No caso de 2022, o link é: https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao

Os arquivos são disponibilizados por estado, um para cada turno.

Descompacte os arquivos na data `data/input`.

## Instalação das dependências

`pip install -r requirements.txt`

## Descompressão dos logs de urna

`python unzip_logs.py -h`

```
usage: unzip_logs.py [-h] [--inputdir INPUTDIR] [--outputdir OUTPUTDIR]

Busca recursivamente arquivos .logjez no diretorio informado e descompacta o arquivo dentro do diretorio de saida.

options:
  -h, --help            show this help message and exit
  --inputdir INPUTDIR, -i INPUTDIR
                        Diretório raiz para busca
  --outputdir OUTPUTDIR, -o OUTPUTDIR
                        Arquivo de saída
```

Para executar o processo pegando do diretório de input padrão (`data/input`) e saída padrão (`data/output/logs`).

`python unzip_logs.py`

## Extração dos dados da urna

`python extract_dados_urna.py -h`

```
usage: extract_dados_urna.py [-h] [--inputdir INPUTDIR] [--output OUTPUT]

Extrai dados da urna a partir de arquivos no diretorio (./data/outputs/logs).

options:
  -h, --help            show this help message and exit
  --inputdir INPUTDIR, -i INPUTDIR
                        Diretório de entrada (logs)
  --output OUTPUT, -o OUTPUT
                        Arquivo de saída
```

Para executar o processo pegando do diretório de input padrão (`data/output/logs`) e saída padrão (`data/output/data`).

`python extract_dados_urna.py`

## Saída

Os dados extraídos dos logs da urna de cada arquivo são armazenados em arquivo .csv com os seguintes campos:

- Arquivo: o arquivo de onde a informação foi extraída
- Município
- Zona Eleitoral
- Local de Votação
- Seção Eleitoral
- Versão da aplicação
- Turno da UE
- Identificação do Modelo de Urna
- Fase da UE
- Serial de votação da MV

```
Arquivo,Município,Zona Eleitoral,Local de Votação,Seção Eleitoral,Versão da aplicação,Turno da UE,Identificação do Modelo de Urna,Fase da UE,Serial de votação da MV
/Users/junior/dev/eleicoes/data/output/logs/bu_imgbu_logjez_rdv_vscmr_2022_1t_AL__o00406-2871100180246.txt,28711,0018,1198,0246,8.26.0.0 - Onça-pintada,1º turno,UE2020,Oficial,9083DE64
/Users/junior/dev/eleicoes/data/output/logs/bu_imgbu_logjez_rdv_vscmr_2022_1t_AL__o00406-2837100080056.txt,28371,0008,1074,0056,8.26.0.0 - Onça-pintada,1º turno,UE2020,Oficial,F276ED66
/Users/junior/dev/eleicoes/data/output/logs/bu_imgbu_logjez_rdv_vscmr_2022_1t_AL__o00406-2757000440008.txt,27570,0044,1040,0008,8.26.0.0 - Onça-pintada,1º turno,UE2009,Oficial,7BE138E8
/Users/junior/dev/eleicoes/data/output/logs/bu_imgbu_logjez_rdv_vscmr_2022_1t_AL__o00406-2703000480149.txt,27030,0048,1210,0149,8.26.0.0 - Onça-pintada,1º turno,UE2009,Oficial,9E16CD72
```
