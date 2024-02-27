FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]