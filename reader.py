import pandas as pd
import glob
import os


def get_product_codes(xlsx_folder: str) -> list:
    # Игнорируем временные файлы Excel
    xlsx_files = [f for f in glob.glob(os.path.join(xlsx_folder, "*.xlsx"))
                  if not os.path.basename(f).startswith("~$")]

    codes = set()

    for file_path in xlsx_files:
        df = pd.read_excel(file_path, header=None ,dtype=str) # читаем всё как строки
        header_row_idx = None

        for idx,row in df.iterrows():
            if any (str(cell).lower() in ["код"] for cell in row):
                header_row_idx = idx
                break

        if header_row_idx is not None:
            df.columns = df.iloc[header_row_idx] #делаем эту строку заголовком
            df= df.iloc[header_row_idx+2:] #берем все строки после заголовка начиная с третьей
            #определяем столбец с кодами
            code_column= None
            for col_name in df.columns:
                if str(col_name).lower()== "код":
                    code_column = col_name
                    break
            if code_column :
                valid_codes = df[code_column].dropna().astype(str)
                valid_codes = valid_codes[valid_codes.str.isdigit()]
                codes.update(valid_codes.tolist())

    return list(codes)


# Использование
xlsx_folder = r"C:\Users\SETSY\PycharmProjects\stock_for_TT\File\FACT_PL\_xlsx"
codes = get_product_codes(xlsx_folder)
print("Коды товаров для запроса:", codes)
