FROM python:3.11.0-slim-buster as api
COPY ./server.crt ./
COPY ./server.key ./
COPY ./requirements.txt ./
RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN pip3 install psycopg2
RUN pip3 install -r requirements.txt
COPY ./app.py ./
COPY ./wsgi.py ./
COPY ./clients ./clients
RUN mkdir ./uploads
ENTRYPOINT ["gunicorn", "--bind", "api:5000", "--certfile=server.crt", "--keyfile=server.key", "wsgi:app"]
