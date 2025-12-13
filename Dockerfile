Filename: Dockerfile
Contents:
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY 
COPY . .
RUN mkdir -p instanceRun seed to create DB
 
RUN python seed.py
EXPOSE 5000
CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:5000", "--workers", "2"]
