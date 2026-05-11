#!/bin/sh
echo "--- STARTING VIC-OS STARTUP SEQUENCE ---"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Create admin user
echo "Creating/Updating admin user..."
python create_admin.py

# Start the server
echo "Starting Daphne server..."
exec daphne -b 0.0.0.0 -p $PORT vic_os_project.asgi:application
