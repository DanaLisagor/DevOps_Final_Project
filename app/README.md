# Hello Flask

## Overview

This directory contains the Python Flask application used in the DevOps Final Project.

The application returns a simple **"Hello, World!"** response and is used to demonstrate Docker containerization.

---

## Prerequisites

Before running the application, make sure the following tools are installed:

- Docker
- Docker Compose

---

## Running the Application

### Using Docker Compose (Recommended)

```bash
docker compose up --build
```

### Using Docker

Build the Docker image:

```bash
docker build -t hello-flask .
```

Run the container:

```bash
docker run -p 5000:5000 hello-flask
```

---

## Access the Application

After the container starts, open your browser and navigate to:

```
http://localhost:5000
```

You should see:

```
Hello, World!
```

---

## Docker Hub

The Docker image used in this project is available at:

https://hub.docker.com/r/danalisagor/hello-flask

---

## Additional Docker Commands

### Run the container in detached mode

```bash
docker run -d -p 5000:5000 --name hello-container hello-flask
```

### Create a Docker volume

```bash
docker volume create flask_data
```

### Run the container with a volume

```bash
docker run -d -p 5000:5000 --name hello-container -v flask_data:/app/logs hello-flask
```

---

## Project Context

This application is the Docker component of the **DevOps Final Project** and serves as the foundation for the Kubernetes and Helm deployment stages.