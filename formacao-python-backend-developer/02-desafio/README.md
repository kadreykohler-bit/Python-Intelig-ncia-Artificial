# 🐍 Desafios de Filtragem de Dados com Python

Este repositório contém as soluções para a trilha de algoritmos da formação **Python Backend Developer** da [DIO](https://web.dio.me/). Os desafios focam em manipulação de strings, conversão de tipos e estruturas de repetição para filtragem de coleções de dados. 📊

## 📋 Sumário
1. [Filtragem de Produtos em Estoque](#1-estoque)
2. [Transações Acima do Limite](#2-transacoes)
3. [Segmentação de Clientes por Cidade](#3-clientes)

---

<a name="1-estoque"></a>
## 1. 🛒 Filtragem de Produtos em Estoque
**Objetivo:** Receber uma lista de produtos e retornar apenas aqueles que possuem quantidade maior que zero em estoque.

**Entrada:** `Nome:Preço:Quantidade` (separados por `;`)  
**Exemplo:** `Teclado:50.0:10;Mouse:30.0:0;Monitor:500.0:5`  
**Saída:** `['Teclado:50.0:10', 'Monitor:500.0:5']`

---

<a name="2-transacoes"></a>
## 2. 💳 Transações Acima do Limite
**Objetivo:** Filtrar transações financeiras cujo valor ultrapasse um limite de segurança definido pelo usuário.

**Entrada:** 1. Valor Limite (`float`)
2. Lista de transações: `ID:Valor` (separadas por `;`)

**Exemplo:** - Limite: `150.00`  
- Transações: `1:100.00;2:200.50;3:150.75`  
**Saída:** `['2:200.5', '3:150.75']`

---

<a name="3-clientes"></a>
## 3. 📍 Segmentação de Clientes por Cidade
**Objetivo:** Filtrar clientes que residem em uma cidade específica para campanhas de marketing direcionadas.

**Entrada:**
1. Cidade de interesse
2. Lista de clientes: `Nome:Cidade` (separados por `;`)

**Exemplo:** - Cidade: `São Paulo`  
- Clientes: `Alice:São Paulo;Bob:Rio de Janeiro;Carlos:São Paulo`  
**Saída:** `[('Alice', 'São Paulo'), ('Carlos', 'São Paulo')]`

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x** 🐍
* **Métodos de String:** `.split()`, `.strip()`, `.append()`
* **Estruturas de Dados:** Listas e Tuplas
* **Lógica:** List Comprehensions e Laços `for`