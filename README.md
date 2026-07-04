# DevOps Final Project

## Overview

This repository contains a complete DevOps project that demonstrates the process of containerizing, deploying, and automating a Python Flask application using modern DevOps tools.

The project is organized into several components, each responsible for a different part of the DevOps workflow.

The project includes:

- Containerizing a Python Flask application with Docker.
- Deploying the application to Kubernetes.
- Packaging the application with Helm.
- Automating deployment validation using Jenkins.

---

## Technologies Used

- Python
- Flask
- Git & GitHub
- Docker
- Docker Compose
- Kubernetes
- Helm
- Jenkins

---

## Repository Structure

```
Final_Project/
│
├── app/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── hello_world.py
│   ├── requirements.txt
│   └── README.md
│
├── kubernetes/
│   ├── configmap.yml
│   ├── cronjob.yml
│   ├── deployment.yml
│   ├── hpa.yml
│   ├── pod.yml
│   ├── secret.yml
│   ├── service.yml
│   └── README.md
│
├── helm/
│   └── hello-flask-chart/
│       ├── .helmignore
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── README.md
│       └── templates/
│           ├── configmap.yml
│           ├── cronjob.yml
│           ├── deployment.yml
│           ├── hpa.yml
│           ├── secret.yml
│           ├── service.yml
│           └── NOTES.txt
│
├── Jenkinsfile
├── README.md
└── .gitignore
```

---

## Docker

The Docker component containerizes the Python Flask application and defines the environment required to run it.

This component includes:

- Dockerfile
- Docker Compose configuration
- Python Flask application
- Requirements file

---

## Kubernetes

The Kubernetes component deploys the application using Kubernetes manifest files.

The following Kubernetes resources are included:

- Deployment
- Service
- ConfigMap
- Secret
- CronJob
- Horizontal Pod Autoscaler (HPA)

---

## Helm

The Helm component defines the application deployment using reusable and configurable Helm templates.

The Helm chart includes:

- Chart metadata (`Chart.yaml`)
- Default configuration (`values.yaml`)
- Reusable Kubernetes templates
- A dedicated README with usage instructions

---

## Jenkins Pipeline

The Jenkins pipeline performs the following actions:

1. Builds the Docker image.
2. Verifies the Python application.
3. Validates the Helm chart using a dry-run deployment.

---

## Author

Dana Lisagor

GitHub: https://github.com/DanaLisagor