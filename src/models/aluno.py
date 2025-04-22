from models.pessoa import Pessoa;
from services.json_service import salvar_dados, ler_dados;

class Aluno(Pessoa):

    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome,data_nascimento,CPF,email,senha,telefone);
        self.RA = RA;

    def novoAluno(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "RA": self.RA
        }
    
    def cadastrar(self):
        dados = ler_dados();
        dados.append(self.novoAluno());
        salvar_dados(dados);

        
        

    




