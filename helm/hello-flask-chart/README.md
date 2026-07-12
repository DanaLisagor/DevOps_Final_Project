# Hello Flask Helm Chart

## Overview

This directory contains the Helm chart used to deploy the Flask application to Kubernetes as part of the DevOps Final Project.

The Helm chart provides reusable and configurable Kubernetes templates for application deployment, configuration management, health monitoring, scheduled tasks, and automatic scaling.

---

## Prerequisites

Before deploying the application, make sure the following tools are installed:

- Docker
- Minikube
- kubectl
- Helm

The Docker image used by the deployment is available on Docker Hub:

`danalisagor/hello-flask-k8s:latest`

---

## Helm Chart Structure

```text
hello-flask-chart/
│
├── .helmignore
├── Chart.yaml
├── values.yaml
├── README.md
└── templates/
    ├── configmap.yml
    ├── cronjob.yml
    ├── deployment.yml
    ├── hpa.yml
    ├── secret.yml
    ├── service.yml
    └── NOTES.txt
```

---

## Kubernetes Resources

The Helm chart creates the following Kubernetes resources:

- Deployment
- Service
- ConfigMap
- Secret
- CronJob
- Horizontal Pod Autoscaler (HPA)

The Deployment also includes:

- CPU resource requests
- CPU resource limits
- Liveness Probe
- Readiness Probe

Both health probes use the `/health` application endpoint.

---

# Deployment Steps

## 1. Start Minikube

Start the local Kubernetes cluster:

```bash
minikube start
```

## 2. Enable Metrics Server

Enable the Metrics Server addon required for CPU metrics and HPA:

```bash
minikube addons enable metrics-server
```

## 3. Validate the Helm Chart

From the `helm` directory, validate the generated Kubernetes resources without deploying them:

```bash
helm upgrade --install hello-flask-test ./hello-flask-chart --dry-run
```

## 4. Deploy the Application

Deploy the application using Helm:

```bash
helm upgrade --install hello-flask-test ./hello-flask-chart
```

## 5. Verify the Pods

Verify that the application Pods are running:

```bash
kubectl get pods
```

## 6. Access the Application

Run:

```bash
minikube service hello-flask-service --url
```

Keep the terminal open while using the generated URL.

---

# Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns the application response |
| `/health` | Health check used by Kubernetes probes |
| `/load` | Generates CPU load for HPA testing |

---

# HPA Testing Guide

## 1. Ensure Metrics Server Is Running

Verify the Metrics Server deployment:

```bash
kubectl get deployment metrics-server -n kube-system
```

Verify that CPU metrics are available:

```bash
kubectl top nodes
```

You can also check Pod CPU usage:

```bash
kubectl top pods
```

## 2. Verify HPA Status

Run:

```bash
kubectl get hpa
```

The `hello-flask-hpa` resource is configured with:

- Minimum replicas: 2
- Maximum replicas: 10
- Target CPU utilization: 60%

If the CPU target initially appears as `<unknown>`, wait for the Metrics Server to collect CPU metrics and check again.

## 3. Monitor HPA Scaling

Monitor the HPA in real time:

```bash
kubectl get hpa -w
```

Keep this terminal open while generating CPU load.

## 4. Generate CPU Load

Get the application URL:

```bash
minikube service hello-flask-service --url
```

In another terminal, call the `/load` endpoint:

```bash
curl <APPLICATION_URL>/load
```

The application starts CPU-intensive processing to increase CPU utilization.

## 5. Verify Automatic Scaling

Continue monitoring:

```bash
kubectl get hpa -w
```

When CPU utilization exceeds the configured 60% target, the HPA automatically increases the number of application replicas.

During project testing, CPU utilization increased to approximately 102%, and the Deployment automatically scaled from 2 replicas to 4 replicas.

---

# Configuration

The default Helm configuration is stored in `values.yaml`.

The following settings can be configured:

- Docker image repository
- Docker image tag
- Replica count
- Container port
- Service type and ports
- HPA minimum and maximum replicas
- HPA CPU utilization target
- CronJob schedule and command

---

# Health Checks

The Deployment includes both Liveness and Readiness Probes.

Both probes use:

```text
/health
```

The endpoint returns:

```text
OK
```

The Liveness Probe monitors application health, while the Readiness Probe determines when the application is ready to receive traffic.

---

# Project Context

This Helm chart represents the Kubernetes deployment component of the DevOps Final Project.

It demonstrates Kubernetes configuration management, health monitoring, scheduled tasks, resource management, and Horizontal Pod Autoscaling using reusable Helm templates.