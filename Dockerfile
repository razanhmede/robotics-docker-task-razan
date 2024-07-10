# Stage 1: Build stage
FROM python:3.9-slim as build

# Set the working directory
WORKDIR /app

# Copy  
COPY ./api/ .

ENV PIP_DEFAULT_TIMEOUT=100
# Install  dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2 as production stage
FROM python:3.9-slim as production

# Set the working directory
WORKDIR /app

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the rest of the application code
COPY ./api/ .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


# Command to run the Flask application
CMD ["python", "app.py"]


