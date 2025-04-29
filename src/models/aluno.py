from models.pessoa import Pessoa
from services.json_service import ler_dados, salvar_dados
from cryptografia.seguranca import criptografar, descriptografar

class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone)
        self.RA = RA

    @staticmethod
    def menuLoginCadastro():
        print("=== Menu ===");
        print("1)Login 2)Cadastrar nova conta");
        valor = int(input("Digite a opção desejada:"));
        
        if (valor == 1):
            return Aluno.menuLogin();
        if (valor == 2):
            return Aluno.menuCadastro();

    @staticmethod
    def menuLogin():
        print("=== Login de Aluno ===");
        RA = str(input("Digite seu RA e aperte enterpara confirmar:"))
        senha = str(input("Digite sua senha e aperte enterpara confirmar:"))
        Aluno.login_por_RA(RA, senha);

    # Menu de Cadastro de Aluno
    @staticmethod
    def menuCadastro():
        print("=== Cadastro de Aluno ===")
        nome = input("Digite o nome do aluno: ").strip()
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        CPF = input("Digite o CPF: ").strip()
        email = input("Digite o email: ").strip()
        senha = input("Digite a senha: ").strip()
        telefone = input("Digite o telefone: ").strip()
        RA = input("Digite o RA:").strip()
        
        aluno = Aluno(nome, data_nascimento, CPF, email, senha, telefone, RA)
        aluno.cadastrar()
        print(f"Aluno {nome} cadastrado com sucesso!")

    # Função para salvar o aluno em um arquivo
    def cadastrar(self):
        # Aqui você pode chamar a função de salvar os dados (como salvar em JSON ou outro formato)
        aluno_data = {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "email": self.email,
            "senha": criptografar(self.senha),
            "telefone": self.telefone,
            "RA": self.RA
        }
        salvar_dados(aluno_data)  # Isso deve ser implementado na função salvar_dados()

    
    def login_por_RA(RA, senha_informada):
        dados = ler_dados();
        aluno = Aluno();
        for aluno in dados:
            if aluno["RA"] == RA:
                senha_criptografada = aluno["senha"]
                senha_descriptografada = descriptografar(senha_criptografada)
                if senha_descriptografada == senha_informada:
                    return aluno
        return "Erro"  # Login falhou
