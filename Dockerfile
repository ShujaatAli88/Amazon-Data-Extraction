FROM python:3.10-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Set the working directory
WORKDIR /app
COPY . /app
# Command to run the application
CMD ["python","main.py"]