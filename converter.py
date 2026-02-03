import os

import pandas as pd


def conv_xls_to_xlsx(input_path, output_dir=None):
    # 1. Если output_dir не указан, берем ту же папку, где исходник
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(input_path), "_xlsx")
    # Создаем папку, если ее еще нет
    os.makedirs(output_dir, exist_ok=True)

    # 3. Получаем имя файла без пути
    base_name = os.path.basename(input_path)
    # 4. Убираем расширение .xls
    name_without_ext = os.path.splitext(base_name)[0]
    # 5. Создаем новое имя с префиксом и расширением
    new_name = f"{name_without_ext}.xlsx"
    # 6. Полный путь к новому файлу
    output_path = os.path.join(output_dir, new_name)

    # Конвертация
    df = pd.read_excel(input_path)
    df.to_excel(output_path, index=False, engine="openpyxl")

    return output_path
