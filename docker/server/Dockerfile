FROM amazonlinux:2023 AS amazonlinux
ARG PYTHON_VERSION
RUN yum update -y && \
  yum install -y wget tar make gzip gcc zlib-devel && \
  wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
  tar xzf Python-${PYTHON_VERSION}.tgz && \
  cd Python-${PYTHON_VERSION} && \
  ./configure --enable-optimizations && \
  make altinstall && \
  cd .. && \
  rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz && \
  wget https://bootstrap.pypa.io/get-pip.py && \
  python3 get-pip.py && \
  rm get-pip.py && \
  yum clean all
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
RUN pip install --upgrade pip setuptools wheel

FROM amazonlinux AS python-libs
WORKDIR /app
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python -
COPY ta-api/pyproject.toml ta-api/poetry.lock ta-api/main.py ta-core/alembic.ini .
COPY ta-api/ta_api ./ta_api
COPY ta-core/alembic ./alembic
COPY ta-core/ta_core ./ta_core
RUN poetry config virtualenvs.create false && \
  poetry install --only main --no-root
