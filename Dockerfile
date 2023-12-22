FROM python:3

WORKDIR /code
LABEL authors="petr"
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


