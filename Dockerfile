# Stage 1: Build stage
FROM python:3.9-slim as build

# Set the working directory
WORKDIR /app

# Copy only the requirements file 
COPY api/requirements.txt .

# Install  dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the rest of the application code
COPY api/ .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask application
CMD ["flask", "run"]


