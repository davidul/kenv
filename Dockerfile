FROM python:3.10.7-alpine3.16

ADD kenv.py .
ENTRYPOINT ["python", "./kenv.py"]