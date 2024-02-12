FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY ligthlife /ligthlife
WORKDIR /ligthlife
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password ligthlife-user

USER ligthlife-user