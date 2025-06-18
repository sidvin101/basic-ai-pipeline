# Use an official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create upload folder
RUN mkdir -p uploads

# Expose port 8080 for AWS App Runner
EXPOSE 8080

# Set environment variable for Flask
ENV FLASK_APP=app.py

CMD ["python", "app.py"]
