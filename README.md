# EducaTech

## Descrição do Projeto

EducaTech é um sistema desenvolvido em Python que utiliza arquivos JSON para armazenamento de dados. O sistema possui três perfis principais de usuário: **Administrador**, **Aluno** e **Professor**.

* O perfil **Administrador** permite criar e gerenciar contas de professores e alunos.
* O login de administrador é necessário para acesso a funcionalidades administrativas.

## Credenciais para Teste

Para testar o sistema, utilize o login do administrador:

* **Email:** [admin@educatech.com](mailto:admin@educatech.com)
* **Senha:** admin123

## Requisitos

Antes de executar o sistema, é necessário instalar as bibliotecas utilizadas:

```bash
pip install cryptography bcrypt
```

## Bibliotecas Utilizadas

* `cryptography.fernet` (para criptografia e segurança)
* `bcrypt` (para hash de senhas)
* `re` (para validação de formatos, como e-mail e senhas)
* `json` (para manipulação dos arquivos JSON que armazenam os dados)
* `webbrowser` (para abrir páginas no navegador, se necessário)

## Como Executar

Após instalar as dependências, execute o arquivo principal da aplicação:

```bash
python main.py
```
