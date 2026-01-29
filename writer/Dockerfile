FROM python:3.9-slim

WORKDIR /app

# Copia i requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice
COPY main.py .

# Esponi la porta
EXPOSE 8000

# Comando di avvio: Lancia il server web
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]