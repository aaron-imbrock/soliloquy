# PULL BASE IMAGE
from python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# SET WORK DIRECTORY
WORKDIR /code

# INSTALL DEPENDENCIES
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .