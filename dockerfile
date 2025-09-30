# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instala dependências
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Cria pasta para uploads
RUN mkdir -p data/audio

EXPOSE 8000

# Ajuste: main.py está na raiz, então referência é só "main:app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
