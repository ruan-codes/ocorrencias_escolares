# 📘 Ocorrências AFS

Sistema web em Django para a gestão escolar registrar, consultar e acompanhar ocorrências disciplinares de alunos.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=FFD43B)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

## Funcionalidades

- **Login obrigatório** com o sistema de autenticação do Django
- **Dashboard** com total de ocorrências, contagem por gravidade (leve, média, grave), alunos ativos e ocorrências por curso
- **Ocorrências:** cadastrar, editar, excluir e consultar, com filtros por nome, curso, ano e gravidade
- **Alunos:** cadastro, edição e histórico de ocorrências de cada aluno
- **Rastreabilidade:** cada ocorrência guarda quem a registrou
- Listagens com paginação e painel administrativo do Django

## Tecnologias

Python · Django · SQLite · HTML · CSS · python-dotenv

## Como rodar

> Requer Python 3.12 ou superior (Django 6).

```bash
git clone https://github.com/ruan-codes/ocorrencias_escolares.git
cd ocorrencias_escolares

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt
cp .env.example .env           # depois defina uma SECRET_KEY

cd ocorrencias_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` e entre com o usuário criado.

## Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True` em desenvolvimento, `False` em produção |
| `ALLOWED_HOSTS` | Domínios permitidos, separados por vírgula |
