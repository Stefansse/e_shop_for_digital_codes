# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose a port (if your application uses a specific port)
EXPOSE 8000

# Define the command to run your application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
