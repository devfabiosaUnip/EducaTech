from models.pessoa import Pessoa;
from services.json_service import salvar_dados, ler_dados;
from cryptografia.seguranca import descriptografar

class Aluno(Pessoa):

    def __init__(self, nome, data_nascimento, CPF, email, senha, telefone, RA):
        super().__init__(nome,data_nascimento,CPF,email,senha,telefone);
        self.RA = RA;

    def novoAluno(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
            "RA": self.RA
        }
    
    def cadastrar(self):
        dados = ler_dados();
        dados.append(self.novoAluno());
        salvar_dados(dados);

    def login(self, CPF):
     self.CPF = CPF
     stts_pesquisa = False

     for aluno in ler_dados():
        try:
            cpf_criptografado = aluno["CPF"]

            # Se estiver como string no JSON, precisa ser convertido para bytes
            if isinstance(cpf_criptografado, str):
                cpf_criptografado = cpf_criptografado.encode()

            descriptografar_cpf = descriptografar(cpf_criptografado)

            if CPF == descriptografar_cpf:
                stts_pesquisa = True
                print("CPF ENCONTRADO:", descriptografar_cpf)
                break

        except Exception as e:
            print("Erro ao descriptografar:", e)

     if not stts_pesquisa:
        print("CPF não encontrado.")

            
                    

            


        
        

    




