FROM alpine:latest
MAINTAINER Sahil Shah

RUN apk add --no-cache --update python3 py3-pip bash

WORKDIR /ventilator_pressure

COPY ./requirements.txt /ventilator_pressure/requirements.txt

RUN pip3 install --no-cache-dir -q -r /ventilator_pressure/requirements.txt

COPY ./ /ventilator_pressure/

CMD uvicorn main:app --host=0.0.0.0 --port=5000 --reload --debug












