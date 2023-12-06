FROM python:3.11.5-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install --no-install-recommends -y gdal-bin build-essential libcurl4-openssl-dev libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/