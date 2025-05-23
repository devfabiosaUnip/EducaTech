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
        email = input("Email: ")
        senha = input("Senha: ")

        professores = carregar_dados(CAMINHO_ARQUIVO)
        for prof in professores:
            if descriptografar(prof["email"]) == email and descriptografar(prof["senha"]) == senha:
                print(f"Bem-vindo(a), Professor {descriptografar(prof['nome'])}")
                cls.menu_conteudo(prof)
                return
        print("Credenciais inválidas.")

    @classmethod
    def menu_conteudo(cls, prof):
        materia = descriptografar(prof["materia"])
        print(f"\nMatéria: {materia}")

        while True:
            print("\n=== Menu de Conteúdo ===")
            print("1. Visualizar Aulas por Módulo")
            print("2. Adicionar Módulo")
            print("3. Adicionar Aula em Módulo Existente")
            print("4. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                cls.visualizar_aulas(materia)
            elif escolha == "2":
                cls.adicionar_modulo(materia)
            elif escolha == "3":
                cls.adicionar_aula(materia)
            elif escolha == "4":
                break
            else:
                print("Opção inválida.")

    @classmethod
    def adicionar_modulo(cls, materia):
        print("\n=== Adicionar Módulo ===")
        titulo = input("Título do módulo: ")
        descricao = input("Descrição: ")

        dados = carregar_dados(CAMINHO_CONTEUDO)
        dados.append({
            "materia": materia,
            "tipo": "modulo",
            "titulo": titulo,
            "descricao": descricao,
            "status": "pendente"
        })
        salvar_dados(CAMINHO_CONTEUDO, dados)
        print("Módulo enviado para revisão do administrador.")

    @classmethod
    def adicionar_aula(cls, materia):
        print("\n=== Adicionar Aula a um Módulo ===")
        dados = carregar_dados(CAMINHO_CONTEUDO)

        modulos = [d for d in dados if d["materia"] == materia and d.get("tipo") == "modulo"]
        if not modulos:
            print("Nenhum módulo encontrado. Adicione um módulo primeiro.")
            return

        print("Módulos disponíveis:")
        for i, m in enumerate(modulos, 1):
            print(f"{i}. {m['titulo']} - {m['descricao']}")

        try:
            escolha = int(input("Escolha o número do módulo: ")) - 1
            modulo_escolhido = modulos[escolha]["titulo"]
        except (IndexError, ValueError):
            print("Escolha inválida.")
            return

        titulo_aula = input("Título da aula: ")
        link_video = input("Link do vídeo/conteúdo: ")
        link_quiz = input("Link do quiz: ")

        dados.append({
            "materia": materia,
            "tipo": "aula",
            "modulo": modulo_escolhido,
            "titulo": titulo_aula,
            "link_video": link_video,
            "link_quiz": link_quiz,
            "status": "pendente"
        })

        salvar_dados(CAMINHO_CONTEUDO, dados)
        print("Aula enviada para revisão do administrador.")

    @classmethod
    def visualizar_aulas(cls, materia):
        print("\n=== Visualizar Aulas por Módulo ===")
        dados = carregar_dados(CAMINHO_CONTEUDO)
        modulos = [d for d in dados if d["materia"] == materia and d.get("tipo") == "modulo"]

        if not modulos:
            print("Nenhum módulo disponível.")
            return

        for i, m in enumerate(modulos, 1):
            print(f"\n{i}. Módulo: {m['titulo']} - {m['descricao']}")
            aulas = [a for a in dados if a.get("tipo") == "aula" and a.get("modulo") == m["titulo"] and a["materia"] == materia]
            if not aulas:
                print("   Nenhuma aula cadastrada.")
            else:
                for aula in aulas:
                    print(f"   Aula: {aula['titulo']}")
                    print(f"     Link Vídeo: {aula['link_video']}")
                    print(f"     Link Quiz: {aula['link_quiz']}")
                    print(f"     Status: {aula['status']}")
