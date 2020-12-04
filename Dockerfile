FROM python:3.7

ENV DJANGO_SETTINGS_MODULE peluqueriarumps.production

ENV PYTHONUNBUFFERED 1

RUN mkdir peluqueriarumps

WORKDIR /peluqueriarumps

ADD . /peluqueriarumps

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80
