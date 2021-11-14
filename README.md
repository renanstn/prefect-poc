# prefect-poc

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

## Descrição

Pequeno ambiente criado para estudo diversos usando a ferramenta [Prefect](https://www.prefect.io/).

O ambiente consiste atualmente em:

- 1 API (FastAPI) que fornecem números aleatórios
- 1 API (FastAPI) que fornecem nomes aleatórios
- 1 API (Django + Django Rest Framework)
- 1 Nginx fazendo o proxy reverso até essas APIs
- 1 Banco de dados Postgres
- 1 App Prefect para servir de server

## Setup do ambiente
```
docker-compose up
```

## Setup do Prefect Server

Alterar o backend default para o server
```
prefect backend server
```

Iniciar o server
```
prefect server start
```

Pela UI, criar um project

Registrar seu flow com o comando:
```
flow.register(project_name="<nome do project criado via UI>")
```

Caos queira usar o scheduler, é necessário iniciar um Agent local também
```
prefect agent local start
```
