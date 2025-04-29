# ---------  Etapa 1: Construcción ----------
FROM python:3.11-alpine AS builder

#PYTHONDONTWRITEBYTECODE: No escribir archivos .pyc
#PYTHONUNBUFFERED: No almacenar en buffer la salida de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Dependencias del sistema para compilar paquetes
RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

WORKDIR /app

#Dependencias de la app de python
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------

# --------- Etapa 2: Imagen final ----------
FROM python:3.11-alpine

#PYTHONDONTWRITEBYTECODE: No escribir archivos .pyc
#PYTHONUNBUFFERED: No almacenar en buffer la salida de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Instalo las dependencias mínimas
RUN apk add --no-cache libpq

WORKDIR /app

#Copio las dependencias generadas por la etapa anterior
COPY --from=builder /install /usr/local

#Copio el resto del código
COPY . .

#Expongo puerto 8000
EXPOSE 8000

#Ejecuta migraciones y luego levanta el server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]