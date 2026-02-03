import os
# 1. Корень проекта — вычисляем автоматически
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Основные папки для исходных данных
INPUT_FOLDERS = {
    "TT310_CHR": os.path.join(ROOT_DIR, "File", "TT310_CHR"),
    "TT310_PL": os.path.join(ROOT_DIR, "File","TT310_PL"),
    "STOCK_CHR": os.path.join(ROOT_DIR, "File","STOCK_CHR"),
    "STOCK_PL": os.path.join(ROOT_DIR, "File","STOCK_PL"),
    "FACT_CHR": os.path.join(ROOT_DIR,"File", "FACT_CHR"),
    "FACT_PL": os.path.join(ROOT_DIR, "File","FACT_PL"),
}
# 3. Папка для конвертированных файлов
CONVERTED_FOLDER = os.path.join(ROOT_DIR,"conv_xlsx")

# 4. Расширения файлов
INPUT_EXTENSION = ".xlx"
OUTPUT_EXTENSION = ".xlsx"

CONVERT_PREFIX = "conv_"
