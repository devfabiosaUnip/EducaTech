from cryptography.fernet import Fernet

# Gerar uma chave e salvar em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as cf:
        cf.write(chave)

# Carregar a chave de criptografia
def carregar_chave():
    with open("chave.key", "rb") as cf:
        return cf.read()

# Função para criptografar uma mensagem
def criptografar(mensagem: str) -> str:
    chave = carregar_chave()
    fernet = Fernet(chave)
    return fernet.encrypt(mensagem.encode()).decode()

# Função para descriptografar uma mensagem
def descriptografar(token: str) -> str:
    chave = carregar_chave()
    fernet = Fernet(chave)
    return fernet.decrypt(token.encode()).decode()
