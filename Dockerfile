# Imagen base oficial de Python
FROM python:3.11-slim

# Crear directorio de la app
WORKDIR /app

# Copiar archivos de la app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto en el que escucha Flask
ENV PORT=8080

# Comando de ejecución
CMD ["python", "main.py"]
