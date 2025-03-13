# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files
COPY . /app

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Install required dependencies (add scikit-learn)
RUN pip install --no-cache-dir flask flask-cors scikit-learn

# Set environment variable for debug mode
ENV FLASK_DEBUG=${FLASK_DEBUG}

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
