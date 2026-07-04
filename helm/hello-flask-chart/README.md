# Helm Chart

## Overview

This directory contains the Helm chart used to deploy the Flask application as part of the DevOps Final Project.

The Helm chart packages the Kubernetes resources into reusable and configurable templates, making application deployment easier and more maintainable.

---

## Prerequisites

Before using the Helm chart, make sure the following tools are installed:

- Docker
- Minikube
- kubectl
- Helm

Start the Kubernetes cluster:

```bash
minikube start
```

---

## Helm Chart Structure

The chart includes the following files and directories:

- `Chart.yaml` – Chart metadata
- `values.yaml` – Default configuration values
- `templates/` – Kubernetes resource templates
- `.helmignore` – Files ignored when packaging the chart

---

## Kubernetes Resources

The Helm chart templates include:

- `deployment.yml`
- `service.yml`
- `configmap.yml`
- `secret.yml`
- `cronjob.yml`
- `hpa.yml`

---

## Install the Chart

Install the application using Helm:

```bash
helm install hello-flask-test ./hello-flask-chart
```

---

## Validate the Chart

Validate the chart without deploying resources:

```bash
helm upgrade --install hello-flask-test ./hello-flask-chart --dry-run
```

---

## Configuration

The default configuration is stored in `values.yaml`.

The file can be modified to customize deployment settings such as:

- Image repository
- Image tag
- Replica count
- Service configuration
- Resource limits

---

## Project Context

This directory represents the Helm component of the DevOps Final Project.

The Helm chart provides a reusable and configurable deployment for the Flask application using Kubernetes templates.