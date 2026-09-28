FROM python:3.13-slim

WORKDIR /app

RUN useradd -u 15000 chris

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER 15000

EXPOSE 5000

CMD ["python", "app.py"]