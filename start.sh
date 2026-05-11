#!/bin/sh

# Run migrations
python manage.py migrate --noinput

# Create admin user
python create_admin.py

# Start the server
exec daphne -b 0.0.0.0 -p $PORT vic_os_project.asgi:application
