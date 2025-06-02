# Tend Attend (Backend)

Tend Attend is an intuitive event management tool. It stands out by offering features that predict attendee status, enabling event organizers to leverage this information for effective management.

## Local Setup

We will be using `pyenv`, `poetry` and `docker`.

### Python installation using pyenv

https://github.com/pyenv/pyenv

```sh
cd ta-api
pyenv install `cat .python-version`
cd ..
cd ta-ml
pyenv install `cat .python-version`
```

### Dependencies installation using Poetry

https://python-poetry.org

```sh
./scripts/poetry-all.sh install
```

### Build and run the application using Docker Compose

https://docs.docker.com/compose

```sh
docker compose up
```

### Run an ASGI web server using uvicorn

```sh
cd ta-api
poetry run uvicorn main:app --reload --port=8000
```

```sh
cd ta-ml
poetry run uvicorn main:app --reload --port=8001
```
