from pathlib import Path

BASE_PATH = Path(__file__).parent.absolute()
DATA_PATH = BASE_PATH / "data"
INPUT_PATH = DATA_PATH / "input"
OUTPUT_PATH = DATA_PATH / "output"
OUTPUT_LOGS_PATH = OUTPUT_PATH / "logs"
OUTPUT_DATA_PATH = OUTPUT_PATH / "data"

for path in (DATA_PATH, INPUT_PATH, OUTPUT_PATH, OUTPUT_LOGS_PATH, OUTPUT_DATA_PATH):
    if not path.exists():
        path.mkdir(parents=True)
