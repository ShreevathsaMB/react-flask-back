# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY server.py .

# Expose the port your application runs on (if needed)
EXPOSE 5000

# Start the application
CMD ["python", "server.py"]
