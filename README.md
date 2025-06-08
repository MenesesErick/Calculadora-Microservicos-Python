# Calculadora de Microserviços com Python e Docker 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

[cite_start]Este repositório contém uma implementação prática e didática de uma **arquitetura de microserviços** com Python e Docker.  [cite_start]O objetivo é demonstrar como uma aplicação simples, neste caso uma calculadora, pode ser decomposta em serviços menores, independentes e que se comunicam via API. 

[cite_start]Este projeto foi desenvolvido para a disciplina de **Engenharia de Software**, inspirado conceitualmente pelo artigo "Microserviços com Python. Implementação Prática" de Hugo Habbema. 

## 📖 Sobre o Projeto

O problema abordado é a criação de uma calculadora simples. [cite_start]Em vez de uma abordagem monolítica (um único programa), a aplicação foi dividida em dois microserviços distintos:

1.  [cite_start]**Serviço de Soma:** Um serviço totalmente independente responsável apenas por realizar a operação de adição. 
2.  [cite_start]**Serviço de Subtração:** Outro serviço independente, responsável apenas pela subtração. 

[cite_start]Essa separação, que é o pilar da arquitetura de microserviços, permite que cada parte da aplicação seja desenvolvida, atualizada e escalada de forma autônoma.  [cite_start]A comunicação entre os serviços é feita através de requisições HTTP, orquestradas pelo Docker Compose. 

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Python (3.9+)**: Linguagem de programação principal para o desenvolvimento dos serviços. 
* **Flask**: Micro-framework web utilizado para criar as APIs de forma rápida e leve.
* [cite_start]**Docker**: Utilizado para "empacotar" cada serviço em um contêiner, garantindo um ambiente de execução consistente e isolado. 
* [cite_start]**Docker Compose**: Ferramenta para definir e gerenciar a aplicação multi-contêiner, facilitando a comunicação entre os serviços. 

## 🏗️ Arquitetura e API

[cite_start]A aplicação é composta por dois microserviços, cada um com um endpoint específico para sua operação. 

#### 1. Serviço de Soma (`servico-soma`)
* [cite_start]**Descrição**: API que recebe dois números e retorna a soma. 
* **Porta**: `5001`
* **Parâmetros**: `a` e `b` (números)
* **Exemplo**: `http://localhost:5001/somar?a=100&b=50`

#### 2. Serviço de Subtração (`servico-subtracao`)
* [cite_start]**Descrição**: API que recebe dois números e retorna a diferença entre eles. 
* **Porta**: `5002`
* **Parâmetros**: `a` e `b` (números)
* **Exemplo**: `http://localhost:5002/subtrair?a=100&b=50`

## 🚀 Começando

Para executar este projeto localmente, siga os passos abaixo.

### Pré-requisitos
* **Git**
* [cite_start]**Docker** e **Docker Compose** 

### Instalação e Execução
1.  Clone o repositório para a sua máquina local (lembre-se de trocar `SEU-USUARIO`):
    ```sh
    git clone [https://github.com/SEU-USUARIO/Calculadora-Microservicos-Python.git](https://github.com/SEU-USUARIO/Calculadora-Microservicos-Python.git)
    ```
2.  Navegue até o diretório do projeto:
    ```sh
    cd Calculadora-Microservicos-Python
    ```
3.  Execute o Docker Compose para construir as imagens e iniciar os contêineres: 
    ```sh
    docker-compose up --build
    ```
    Após a conclusão, os dois serviços estarão ativos e prontos para uso. 

## 📊 Testando a Aplicação

Com os serviços em execução, você pode testar os endpoints usando um navegador ou uma ferramenta como o `curl` no terminal.

### ✅ Teste de Soma

```bash
curl "http://localhost:5001/somar?a=10&b=5"
```

**Saída esperada (JSON):**
```json
{
  "resultado": 15.0
}
```

---

### ✅ Teste de Subtração

```bash
curl "http://localhost:5002/subtrair?a=10&b=5"
```

**Saída esperada (JSON):**
```json
{
  "resultado": 5.0
}
```

---

## ✍️ Autores

Este projeto foi desenvolvido por:

- **Erick Meneses**

