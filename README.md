# Desafio Técnico - Login

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte de um processo seletivo e consiste em uma aplicação de login e registro de usuários. A solução foi construída utilizando o framework Django e um banco de dados relacional SQLite, proporcionando uma interface simples e segura para a gestão de autenticação de usuários.

A aplicação contém:
- Tela de Login com validação de credenciais
- Tela de Registro com validação de dados
- Redirecionamento para uma tela de Menu após o login bem-sucedido

---
## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Django**
- **SQLite**
- **HTML, CSS e JavaScript**
- **Tailwind CSS (para estilização)**

---
## 📂 Estrutura do Projeto

```
/desafio-login/
│── app/                 # Aplicação principal
│   ├── migrations/      # Arquivos de migração do banco de dados
│   ├── static/          # Arquivos estáticos (CSS, JS, etc.)
│   ├── templates/       # Templates HTML
│   ├── views.py         # Lógica das telas
│   ├── models.py        # Modelos do banco de dados
│   ├── forms.py         # Formulários para validação de entrada do usuário
│── desafio_login/       # Configuração principal do Django
│── db.sqlite3           # Banco de dados SQLite
│── manage.py            # Comando principal para rodar a aplicação
│── requirements.txt     # Dependências do projeto
│── README.md            # Documentação
```

---
## ⚙️ Como Configurar o Projeto

⚠️ Pré-requisitos
- Python 3 instalado (verifique com `python --version`)
- Git instalado (opcional, se quiser clonar o repositório)
- Ambiente virtual recomendado para isolar as dependências


### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/desafio-login.git
cd desafio-login
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o Banco de Dados
- O projeto utiliza **SQLite**, então o banco já está configurado por padrão.

### 5️⃣ Aplicar Migrações e Criar um Superusuário
```bash
python manage.py migrate
python manage.py createsuperuser  # (Opcional para acessar o admin do Django)
```

### 6️⃣ Rodar a Aplicação
```bash
python manage.py runserver
```
Acesse no navegador: **http://127.0.0.1:8000/**

## 🛠 Como Testar a Aplicação
- Criar um usuário pela tela de registro e testar o login
- Certifique-se de que usuários não logados não conseguem acessar a tela do menu diretamente.

### Teste a Tela de Registro
- Verifique se o formulário contém os campos “nome”, “e-mail”, “senha” e “confirmar senha”.
- Confirme que o campo “nome” aceita apenas letras e que erros são exibidos para entradas inválidas.
- Valide que o campo “e-mail” aceita apenas e-mails válidos com “@”.
- Teste se o campo “senha” atende os requisitos (mínimo de 8 caracteres, 1 especial, 1 número e 1 maiúscula).
- Verifique se o campo “confirmar senha” deve ser igual à “senha”.
- Confirme a funcionalidade de visualizar as senhas, que devem estar ocultas por padrão.
- Certifique-se de que os botões “Registrar” e “Cancelar” funcionam corretamente.
- Realize testes adicionais com dados inválidos para garantir que os erros sejam exibidos corretamente.
---
## 🔑 Funcionalidades Implementadas

### ✅ Tela de Login
- Validação de login (e-mail e senha obrigatórios)
- Mensagens de erro para credenciais inválidas
- Redirecionamento para a tela "Menu" após login bem-sucedido

### ✅ Tela de Registro
- Formulário com **nome, e-mail, senha e confirmar senha**
- Validações:
  - Nome: Apenas letras
  - E-mail: Deve conter "@"
  - Senha: Mínimo de 8 caracteres, 1 caractere especial, 1 número e 1 maiúscula
  - Confirmação de senha deve ser idêntica
- Opção para visualizar a senha
- Botão "Registrar" e "Cancelar" (redireciona para a tela de Login)

### ✅ Tela do Menu
- Ao realizar o login, o Usuário deverá ser direcionado para uma tela chamada “Menu”, que não precisa ter nenhum componente internamente, apenas a mudança da tela

### ✅ Implementações extras
 - Estilização moderna: Utilizei Tailwind CSS para criar um layout clean e responsivo.
 - Acesso restrito: O acesso à página de menu foi configurado para ser exclusivo de usuários logados, garantindo maior segurança.
 - Redirecionamento inteligente: Caso um usuário não autenticado tente acessar a página do menu, ele será automaticamente redirecionado para a página de login.

---

## 📜 Licença
Este projeto foi desenvolvido exclusivamente para fins do processo seletivo e não possui licença de uso público.

---
**Desenvolvido por Lucas Oliveira. 🖥️**
