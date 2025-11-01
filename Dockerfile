FROM python:3.11-slim

LABEL maintainer="Mateo Villada - Juan Carlos Fernandez"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "main.py"]
