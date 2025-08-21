# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port (if required for the bot's operation)
EXPOSE 5000

# Set the command to run your bot script
CMD ["python", "bot.py"]
