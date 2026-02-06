
from api_client import get_api
from reader import get_product_codes

# params = {"filter": "code=30491247"}
data = get_api("entity/store")

for store in data["rows"]:
    name = store["name"]
    uuid = store["meta"]["href"].split("/")[-1]
    print(f"{name} - {uuid}")



xlsx_folder = r"C:\Users\SETSY\PycharmProjects\stock_for_TT\File\FACT_PL\_xlsx"
codes = get_product_codes(xlsx_folder)

print("Коды товаров для запроса:", codes)
# берём UUID товара
# if data["rows"]:
#     uuid = data["rows"][0]["id"]
# else:
#     raise ValueError("Товар с таким кодом не найден")
#
# params = {"filter": f"assortment.id={uuid}"}
# stock_data = get_api("report/stock/all", params=params)


