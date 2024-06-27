# Poke-berries Statistics API

## Instructions to Run the Project

### 1. Environment Setup

#### - Using Docker
Make sure you have Docker installed on your system. Then, follow these steps to build and run the application inside a Docker container:

docker build -t poke_api .

docker run -p 5000:5000 --name poke_api poke_api

#### - Without Docker
Make sure you have Python and pip installed on your system. Then, follow the steps below to set up the environment:

python -m venv venv

source venv/bin/activate  # For Linux/Mac

venv\Scripts\activate  # For Windows

pip install -r requirements.txt

### 2. Running the Application

#### - Using Docker

Once the Docker container is running, you can access your Flask application at http://localhost:5000.

#### - Without Docker

After setting up the environment, you can start the Flask application by running the following command:

flask run

### 3. Running the Tests

To run the automated tests, use the following command:

#### - Using Docker

docker exec -it poke_api pytest

#### - Without Docker

pytest


These instructions will help you set up the environment, run the application, and verify the API tests.
