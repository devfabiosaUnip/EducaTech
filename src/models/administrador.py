
from models.pessoa import Pessoa
from models.professor import Professor
class Administrador(Pessoa):
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone, RA)3
    # Funções administrativas, como adicionar professores
    def cadastrar_professor(self, professor):
        print("=== formulario para cadastro de novo professor ===");
        nome = input("Digite o nome");
        data_nascimento = input("Digite a data de nascimento xx/xx/xxxx");
        CPF = input("Digite o seu cpf:");
        email = input("Digite seu email:");
        senha = input("cadastre uma senha provisoria:");
        telefone = input("Cadastre uma senha provisoria");
        RA = input("Cadastre o RA de professor:");
        professor = Professor(nome, data_nascimento, CPF, email, senha, telefone, RA);
        
    def revisao_de_tarfefas(self, professor):
      pass
