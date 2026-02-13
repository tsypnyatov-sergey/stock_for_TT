import pandas as pd

from reader import read_fact_stock
from api_logic import (
    get_product_by_code,
    get_stock_by_product,
    extract_stocks
)

xlsx_folder = r"C:\Users\SETSY\PycharmProjects\stock_for_TT\File\FACT_PL\_xlsx"

fact_stock = read_fact_stock(xlsx_folder)

print("Товаров в инвентаризации:", len(fact_stock))

result_rows = []

for code, fact_value in fact_stock.items():

    print("\nОбрабатываем:", code)

    product = get_product_by_code(code)

    if not product:
        print("❌ Товар не найден")
        continue

    stock_report = get_stock_by_product(product["meta"]["href"])

    stocks = extract_stocks(stock_report)

    row = {
        "code": code,
        "fact": fact_value,
        **stocks
    }

    result_rows.append(row)

df_result = pd.DataFrame(result_rows)

print("\nИТОГ:")
print(df_result)
