FROM python:3.13-apline

COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./pyproject.toml .

RUN uv sync

COPY . .

RUN python3 manage.py migrate

ENTRYPOINT [ "python3", "manage.py", "runserver" ]
