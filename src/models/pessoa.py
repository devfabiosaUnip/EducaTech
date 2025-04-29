from services.json_service import ler_dados, salvar_dados
from cryptografia.seguranca import carregar_chave, criptografar, descriptografar

# Definição de Pessoa (classe base)
class Pessoa:
    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.CPF = CPF
        self.email = email
        self.senha = senha
        self.telefone = telefone

    
    # Função para criptografar a senha ao cadastrar
    def criptografar_email(self):
        return criptografar(self.email)
    
    
    # Função para criptografar a senha ao cadastrar
    def criptografar_senha(self):
        return criptografar(self.senha)

    # Função para descriptografar a senha
    def descriptografar_email(self, email_criptografado):
        return descriptografar(email_criptografado)
    
    def descriptografar_senha(self, senha_criptografada):
        return descriptografar(senha_criptografada)
