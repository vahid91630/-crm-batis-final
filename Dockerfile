# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Set environment variables (optional if using .env manually)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]
