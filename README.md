# projeto-Integrador-Transdisciplinar-em-Sistemas-de-Informa-o-II

# Sistema de Biblioteca Online

Este projeto implementa um sistema de biblioteca online usando Flask, permitindo que os usuários se cadastrem, façam login, visualizem livros disponíveis, reservem livros e simulem o processo de finalização de reserva com diferentes opções de pagamento.

## Árvore do Projeto

Sistema-biblioteca/
├── app/
│   ├── static/
│   │   └── imagens/
│   ├── templates/
│   ├── __init__.py                
│   ├── models.py                  
│   ├── routes.py
├── blblioteca.db 
├── config.py              
├── init_db.py             
├── README.md             
├── requirements.txt              
└── run.py

## Como Funciona o Projeto

O projeto usa o framework Flask para criar uma aplicação web. O SQLAlchemy é usado como um ORM (Object-Relational Mapper) para interagir com o banco de dados. O Flask-Login gerencia a autenticação do usuário. O Jinja2 é usado como template engine para renderizar as páginas HTML.

O sistema permite que os usuários se cadastrem com nome, sobrenome, email, CPF e idade. Após o cadastro, o usuário é automaticamente logado. Os usuários logados podem visualizar os livros disponíveis, reservar livros e prosseguir para a página de finalização de reserva.  A página de finalização de reserva exibe as reservas do usuário, o total a pagar e um formulário para selecionar a forma de pagamento (cartão de crédito, débito, boleto ou PIX). Atualmente, a integração com gateways de pagamento não está implementada, sendo apenas uma simulação.


## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**

   * Aplique as migrações para criar as tabelas:

     ```bash flask db upgrade
     ```

5. **Execute o aplicativo:**

   ```bash flask run
   ```

   O aplicativo será executado em `http://127.0.0.1:5000/` por padrão.


## Como Atualizar o Projeto

1. **Atualize o código-fonte:**

   ```bash git pull
   ```

2. **Atualize as dependências (se necessário):**

   ```bash pip install --upgrade -r requirements.txt
   ```

3. **Aplique novas migrações (se houver alterações no modelo do banco de dados):**

   ```bash flask db migrate
   flask db upgrade
   ```

## Considerações Adicionais

*   O projeto usa Decimal para cálculos financeiros, garantindo maior precisão.
*   O sistema de autenticação de usuário é feito com Flask-Login.
*   O processamento de pagamento é simulado, sem integração com gateways reais.


## Possíveis Melhorias

*   Implementar a integração com gateways de pagamento reais.
*   Adicionar a funcionalidade de exclusão de reservas.
*   Implementar a visualização do histórico de reservas do usuário.
*   Adicionar um sistema de busca de livros.
*   Implementar um sistema de gerenciamento de estoque de livros.


## Contribuições

**Esclarecimentos:**

*   **Ambiente Virtual:**  Criar e ativar um ambiente virtual é altamente recomendado para isolar as dependências do projeto.
*   **Banco de Dados:** O projeto está configurado para usar SQLite por padrão.  As instruções para configurar outro banco de dados foram adicionadas.
*   **Migrações:** Aplicar as migrações (`flask db upgrade`) é essencial para criar as tabelas no banco de dados.
*   **URL:**  A URL padrão para acessar o aplicativo localmente é `http://127.0.0.1:5000/`.
