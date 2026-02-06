from api_client import get_api


# params = {"filter": "code=30491247"}
data = get_api("entity/store")

for store in data["rows"]:
    name = store["name"]
    uuid = store["meta"]["href"].split("/")[-1]
    print(f"{name} - {uuid}")


# ЧР ТТ390 (брак) - 2117cbc2-9f30-11ee-0a80-026e0010b8bf
# Московский выставка - 21e1506b-c29e-11ee-0a80-07e30014ada8
# Внешка Полюстровский - 28fe3de8-be0d-11ef-0a80-1aac000fcf1d
# Маркетплейсы - 3da4fcde-3dcc-11ef-0a80-09dd000a6e84
# ПЛ ТТ390 (брак) - 463dc6c3-be0d-11ef-0a80-07f500102cf1
# Архивный (Конс. Торжковская) - 5dc129d3-b1fe-11ed-0a80-116f0017f2bb
# Сводный Маркеты - 681a7b0d-040c-11f0-0a80-0c2c0012539c
# ПЛ ТТ310 (выставка) - 7c790b8e-42cc-11f0-0a80-1b74000cc2a7
# FBO озон - 8a724246-040c-11f0-0a80-164d0012435e
# ЧР ТТ310 (выставка) - 8cbcce7c-aede-11ee-0a80-0dfd007bd0bc
# Полюстровский - 8d54a9fc-ae55-11ef-0a80-07b6009b8b63
# ЧернаяРечка - 8eecadfd-0367-11ed-0a80-0b430036e29c
# Маркеты ТТ390 - be787264-ec3d-11ef-0a80-1633001e7428
# Инвентаризация - c5ff728d-cf89-11f0-0a80-09ec0014674f
# Московский - d75a77ac-0435-11ed-0a80-0b49000cfab1
# Транзитный - e8151378-8fda-11f0-0a80-17cb0010442f
# Уценка - f3132bd1-affd-11f0-0a80-1bab00205740
