#FROM python:3.7-alpine
FROM python:slim-buster
MAINTAINER twang "want2015@yeah.net"

WORKDIR /

COPY . /

RUN pip install --upgrade pip
RUN python --version
RUN pip --version
RUN pip install -r requirements.txt

CMD ["python3", "demo3-apscheduler.py" ]
