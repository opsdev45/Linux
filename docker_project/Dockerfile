FROM python:3.11-slim  # Base image with Python 3.11 (slim version for smaller size)

WORKDIR /app

# Install dependencies (adapt based on your Flask app's needs)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your web application code
COPY . .

# Expose the web server port (adjust for your framework's default port)
EXPOSE 8000

# Command to run the web server (replace with your application's entry point)
CMD ["python", "app.py"]