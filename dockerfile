# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instala dependências necessárias
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Cria pasta para uploads
RUN mkdir -p data/audio

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
