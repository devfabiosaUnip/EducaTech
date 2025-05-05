from cryptografia.seguranca import criptografar, descriptografar
from services.json_service import carregar_dados, salvar_dados
from utils.helpers import gerar_RA
from models.pessoa import Pessoa
from cryptography.fernet import InvalidToken
import bcrypt
import re
import json
import webbrowser


CAMINHO_ARQUIVO = "dados/alunos.json"
CAMINHO_CONTEUDO = "dados/conteudo.json"

class Aluno(Pessoa):
    

    @staticmethod
    def validar_cpf(cpf):
        return bool(re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf))

    @staticmethod
    def validar_email(email):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @classmethod
    def cadastrar(cls):
        print("\n=== Cadastro de Aluno ===")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        if not cls.validar_cpf(cpf):
            print("CPF inválido.")
            return
        email = input("Email: ")
        if not cls.validar_email(email):
            print("Email inválido.")
            return
        senha = input("Senha: ")
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        telefone = input("Telefone: ")

        documentos = {}
        doc_opcional = input("Deseja adicionar RG/CNH? (s/n): ").lower()
        if doc_opcional == "s":
            documentos["RG"] = input("RG: ")
            documentos["CNH"] = input("CNH: ")

        alunos = carregar_dados(CAMINHO_ARQUIVO)
        for aluno in alunos:
            try:
                if descriptografar(aluno["cpf"]) == cpf:
                    print("Aluno já cadastrado com este CPF.")
                    return
            except InvalidToken:
                print("Erro na descriptografia dos dados.")
                return

        novo_aluno = {
            "nome": criptografar(nome),
            "data_nascimento": criptografar(data_nascimento),
            "cpf": criptografar(cpf),
            "email": criptografar(email),
            "senha": senha_hash.decode('utf-8'),
            "telefone": criptografar(telefone),
            "RA": gerar_RA(),
            "documentos": {k: criptografar(v) for k, v in documentos.items()},
            "rendimento": {"media": "00", "moda": "00", "mediana": "00"},
            "aulas": {}  # Inicialmente vazio, será preenchido por conteúdos aprovados
        }

        alunos.append(novo_aluno)
        salvar_dados(CAMINHO_ARQUIVO, alunos)
        print("Cadastro realizado com sucesso!")

    @classmethod
    def login(cls):
        print("\n=== Login do Aluno ===")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        alunos = carregar_dados(CAMINHO_ARQUIVO)
        for aluno in alunos:
            try:
                if descriptografar(aluno["cpf"]) == cpf:
                    senha_hash = aluno["senha"].encode('utf-8')
                    if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
                        print("Login bem-sucedido.")
                        cls.painel_aluno(aluno)
                        return
                    else:
                        print("Senha incorreta.")
                        return
            except InvalidToken:
                print("Erro na descriptografia dos dados.")
                return

        print("CPF não encontrado.")

    @classmethod
    def painel_aluno(cls, dados_aluno):
        while True:
            print(f"\n=== Painel do Aluno: {descriptografar(dados_aluno['nome'])} ===")
            print("1 - Ver meus dados")
            print("2 - Ver rendimento")
            print("3 - Ver conteúdo das matérias")
            print("0 - Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("\n--- Meus Dados ---")
                for chave, valor in dados_aluno.items():
                    if chave == "documentos":
                        print("Documentos:")
                        for doc_k, doc_v in valor.items():
                            try:
                                print(f"  {doc_k}: {descriptografar(doc_v)}")
                            except InvalidToken:
                                print(f"  {doc_k}: Erro ao descriptografar")
                    else:
                        try:
                            print(f"{chave}: {descriptografar(valor) if isinstance(valor, str) else valor}")
                        except InvalidToken:
                            print(f"{chave}: Erro ao descriptografar")

            elif escolha == "2":
                print("\n--- Rendimento ---")
                rendimento = dados_aluno.get('rendimento', {'media': 'N/A', 'moda': 'N/A', 'mediana': 'N/A'})
                print(f"Média: {rendimento['media']}")
                print(f"Moda: {rendimento['moda']}")
                print(f"Mediana: {rendimento['mediana']}")

            elif escolha == "3":
                print("\n--- Conteúdo das matérias ---")
                try:
                    with open(CAMINHO_CONTEUDO, 'r', encoding='utf-8') as f:
                        conteudos = json.load(f)
                        for conteudo in conteudos:
                            if conteudo.get("status") == "aprovado":
                                print(f"Matéria: {conteudo['materia']}")
                                print(f"  Título: {conteudo['titulo']}")
                                print(f"  Descrição: {conteudo['descricao']}")
                                print(f"  Conteúdo: {conteudo['conteudo']}")
                                print("-" * 30)
                                webbrowser.open("https://www.youtube.com/@JJOMEGA");
                
                except FileNotFoundError:
                    print("Arquivo de conteúdo não encontrado.")
                except json.JSONDecodeError:
                    print("Erro ao ler o conteúdo.")

            elif escolha == "0":
                print("Saindo do painel do aluno...")
                break
            else:
                print("Opção inválida. Tente novamente.")
