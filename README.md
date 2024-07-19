# Sistema de Gerenciamento de Biblioteca Interna

## Descrição
Este projeto é uma plataforma web projetada para gerenciar a biblioteca interna de uma empresa. Permite que os usuários registrem, visualizem e acompanhem o status dos livros (disponíveis ou emprestados). Cada livro possui uma página de perfil exibindo informações detalhadas, incluindo um resumo e histórico de empréstimos. Os usuários também podem reservar livros e entrar em uma lista de espera para livros emprestados. A plataforma utiliza a infraestrutura da AWS, utilizando o DynamoDB para gerenciamento do banco de dados e uma arquitetura serverless para escalabilidade e desempenho. O frontend é construído com Streamlit para simplicidade, e o backend é implementado usando FastAPI.

## Funcionalidades
- Registrar e editar informações do livro (título, autor, categoria)
- Visualizar o status dos livros (disponíveis ou emprestados)
- Página de perfil do livro com detalhes e histórico de empréstimos
- Reservar livros e entrar em uma lista de espera
- Autenticação usando AWS Cognito
- Arquitetura serverless com AWS Lambda e API Gateway
- Gerenciamento de banco de dados usando DynamoDB

## Stack Tecnológico
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Banco de Dados**: DynamoDB
- **Autenticação**: AWS Cognito
- **Infraestrutura**: AWS Lambda, API Gateway, CloudWatch
- **Controle de Versão**: GitHub

## Começando

### Pré-requisitos
- Python 3.7+
- Conta AWS
- AWS CLI configurado
- Git

### Instalação
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/yourusername/internal-library-management-system.git
   cd internal-library-management-system

   
2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Instale os pacotes necessários:**
   ```bash
   pip install -r requirements.txt

4.  **Configure os recursos da AWS:**

 - Configure as tabelas DynamoDB
 - Configure o AWS Cognito para autenticação de usuários
 - Implemente as funções AWS Lambda e o API Gateway



