# syntax=docker/dockerfile:1
FROM python:3.9.6

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy backend
COPY . /app/

ENTRYPOINT ["sh", "entrypoint.sh"]