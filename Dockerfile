# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Install system dependencies for Tkinter
RUN apt-get update && \
    apt-get install -y python3-tk libx11-6 libxcb1 libxext6 libxrender1 libtk8.6 libtcl8.6 && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=DNSpy

# Run dnspy_gui.py when the container launches
CMD ["python", "dnspy_gui.py"]
