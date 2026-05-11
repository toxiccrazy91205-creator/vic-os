# Use official Python image as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create static directory if it doesn't exist
RUN mkdir -p /app/static /app/staticfiles

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start command (using Daphne for WebSockets)
CMD daphne -b 0.0.0.0 -p $PORT vic_os_project.asgi:application
