FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3.5

RUN mkdir -p /app/files
WORKDIR /app

ADD io.py /app

ADD files /app/files

CMD ["python3.5", "io.py"]
