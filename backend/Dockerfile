FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

# Install required system libraries including OpenBLAS
RUN apk update && apk add build-base libffi-dev python3-dev openblas-dev

# Install CFFI
RUN apk add py3-cffi

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files (if necessary)
RUN python manage.py collectstatic --noinput
