class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, email, senha, telefone, documentos=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.documentos = documentos or {}
