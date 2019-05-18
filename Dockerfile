# Base Image
FROM python:3.7-alpine 
MAINTAINER Jeff Eck


# Recommended for Docker
ENV PYTHONUNBUFFERED 1


# Dependencies
COPY ./requirements.txt /requirements.txt 


# Run pip
RUN pip install -r /requirements.txt 


# Make Directory to store source code
RUN mkdir /app 
# Switch to default directory
WORKDIR /app 
# Copy from local machine to app folder in image
COPY ./app /app 


# Create user to run application 
RUN adduser -D user 
# Switch to new user profiles
USER user 







