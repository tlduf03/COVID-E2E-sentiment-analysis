#pull the base image from dockerhub
FROM python:3.9

#copy current location to /app folder with in that base image
COPY . /app

#same location
WORKDIR /app

RUN pip install -r requirements.txt

#port
EXPOSE $port

#local port for heroku cloud platform
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app