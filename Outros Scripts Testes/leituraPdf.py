import os
import re
import shutil
import pdfplumber
import pandas as pd
from datetime import datetime

# Pastas (mantendo seus caminhos originais)
pasta_entrada = r"C:\Users\fred\Desktop\Pasta Cotação para NH\Fila Arquivo"
pasta_saida = r"C:\Users\fred\Desktop\Pasta Cotação para NH\Saída Arquivo"
pasta_historico = r"C:\Users\fred\Desktop\Pasta Cotação para NH\Histórico"

# Garantir que as pastas existam
os.makedirs(pasta_entrada, exist_ok=True)
os.makedirs(pasta_saida, exist_ok=True)
os.makedirs(pasta_historico, exist_ok=True)


def limpar_numero(valor):
    pass # Logica de negocio removida por seguranca corporativa



def extrair_dados_pdf(caminho_pdf):
    pass # Logica de negocio removida por seguranca corporativa
