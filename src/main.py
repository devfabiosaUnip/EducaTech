from models.aluno import Aluno
from models.professor import Professor
from models.administrador import Administrador
from cryptografia.seguranca import descriptografar

def main():
    print(descriptografar("gAAAAABoFSu5rhv_8ZWGPbaCJCcG-tCVfFUnOjn13NdGdLDoyrcSx-sspknUsWO9G08oYJCJVQ65YrXrqeDO7XmIQfvFoxPv5oGOFyo93qmPoTsk2amDG0o="))
    while True:
        print("\n=== EducaTech ===")
        print("1 - Login como aluno")
        print("2 - Cadastrar novo aluno")
        print("3 - Login como professor")
        print("4 - Login como administrador")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            Aluno.login()
        elif opcao == "2":
            Aluno.cadastrar()
        elif opcao == "3":
            Professor.login()
        elif opcao == "4":
            Administrador.login()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

    


if __name__ == "__main__":
    Administrador.verificar_adm_inicial()  # Verifica e cria o administrador inicial, se necessário
    main()



