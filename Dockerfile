FROM python:3.7-alpine

ENV PYTHONBUFFERED 1

COPY ./requierments.txt requierments.txt
RUN pip install -r /requierments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

