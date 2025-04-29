
from models.pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone, RA)

    # Funções administrativas, como adicionar professores
    def cadastrar_professor(self, professor):
        # Lógica para adicionar professor ao sistema
        pass
