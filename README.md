# Calculadora de Microserviços com Python e Docker

Este é um projeto simples para demonstrar de forma prática a implementação de uma arquitetura de microserviços utilizando Python, Flask e Docker. A aplicação consiste em uma calculadora básica dividida em dois serviços independentes: um para soma e outro para subtração.

[cite_start]O projeto foi desenvolvido como um exercício prático, inspirado no artigo "Microserviços com Python. Implementação Prática" de Hugo Habbema.

---

### 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flask:** Micro-framework para criar as APIs de cada serviço.
* **Docker:** Para criar contêineres isolados para cada microserviço.
* **Docker Compose:** Para orquestrar e gerenciar os múltiplos contêineres da aplicação.

---

### 📁 Estrutura do Projeto

[cite_start]A estrutura do projeto está organizada da seguinte forma:

.
├── Calculadora-Microservicos-Python/
│   ├── servico_soma/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── servico_subtracao/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── docker-compose.yml
└── README.md


---

### ⚙️ Como Executar

Para executar este projeto em sua máquina local, siga os passos abaixo.

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem com o Docker Desktop)

**Passos:**

1.  **Clone o repositório (lembre-se de trocar `SEU-USUARIO`):**
    ```bash
    git clone [https://github.com/SEU-USUARIO/Calculadora-Microservicos-Python.git](https://github.com/SEU-USUARIO/Calculadora-Microservicos-Python.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Calculadora-Microservicos-Python
    ```

3.  **Suba os contêineres com Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    Os serviços estarão rodando e prontos para receber requisições.

---

###  API - Como Usar

Os microserviços expõem os seguintes endpoints:

#### **Serviço de Soma**
* **Endpoint:** `GET /somar`
* **Porta:** `5001`
* **Exemplo de uso (via curl):**
    ```bash
    curl "http://localhost:5001/somar?a=10&b=5"
    ```
* **Resposta esperada:**
    ```json
    {
      "resultado": 15.0
    }
    ```

#### **Serviço de Subtração**
* **Endpoint:** `GET /subtrair`
* **Porta:** `5002`
* **Exemplo de uso (via curl):**
    ```bash
    curl "http://localhost:5002/subtrair?a=10&b=5"
    ```
* **Resposta esperada:**
    ```json
    {
      "resultado": 5.0
    }
    ```

---

### 🛑 Como Parar a Aplicação

Para parar os contêineres, volte ao terminal onde o `docker-compose` está rodando e pressione `Ctrl + C`. Para remover os contêineres e a rede criada, use o comando:

```bash
docker-compose down
