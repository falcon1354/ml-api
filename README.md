# ML Docker API

A simple Machine Learning API built with Flask and containerized using Docker. This project demonstrates how to deploy a scikit-learn model as a RESTful service.

## Project Structure

- `app/app.py`: The Flask application serving the model.
- `model/`: Contains the trained model (`model.pkl`) and training script.
- `Dockerfile`: Configuration for building the Docker image.
- `requirements.txt`: Python dependencies.

## Setup and Usage

### Prerequisites
- Docker installed on your machine.

### 1. Build the Docker Image
```bash
docker build -t falcon1354/ml-api:latest .
```

### 2. Run the Container
```bash
docker run -p 5000:5000 falcon1354/ml-api:latest
```

### 3. API Endpoints

- **GET /**: Health check to verify the API is running.
- **POST /predict**: Predict based on input features (`age`, `salary`).
  - **Payload**: `{"age": 30, "salary": 50000}`
  - **Response**: `{"prediction": 1}`

## Deployment

The image is also available on Docker Hub:
```bash
docker pull falcon1354/ml-api:latest
```

## Technologies Used
- Python 3.11
- Flask
- Scikit-learn
- Docker
