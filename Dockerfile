# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the secrets folder (you can manage this more securely with Docker secrets or environment variables)
COPY secrets /app/secrets

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for the secret API key
ENV API_KEY_FILE=/app/secrets/api.txt

# Run app.py when the container launches
CMD ["python", "app/app.py"]
