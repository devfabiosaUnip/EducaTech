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
        if input("Deseja adicionar RG/CNH? (s/n): ").lower() == "s":
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
            "aulas": []  # Apenas aulas que o aluno tem acesso
        }

        alunos.append(novo_aluno)
        salvar_dados(CAMINHO_ARQUIVO, alunos)
        print("Cadastro realizado com sucesso!")

    @classmethod
    def login(cls):
        print("\n=== Login do Aluno ===")
        email = input("email: ")
        senha = input("Senha: ")

        alunos = carregar_dados(CAMINHO_ARQUIVO)
        for aluno in alunos:
            try:
                if descriptografar(aluno["email"]) == email:
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

        print("Aluno não encontrado.")

    @classmethod
    def painel_aluno(cls, dados_aluno):
        while True:
            print(f"\n=== Painel do Aluno: {descriptografar(dados_aluno['nome'])} ===")
            print("1 - Ver meus dados")
            print("2 - Ver rendimento")
            print("3 - Ver conteúdo das matérias")
            print("4 - Explorar módulos e aulas")
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

                    if not dados_aluno.get("aulas"):
                        print("Nenhuma aula atribuída ao seu perfil ainda.")
                        continue

                    for conteudo in conteudos:
                        if conteudo.get("status") == "aprovado" and conteudo.get("id") in dados_aluno.get("aulas", []):
                            print(f"Matéria: {conteudo.get('materia', 'N/A')}")
                            print(f"  Título: {conteudo.get('titulo', 'N/A')}")
                            print(f"  Descrição: {conteudo.get('descricao', 'N/A')}")
                            print(f"  Conteúdo: {conteudo.get('conteudo', 'N/A')}")
                            print("-" * 30)

                except FileNotFoundError:
                    print("Arquivo de conteúdo não encontrado.")
                except json.JSONDecodeError:
                    print("Erro ao ler o conteúdo.")

            elif escolha == "4":
                cls.explorar_modulos_e_aulas(dados_aluno)

            elif escolha == "0":
                print("Saindo do painel do aluno...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    @classmethod
    def explorar_modulos_e_aulas(cls, dados_aluno):
        modulo_selecionado = "Módulo 1"
        aulas_modulo = [{
            "titulo": "Tipos e Variáveis",
            "link_video": "https://youtu.be/FhMtGkcnYKg",
            "link_quiz": "https://kahoot.it/challenge/08265274?challenge-id=cb8bf36c-1e5d-442a-b615-f0c245f266c5_1747874782012"
        }]

        print(f"\n=== Aulas do módulo '{modulo_selecionado}' ===")
        for i, aula in enumerate(aulas_modulo, 1):
            print(f"{i} - {aula.get('titulo', '[sem título]')}")

        escolha_aula = input("Escolha uma aula pelo número (ou 0 para sair): ").strip()
        if escolha_aula == "0":
            return
        if not escolha_aula.isdigit() or int(escolha_aula) < 1 or int(escolha_aula) > len(aulas_modulo):
            print("Opção inválida.")
            return

        aula_selecionada = aulas_modulo[int(escolha_aula) - 1]

        print("\nEscolha a opção para a aula:")
        print("1 - Quizz")
        print("2 - Videoaula")
        escolha_opcao = input("Opção: ").strip()

        if escolha_opcao == "1":
            quizz_url = aula_selecionada.get("link_quiz")
            if quizz_url:
                print("Abrindo quizz no navegador padrão...")
                webbrowser.open(quizz_url)
            else:
                print("Quizz não disponível para esta aula.")
        elif escolha_opcao == "2":
            video_url = aula_selecionada.get("link_video")
            if video_url:
                print("Abrindo videoaula no navegador padrão...")
                webbrowser.open(video_url)
            else:
                print("Videoaula não disponível para esta aula.")
        else:
            print("Opção inválida.")
