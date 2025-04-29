import os
import json

ARQUIVO = "alunos.json"

# Ler os dados do arquivo JSON
def ler_dados():
    try:
        if os.path.exists(ARQUIVO) and os.path.getsize(ARQUIVO) > 0:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        pass  # Se o arquivo estiver corrompido ou não puder ser lido, ignora e retorna lista vazia

    # Se não existir, estiver vazio ou inválido
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)
    return []

# Salvar dados no arquivo JSON
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
