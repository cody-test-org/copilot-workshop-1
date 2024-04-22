# Use the official Docker Hub Postgres image
FROM postgres:latest

ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_DB

# Set the working directory in the container
WORKDIR /docker-entrypoint-initdb.d/

# Copy the SQL script into the container
COPY create-data.sql .

# Set environment variables
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_DB=$POSTGRES_DB

# Expose port 5432
# EXPOSE 5432

# This script will be executed on container startup
CMD ["postgres"]