import pandas as pd
import os
from datetime import datetime

base_path = r"\\10.1.1.106\Analytics2\Clinical\Pasta Log IA - Sem Histórico"
for i in range(1, 6):
    old_name = os.path.join(base_path, f"log.txt.{i}")
    new_name = os.path.join(base_path, f"log{i}.txt")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renomeado: {old_name} → {new_name}")
    else:
        print(f"Arquivo não encontrado: {old_name}")

file_names = ["log.txt"] + [f"log{i}.txt" for i in range(1, 6)]
arquivos_validos = [os.path.join(
    base_path, name) for name in file_names if os.path.exists(os.path.join(base_path, name))]
