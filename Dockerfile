FROM python:3.7-alpine

RUN apk update && apk add tzdata \
     && cp -r -f /usr/share/zoneinfo/Europe/Moscow /etc/localtime

COPY . /application
WORKDIR /application
RUN apk add build-base && pip install --upgrade pip && pip install -r /application/requirements.txt
CMD ["python", "main.py"]