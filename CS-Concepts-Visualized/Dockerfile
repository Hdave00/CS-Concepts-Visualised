# Set the base image
FROM python:3.12.3

# Copy the current directory contents into the container
COPY . /usr/src/app

# Setup .env file to load environment variables
COPY .env /usr/src/app/.env

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
RUN pip install -r requirements.txt

# Run the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]
