FROM python:3.10-slim-bookworm AS base
RUN apt-get update && apt-get install --no-install-recommends -y \
  gcc \
  curl \
  python3-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
ENV PYTHONIOENCODING=utf-8 \
  LANG=C.UTF-8 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_ROOT_USER_ACTION=ignore \
  POETRY_HOME=/opt/poetry \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_NO_INTERACTION=1
ENV PATH="${POETRY_HOME}/bin:${PATH}"
RUN python -m pip install --upgrade pip setuptools wheel
WORKDIR /app
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python -
COPY ta-ml/pyproject.toml ta-ml/poetry.lock ta-ml/src/main.py ta-ml/src/gunicorn.conf.py ./
COPY ta-ml/src/ta_ml ./ta_ml
RUN poetry config virtualenvs.create false && \
  poetry install --only main --no-root

FROM base AS development
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS production
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.conf.py"]
