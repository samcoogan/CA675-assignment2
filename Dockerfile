# syntax=docker/dockerfile:1
FROM python:3.9-slim

ENV PORT 80
ENV HOST 0.0.0.0

RUN apt-get update -y && \
	apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]