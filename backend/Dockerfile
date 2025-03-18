# Use an official Python runtime as the parent image
FROM python:3.12.9-slim

# Prevents Python from writing pyc files to disc & ensures output is sent straight to terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Command to run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
