# Stage 1: Base build stage
FROM python:3.13-slim AS builder
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 


# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg dependencies
  libpq-dev

# Install dependencies first for caching benefit
RUN pip install --upgrade pip 
COPY requirements.txt /app/ 
RUN pip install --no-cache-dir -r requirements.txt
 
# Stage 2: Production stage
FROM python:3.13-slim
 
RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # entrypoint
  wait-for-it \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
 
# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
# Set the working directory
WORKDIR /app
 
# Copy application code
COPY --chown=appuser:appuser ./app/ .
RUN mkdir -p ./media
COPY --chown=appuser:appuser ./compose/django/entrypoint.sh .
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Switch to non-root user
USER appuser

RUN DATABASE_URL="" \
  DJANGO_SETTINGS_MODULE="config.settings.prod" \
  python manage.py compilemessages 
  #python manage.py collectstatic --noinput
 
# Expose the application port
EXPOSE 8000 

# Make entry file executable
RUN chmod +x  /app/entrypoint.sh
 
# Start the application using Gunicorn
CMD ["/app/entrypoint.sh"]