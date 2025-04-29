from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome, data_nascimento, CPF, email, senha, telefone, RA)

    # O professor tem funções para postar atividades e gerenciar conteúdos
    def postar_atividade(self, atividade):
        # Logica para salvar atividade
        pass
