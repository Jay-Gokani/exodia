# specify base image
FROM python:3.10-alpine

# organising code within a self-contained dir of the container image
WORKDIR /code


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0 

RUN apk add --no-cache gcc musl-dev linux-headers

# copy requirements into a file with the same name in the image
COPY requirements.txt requirements.txt

# install the requirements on the image
RUN pip3 install -r requirements.txt

EXPOSE 5000

# copying everything else from the current dir
COPY . .

# python flask app is exposed to the internet and can be run as a module
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run"]