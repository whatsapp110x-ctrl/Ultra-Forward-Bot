# Use Python 3.9-slim instead of the default Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (if required)
EXPOSE 5000

# Run the bot
CMD ["python", "bot.py"]
