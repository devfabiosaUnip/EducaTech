### onde terão as funções de ler, escrever a manipular o json

import json;
import os;

ARQUIVO = "data.json";

def ler_dados():
    from models.aluno import Aluno
    if os.path.exists(ARQUIVO):              #  Verifica se o arquivo existe
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)              #  Carrega o JSON do arquivo e transforma em lista/dict
    return []            

def salvar_dados(dados):
    from models.aluno import Aluno
    with open (ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)