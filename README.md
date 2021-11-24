# prefect-poc

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat&logo=nginx&logoColor=white)](https://www.nginx.com/)

## Descrição

Pequeno ambiente criado para estudo diversos usando a ferramenta [Prefect](https://www.prefect.io/).

O ambiente consiste atualmente em:

- 1 API que fornecem números aleatórios (FastAPI)
- 1 API que fornecem nomes aleatórios (FastAPI)
- 1 API que soma 2 valores e retorna o resultado (FastAPI)
- 1 API central que chamará todas as outras e armazenará os resultados (Django Rest Framework)
- 1 Nginx fazendo o proxy reverso até essas APIs
- 1 Banco de dados Postgres
- 1 App Prefect para servir de server
- 1 worker para rodar as tasks do Celery
- 1 broker RabbitMQ para que o Celery funcione

Para estudo, foi criado um fluxo extremamente aleatório onde, ao receber um `POST` no endpoint `/api/start_flux/`, a API Core:

- Busca um nome aleatório na API `random_name`
- Busca 2 números aleatórios na API `random_number`
- Soma os 2 números usando a API `calculator`
- Concatena o nome buscado com o resultado da soma no seguinte formato: `"{nome}-{soma}"`
- Salva o resultado no banco para eventuais consultas

## Setup do ambiente
```
docker-compose up
```

### Disparar fluxo de exemplo
```
curl -X POST http://localhost:8000/api/start_flux/
```

### Disparar exemplo de tarefa assíncrona usando o celery
```
curl -X POST http://localhost:8000/api/celery/
```

## Setup do Prefect Server

Alterar o backend default para o server local
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
