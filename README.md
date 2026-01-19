# 🔐 Criptografador de Fluxo ASCII com Coeficiente Dinâmico

Este é um projeto de criptografia simétrica baseado na tabela ASCII, desenvolvido para fins educacionais e de estudo lógico. O sistema utiliza uma combinação de **ofuscação por ruído**, **padding de blocos fixos** e **rotação de bases numéricas**.



## 🚀 Como Funciona a Lógica?

Diferente de uma substituição simples, este algoritmo utiliza quatro pilares de segurança:

1.  **Regra dos 5 Dígitos (Padding):** Todo caractere (seja mensagem ou ruído) é convertido para um bloco fixo de 5 caracteres. Isso elimina ambiguidades na leitura da string.
2.  **Coeficiente Dinâmico (Chave):** O usuário escolhe um coeficiente ($N$). O algoritmo agrupa $N$ letras da mensagem e, após cada grupo, insere $N$ blocos de ruído aleatório.
3.  **Rotação de Bases:** Para dificultar a análise de frequência, o sistema rotaciona a base numérica de cada caractere da mensagem entre:
    * **Hexadecimal** (ex: `0006F`)
    * **Octal** (ex: `00157`)
    * **Entidade HTML** (ex: `&#111`)
4.  **Filtro de Ruído:** Os ruídos são gerados apenas no intervalo decimal `0-19` (caracteres de controle), enquanto a mensagem utiliza apenas caracteres imprimíveis (`> 31`), permitindo uma distinção clara durante a descriptografia.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Core da lógica de criptografia.
* **Flask**: Micro-framework para a interface web.
* **HTML5/CSS3**: Interface em Dark Mode responsiva.
* **JavaScript**: Funcionalidade de cópia para a área de transferência.

## 💻 Instalação e Uso Local

1.  Clone o repositório:
    ```bash
    git clone [[https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)](https://github.com/ROM4-sec/Criptografia-Basica-com-Tabela-ASCII-em-FLASK.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute a aplicação:
    ```bash
    python app.py
    ```
4.  Acesse no navegador: `http://127.0.0.1:5000`

## 📊 Exemplo Prático

**Mensagem:** `casa` | **Coeficiente:** `3`

O algoritmo converterá as letras `c`, `a`, `s` usando bases diferentes, adicionará 3 blocos de ruído, depois converterá a última letra `a` e adicionará mais 3 blocos de ruído final. 

---

## 🤝 Contribuições
Este projeto foi desenvolvido em conjunto por um grupo de amigos entusiastas de cibersegurança. Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.
