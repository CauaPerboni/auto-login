# Automação de Login com Selenium

Este projeto tem como objetivo demonstrar a automação de login em uma página HTML usando a biblioteca Selenium. O script preenche automaticamente um formulário de login e simula um clique no botão de login.

## Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas:

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
- Um navegador compatível (neste caso, Google Chrome)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git

2. Navegue até o diretório do projeto:
    ```bash
    cd nome_do_repositorio

3. Instale as dependências necessárias:
    ```bash
    pip install selenium webdriver-manager

## Como usar

1. Abra o arquivo **main.py** e substitua os valores de "username" e "password" pelos seus dados:
    login_to_site(driver, login_url, 'seu_usuario', 'sua_senha')

2. Execute o script:
    python automacao_login/main.py

3. Uma janela do navegador será aberta, o formulário será preenchido automaticamente e, em seguida, o navegador será fechado.
