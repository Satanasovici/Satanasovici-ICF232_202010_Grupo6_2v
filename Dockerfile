FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /peluqueriaRumps
WORKDIR /peluqueriaRumps
ADD Requirements.txt /peluqueriaRumps/
RUN pip install -r Requirements.txt
ADD . /peluqueriaRumps/