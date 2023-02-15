FROM python:3.11
ENV PYTHONUNBUFFERED=1
RUN apk update && apk upgrade
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install