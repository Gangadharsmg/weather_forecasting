# FastAPI Weather API Project

This project deploys a FastAPI-based application that provides weather data for any specified city using the OpenWeatherMap API. The solution includes automated deployment via CI/CD, monitoring with Prometheus and Grafana, and supports staging and production environments.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup and Configuration](#setup-and-configuration)
   - [Environment Variables](#environment-variables)
   - [Example Configuration Files](#example-configuration-files)
3. [Deployment Instructions](#deployment-instructions)
   - [GitHub Actions Workflow](#github-actions-workflow)
   - [CI/CD Pipeline Steps](#cicd-pipeline-steps)
4. [Monitoring and Metrics](#monitoring-and-metrics)
5. [Troubleshooting Guide](#troubleshooting-guide)
6. [CI/CD Pipeline Documentation](#cicd-pipeline-documentation)


---

## Project Overview

This FastAPI application allows users to retrieve weather data by city name using the OpenWeatherMap API. It supports automated deployments through CI/CD in GitHub Actions, and monitoring is provided through Prometheus and Grafana.

---

## Setup and Configuration

### Environment Variables

Make sure the following environment variables are set before deploying:

- `API_KEY`: OpenWeatherMap API key for accessing weather data.

### Example Configuration Files

- **Docker Compose (`docker-compose.yml`)**:

    ```yaml
    version: '3.8'
    services:
      app:
        build: .
        ports:
          - "8000:8000"
        environment:
          - API_KEY=${API_KEY}
    ```

- **Kubernetes Deployment (`kubernetes_deployment.yml`)**:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: fastapi-weather-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: weather
      template:
        metadata:
          labels:
            app: weather
        spec:
          containers:
          - name: app
            image: your_docker_image
            env:
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: api-key-secret
                  key: API_KEY
    ```

---

## Deployment Instructions

### GitHub Actions Workflow

The GitHub Actions CI/CD pipeline is set up to automate testing, deployment, and monitoring.

- **Staging**: Deploys on push to the `main` branch.
- **Production**: Deploys on push to the `prod` branch.

### CI/CD Pipeline Steps

1. **Run Tests**: Executes `pytest` to validate the API functionality.
2. **Build and Deploy**: Builds Docker image, pushes to registry, and applies Kubernetes configuration.
3. **Automated Rollback**: Triggers rollback if health checks fail.

### Manual Rollback

If a manual rollback is required:
```bash
kubectl rollout undo deployment/fastapi-weather-app
