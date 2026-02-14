import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

from config import INPUT_FOLDERS
from reader import read_fact_stock
from api_logic import get_product_by_code, get_stock_by_product, extract_stocks

# -----------------------------
# Подключение к Google Sheets
# -----------------------------
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
client = gspread.authorize(creds)

# Открываем уже созданную Google таблицу
spreadsheet_name = "Сравнение стоков"
spreadsheet = client.open(spreadsheet_name)

# -----------------------------
# Проходим по всем подпапкам из конфига
# -----------------------------
for folder_name, folder_path in INPUT_FOLDERS.items():
    print(f"\nОбрабатываем папку: {folder_name} ({folder_path})")

    # 1️⃣ Читаем файлы с фактическим остатком
    fact_stock = read_fact_stock(folder_path)
    print("Товаров в инвентаризации:", len(fact_stock))

    if fact_stock.empty:
        print(f"⚠️ Нет данных в папке {folder_name}")
        continue

    result_rows = []

    # 2️⃣ Обрабатываем каждый товар
    for _, row in fact_stock.iterrows():
        code = row["Код"]
        name = row["Наименование"]
        fact_value = row["Посчитано"]

        #print(f"\nОбрабатываем: {code}")

        product = get_product_by_code(code)
        if not product:
            print(f"❌ Товар не найден: {code}")
            continue

        stock_report = get_stock_by_product(product["meta"]["href"])
        stocks = extract_stocks(stock_report)

        result_row = {
            "Код": code,
            "Наименование": name,
            "Посчитано": fact_value,
            **stocks
        }
        result_rows.append(result_row)

    df_result = pd.DataFrame(result_rows)

    #Добавляем пустые колонки
    if "STOCK_CHR" in df_result.columns and "STOCK_PL" in df_result.columns:
        idx_chr = df_result.columns.get_loc("STOCK_CHR")+1
        idx_pl = df_result.columns.get_loc("STOCK_PL")+2

        df_result.insert(idx_chr, "FACT_CHR", "")
        df_result.insert(idx_pl, "FACT_PL", "")


    # -----------------------------
    # Работа с листом Google Sheets
    # -----------------------------
    try:
        worksheet = spreadsheet.worksheet(folder_name)  # ищем лист с названием папки
        worksheet.clear()  # очищаем, если есть
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=folder_name, rows="100", cols="20")  # создаём новый лист

    # Подготовка данных
    data_for_sheets = [df_result.columns.tolist()] + df_result.to_numpy().tolist()
    worksheet.update(data_for_sheets)

    # Перенос текста для колонки "Наименование"
    worksheet.format("B:B", {"wrapStrategy": "WRAP"})
    body = {
        "requests": [
            {
                "autoResizeDimensions": {
                    "dimensions": {
                        "sheetId": worksheet.id,
                        "dimension": "COLUMNS",
                        "startIndex": 1,  # колонка B → индекс 1
                        "endIndex": 2
                    }
                }
            }
        ]
    }

    spreadsheet.batch_update(body)

    print(f"✅ Лист '{folder_name}' обновлён в Google таблице '{spreadsheet_name}'")

print("\nВсе папки обработаны.")
