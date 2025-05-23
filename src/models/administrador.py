from cryptografia.seguranca import criptografar, descriptografar
from services.json_service import carregar_dados, salvar_dados
from models.pessoa import Pessoa
from models.professor import Professor

CAMINHO_ADMS = "dados/administradores.json"
CAMINHO_CONTEUDO = "dados/conteudo.json"
CAMINHO_ALUNOS = "dados/alunos.json"

class Administrador(Pessoa):

    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone, RA)

    # Verificação inicial
    @classmethod
    def verificar_adm_inicial(cls):
        try:
            adms = carregar_dados(CAMINHO_ADMS)
        except FileNotFoundError:
            adms = []

        if not adms:
            print("Nenhum administrador encontrado. Cadastrando administrador inicial...")
            administrador_inicial = {
                "nome": criptografar("Administrador Inicial"),
                "data_nascimento": criptografar("01/01/1980"),
                "cpf": criptografar("12345678900"),
                "email": criptografar("admin@educatech.com"),
                "senha": criptografar("admin123"),
                "telefone": criptografar("11987654321")
            }
            adms.append(administrador_inicial)
            salvar_dados(CAMINHO_ADMS, adms)
            print("Administrador inicial cadastrado com sucesso!")

    # Cadastro de novos administradores
    @classmethod
    def cadastrar(cls):
        print("\n=== Cadastro de Administrador ===")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")

        adms = carregar_dados(CAMINHO_ADMS)
        for adm in adms:
            if descriptografar(adm["cpf"]) == cpf:
                print("Administrador já cadastrado.")
                return

        novo_adm = {
            "nome": criptografar(nome),
            "data_nascimento": criptografar(data_nascimento),
            "cpf": criptografar(cpf),
            "email": criptografar(email),
            "senha": criptografar(senha),
            "telefone": criptografar(telefone)
        }

        adms.append(novo_adm)
        salvar_dados(CAMINHO_ADMS, adms)
        print("Administrador cadastrado com sucesso!")

    # Login do administrador
    @classmethod
    def login(cls):
        print("\n=== Login do Administrador ===")
        email = input("Email: ")
        senha = input("Senha: ")

        adms = carregar_dados(CAMINHO_ADMS)
        for adm in adms:
            if descriptografar(adm["email"]) == email and descriptografar(adm["senha"]) == senha:
                print(f"Bem-vindo, {descriptografar(adm['nome'])}")
                cls.menu_adm()
                return
        print("Credenciais inválidas.")

    # Menu do administrador
    @classmethod
    def menu_adm(cls):
        while True:
            print("\n--- Painel Administrativo ---")
            print("1 - Cadastrar novo professor")
            print("2 - Cadastrar outro administrador")
            print("3 - Avaliar conteúdos postados")
            print("0 - Sair")
            op = input("Escolha: ").strip()
            if op == "1":
                Professor.cadastrar()
            elif op == "2":
                cls.cadastrar()
            elif op == "3":
                cls.avaliar_conteudos()
            elif op == "0":
                break
            else:
                print("Opção inválida.")

    # Avaliação de conteúdos pendentes
    @classmethod
    def avaliar_conteudos(cls):
        dados = carregar_dados(CAMINHO_CONTEUDO)
        pendentes = [c for c in dados if c.get("status") == "pendente"]

        if not pendentes:
            print("Nenhum conteúdo pendente.")
            return

        for i, conteudo in enumerate(pendentes, 1):
            print(f"\n[{i}] {conteudo.get('titulo', '[sem título]')}")
            print(f"Descrição: {conteudo.get('descricao', '[sem descrição]')}")
            print(f"Conteúdo: {conteudo.get('conteudo', '[sem conteúdo]')}")

            decisao = input("Aprovar? (s/n): ").lower()
            if decisao == "s":
                conteudo["status"] = "aprovado"
                aluno_ra = conteudo.get("ra_aluno")
                materia = conteudo.get("materia")

                if aluno_ra and materia:
                    alunos = carregar_dados(CAMINHO_ALUNOS)
                    for aluno in alunos:
                        if aluno.get("RA") == aluno_ra:
                            aluno["aulas"][materia] = "Aprovado"
                            salvar_dados(CAMINHO_ALUNOS, alunos)
                            print(f"Aluno {descriptografar(aluno['nome'])} foi notificado sobre a aprovação.")
            else:
                conteudo["status"] = "rejeitado"

        salvar_dados(CAMINHO_CONTEUDO, dados)
        print("Avaliação concluída.")

    # Cadastro de professor via menu (não utilizado, pois usa Professor.cadastrar())
    def cadastrar_professor(self, professor):
        print("=== Formulário para cadastro de novo professor ===")
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento (xx/xx/xxxx): ")
        CPF = input("Digite o CPF: ")
        email = input("Digite o email: ")
        senha = input("Cadastre uma senha provisória: ")
        telefone = input("Digite o telefone: ")
        RA = input("Cadastre o RA de professor: ")
        professor = Professor(nome, data_nascimento, CPF, email, senha, telefone, RA)

    def revisao_de_tarfefas(self, professor):
        pass  # A implementar
