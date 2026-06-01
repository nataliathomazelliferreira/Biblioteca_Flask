# Biblioteca Flask

Projeto desenvolvido para a disciplina **Linguagem de Programação II**, do curso de **Inteligência Artificial da FATEC**.

## Sobre o trabalho

O objetivo deste trabalho foi estudar a biblioteca **Flask**, compreender seus principais recursos e desenvolver uma aplicação prática para demonstrar seu funcionamento.

Durante o estudo da biblioteca, foi desenvolvido um mini projeto chamado **English Study Platform**, utilizado como exemplo para aplicar os conceitos aprendidos e demonstrar como o Flask pode ser utilizado na criação de aplicações web.

O foco principal deste trabalho é a biblioteca Flask, enquanto a plataforma desenvolvida serve como uma demonstração prática de suas funcionalidades.

## O que é Flask?

Flask é um microframework web para Python que permite desenvolver aplicações web de forma simples, rápida e organizada.

Por ser um microframework, o Flask fornece apenas os recursos essenciais para o desenvolvimento, permitindo que o programador escolha quais ferramentas adicionais deseja utilizar.

O Flask pode ser utilizado para:

* Desenvolvimento de aplicações web;
* Criação de APIs;
* Sistemas com formulários;
* Páginas dinâmicas;
* Dashboards;
* Protótipos de software;
* Projetos acadêmicos.

## Principais recursos do Flask

Durante o desenvolvimento deste projeto foram utilizados alguns recursos importantes da biblioteca Flask.

### Rotas

As rotas definem os caminhos que o usuário pode acessar dentro da aplicação.

Exemplo:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

### Templates HTML

O Flask utiliza templates para separar o código Python das páginas HTML.

Exemplo:

```python
return render_template("levels.html")
```

### Formulários

Os formulários permitem que o usuário envie informações para o servidor.

Exemplo:

```python
nome = request.form.get("nome")
```

### Sessões

As sessões permitem armazenar informações temporárias durante a navegação do usuário.

Exemplo:

```python
session["nome"] = nome
```

### Comunicação Cliente-Servidor

O Flask recebe as informações enviadas pelo navegador, processa esses dados no Python e retorna uma resposta para o usuário em forma de página web.

## Aplicação prática: English Study Platform

Para demonstrar o funcionamento da biblioteca Flask, foi desenvolvido o projeto **English Study Platform**.

A aplicação consiste em uma plataforma simples para estudos de inglês, permitindo que o usuário realize atividades em diferentes níveis de dificuldade.

### Funcionalidades

* Inserção do nome do usuário;
* Seleção do nível de inglês;
* Exercícios de Grammar;
* Exercícios de Reading;
* Atividade de Listening;
* Atividade de Speaking;
* Quiz final;
* Exibição de resultado.

## Tecnologias utilizadas

* Python
* Flask
* HTML5
* CSS3
* Jinja2
* Git
* GitHub

## Repositório do projeto

```bash
git clone https://github.com/nataliathomazelliferreira/Biblioteca-Flask-.git
```

Ou acesse diretamente:

https://github.com/nataliathomazelliferreira/Biblioteca-Flask-

---

# Instalação e execução

## 1. Clonar o repositório

Abra o terminal, PowerShell ou terminal do VS Code e execute:

```bash
git clone https://github.com/nataliathomazelliferreira/Biblioteca-Flask-.git
```

Entre na pasta principal do projeto:

```bash
cd Biblioteca-Flask-
```

Entre na pasta da aplicação:

```bash
cd "English Study Platform"
```

---

## 2. Criar o ambiente virtual

Dentro da pasta **English Study Platform**, crie o ambiente virtual:

```bash
python -m venv venv
```

Esse comando cria uma pasta chamada `venv`, onde serão instaladas as dependências do projeto.

---

## 3. Ativar o ambiente virtual

### Windows PowerShell

Caso apareça erro de permissão, execute:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois ative o ambiente virtual:

```bash
venv\Scripts\Activate.ps1
```

### Windows CMD

```bash
venv\Scripts\activate
```

### Linux ou macOS

```bash
source venv/bin/activate
```

Quando o ambiente estiver ativado, aparecerá algo parecido com:

```bash
(venv)
```

---

## 4. Instalar o Flask

Com o ambiente virtual ativado, instale o Flask:

```bash
pip install flask
```

Caso exista um arquivo `requirements.txt`, também é possível instalar as dependências com:

```bash
pip install -r requirements.txt
```

---

## 5. Rodar o projeto

Ainda dentro da pasta **English Study Platform**, execute:

```bash
python app.py
```

O terminal exibirá uma mensagem parecida com:

```bash
* Running on http://127.0.0.1:5000
```

Abra o navegador e acesse:

```bash
http://127.0.0.1:5000
```

---

## 6. Parar o servidor

Para encerrar o servidor Flask, volte ao terminal e pressione:

```bash
CTRL + C
```

---

# Estrutura do projeto

```bash
Biblioteca-Flask/
│
├── English Study Platform/
│   │
│   ├── app.py
│   │
│   ├── static/
│   │   │
│   │   └── css/
│   │       │
│   │       └── style.css
│   │
│   └── templates/
│       │
│       ├── activity.html
│       ├── base.html
│       ├── index.html
│       ├── levels.html
│       └── result.html
│
├── venv/
│
├── Biblioteca Flask.pptx
│
└── README.md
```

## Descrição dos arquivos

### app.py

Arquivo principal da aplicação Flask. Nele estão as rotas, o processamento das requisições, as sessões e a comunicação entre o servidor e as páginas HTML.

### templates/

Pasta onde ficam as páginas HTML da aplicação.

* **base.html**: estrutura principal compartilhada pelas páginas.
* **index.html**: página inicial, onde o usuário informa seu nome.
* **levels.html**: página para seleção do nível de inglês.
* **activity.html**: página das atividades de inglês.
* **result.html**: página que exibe o resultado final.

### static/

Pasta utilizada para armazenar arquivos estáticos, como CSS, imagens e scripts.

### static/css/style.css

Arquivo responsável pelo estilo visual da aplicação, incluindo cores, botões, cards, layout e responsividade.

### venv/

Ambiente virtual Python utilizado para instalar as dependências do projeto.

### Biblioteca Flask.pptx

Apresentação utilizada para explicar a biblioteca Flask e demonstrar sua aplicação prática.

### README.md

Arquivo de documentação do projeto.

---

# Objetivos de aprendizagem

Com este projeto foi possível aprender:

* O que é a biblioteca Flask;
* Como criar uma aplicação web com Python;
* Como criar rotas;
* Como renderizar páginas HTML;
* Como trabalhar com formulários;
* Como utilizar sessões;
* Como organizar arquivos estáticos e templates;
* Como ocorre a comunicação entre cliente e servidor.

---

# Possíveis melhorias futuras

* Adicionar banco de dados;
* Criar sistema de login;
* Salvar o progresso do usuário;
* Adicionar mais exercícios;
* Criar ranking de pontuação;
* Melhorar o sistema de correção;
* Adicionar novas atividades de inglês.

---

Projeto desenvolvido exclusivamente para fins acadêmicos.
