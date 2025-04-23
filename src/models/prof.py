from models.pessoa import Pessoa;
from services.json_service import salvar_dados, ler_dados;

class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone)

def novoProfessor(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
        }
    
    def cadastrarProfessor(self):
        dados = ler_dados();
        dados.append(self.novoProfessor());
        salvar_dados(dados);