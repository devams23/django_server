FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-distutils \
    && apt-get clean

RUN pip install Django==5.1.4

# Copy project files
COPY . /app
WORKDIR /app

# Run migrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
