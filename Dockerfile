# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install system dependencies and update CA certificates
RUN apt-get update && apt-get install -y \
    ca-certificates curl \
    && update-ca-certificates \
    && apt-get clean

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt

# Copy the project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run pytest with Allure results
CMD ["pytest", "--alluredir=reports/allure-results"]
