FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN python3 -m pip install -r requirements.txt


EXPOSE 8000

RUN ["chmod", "+x", "./entrypoint.sh"]

CMD "./entrypoint.sh"