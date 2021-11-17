# syntax=docker/dockerfile:1
FROM python:3.9-slim
WORKDIR /ca675_ass2
ADD . /ca675_ass2
RUN pip install -r requirements.txt
CMD ["python", "main.py"]