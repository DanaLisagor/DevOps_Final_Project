# Hello Flask

## Description
A simple Python Flask application that returns a "Hello, World!" message when accessed.
## Requirements
- Docker installed
- Docker Compose installed

## Run the application

### Option 1: Using Docker Compose (recommended)
```bash
docker compose up --build
```

### Option 2: Using Docker directly
```bash
docker build -t hello-flask .
docker run -p 5000:5000 hello-flask
```

## Access the application
Open your browser and go to:
http://localhost:5000

## Stop the application
Press CTRL + C in the terminal

## Docker Hub
https://hub.docker.com/r/danalisagor/hello-flask

## Containerization with Docker

### Run the container
```bash
docker run -d -p 5000:5000 --name hello-container hello-flask
```

### Create a volume
```bash
docker volume create flask_data
```

### Run the container with a volume
```bash
docker run -d -p 5000:5000 --name hello-container -v flask_data:/app/logs hello-flask
```
