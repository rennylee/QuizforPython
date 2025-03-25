# Use an official Python runtime as a base image
FROM python:3.9
# Set the working directory
WORKDIR /app
# Copy application files to the container
COPY . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 5000
EXPOSE 5000
# Define environment variables
ENV FLASK_APP=app.py
# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
