# Rebuild the Docker image
docker build -t diabetes-prediction-app .

# Run the container
docker run -p 8501:8501 diabetes-prediction-app
