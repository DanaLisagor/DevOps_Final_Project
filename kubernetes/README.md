# Kubernetes Deployment

## Overview

This directory contains the Kubernetes manifests used to deploy the Flask application as part of the DevOps Final Project.

The manifests demonstrate application deployment, service exposure, configuration management, health monitoring, and automatic scaling.

---

## Prerequisites

Before applying the manifests, make sure the following tools are installed:

- Docker
- Minikube
- kubectl

Start the Kubernetes cluster:

```bash
minikube start
```

Verify the cluster is running:

```bash
kubectl get nodes
```

The node should be in the **Ready** state.

---

## Kubernetes Resources

This directory contains the following Kubernetes resources:

- `deployment.yml`
- `service.yml`
- `configmap.yml`
- `secret.yml`
- `cronjob.yml`
- `hpa.yml`
- `pod.yml`

---

## Deployment

The application is deployed using a Kubernetes Deployment.

Configuration includes:

- 2 replicas
- Docker Hub image
- CPU resource requests
- Automatic pod recreation

---

## Service

A NodePort Service exposes the application outside the cluster.

The application can be accessed using:

```bash
minikube service hello-flask-service
```

---

## Horizontal Pod Autoscaler (HPA)

The project includes an HPA configured with:

- Minimum replicas: 2
- Maximum replicas: 10
- Target CPU utilization: 60%

The metrics-server addon is required to collect CPU metrics.

---

## Configuration Management

### ConfigMap

Stores non-sensitive configuration values such as the application port.

### Secret

Stores sensitive values such as `SECRET_KEY`.

Both resources are injected into the application as environment variables.

---

## CronJob

A CronJob runs a scheduled task every minute.

Each execution creates a Pod, runs the configured command, and exits automatically.

---

## Health Checks

The application includes:

- **Readiness Probe** – determines when the application is ready to receive traffic.
- **Liveness Probe** – detects failures and automatically restarts the container when necessary.

Both probes perform HTTP checks on the application's root endpoint.

---

## Project Context

This directory represents the Kubernetes component of the DevOps Final Project.

The Kubernetes manifests provided here were later converted into reusable Helm templates located in the `helm` directory.