FROM python:3.12

WORKDIR /app

COPY ./admin /app
COPY ./shared /app/shared

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

RUN pip install --no-cache-dir -r requirements.txt