from cryptografia.seguranca import criptografar, descriptografar
from services.json_service import carregar_dados, salvar_dados
from models.pessoa import Pessoa

CAMINHO_ARQUIVO = "dados/professores.json"
CAMINHO_CONTEUDO = "dados/conteudo.json"

class Professor(Pessoa):
    @classmethod
    def cadastrar(cls):
        print("\n=== Cadastro de Professor (via ADM) ===")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")
        materia = input("Matéria que irá lecionar: ")

        professores = carregar_dados(CAMINHO_ARQUIVO)
        for prof in professores:
            if descriptografar(prof["cpf"]) == cpf:
                print("Professor já cadastrado.")
                return

        novo_prof = {
            "nome": criptografar(nome),
            "data_nascimento": criptografar(data_nascimento),
            "cpf": criptografar(cpf),
            "email": criptografar(email),
            "senha": criptografar(senha),
            "telefone": criptografar(telefone),
            "materia": criptografar(materia)
        }

        professores.append(novo_prof)
        salvar_dados(CAMINHO_ARQUIVO, professores)
        print("Professor cadastrado com sucesso!")

    @classmethod
    def login(cls):
        print("\n=== Login do Professor ===")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        professores = carregar_dados(CAMINHO_ARQUIVO)
        for prof in professores:
            if descriptografar(prof["cpf"]) == cpf and descriptografar(prof["senha"]) == senha:
                print(f"Bem-vindo(a), Professor {descriptografar(prof['nome'])}")
                cls.menu_conteudo(prof)
                return
        print("Credenciais inválidas.")

    @classmethod
    def menu_conteudo(cls, prof):
        materia = descriptografar(prof["materia"])
        print(f"\nMatéria: {materia}")
        conteudo = carregar_dados(CAMINHO_CONTEUDO)
        aulas = [a for a in conteudo if a["materia"] == materia]

        if not aulas:
            print("Nenhum conteúdo encontrado. Você pode adicionar novo material.")
        else:
            print("Conteúdo existente:")
            for i, aula in enumerate(aulas, 1):
                print(f"{i}. {aula['titulo']} (Status: {aula['status']})")

        opc = input("Deseja adicionar ou editar conteúdo? (s/n): ").lower()
        if opc == "s":
            cls.adicionar_conteudo(materia)

    @classmethod
    def adicionar_conteudo(cls, materia):
        titulo = input("Título do módulo: ")
        descricao = input("Descrição: ")
        conteudo = input("Conteúdo/aula:")


        dados = carregar_dados(CAMINHO_CONTEUDO)
        dados.append({
            "materia": materia,
            "titulo": titulo,
            "descricao": descricao,
            "conteudo": conteudo,
            "status": "pendente"
        })
        salvar_dados(CAMINHO_CONTEUDO, dados)
        print("Conteúdo enviado para revisão do administrador.")
