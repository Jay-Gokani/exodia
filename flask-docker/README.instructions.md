### Instructions for building the Docker container

1. python3 -m ensure pip 

2. pip3 install Flask

3. write the Flask app

4. pip3 freeze > requirements.txt 
*generates a requirements text file which will be build in the image*

5. write the Dockerfile

6. docker build --tag flask-docker .
*builds the image in the current dir and names it*

7. docker run -d -p 5000:5000 flask-docker
*starts the container in detached mode with port 5000 allocated to the container on my machine and 5000 where the app runs*

8. visit http://localhost:5000/
*the text is shown 'Hello there, Jay'*