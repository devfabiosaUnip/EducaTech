import random
import string

def gerar_RA() -> str:
    return ''.join(random.choices(string.digits, k=8))

def validar_email(email: str) -> bool:
    return "@" in email and "." in email
