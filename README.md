# PROJECT NAME: political_candidate

## CONTENTS:
1. Running the app via a Virtual Environment (VENV)
1. Running the app on Docker

### Running the app via a Virtual Environment (VENV) - For those operating Macbooks
1. Clone this repository on to your machine
1. Open a terminal window
1. Navigate to the directory where you want to create the virtual environment.
1. Enter the following command to create a new virtual environment:"python3 -m venv [name of virtual environment]" or "python -m venv [name of virtual environment]
1. activate the virtual environment by running the following command: "source [name of virtual environment]/bin/activate" or "[name of virtual environment]\Scripts\activate"
1. Navigate to the project server (you should see 'manage.py' as one of the files) and run the server: "python3 manage.py runserver" or "python manage.py runserver"
1. You will then be provided with a link - copy this into your browser and the website should be visible

### Running the app on Docker
1. Clone this repository onto your machine
1. If you have not already done so, you will need to download Docker Desktop by visiting https://www.docker.com/products/docker-desktop/
1. If you don't already have a Docker Hub account, visit this website and create one: https://hub.docker.com
1. Navigate to the directory which contains the Dockerfile and build a Docker image by running this command (Macbooks): "docker build --platform linux/amd64/v8 -t [name of your docker image] ./" or (Windows): "cd 1project", "docker build -t [name of your docker image]
1. Create the Docker container by running the image by issuing the following command: "docker run -d -p 8000:8000 [name of docker image]"
1. Open your browser and go to the http://localhost:8000 and the website should be visible
1. Please note that Docker will continue to run the image until you stop it by entering: "docker stop [container ID]"

