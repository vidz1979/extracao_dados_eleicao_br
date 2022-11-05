from pathlib import Path

BASE_PATH = Path(__file__).parent.absolute()
OUTPUT_PATH = BASE_PATH / "output"

for path in [OUTPUT_PATH]:
    if not path.exists():
        path.mkdir(parents=True)

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

HEADERS = ["Diretório", "Arquivo"] + ATRIBUTOS_BUSCA
