import requests
from config import API_TOKEN, API_BASE_URL


headers = {
    "authorization": f"Bearer {API_TOKEN}",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json",
}

"""
Универсальный GET-запрос к API МойСклад
path: 'entity/product', 'report/stock/all' и т.д.
"""
def get_api(path:str, params:dict | None=None):
    url = f"{API_BASE_URL}/{path.lstrip('/')}"
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

