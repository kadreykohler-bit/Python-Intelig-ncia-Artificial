# 🐍 Formação Python Back-end Developer - DIO

Este repositório centraliza todos os desafios de código e projetos práticos realizados durante a formação da DIO. O programa foca na construção de sistemas robustos utilizando Python, FastAPI, Docker e bancos de dados SQL.

## 📚 Ementa e Competências

A trilha foi estruturada em três pilares principais:
1. **Fundamentos de Python:** Sintaxe, estruturas de dados, algoritmos e Programação Orientada a Objetos (POO).
2. **Desenvolvimento Back-end:** Criação de APIs RESTful assíncronas com FastAPI, segurança (JWT) e tratamento de exceções.
3. **Infraestrutura e Dados:** Modelagem SQL/NoSQL e containerização com Docker.

---

## 📂 Projetos Desenvolvidos

### 1️⃣ Extração e Conversão de Dados (`/01-desafio`)
* **Objetivo:** Aplicar lógica de programação pura para manipular strings e fluxos de dados.
* **Tecnologias:** Python puro (ETL básico).

### 2️⃣ Processamento de Fluxo Financeiro (`/02-desafio`)
* **Objetivo:** Filtragem avançada de transações e gestão de clientes utilizando List Comprehension e filtros otimizados.
* **Tecnologias:** Python Avançado.

### 3️⃣ API de Sistema Bancário com Validação de Saldo (`/03-projeto`)
* **Destaque:** Este é o projeto final da formação.
* **Funcionalidades:** * Autenticação Segura (OAuth2/JWT).
    * Validação de Saldo em tempo real para impedir operações inválidas.
    * Persistência de dados com SQLAlchemy.
* **Infraestrutura:** Projeto totalmente Dockerizado para facilitar o deploy.

---

## 🛠️ Como Executar o Projeto Principal

Se você deseja testar a API localmente:

```powershell
# Acesse a pasta do projeto
cd formacao-python-backend-developer/03-projeto

# Construa a imagem Docker
docker build -t api-financeira .

# Rode o container
docker run -d -p 8000:8000 api-financeira
