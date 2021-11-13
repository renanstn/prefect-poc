# =============================================================================
# Base
# =============================================================================
FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
ENV DOCKERENV 1
RUN pip install --upgrade pip
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# =============================================================================
# Development
# =============================================================================
FROM base as development
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
RUN black
COPY . /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# =============================================================================
# Prod
# =============================================================================
FROM base as production
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY . /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
