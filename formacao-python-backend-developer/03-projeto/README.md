# 💰 API Bancária Assíncrona - Controle Financeiro

Projeto desenvolvido como desafio final da trilha de Python Back-end da DIO. A aplicação consiste em um sistema robusto de gerenciamento de usuários e movimentações financeiras (receitas e despesas), utilizando conceitos de programação assíncrona, segurança JWT e containerização.

## 🚀 Tecnologias Utilizadas
* **Python 3.10+**: Linguagem base.
* **FastAPI**: Framework moderno para construção de APIs assíncronas de alta performance.
* **SQLAlchemy**: ORM para interação com banco de dados SQLite.
* **Docker & Docker Desktop**: Isolamento de ambiente e facilidade de deploy.
* **Pydantic**: Validação de dados e definição de esquemas (Schemas).
* **JWT (JSON Web Token)**: Autenticação segura de usuários.
* **Passlib (Bcrypt)**: Criptografia avançada de senhas.

## 🧠 Regras de Negócio Implementadas
* **Validação de Saldo**: O sistema impede a criação de transações do tipo "despesa" caso o saldo acumulado do usuário seja insuficiente.
* **Autenticação**: Endpoints de transações e extratos são protegidos, exigindo um Bearer Token gerado no login.
* **Persistência Automática**: O banco de dados SQLite é inicializado automaticamente ao rodar a aplicação pela primeira vez.

## 🐳 Como Executar (Docker)

Para rodar o projeto sem precisar configurar o ambiente localmente:

1. **Construir a imagem Docker**:
   ```bash
   docker build -t api-financeira .