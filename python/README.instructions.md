### Instructions for building the Docker container

1. Write the Python application

2. Write the Dockerfile

3. cd into the python dir through the terminal

4. docker build -t python-cinema .
*builds the docker image in the current dir and tags it with a name*

5. docker run -i -t python-cinema
*spins up the container with an interactive terminal to allow for input as per our python script*

6. docker ps
*to obtain the container ID*

6. docker stop <container ID>
*stops the container*

7. docker rm <container ID>
*destroys the container*