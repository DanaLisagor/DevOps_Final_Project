# Kubernetes Application Deployment – Phase 2

## 1. Introduction
The goal of this project is to deploy a scalable and highly available web application using Kubernetes.
The application was containerized using Docker and then orchestrated using Kubernetes resources such as Deployments, Services, and Horizontal Pod Autoscalers (HPA).

---

## 2. Cluster Setup
A local Kubernetes cluster was created using Minikube.

Steps performed:
- Started the cluster using:
    minikube start

- Verified cluster status:
    kubectl get nodes

The node was in `Ready` state, confirming that the cluster was operational.

---

## 3. Application Deployment
The application was previously containerized using Docker and pushed to Docker Hub.

A Kubernetes Deployment was created to manage the application:
- Ensures high availability by running multiple replicas
- Automatically recreates failed Pods

The Deployment was configured with:
- 2 replicas
- Container image from Docker Hub
- CPU resource requests

---

## 4. Service Exposure
To allow external access to the application, a Kubernetes Service of type **NodePort** was created.

- The Service exposes the application on a specific port
- Access was verified using:
    minikube service hello-flask-service

This allowed accessing the application via a browser.

---

## 5. Horizontal Pod Autoscaling (HPA)
An HPA resource was implemented to automatically scale the number of Pods based on CPU usage.

Configuration:
- Minimum replicas: 2
- Maximum replicas: 10
- Target CPU utilization: 60%

The metrics-server addon was enabled to allow Kubernetes to monitor CPU usage.

---

## 6. Configuration Management

### ConfigMap
A ConfigMap was used to store non-sensitive configuration (e.g., application port).

### Secret
A Secret was used to store sensitive data (e.g., `SECRET_KEY`).

Both were injected into the container using environment variables.

---

## 7. CronJob
A Kubernetes CronJob was created to execute a periodic task.

- Schedule: every minute
- The job creates a Pod that runs a simple command and then exits

This demonstrates automated task execution within the cluster.

---

## 8. Health Checks
Liveness and Readiness Probes were implemented:

- Readiness Probe
  Determines when the application is ready to receive traffic

- Liveness Probe
  Detects failures and restarts the container if needed

Both probes use HTTP checks on the application's root endpoint.

---

## 9. Conclusion
The project demonstrates a complete Kubernetes workflow, including deployment, scaling, configuration management, and monitoring.

The application is now:
- Scalable
- Highly available
- Externally accessible
- Automatically monitored and managed
