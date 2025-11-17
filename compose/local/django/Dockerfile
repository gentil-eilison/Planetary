FROM python:3.13-alpine

COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./pyproject.toml .

RUN uv pip install --system . --group dev

COPY . .

# Local Dockerfile, so this is fine
RUN chmod 777 ./compose/local/django/entrypoint.sh

ENTRYPOINT [ "./compose/local/django/entrypoint.sh" ]
