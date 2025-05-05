from cryptography.fernet import Fernet

def gerar_chave():
    with open("chave.key", "wb") as chave:
        chave.write(Fernet.generate_key())

def carregar_chave():
    with open("chave.key", "rb") as chave:
        return chave.read()

chave = carregar_chave()
fernet = Fernet(chave)

def criptografar(texto: str) -> str:
    return fernet.encrypt(texto.encode()).decode()

def descriptografar(texto_criptografado: str) -> str:
    return fernet.decrypt(texto_criptografado.encode()).decode()
