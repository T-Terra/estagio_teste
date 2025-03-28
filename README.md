# 📌 Django + Vue.js + Web Scraping

## 📝 Sobre o Projeto
Este projeto utiliza **Django** como backend, **Vue.js** como frontend e um sistema de **web scraping** com **Selenium** para baixar arquivos PDF. Além disso, há um módulo para **extração de tabelas** dos PDFs e uma **API de testes** usando Postman.

---

**Acesso ao frontend da aplicação:** [App](https://estagio-teste-five.vercel.app/)

---

## 📂 Estrutura do Projeto
```
├── backend/              # 4. TESTE DE API
│   ├── api/              # 4.2 TESTE DE API
│   ├── core/             # 4.2 TESTE DE API
│   ├── db/               # 3. TESTE DE BANCO DE DADOS
│   ├── scraping/         # Web Scraping com Selenium
│   ├── data_extraction/  # 2. TESTE DE TRANSFORMAÇÃO DE DADOS
│   ├── web_scraping/     # 1. TESTE DE WEB SCRAPING
│   ├── tests/            # Testes de API
|   |   ├── api/
|   |       ├── postman_collection/ # 4.3 Elabore uma coleção no Postman
|   |       ├── report/
│   ├── manage.py         # Script principal do Django
│   └── ...
├── frontend/             # 4. TESTE DE API
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── downloads/               # 2. TESTE DE TRANSFORMAÇÃO DE DADOS
|   ├── Teste_gabriel_terra.zip  # 2.3 Compacte o csv em um arquivo zip
│   └── ...
├── CHANGELOG.md          # Versões do projeto
├── pyproject.toml        # Configuração do Poetry
├── README.md             # Documentação do projeto
│   └── ...
```

---

## 🚀 Tecnologias Utilizadas
### 🔹 Backend (Django + DRF)
- Django (5.1.7)
- Django REST Framework
- Django CORS Headers
- PostgreSQL
- Gunicorn
- Django Filters

### 🔹 Web Scraping e Extração de PDF
- Selenium
- Webdriver Manager
- Tabula-py
- PyPDF2
- JPype1

### 🔹 Frontend (Vue.js)
- Vue.js 3
- Vite

### 🔹 Ferramentas Auxiliares
- Poetry 
- Postman (Testes de API)

---

## ⚙️ Configuração e Instalação
### 🔹 Clone o Repositório
```bash
git clone https://github.com/T-Terra/estagio_teste.git
cd estagio_teste
```

### 🔹 Configuração do Backend (Django)
1. Instale as dependências:
```bash
poetry install
```
2. Configure as variáveis de ambiente no `.env` (verifique o arquivo example.env)
3. Execute as migrações:
```bash
poetry run python backend/manage.py migrate
```
4. Inicie o servidor:
```bash
poetry run python backend/manage.py runserver
```

### 🔹 Configuração do Web Scraping
1. Certifique-se de ter o Chrome instalado.
2. Execute o script:
```bash
poetry run python backend/web_scraping/main.py
```

### 🔹 Configuração do Frontend (Vue.js)
1. Instale as dependências:
```bash
cd frontend
yarn install
```
2. Inicie o servidor:
```bash
yarn dev
```

---

## ✅ Testes
### 🔹 Testes de API (Postman)
- A collection do **Postman** está na pasta `backend/tests/api/postman_collection`.
- Para rodar os testes:
  - Importe a collection no Postman.
  - Execute os testes.

---

## 📞 Contato
- [LinkedIn](https://www.linkedin.com/in/gabriel-pereira-terra/)
- [Email](mailto:gabrielterra322@gmail.com)

🔹 **Feito com 💻 e ☕ por Gabriel Terra** 🚀

