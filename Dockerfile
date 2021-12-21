FROM python:3.6.13-slim
MAINTAINER Sahil Shah

# Install dependencies
RUN apt-get update \
    && pip install --upgrade pip

WORKDIR /ventilator_pressure

COPY ./requirements.txt /ventilator_pressure/requirements.txt

RUN pip install --no-cache-dir -q -r /ventilator_pressure/requirements.txt

COPY ./ /ventilator_pressure/

CMD uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000} --reload --debug













