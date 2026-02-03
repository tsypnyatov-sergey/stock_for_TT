import os

from process_folders import folder_path

files_to_analyze = {}

for xls_file in os.listdir(folder_path):
    if xls_file.lower().endswith(".xls"):
        name_without_ext = os.path.splitext(xls_file)[0]
        xlsx_path = os.path.join(folder_path,"_xlsx",f"{name_without_ext}.xlsx")
        if os.path.exists(xlsx_path):
            files_to_analyze[name_without_ext] = xlsx_path

print(files_to_analyze)