# Use a slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies first (optional but helps)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --prefer-binary -r requirements.txt

# Now copy the rest of your app
COPY . .

# Default command
CMD ["streamlit", "run", "app.py"]
