FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirmenets.txt

COPY ..

CMD ["python", "-m', "app.calculator"]
