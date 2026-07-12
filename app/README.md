# Hello Flask Application

## Overview

This directory contains the Python Flask application used in the DevOps Final Project.

The application provides a basic web endpoint, a health check endpoint for Kubernetes probes, and a CPU load endpoint used to demonstrate Horizontal Pod Autoscaling (HPA).

---

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns the application response |
| `/health` | Health check used by Kubernetes probes |
| `/load` | Generates CPU load for HPA testing |

### Home Endpoint

```text
/
```

Returns:

```text
Hello, World!
```

### Health Check Endpoint

```text
/health
```

Returns:

```text
OK
```

This endpoint is used by the Kubernetes Liveness and Readiness Probes.

### CPU Load Endpoint

```text
/load
```

The endpoint starts CPU-intensive processing.

It is used to increase application CPU utilization and demonstrate automatic Pod scaling using Kubernetes HPA.

---

## Prerequisites

Before running the application locally, make sure the following tools are installed:

- Docker
- Docker Compose

---

# Running the Application

## Option 1: Using Docker Compose

### 1. Build and Start the Application

```bash
docker compose up --build
```

### 2. Access the Application

Open:

```text
http://localhost:5000
```

### 3. Stop the Application

Press:

```text
CTRL + C
```

---

## Option 2: Using Docker

### 1. Build the Docker Image

```bash
docker build -t hello-flask .
```

### 2. Run the Container

```bash
docker run -p 5000:5000 hello-flask
```

### 3. Verify the Application

Open:

```text
http://localhost:5000
```

Verify the health endpoint:

```bash
curl http://localhost:5000/health
```

The expected response is:

```text
OK
```

### 4. Generate CPU Load

Run:

```bash
curl http://localhost:5000/load
```

The expected response is:

```text
CPU load started
```

---

## Docker Image

The Kubernetes deployment uses the following Docker image:

```text
danalisagor/hello-flask-k8s:latest
```

The image contains the Flask application and the endpoints required for Kubernetes health checks and HPA testing.

---

## Docker Volume

Create a Docker volume:

```bash
docker volume create flask_data
```

Run the container with the volume:

```bash
docker run -d -p 5000:5000 --name hello-container -v flask_data:/app/logs hello-flask
```

---

## Project Context

This application represents the application and containerization component of the DevOps Final Project.

The Docker image is deployed to Kubernetes using the Helm chart included in the project.