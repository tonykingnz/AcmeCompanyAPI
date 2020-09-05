FROM python:buster

RUN apt-get update

RUN apt install git
RUN apt install vim -y
RUN apt-get install postgresql

RUN pip install --upgrade pip

RUN pip install connexion[swagger_ui]
RUN pip install gevent
RUN pip install psycopg2
RUN pip install swagger-ui-bundle
RUN pip install openapi-spec-validator

CMD vim
