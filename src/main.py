from models.aluno import Aluno

def switch_case(valor):
    if valor == 1:
        return Aluno.menuLoginCadastro()  # Chama o menu de cadastro do aluno
    elif valor == 2:
        return "Opção 2: Administrador"
    elif valor == 3:
        return "Opção 3: Professor"
    else:
        return "Opção inválida"

def main():
    print("=== Bem-Vindo à EducaTech ===")
    print("=== Informe o seu tipo de login: ===")
    print("=== 1: Aluno / 2: Administrador / 3: Professor ===")
    valor = int(input("Digite a opção desejada:"));
    switch_case(valor);
    


if __name__ == "__main__":
    main()



1























    # Cria o aluno e cadastra


    # print("\n=== Login do Aluno ===")
    # RA_login = input("Digite seu RA para login: ").strip()
    # senha_login = input("Digite sua senha para login: ").strip()

    # print(f"\n[DEBUG] RA inserido: {RA_login}")

    # # Verifica o login com RA e senha
    # aluno_encontrado = Aluno.login_por_RA(RA_login, senha_login)

    # if aluno_encontrado:
    #     print("\nLogin bem-sucedido! Dados do aluno:")
    #     print(f"Nome: {aluno_encontrado['nome']}")
    #     print(f"RA: {aluno_encontrado['RA']}")
    # else:
    #     print("\nRA não encontrado ou erro no login.")





