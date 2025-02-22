# Desafio Técnico - Login

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte de um processo seletivo e consiste em uma aplicação de login e registro de usuários. A solução foi construída utilizando o framework Django e um banco de dados relacional SQLite, proporcionando uma interface simples e segura para a gestão de autenticação de usuários.

A aplicação contém:
- Tela de Login com validação de credenciais
- Tela de Registro com validação de dados
- Redirecionamento para uma tela de Menu após o login bem-sucedido

---
## Tecnologias Utilizadas

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
### Acesse a Aplicação Online
Você pode testar a aplicação diretamente no seguinte link:  
[https://desafio-login.onrender.com](https://desafio-login.onrender.com)

Não é necessário clonar o repositório nem rodar localmente.

OBS: Ao acessar o site, a aplicação pode levar alguns segundos para carregar devido ao sistema de hospedagem. Por favor, aguarde enquanto a tela é inicializada.


---

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
## Funcionalidades Implementadas

### Tela de Login
- Validação de login (e-mail e senha obrigatórios)
- Mensagens de erro para credenciais inválidas
- Redirecionamento para a tela "Menu" após login bem-sucedido

### Tela de Registro
- Formulário com **nome, e-mail, senha e confirmar senha**
- Validações:
  - Nome: Apenas letras
  - E-mail: Deve conter "@"
  - Senha: Mínimo de 8 caracteres, 1 caractere especial, 1 número e 1 maiúscula
  - Confirmação de senha deve ser idêntica
- Opção para visualizar a senha
- Botão "Registrar" e "Cancelar" (redireciona para a tela de Login)

### Tela do Menu
- Ao realizar o login, o Usuário deverá ser direcionado para uma tela chamada “Menu”, que não precisa ter nenhum componente internamente, apenas a mudança da tela

### Implementações extras
 - Estilização moderna: Utilizei Tailwind CSS para criar um layout clean e responsivo.
 - Acesso restrito: O acesso à página de menu foi configurado para ser exclusivo de usuários logados, garantindo maior segurança.
 - Redirecionamento inteligente: Caso um usuário não autenticado tente acessar a página do menu, ele será automaticamente redirecionado para a página de login.

---

## 📜 Licença
Este projeto foi desenvolvido exclusivamente para fins de processos seletivos e não possui licença de uso público.

---
**Desenvolvido por Lucas Oliveira. 🖥️**
