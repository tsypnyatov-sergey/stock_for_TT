import pandas as pd
import glob
import os


def read_fact_stock(xlsx_folder: str) -> dict:

    xlsx_files = [f for f in glob.glob(os.path.join(xlsx_folder, "*.xlsx"))
                  if not os.path.basename(f).startswith("~$")]

    fact_data = {}

    for file_path in xlsx_files:

        print("\nФайл:", file_path)

        df = pd.read_excel(file_path, header=None, dtype=str)

        header_row_idx = None

        # Ищем строку заголовков
        for idx, row in df.iterrows():
            if any(str(cell).strip().lower() == "код" for cell in row):
                header_row_idx = idx
                break

        if header_row_idx is None:
            print("Заголовок не найден")
            continue

        print("Строка заголовка:", header_row_idx)

        header_row = df.iloc[header_row_idx]

        code_col_idx = None
        fact_col_idx = None

        # Ищем номера колонок
        for i, cell in enumerate(header_row):
            cell_value = str(cell).strip().lower()

            if cell_value == "код":
                code_col_idx = i

            if cell_value == "фактический остаток":
                fact_col_idx = i

        print("Колонка Код:", code_col_idx)
        print("Колонка Факт:", fact_col_idx)

        if code_col_idx is None or fact_col_idx is None:
            print("Нужные колонки не найдены")
            continue

        # Берём строки после заголовка
        data_rows = df.iloc[header_row_idx + 1:]

        for _, row in data_rows.iterrows():

            code = str(row[code_col_idx]).strip()

            if not code.isdigit():
                continue

            fact_value = row[fact_col_idx]

            fact_data[code] = fact_value

    return fact_data


