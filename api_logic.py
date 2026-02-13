from api_client import get_api
from config import TT310_CHR, TT310_PL, STOCK_CHR, STOCK_PL

def get_product_by_code(code:str):
    params = {"filter": f"code={code}"}
    data = get_api("entity/product", params = params)

    if not data["rows"]:
        return None

    return data["rows"][0]

def get_stock_by_product(product_href: str):
    params = {"filter": f"product={product_href}"}
    return get_api("report/stock/bystore",params = params)


def extract_stocks(stock_report):

    result = {
        "TT310_CHR": 0,
        "TT310_PL": 0,
        "STOCK_CHR": 0,
        "STOCK_PL": 0,
    }

    rows = stock_report.get("rows", [])

    if not rows:
        return result

    stores = rows[0].get("stockByStore", [])

    for store in stores:

        store_href = store["meta"]["href"]
        store_uuid = store_href.split("/")[-1]

        stock_value = store.get("stock", 0)

        if store_uuid == TT310_CHR:
            result["TT310_CHR"] = stock_value

        elif store_uuid == TT310_PL:
            result["TT310_PL"] = stock_value

        elif store_uuid == STOCK_CHR:
            result["STOCK_CHR"] = stock_value

        elif store_uuid == STOCK_PL:
            result["STOCK_PL"] = stock_value

    return result