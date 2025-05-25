# Basis-Image mit Python 3.11
FROM python:3.11

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Abhängigkeitsdateien und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Code ins Container-Image
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Alembic
RUN pip install alembic

# Setze Umgebungsvariablen für FastAPI
ENV PYTHONUNBUFFERED=1

# Führe Alembic-Migrationen aus
RUN alembic upgrade head

# Expose port 5000 for the Flask app
EXPOSE 8000

# Run alembic upgrade when the container starts
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host=0.0.0.0 --port=8000"]
