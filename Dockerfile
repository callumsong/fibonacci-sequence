# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN pytest

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
