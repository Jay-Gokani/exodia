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

9. docker login -u jaygokani 
*this logs me into my Docker Hub account*

10. docker ps -a
*lists my containers*
*copy the Container ID*

11. docker commit <Container ID> <DockerHub Username>/<Repo>:<tag> 
*e.g. docker commit 971f90a34791 jaygokani/flask-test-image:2*
*this commits a new image from the container*

12. docker push <Username>/<Repo>:<tag>

13. to push another tag to the repo, repeat the two steps above and change the tag

14. to push the same tag to a different repo, just change the Repo - it can be pre-existing or new

15. docker image rm jaygokani:getting-started2:latest
*This removes the image locally*

16. docker pull jaygokani:getting-started2:latest
*This pulls the image from DockerHub*

