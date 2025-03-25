# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy project files
COPY src/ /app/src/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose a port (for FastAPI, Flask, or Gradio apps)
EXPOSE 7860

# Run the application
CMD ["python", "/app/src/main.py"]