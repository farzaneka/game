 # Set base image
FROM python:3.10

# Set working directory in container
WORKDIR /game

# Install required packages
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to container
COPY . .

# Expose required ports
EXPOSE 8000

# Set default command to run the app
CMD ["uvicorn", "main:app", "--reload"]