FROM python:3.9.0

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "server:app", "--host","0.0.0.0","--port","8080", "--workers","3"]