from cryptography.fernet import Fernet


chave = Fernet.generate_key();

with open("chave.key", "wb") as cf:
    cf.write(chave);

def carregar_chave():
    with open("chave.key", "rb") as cf:
        return cf.read();

def criptografar(mensagem: str) -> bytes:
    chave = carregar_chave()         # Pega a chave do arquivo
    fernet = Fernet(chave)           # Cria o "fernet" com a chave
    return fernet.encrypt(mensagem.encode())  # Criptografa a string

def descriptografar(token: bytes) -> str:
    chave = carregar_chave()
    fernet = Fernet(chave)
    return fernet.decrypt(token).decode()