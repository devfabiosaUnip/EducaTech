def main():
 from models.aluno import Aluno;  
 from cryptografia.seguranca import criptografar, descriptografar;

 nome =  input("Digite seu nome:");
 data_nascimento = input("Digite sua data de nascimento:");
 CPF = input("Digite seu CPF:");
 email = input("Digite seu email:");
 senha = input("Digite sua senha:");
 telefone = input("Digite seu telefone:");
 RA = input("Digite seu RA:");
 tokenNome = criptografar(nome).decode();
 tokenCPF = criptografar(CPF).decode();

 aluno =  Aluno(tokenNome, data_nascimento, tokenCPF, email, senha, telefone, RA);
 aluno.cadastrar();
 CPF = tokenCPF;
 aluno.login(CPF);

if __name__ == "__main__":
    main()
