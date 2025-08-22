FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --co-cahce-dir -r requirements.txt

COPY ..
CMD ["python", "calculator.py"]
