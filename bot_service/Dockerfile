FROM python:3.12

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./bot_service /app

COPY ./intentions_service /app

#COPY ../shared /app/shared

WORKDIR /app

CMD python -m spacy download ru_core_news_sm && python -m bot_service

