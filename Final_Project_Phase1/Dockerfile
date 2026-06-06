FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY hello_world.py .

CMD ["python", "hello_world.py"]
