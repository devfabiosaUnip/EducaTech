from cryptografia.seguranca import criptografar, descriptografar
from services.json_service import carregar_dados, salvar_dados
from models.pessoa import Pessoa
from models.professor import Professor

CAMINHO_ADMS = "dados/administradores.json"
CAMINHO_CONTEUDO = "dados/conteudo.json"
CAMINHO_ALUNOS = "dados/alunos.json"  # Caminho para o arquivo de alunos

class Administrador(Pessoa):
    
    @classmethod
    def verificar_adm_inicial(cls):
        # Verifica se o arquivo de administradores está vazio ou não existe
        try:
            adms = carregar_dados(CAMINHO_ADMS)
        except FileNotFoundError:
            adms = []

        if not adms:  # Se o arquivo estiver vazio ou não existir
            # Cadastrar o administrador inicial
            print("Nenhum administrador encontrado. Cadastrando administrador inicial...")
            administrador_inicial = {
                "nome": criptografar("Administrador Inicial"),
                "data_nascimento": criptografar("01/01/1980"),
                "cpf": criptografar("12345678900"),  # CPF fictício do administrador inicial
                "email": criptografar("admin@educatech.com"),
                "senha": criptografar("admin123"),  # Senha fictícia do administrador inicial
                "telefone": criptografar("11987654321")
            }
            adms.append(administrador_inicial)
            salvar_dados(CAMINHO_ADMS, adms)
            print("Administrador inicial cadastrado com sucesso!")
        
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

    @classmethod
    def login(cls):
        print("\n=== Login do Administrador ===")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        adms = carregar_dados(CAMINHO_ADMS)
        for adm in adms:
            if descriptografar(adm["cpf"]) == cpf and descriptografar(adm["senha"]) == senha:
                print(f"Bem-vindo, {descriptografar(adm['nome'])}")
                cls.menu_adm()
                return
        print("Credenciais inválidas.")

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

    @classmethod
    def avaliar_conteudos(cls):
        dados = carregar_dados(CAMINHO_CONTEUDO)
        pendentes = [c for c in dados if c["status"] == "pendente"]

        if not pendentes:
            print("Nenhum conteúdo pendente.")
            return

        for i, conteudo in enumerate(pendentes, 1):
            print(f"\n[{i}] {conteudo['titulo']}")
            print(f"Descrição: {conteudo['descricao']}")
            print(f"Conteúdo: {conteudo['conteudo']}")
            decisao = input("Aprovar? (s/n): ").lower()
            if decisao == "s":
                conteudo["status"] = "aprovado"
                # Agora, notificamos o aluno e atualizamos o status de suas aulas
                aluno_ra = conteudo.get("ra_aluno")  # Atribuindo o RA do aluno que postou o conteúdo
                alunos = carregar_dados(CAMINHO_ALUNOS)
                for aluno in alunos:
                    if aluno.get("RA") == aluno_ra:
                        aluno["aulas"][conteudo["materia"]] = "Aprovado"
                        salvar_dados(CAMINHO_ALUNOS, alunos)  # Salvando a atualização no arquivo
                        print(f"Aluno {descriptografar(aluno['nome'])} foi notificado sobre a aprovação.")
            else:
                conteudo["status"] = "rejeitado"

        salvar_dados(CAMINHO_CONTEUDO, dados)
        print("Avaliação concluída.")
