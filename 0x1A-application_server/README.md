# Setting up Nginx with Flask and Gunicorn

This guide outlines the process of configuring Nginx to serve a Flask application using Gunicorn as the application server. The Flask application will be served on port 80, and requests will be proxied to Gunicorn, which will be running the Flask application on port 5000.

## Prerequisites

- Ubuntu server with sudo privileges
- Flask application
- Gunicorn installed (`pip install gunicorn`)
- Nginx installed (`sudo apt update && sudo apt install nginx`)

## Steps

1. **Configure Gunicorn to Serve the Flask Application**

   Run the following command to start Gunicorn and bind it to port 5000:

   ```bash
   gunicorn --bind 0.0.0.0:5000 your_flask_app:app
