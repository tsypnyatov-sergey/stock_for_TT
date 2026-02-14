import os
import dotenv
dotenv.load_dotenv()
# 1. Корень проекта — вычисляем автоматически
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

API_BASE_URL = "https://api.moysklad.ru/api/remap/1.2"
API_TOKEN = os.getenv("TOKEN")

TT310_CHR= "8cbcce7c-aede-11ee-0a80-0dfd007bd0bc"
TT310_PL="7c790b8e-42cc-11f0-0a80-1b74000cc2a7"
STOCK_CHR= "8eecadfd-0367-11ed-0a80-0b430036e29c"
STOCK_PL= "8d54a9fc-ae55-11ef-0a80-07b6009b8b63"



# 2. Основные папки для исходных данных
INPUT_FOLDERS = {
    "FACT_CHR": os.path.join(ROOT_DIR,"File", "FACT_CHR","_xlsx"),
    "FACT_PL": os.path.join(ROOT_DIR, "File","FACT_PL","_xlsx"),
}
# 3. Папка для конвертированных файлов
CONVERTED_FOLDER = os.path.join(ROOT_DIR,"conv_xlsx")

# 4. Расширения файлов
INPUT_EXTENSION = ".xlx"
OUTPUT_EXTENSION = ".xlsx"

CONVERT_PREFIX = "conv_"

