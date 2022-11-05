# Extração de dados de eleição do Brasil 🇧🇷

Este pacote de ferramentas busca facilitar a extração de dados sobre informações das urnas que não foram disponibilizados de forma automática pela apuração.

## Download dos arquivos do TSE

Para realizar o download dos arquivos, vá até o site [Dados Abertos do TSE](https://dadosabertos.tse.jus.br/dataset/).

Procure por "arquivos transmitidos para totalização". No caso de 2022, o link é: https://dadosabertos.tse.jus.br/dataset/resultados-2022-arquivos-transmitidos-para-totalizacao

Os arquivos são disponibilizados por estado, um para cada turno.

> **_DICA:_** Não é necessário descompactar o arquivo zip, o script lê os arquivos .logjez diretamente! Se já possuir os arquivos .logjez descompactado, informe a pasta.

## Instalação das dependências

`pip install -r requirements.txt`

## Descompressão dos logs de urna

`python main.py -h`

```
usage: main.py [-h] [--folder FOLDER] [--zip ZIP] [--output OUTPUT]

Busca arquivos .logjez e gera arquivo de informações da urna eletrônica. Especifique um diretório ou um arquivo zip contendo arquivos .logjez.

options:
  -h, --help            show this help message and exit
  --folder FOLDER, -f FOLDER
                        Diretório contendo .logjez
  --zip ZIP, -z ZIP     Arquivo zip contendo .logjez
  --output OUTPUT, -o OUTPUT
                        Arquivo de saída. Utiliza por padrão o nome do diretório/zip.
```

Para executar o processo pegando de um arquivo zip (recomendado!):

`python main.py -z 2022_2t_RR.zip`

Para executar o processo pegando de uma pasta:

`python main.py -f 2022_2t_RR`

## Saída

Os dados extraídos dos logs da urna de cada arquivo são armazenados em arquivo .csv com os seguintes campos:

- Diretório: pasta ou arquivo zip de origem
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
Diretório,Arquivo,Município,Zona Eleitoral,Local de Votação,Seção Eleitoral,Versão da aplicação,Turno da UE,Identificação do Modelo de Urna,Fase da UE,Serial de votação da MV
2022_2t_RR,o00407-0300000040011.logjez,03000,0004,1015,0011,8.26.0.0 - Onça-pintada,1º turno,UE2015,Oficial,5A434CF5
2022_2t_RR,o00407-0300000040012.logjez,03000,0004,1015,0012,8.26.0.0 - Onça-pintada,1º turno,UE2015,Oficial,D9BEEE10
2022_2t_RR,o00407-0300000040013.logjez,03000,0004,1015,0013,8.26.0.0 - Onça-pintada,1º turno,UE2015,Oficial,11549FFC
2022_2t_RR,o00407-0300000040014.logjez,03000,0004,1023,0014,8.26.0.0 - Onça-pintada,1º turno,UE2020,Oficial,A164149A
2022_2t_RR,o00407-0300000040015.logjez,03000,0004,1023,0015,8.26.0.0 - Onça-pintada,1º turno,UE2020,Oficial,0E926E87
2022_2t_RR,o00407-0300000040016.logjez,03000,0004,1031,0016,8.26.0.0 - Onça-pintada,1º turno,UE2020,Oficial,F7C04159
...
```

## Contribuições

Estou trabalhando para juntar exportar o CSV, mas a quantidade de dados é enorme. Se alguém tiver mais informações ou contribuições, mande PR.
