FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN apk update && apk add build-base musl-dev
RUN apk add libffi-dev
RUN apk add openblas

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev \

RUN apk update && apk add build-base libffi-dev python3-dev
RUN apk add py3-cffi

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput