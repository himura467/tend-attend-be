FROM amazonlinux:2023 AS amazonlinux
ARG PYTHON_VERSION
ENV PYTHONIOENCODING=utf-8 \
  LANG=C.UTF-8 \
  PYTHON_HOME=/opt/python/versions/${PYTHON_VERSION} \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  POETRY_HOME=/opt/poetry \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_NO_INTERACTION=1
RUN yum update -y && \
  yum install -y wget tar make gzip gcc zlib-devel openssl-devel libffi-devel && \
  wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
  tar xzf Python-${PYTHON_VERSION}.tgz && \
  cd Python-${PYTHON_VERSION} && \
  ./configure --enable-optimizations --with-lto --prefix=${PYTHON_HOME} && \
  make altinstall && \
  cd .. && \
  rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz && \
  yum clean all
RUN ln -s ${PYTHON_HOME}/bin/python$(echo ${PYTHON_VERSION} | cut -d. -f1-2) ${PYTHON_HOME}/bin/python
ENV PATH="${PYTHON_HOME}/bin:${PATH}"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
COPY ta-api ./app/ta-api
COPY ta-core ./app/ta-core
WORKDIR /app/ta-api
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry config virtualenvs.create false && \
  poetry install --only main --no-root
