FROM python:3.12-slim

WORKDIR /pipeline

ENV PYTHONPATH=/pipeline

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt