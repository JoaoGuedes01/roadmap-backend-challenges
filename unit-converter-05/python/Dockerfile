# Use official Python image as base
FROM python:3.12.10-alpine

# Set working directory
WORKDIR /app

# Copy requirements file if present
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variable for Flask debug mode
ENV FLASK_DEBUG=False

# Set default command (adjust as needed)
CMD ["python", "app.py"]