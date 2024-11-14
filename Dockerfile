FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt e instala las dependencias
COPY requirements.txt /app/
RUN pip install  -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . /app/

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080