import os

import converter
from config import INPUT_FOLDERS

converted_files = []

for folder_name, folder_path in INPUT_FOLDERS.items():
    os.makedirs(folder_path, exist_ok=True)
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".xls"):
            input_path = os.path.join(folder_path, file_name)

            output_file = converter.conv_xls_to_xlsx(input_path, output_dir=os.path.join(folder_path, "_xlsx"))

            converted_files.append(output_file)

print(converted_files)
